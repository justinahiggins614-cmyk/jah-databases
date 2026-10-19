#!/usr/bin/env python3
"""Entries for The Unsolved Atmospheric Science Database (unsolved-atmospheric-science) and its
Signature half (unsolved-atmospheric-science-signature).

34 famous unsolved problems in atmospheric science, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
through the Signature lens, ALWAYS labeled as proposals, never established
science.

ID prefixes JAH-USAT- / JAH-USATS- verified free in manifest id_prefix
values (exact + substring, both directions).
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

FIELD = {
 "tag": "atmospheric-science",
 "disp": "atmospheric science",
 "name": "The Unsolved Atmospheric Science Database",
 "sig_name": "The Unsolved Atmospheric Science Signature Database",
 "prefix": "JAH-USAT-",
 "sig_prefix": "JAH-USATS-",
 "ai": "JAH Unsolved Atmospheric Science Archivist",
 "tagline": ("Thirty-four famous open problems in atmospheric science, from convection and clouds to climate "
             "sensitivity and the unified atmosphere: real, fact-checked, each with its full story and a clearly "
             "labeled Signature proposed solution."),
 "sig_tagline": ("His original Signature solution method applied to all 34 great open problems of atmospheric "
                 "science: Signature-generated proposed solutions with assumptions declared, confirm and refute "
                 "conditions stated, and limits honestly marked. Clearly labeled Signature-made, never established "
                 "science."),
 "pub_line": ("Public records - 34 famous open problems in atmospheric science, real and fact-checked: convection "
              "parameterization, cloud feedback, aerosols, ozone recovery, lightning, tornadoes, hurricanes, "
              "monsoons, El Nino, stratosphere coupling, and atmospheric rivers - every record carrying the "
              "problem statement, background, why it matters, key points, requirements, standards, citations, "
              "and a working solution-explorer demonstration, organized in the Signature system."),
 "sig_line": ("Signature originals - his original Signature solution method: the same 34 famous unsolved "
              "atmospheric science problems approached as a covenant between the known and the unknown, each "
              "carrying the full Signature-generated proposed solution with its assumptions declared, its "
              "confirm and refute conditions stated, and its limits honestly marked. Clearly labeled "
              "Signature-made, never presented as established science or authentic public record."),
 "ladder_text": (" Records are ordered by the teaching ladder: Foundations (convection parameterization, "
                 "cloud feedback, aerosol indirect effects, ozone recovery, lightning initiation, "
                 "tornadogenesis, hurricane intensification, monsoon prediction, El Nino diversity, "
                 "stratosphere-troposphere coupling, atmospheric rivers) -> Compounded (boundary-layer "
                 "turbulence, cloud microphysics, ice nucleation, chemistry coupling, methane budget, ozone "
                 "hole chemistry, polar vortex, sudden stratospheric warming, QBO, MJO, blocking highs, jet "
                 "stream meandering) -> Advanced (climate sensitivity, hydrological amplification, cyclone "
                 "frequency, tipping points, paleoclimate mismatch, urban air chemistry, geoengineering "
                 "governance, atmospheric electricity, noctilucent clouds, atmospheric tides, the unified "
                 "atmosphere)."),
 "search_ph": ("Search convection, clouds, aerosols, ozone, lightning, hurricanes, monsoons, climate "
               "sensitivity, tipping points..."),
 "chat_ph": "Ask about the great open problems of atmospheric science...",
 "greet_pub": ("I am the JAH Unsolved Atmospheric Science Archivist. Ask me about the great open problems of "
               "atmospheric science - from convection, clouds, and aerosols through lightning, hurricanes, and "
               "monsoons, to climate sensitivity, tipping points, and the unified atmosphere."),
 "greet_sig": ("I am the JAH Unsolved Atmospheric Science Archivist (Signature). Ask me about the Signature "
               "proposed solutions to the great open problems of atmospheric science - every approach labeled "
               "as a proposal, never established science."),
 "role_pub": ("unsolved atmospheric science archivist - the great open problems of atmospheric science, from "
              "convection, clouds, and aerosols through lightning, hurricanes, and monsoons, to climate "
              "sensitivity, tipping points, and the unified atmosphere; teaches progressively along the ladder "
              "from foundations through compounded to advanced; answers from many angles - definition, example, "
              "analogy, application, history, math - using only archive data from this system"),
 "role_sig": ("unsolved atmospheric science archivist - Signature editions: his original Signature solution "
              "method applied to the 34 great open problems of atmospheric science, each carrying the full "
              "Signature-generated proposed solution, clearly labeled Signature-made and never presented as "
              "established science; teaches progressively along the ladder from foundations through compounded "
              "to advanced; answers from many angles - definition, example, analogy, application, history, "
              "math - using only archive data from this system"),
 "gen_desc": "Generate clearly-labeled unsolved atmospheric science studies. Seeded archive records are the authoritative entries.",
 "standards": [
  "Problem statements verified against the published literature; open status confirmed as of 2026.",
  "Quantitative claims cross-checked against standard references (Holton, An Introduction to Dynamic Meteorology; Wallace and Hobbs, Atmospheric Science).",
  "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
 ],
 "sig_tail": ("Signature editions carry the Signature system's proposed solution approaches to famous "
              "unsolved problems. Every solution is labeled a Signature-generated proposal, never "
              "established science, never peer-accepted, never proof."),
}

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "as-convection",
 "name": "The Convection Parameterization Problem",
 "group": "Atmospheric Dynamics",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Thunderstorms are too small for climate models to resolve - but how can their effects be represented when the physics happens below the grid scale?",
 "background": "Convection - the vertical transport of heat and moisture by cumulus clouds - drives the tropical circulation, yet climate models with 100-km grids cannot resolve 1-km storms: the effects must be parameterized (Arakawa-Schubert, mass-flux schemes). But the parameterizations assume quasi-equilibrium between convection and its environment that breaks down at gray-zone resolutions (1-10 km), and they struggle with the diurnal cycle, the MJO, and organized convection. The parameterization is the largest uncertainty in tropical climate simulation - the storms that make the weather are sub-grid everywhere that matters.",
 "why_it_matters": "Tropical rainfall, monsoons, and the MJO all hinge on parameterized convection. The sub-grid storms are the climate model's blind spot.",
 "sig_lens": "The Signature lens reads convection as the atmosphere's engine room: the protocol must represent the engines honestly at every resolution, not just the convenient ones.",
 "sig_solution": LABEL + " Assumptions: (1) quasi-equilibrium assumptions break at gray-zone resolutions; (2) organized convection defeats the schemes. Reasoning path: make parameterizations scale-aware - let them hand off smoothly to resolved convection as resolution refines. Proposed mechanism: an engine-room protocol with scale-aware convection schemes, stochastic elements representing sub-grid variability, and validation against the diurnal cycle and MJO. Confirm: scale-aware schemes improve tropical rainfall simulation. Kill: the gray zone proves unparameterizable and only resolution helps. Does NOT claim: resolved convection everywhere - it represents the engines honestly at each scale.",
 "pointer": "The Signature system's proposed approach builds scale-aware convection parameterizations; the companion Signature Edition record specifies the engine-room protocol.",
 "key_points": [
  "Climate grids (~100 km) cannot resolve storms (~1 km).",
  "Quasi-equilibrium assumptions break at gray-zone resolutions.",
  "Parameterizations struggle with the diurnal cycle and MJO.",
  "Convection is the largest tropical simulation uncertainty.",
 ],
 "requirements": [
  "Scale-aware convection schemes with smooth gray-zone handoff.",
  "Stochastic representation of sub-grid variability.",
  "Validation against diurnal cycle and MJO.",
 ],
 "citations": [
  "Arakawa A, Schubert WH (1974) Interaction of a cumulus cloud ensemble with the large-scale environment. J. Atmospheric Sciences 31.",
 ],
 "demo": {"t0": 298.15, "gamma": 6.5, "z": 3.0},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "as-cloud-feedback",
 "name": "The Cloud Feedback Problem",
 "group": "Climate",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Clouds cool by reflecting sunlight and warm by trapping heat - but which effect wins as the climate warms, and why do models disagree on the sign?",
 "background": "Cloud feedback - how clouds change as the planet warms - is the largest uncertainty in climate sensitivity: low clouds cool (reflecting sun) and their response to warming is contested; high clouds warm (trapping infrared) with uncertain changes. Models disagree even on the sign of the total cloud feedback in some regions. The physics spans droplet microphysics to large-scale circulation; observations (satellite cloud records are short) cannot yet constrain the feedback. The newest models (CMIP6) show wider sensitivity partly because of cloud feedbacks - the uncertainty grew, not shrank.",
 "why_it_matters": "Cloud feedback decides how hot the planet gets. The sign disagreement is the difference between manageable warming and catastrophic.",
 "sig_lens": "The Signature lens reads clouds as the climate's thermostat with unknown wiring: the protocol must trace the wires (the mechanisms) before trusting the thermostat's setting.",
 "sig_solution": LABEL + " Assumptions: (1) models disagree on feedback sign in regions; (2) satellite records are too short to constrain. Reasoning path: constrain by mechanism - use process-level observations and emergent constraints to narrow each cloud regime's feedback. Proposed mechanism: a thermostat protocol decomposing cloud feedback by regime (marine low clouds, tropical high clouds), constraining each with targeted observations, and reporting sensitivity with the feedback decomposition shown. Confirm: constrained feedbacks narrow the sensitivity range. Kill: the mechanisms prove unconstrainable and the range stays wide. Does NOT claim: a precise climate sensitivity - it traces the thermostat's wiring.",
 "pointer": "The Signature system's proposed approach constrains cloud feedback by regime with targeted observations; the companion Signature Edition record specifies the thermostat protocol.",
 "key_points": [
  "Cloud feedback is the largest climate-sensitivity uncertainty.",
  "Low clouds cool; high clouds warm; responses are contested.",
  "Models disagree on the feedback sign in some regions.",
  "CMIP6 sensitivity spread widened partly on cloud feedbacks.",
 ],
 "requirements": [
  "Regime-decomposed cloud feedback analysis.",
  "Process-level observational constraints per regime.",
  "Sensitivity reported with feedback decomposition.",
 ],
 "citations": [
  "Bony S et al. (2015) Clouds, circulation and climate sensitivity. Nature Geoscience 8.",
 ],
 "demo": {"t0": 295.15, "gamma": 6.0, "z": 4.0},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "as-aerosol",
 "name": "The Aerosol Indirect Effect Problem",
 "group": "Climate",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Pollution particles seed clouds and change their brightness and lifetime - but how strong is the cooling, and why is it the most uncertain forcing?",
 "background": "Aerosols affect climate directly (scattering sunlight) and indirectly - as cloud condensation nuclei, more particles mean more, smaller droplets: brighter clouds (Twomey effect) that may rain less and live longer (Albrecht effect). But the indirect effects are the most uncertain climate forcing: the pre-industrial aerosol baseline is unknown, the cloud adjustments are hard to isolate observationally, and models parameterize the microphysics crudely. The uncertainty matters enormously: strong aerosol cooling implies strong greenhouse warming masked - the Faustian bargain where cleaning the air accelerates warming.",
 "why_it_matters": "Aerosol cooling masks greenhouse warming; cleaning pollution unmasks it. The most uncertain forcing is the one most entangled with air-quality policy.",
 "sig_lens": "The Signature lens reads aerosols as a Faustian bargain: the protocol must price the cooling before the pollution cleanup spends it.",
 "sig_solution": LABEL + " Assumptions: (1) pre-industrial aerosol baseline unknown; (2) indirect effects are the most uncertain forcing. Reasoning path: constrain the indirect effect with natural laboratories - ship tracks, volcanic eruptions, weekly cycles - and carry the constraint into policy. Proposed mechanism: a bargain protocol using opportunistic experiments to bound aerosol-cloud effects, reporting the masked-warming implication explicitly, and pairing air-quality plans with the warming-unmasking estimate. Confirm: constrained indirect effects narrow the forcing range. Kill: the natural laboratories prove unrepresentative. Does NOT claim: the exact aerosol forcing - it prices the bargain before spending.",
 "pointer": "The Signature system's proposed approach constrains aerosol indirect effects with natural experiments; the companion Signature Edition record specifies the bargain protocol.",
 "key_points": [
  "Aerosol indirect effects are the most uncertain climate forcing.",
  "The pre-industrial baseline is unknown.",
  "Strong cooling implies strong masked greenhouse warming.",
  "Cleaning air quality unmasks the warming (Faustian bargain).",
 ],
 "requirements": [
  "Natural-laboratory constraints (ship tracks, volcanoes).",
  "Explicit masked-warming reporting with air-quality plans.",
  "Microphysics improvements in models.",
 ],
 "citations": [
  "Twomey S (1977) The influence of pollution on the shortwave albedo of clouds. J. Atmospheric Sciences 34.",
 ],
 "demo": {"t0": 293.15, "gamma": 5.5, "z": 2.5},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "as-ozone-recovery",
 "name": "The Stratospheric Ozone Recovery Problem",
 "group": "Atmospheric Chemistry",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "The ozone layer is healing under the Montreal Protocol - but when will it fully recover, and is the recovery on track or stalling?",
 "background": "The Montreal Protocol phased out ozone-depleting substances, and the Antarctic ozone hole is slowly healing - but full recovery is projected for mid-century at the earliest, and the recovery is not smooth: unexpected CFC-11 emissions (traced to eastern China, now declining), the 2020 Australian wildfires' smoke effects, and volcanic aerosols each perturb the trajectory. Climate change itself alters stratospheric dynamics and chemistry in ways that shift the recovery. The success story is real but unfinished - and the monitoring must continue for decades.",
 "why_it_matters": "The ozone layer shields life from UV. The Montreal Protocol is the great environmental success - but success unmonitored can reverse.",
 "sig_lens": "The Signature lens reads ozone recovery as a patient in remission: the protocol must keep the checkups going and investigate every suspicious reading.",
 "sig_solution": LABEL + " Assumptions: (1) recovery is slow and perturbable; (2) unexpected emissions have occurred. Reasoning path: monitor continuously, attribute anomalies fast, and enforce against violations. Proposed mechanism: a remission protocol with sustained ozone and ODS monitoring, rapid attribution of anomalous emissions, and Montreal Protocol enforcement with the CFC-11 episode as the template. Confirm: attributed anomalies get corrected faster. Kill: monitoring funding lapses and the recovery goes unwatched. Does NOT claim: a fixed recovery date - it keeps the patient in checkups.",
 "pointer": "The Signature system's proposed approach sustains ozone monitoring with rapid anomaly attribution; the companion Signature Edition record specifies the remission protocol.",
 "key_points": [
  "Full ozone recovery is projected for mid-century at earliest.",
  "Unexpected CFC-11 emissions showed the treaty's vulnerability.",
  "Wildfires and volcanoes perturb the recovery trajectory.",
  "Climate change alters stratospheric chemistry and dynamics.",
 ],
 "requirements": [
  "Sustained multi-decade ozone and ODS monitoring.",
  "Rapid attribution of anomalous emissions.",
  "Montreal Protocol enforcement on the CFC-11 template.",
 ],
 "citations": [
  "Solomon S et al. (2016) Emergence of healing in the Antarctic ozone layer. Science 353.",
 ],
 "demo": {"t0": 291.15, "gamma": 5.0, "z": 5.0},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "as-lightning",
 "name": "The Lightning Initiation Problem",
 "group": "Atmospheric Electricity",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Thunderclouds make lightning constantly - but how does the discharge actually start when measured electric fields are too weak to break down air?",
 "background": "Lightning initiation is the paradox at the heart of atmospheric electricity: the measured electric fields inside thunderclouds are an order of magnitude below the conventional breakdown field of air, yet lightning starts constantly. Candidate mechanisms - runaway relativistic electrons seeded by cosmic rays, hydrometeor-enhanced fields, streamer cascades - each explain part of the observations but none is confirmed. High-speed cameras and radio arrays (LMA, interferometers) now resolve the first milliseconds, but the initiating event remains elusive. The most common electrical discharge on Earth starts by unknown means.",
 "why_it_matters": "Lightning kills, starts wildfires, and threatens infrastructure. Protection design assumes a physics of initiation nobody has confirmed.",
 "sig_lens": "The Signature lens reads lightning as fire without a visible spark: the protocol must catch the spark in the act with faster eyes.",
 "sig_solution": LABEL + " Assumptions: (1) measured fields are below breakdown; (2) candidate mechanisms are unconfirmed. Reasoning path: observe the initiation directly - deploy faster, closer instruments to capture the first microseconds. Proposed mechanism: a spark protocol with high-speed optical and radio interferometry targeted at initiation, testing runaway-electron versus hydrometeor hypotheses against the captured events. Confirm: captured initiations match one mechanism's predictions. Kill: the initiation proves below instrumental resolution. Does NOT claim: the initiation mechanism - it builds the faster eyes.",
 "pointer": "The Signature system's proposed approach captures lightning initiation with high-speed interferometry; the companion Signature Edition record specifies the spark protocol.",
 "key_points": [
  "In-cloud fields measure below air's breakdown threshold.",
  "Lightning starts constantly despite the paradox.",
  "Runaway electrons and hydrometeor mechanisms are unconfirmed.",
  "The first milliseconds are now resolvable but unexplained.",
 ],
 "requirements": [
  "High-speed optical and radio initiation observations.",
  "Hypothesis testing against captured events.",
  "Protection standards reviewed against findings.",
 ],
 "citations": [
  "Dwyer JR, Uman MA (2014) The physics of lightning. Physics Reports 534.",
 ],
 "demo": {"t0": 301.15, "gamma": 7.0, "z": 2.0},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "as-tornado",
 "name": "The Tornadogenesis Problem",
 "group": "Severe Weather",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Supercells rotate, but few make tornadoes - so what is the missing ingredient that turns a rotating storm into a tornado?",
 "background": "Tornadogenesis - how tornadoes form - remains partially mysterious: supercell mesocyclones are necessary but not sufficient; the rear-flank downdraft, streamwise vorticity, and near-ground processes each play roles that are debated. High-resolution simulations (tens of meters) produce tornado-like vortices, but the real atmosphere's initiation involves scales and processes the models approximate. The operational consequence: tornado warnings have high false-alarm rates because the precursors are ambiguous. VORTEX field campaigns advanced the science without closing the initiation question.",
 "why_it_matters": "Tornadoes are the most violent winds on Earth. The missing initiation ingredient is the false-alarm rate and the missed warning.",
 "sig_lens": "The Signature lens reads tornadogenesis as a recipe missing one spice: the protocol must taste every batch (every storm) and find what the tornadic ones share.",
 "sig_solution": LABEL + " Assumptions: (1) mesocyclones are necessary but insufficient; (2) precursors are ambiguous. Reasoning path: compare tornadic and non-tornadic supercells systematically - find the discriminating near-ground processes. Proposed mechanism: a recipe protocol with mobile radar and in-situ near-ground observations of both storm types, high-resolution ensemble modeling of the discrimination, and warning algorithms keyed to the discriminating signals. Confirm: discriminating signals improve warning skill. Kill: no consistent discriminator exists. Does NOT claim: the tornadogenesis mechanism - it finds the missing spice.",
 "pointer": "The Signature system's proposed approach discriminates tornadic from non-tornadic supercells observationally; the companion Signature Edition record specifies the recipe protocol.",
 "key_points": [
  "Mesocyclones are necessary but not sufficient for tornadoes.",
  "Rear-flank downdraft and vorticity roles are debated.",
  "High-resolution models produce tornado-like vortices approximately.",
  "Warning false-alarm rates reflect precursor ambiguity.",
 ],
 "requirements": [
  "Near-ground observations of tornadic and non-tornadic storms.",
  "High-resolution ensemble discrimination modeling.",
  "Warning algorithms on discriminating signals.",
 ],
 "citations": [
  "Markowski P, Richardson Y (2009) Tornadogenesis. Atmospheric Research 93.",
 ],
 "demo": {"t0": 299.15, "gamma": 6.8, "z": 1.5},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "as-hurricane",
 "name": "The Hurricane Intensification Problem",
 "group": "Severe Weather",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Hurricane track forecasts improved dramatically, but intensity forecasts lag - so why do some storms explode while models predict weakening?",
 "background": "Tropical cyclone intensity prediction is the great forecast asymmetry: track errors halved in decades while intensity errors improved modestly. Rapid intensification - 35+ knot increases in 24 hours - is the nightmare scenario (Harvey, Michael, Otis), driven by inner-core processes (eyewall replacement, ocean coupling, shear) at scales models barely resolve. The ocean coupling is critical: storms cool their own wake, but the pre-storm ocean heat content is under-observed. Intensity guidance remains the forecast's weak half - and the half that decides evacuations.",
 "why_it_matters": "Rapid intensification before landfall is the evacuation nightmare. The forecast's weak half is the half that kills.",
 "sig_lens": "The Signature lens reads hurricanes as heat engines with hidden fuel gauges: the protocol must measure the ocean fuel and the engine's inner workings.",
 "sig_solution": LABEL + " Assumptions: (1) inner-core processes are under-resolved; (2) ocean heat content is under-observed. Reasoning path: observe the fuel and the engine - expand ocean heat-content monitoring and inner-core reconnaissance, and model the coupling. Proposed mechanism: a heat-engine protocol with enhanced pre-storm ocean observations, inner-core process modeling at resolving scales, and intensity forecasts carrying rapid-intensification probabilities. Confirm: fueled models improve intensity skill. Kill: the inner core proves chaotic beyond useful prediction. Does NOT claim: exact intensity prediction - it reads the fuel gauge.",
 "pointer": "The Signature system's proposed approach couples ocean heat observations to inner-core intensity modeling; the companion Signature Edition record specifies the heat-engine protocol.",
 "key_points": [
  "Track forecasts improved dramatically; intensity lagged.",
  "Rapid intensification (35+ kt/24h) defeats the models.",
  "Ocean heat content - the fuel - is under-observed.",
  "Intensity is the forecast half that decides evacuations.",
 ],
 "requirements": [
  "Expanded pre-storm ocean heat-content monitoring.",
  "Inner-core process modeling at resolving scales.",
  "Rapid-intensification probabilities in forecasts.",
 ],
 "citations": [
  "Emanuel K (2003) Tropical cyclones. Annual Review EPS 31.",
 ],
 "demo": {"t0": 302.15, "gamma": 6.2, "z": 3.5},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "as-monsoon",
 "name": "The Monsoon Prediction Problem",
 "group": "Climate",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Monsoons water billions - but how can their onset, breaks, and seasonal totals be predicted when the models struggle with the coupled system?",
 "background": "Monsoons - the seasonal wind reversals watering South Asia, West Africa, East Asia - are coupled ocean-land-atmosphere phenomena that models simulate with persistent biases: the Indian monsoon rainfall is too weak or misplaced in many models, the West African monsoon jumps north too far, and the onset timing (the farmer's critical date) is poorly predicted. The biases trace to convection parameterization, orography representation, and ocean coupling - the whole coupled-system challenge in one phenomenon. Billions plan planting on forecasts the models cannot reliably give.",
 "why_it_matters": "Monsoon onset decides planting for billions. The coupled-system biases are food-security biases.",
 "sig_lens": "The Signature lens reads monsoons as the planet's irrigation schedule: the protocol must fix the schedule's biases where the farmers live.",
 "sig_solution": LABEL + " Assumptions: (1) persistent coupled-system biases; (2) onset timing is the critical forecast. Reasoning path: attack the biases jointly - convection, orography, ocean coupling - and forecast onset probabilistically. Proposed mechanism: an irrigation-schedule protocol with bias-targeted model development, multi-model onset forecasts, and farmer-oriented probabilistic onset guidance. Confirm: bias-reduced models improve onset skill. Kill: the biases prove structural and irreducible at current resolution. Does NOT claim: exact monsoon prediction - it fixes the schedule's biases.",
 "pointer": "The Signature system's proposed approach targets monsoon model biases jointly with probabilistic onset forecasts; the companion Signature Edition record specifies the irrigation-schedule protocol.",
 "key_points": [
  "Monsoon simulations carry persistent regional biases.",
  "Onset timing - the farmer's date - is poorly predicted.",
  "Biases trace to convection, orography, and ocean coupling.",
  "Billions depend on forecasts the models cannot reliably give.",
 ],
 "requirements": [
  "Joint bias-targeted model development.",
  "Multi-model probabilistic onset forecasts.",
  "Farmer-oriented onset guidance products.",
 ],
 "citations": [
  "Wang B et al. (2021) Monsoons climate change assessment. BAMS 102(1).",
 ],
 "demo": {"t0": 300.15, "gamma": 5.8, "z": 4.5},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "as-enso",
 "name": "The El Nino Diversity Problem",
 "group": "Climate",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "No two El Ninos are alike - eastern versus central Pacific flavors bring different global impacts, so how can the diversity be predicted?",
 "background": "ENSO - the El Nino-Southern Oscillation - comes in flavors: eastern Pacific (canonical) versus central Pacific (Modoki) events, each with different teleconnections: the same 'El Nino' label brings different rainfall to California, Australia, and East Africa depending on the flavor. Models struggle with the diversity: many simulate too-regular, too-eastern-Pacific ENSO. The predictability differs by flavor and by season (the spring predictability barrier). The diversity question compounds under warming: will the flavors shift? The most predictable climate signal is predictable only in aggregate.",
 "why_it_matters": "ENSO drives global seasonal predictability. Flavor-blind forecasts mislead the regions whose impacts flip with the flavor.",
 "sig_lens": "The Signature lens reads El Nino as a family, not a person: the protocol must identify which sibling is coming, because each behaves differently.",
 "sig_solution": LABEL + " Assumptions: (1) flavors have different teleconnections; (2) models simulate too-regular ENSO. Reasoning path: forecast the flavor, not just the index - predict the spatial pattern and its specific teleconnections. Proposed mechanism: a family protocol with flavor-resolving ENSO forecasts, flavor-specific teleconnection guidance, and model development targeting ENSO diversity. Confirm: flavor forecasts improve regional impact guidance. Kill: the flavors prove unpredictable beyond the aggregate index. Does NOT claim: exact flavor prediction - it identifies the sibling.",
 "pointer": "The Signature system's proposed approach forecasts ENSO flavor with flavor-specific teleconnections; the companion Signature Edition record specifies the family protocol.",
 "key_points": [
  "Eastern vs central Pacific El Ninos bring different global impacts.",
  "Models simulate too-regular, too-eastern-Pacific ENSO.",
  "The spring predictability barrier limits skill.",
  "Flavor shifts under warming are unknown.",
 ],
 "requirements": [
  "Flavor-resolving ENSO forecast products.",
  "Flavor-specific teleconnection guidance.",
  "Model development targeting ENSO diversity.",
 ],
 "citations": [
  "Capotondi A et al. (2015) Understanding ENSO diversity. BAMS 96(6).",
 ],
 "demo": {"t0": 297.15, "gamma": 6.0, "z": 3.0},
},
# ----------------------------------------------------------------- rank 10
{
 "key": "as-strat-trop",
 "name": "The Stratosphere Troposphere Coupling Problem",
 "group": "Atmospheric Dynamics",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "The stratosphere was thought to just sit above the weather - but it influences surface climate, so how does the coupling work?",
 "background": "Stratosphere-troposphere coupling - the two-way interaction once ignored - is now known to matter: sudden stratospheric warmings precede cold-air outbreaks weeks later; the stratospheric polar vortex state predicts the North Atlantic Oscillation; ozone depletion shifted the Southern Hemisphere jet. But the coupling mechanisms (downward wave propagation, eddy feedbacks) are incompletely understood, and models with poor stratospheric resolution miss the coupling - yet most climate models have coarse stratospheres. The forecast skill from the stratosphere (subseasonal prediction's best source) is under-exploited.",
 "why_it_matters": "The stratosphere holds weeks of forecast skill the troposphere-only models waste. The coupling is subseasonal prediction's best untapped source.",
 "sig_lens": "The Signature lens reads the stratosphere as the weather's upstairs neighbor: the protocol must listen through the ceiling, because the footsteps predict the cold snaps.",
 "sig_solution": LABEL + " Assumptions: (1) coupling mechanisms incompletely understood; (2) coarse-stratosphere models miss it. Reasoning path: resolve the stratosphere and exploit its predictability - raise model tops, and build stratosphere-aware subseasonal forecasts. Proposed mechanism: an upstairs protocol requiring high-top models for subseasonal forecasting, stratospheric precursor monitoring (vortex state, SSW detection), and forecast products using the stratospheric lead time. Confirm: stratosphere-aware forecasts beat troposphere-only on subseasonal scales. Kill: the coupling proves too weak for operational skill. Does NOT claim: full coupling understanding - it listens through the ceiling.",
 "pointer": "The Signature system's proposed approach exploits stratospheric predictability for subseasonal forecasts; the companion Signature Edition record specifies the upstairs protocol.",
 "key_points": [
  "SSWs precede cold-air outbreaks by weeks.",
  "Vortex state predicts the North Atlantic Oscillation.",
  "Ozone depletion shifted the Southern Hemisphere jet.",
  "Most climate models have coarse, coupling-missing stratospheres.",
 ],
 "requirements": [
  "High-top models for subseasonal forecasting.",
  "Stratospheric precursor monitoring.",
  "Stratosphere-aware forecast products.",
 ],
 "citations": [
  "Baldwin MP, Dunkerton TJ (2001) Stratospheric harbingers of anomalous weather regimes. Science 294.",
 ],
 "demo": {"t0": 288.15, "gamma": 4.5, "z": 8.0},
},
# ----------------------------------------------------------------- rank 11
{
 "key": "as-atmos-rivers",
 "name": "The Atmospheric Rivers Problem",
 "group": "Climate",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Atmospheric rivers - sky rivers carrying more water than the Amazon - bring both water supply and catastrophic floods, so how can they be predicted and managed?",
 "background": "Atmospheric rivers (ARs) - long, narrow corridors of concentrated moisture transport - deliver up to half of annual precipitation to the US West Coast (and comparable fractions elsewhere) while causing the region's worst floods. AR prediction has improved (the AR scale, 1-5, categorizes impacts), but landfall location errors of 100 km decide between water supply and disaster. Climate change intensifies ARs (more moisture per degree) - the flood risk grows while the water-supply dependence deepens. Forecast-informed reservoir operations (FIRO) try to thread the needle: keep space for the flood, keep water for the summer.",
 "why_it_matters": "ARs are the West's water supply and its flood catastrophe in one phenomenon. The 100-km landfall error is the difference between the two.",
 "sig_lens": "The Signature lens reads atmospheric rivers as the sky's fire hoses: the protocol must aim the reservoir operations at the hose's actual target, not its forecast shadow.",
 "sig_solution": LABEL + " Assumptions: (1) landfall errors decide supply vs disaster; (2) climate intensifies ARs. Reasoning path: operate reservoirs on the AR forecast - release ahead of the flood, store behind it - with the uncertainty priced in. Proposed mechanism: a fire-hose protocol with AR-scale-based reservoir operations, ensemble landfall forecasts, and operating rules updated as AR climatology shifts. Confirm: FIRO-style operations improve both flood safety and supply. Kill: the landfall errors prove irreducible at decision lead times. Does NOT claim: exact AR landfall prediction - it aims operations at the hose.",
 "pointer": "The Signature system's proposed approach operates reservoirs on atmospheric-river forecasts; the companion Signature Edition record specifies the fire-hose protocol.",
 "key_points": [
  "ARs deliver up to half of West Coast annual precipitation.",
  "The same ARs cause the region's worst floods.",
  "100-km landfall errors decide supply versus disaster.",
  "Climate change intensifies AR moisture transport.",
 ],
 "requirements": [
  "AR-scale-based reservoir operating rules.",
  "Ensemble AR landfall forecasts.",
  "Operating rules updated with shifting AR climatology.",
 ],
 "citations": [
  "Dettinger MD et al. (2011) Atmospheric rivers, floods and the water resources of California. Water 3(2).",
 ],
 "demo": {"t0": 294.15, "gamma": 6.0, "z": 3.0},
},
# ----------------------------------------------------------------- rank 12
{
 "key": "as-boundary-layer",
 "name": "The Boundary Layer Turbulence Problem",
 "group": "Atmospheric Dynamics",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "The lowest kilometer of air - where we live - is turbulent at scales models cannot resolve, so how can the surface fluxes be represented?",
 "background": "The planetary boundary layer (PBL) - the turbulent lowest ~1 km - mediates every surface-atmosphere exchange: heat, moisture, momentum, pollutants. But the dominant eddies (tens to hundreds of meters) are sub-grid for weather models: PBL schemes (K-theory, higher-order closure, EDMF) parameterize the fluxes with known deficiencies - the stable boundary layer (nighttime) is particularly badly represented, and the gray zone (100-m grids) breaks the schemes' assumptions. Wind-energy, air-quality, and fog forecasts all inherit the PBL errors. The air we breathe is the models' worst layer.",
 "why_it_matters": "Every surface forecast - wind, fog, pollution, frost - passes through the PBL schemes. The worst-represented layer is the lived-in one.",
 "sig_lens": "The Signature lens reads the boundary layer as the atmosphere's skin: the protocol must feel its turbulence at the right scale, especially at night.",
 "sig_solution": LABEL + " Assumptions: (1) dominant eddies are sub-grid; (2) stable boundary layers are badly represented. Reasoning path: go scale-aware and observation-driven - large-eddy simulation where affordable, better stable-layer physics, and dense surface networks for validation. Proposed mechanism: a skin protocol with scale-aware PBL schemes, targeted stable-boundary-layer physics development, and validation against dense surface flux networks. Confirm: improved schemes reduce wind and fog forecast errors. Kill: the stable layer proves unparameterizable. Does NOT claim: resolved turbulence everywhere - it feels the skin at the right scale.",
 "pointer": "The Signature system's proposed approach improves boundary-layer representation with scale-aware schemes; the companion Signature Edition record specifies the skin protocol.",
 "key_points": [
  "PBL eddies (10s-100s of meters) are sub-grid for weather models.",
  "Stable (nighttime) boundary layers are badly represented.",
  "Gray-zone resolutions break scheme assumptions.",
  "Wind, fog, and pollution forecasts inherit PBL errors.",
 ],
 "requirements": [
  "Scale-aware PBL schemes.",
  "Stable-boundary-layer physics development.",
  "Dense surface-flux validation networks.",
 ],
 "citations": [
  "Stull RB (1988) An Introduction to Boundary Layer Meteorology. Kluwer.",
 ],
 "demo": {"t0": 292.15, "gamma": 5.2, "z": 1.0},
},
# ----------------------------------------------------------------- rank 13
{
 "key": "as-microphysics",
 "name": "The Cloud Microphysics Problem",
 "group": "Atmospheric Dynamics",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Cloud droplets grow, collide, freeze, and fall - but the microphysical details decide rain, so how can they be represented without tracking every drop?",
 "background": "Cloud microphysics - nucleation, condensation, collision-coalescence, riming, aggregation - controls precipitation efficiency: whether a cloud rains itself out or carries water downwind. Bulk schemes (one- or two-moment) approximate the droplet spectrum crudely; bin schemes resolve it at unaffordable cost. The autoconversion (cloud to rain) threshold is a tuned fiction; ice processes multiply the complexity. Aerosol-cloud interactions enter through the microphysics - the indirect effect's home. The rain's physics is parameterized where it matters most.",
 "why_it_matters": "Whether clouds rain or persist decides water supply, floods, and the aerosol indirect effect. The tuned autoconversion is the rainfall's hidden dial.",
 "sig_lens": "The Signature lens reads microphysics as the rain's factory floor: the protocol must audit the machinery (the process rates) against what the factory ships (the rain).",
 "sig_solution": LABEL + " Assumptions: (1) bulk schemes approximate spectra crudely; (2) autoconversion is tuned. Reasoning path: constrain process rates observationally - use radar, aircraft, and lab data to pin the conversion rates. Proposed mechanism: a factory protocol with process-rate constraints from observations, superparameterization or bin schemes where affordable, and precipitation forecasts validated on process fidelity, not just rain totals. Confirm: constrained schemes improve rain timing and amount. Kill: the process rates prove unconstrainable at scale. Does NOT claim: exact microphysics - it audits the factory floor.",
 "pointer": "The Signature system's proposed approach constrains cloud process rates observationally; the companion Signature Edition record specifies the factory protocol.",
 "key_points": [
  "Microphysics controls precipitation efficiency.",
  "Bulk schemes approximate droplet spectra crudely.",
  "Autoconversion thresholds are tuned fictions.",
  "Ice processes multiply the complexity.",
 ],
 "requirements": [
  "Observational constraints on process rates.",
  "Higher-fidelity schemes where affordable.",
  "Process-fidelity forecast validation.",
 ],
 "citations": [
  "Morrison H et al. (2020) Confronting the challenge of modeling cloud and precipitation microphysics. JAMES 12.",
 ],
 "demo": {"t0": 296.15, "gamma": 6.4, "z": 2.0},
},
# ----------------------------------------------------------------- rank 14
{
 "key": "as-ice-nucleation",
 "name": "The Ice Nucleation Problem",
 "group": "Atmospheric Dynamics",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Clouds supercool far below freezing without freezing - so what actually triggers ice formation, and why does it matter for rain and climate?",
 "background": "Ice nucleation - the birth of ice crystals in supercooled clouds - controls precipitation (the Bergeron process) and cloud radiative properties, yet the nucleating agents (ice-nucleating particles: dust, biological fragments) are poorly characterized: their atmospheric concentrations, sources, and temperature-dependent activity are uncertain by orders of magnitude. Homogeneous freezing (below -38 C) is understood; heterogeneous nucleation (the atmospherically relevant kind) is not. Biological ice nucleators (bacteria, pollen) may matter and are barely measured. The rain's freezing trigger is the clouds' least-known ingredient.",
 "why_it_matters": "Ice nucleation decides whether clouds precipitate or persist, brighten or darken. The least-known ingredient controls the cloud's fate.",
 "sig_lens": "The Signature lens reads ice nucleation as the cloud's freezing trigger: the protocol must inventory the triggers (the particles) before predicting the freeze.",
 "sig_solution": LABEL + " Assumptions: (1) INP concentrations uncertain by orders of magnitude; (2) biological nucleators barely measured. Reasoning path: measure the triggers - build the global INP inventory (sources, concentrations, activity spectra). Proposed mechanism: a trigger protocol with systematic INP measurement campaigns, source-resolved inventories (dust, biological, anthropogenic), and nucleation schemes keyed to the measured spectra. Confirm: inventoried schemes improve mixed-phase cloud simulation. Kill: INP prove too variable to inventory usefully. Does NOT claim: exact nucleation prediction - it inventories the triggers.",
 "pointer": "The Signature system's proposed approach builds a global ice-nucleating-particle inventory; the companion Signature Edition record specifies the trigger protocol.",
 "key_points": [
  "Ice nucleation controls precipitation and cloud radiation.",
  "INP concentrations are uncertain by orders of magnitude.",
  "Heterogeneous nucleation (the relevant kind) is poorly understood.",
  "Biological ice nucleators may matter and are barely measured.",
 ],
 "requirements": [
  "Systematic global INP measurement campaigns.",
  "Source-resolved INP inventories.",
  "Nucleation schemes keyed to measured spectra.",
 ],
 "citations": [
  "Hoose C, Mohler O (2012) Heterogeneous ice nucleation on atmospheric aerosols. ACP 12.",
 ],
 "demo": {"t0": 285.15, "gamma": 4.0, "z": 6.0},
},
# ----------------------------------------------------------------- rank 15
{
 "key": "as-chemistry-coupling",
 "name": "The Atmospheric Chemistry Coupling Problem",
 "group": "Atmospheric Chemistry",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Chemistry, aerosols, clouds, and climate all interact - but how can the coupled system be modeled when each component is uncertain alone?",
 "background": "Atmospheric chemistry couples to everything: oxidants (OH) control methane lifetime; aerosols seed clouds; ozone chemistry depends on temperature and dynamics; biogenic emissions respond to climate. Chemistry-climate models include hundreds of reactions, but the mechanisms are uncertain (isoprene oxidation pathways were revised repeatedly), the emissions inventories are approximate, and the coupling feeds back: warming changes chemistry which changes warming. Evaluating the coupled system is hard because the components' errors compensate. The whole is more uncertain than the sum of its parts.",
 "why_it_matters": "Methane lifetime, ozone recovery, and aerosol forcing all live in the coupled chemistry. Compensating errors hide the real uncertainties.",
 "sig_lens": "The Signature lens reads chemistry coupling as a chemical conversation: the protocol must eavesdrop on each exchange (the fluxes) rather than trusting the summary.",
 "sig_solution": LABEL + " Assumptions: (1) component errors compensate in evaluation; (2) mechanisms keep being revised. Reasoning path: evaluate the exchanges, not just the states - constrain chemical fluxes (OH, deposition, emissions) directly. Proposed mechanism: a conversation protocol with flux-focused observations (oxidant budgets, deposition networks), mechanism testing against the fluxes, and coupled-model evaluation on exchange fidelity. Confirm: flux-constrained models agree better on methane lifetime. Kill: the fluxes prove unmeasurable at scale. Does NOT claim: exact coupled chemistry - it eavesdrops on the exchanges.",
 "pointer": "The Signature system's proposed approach constrains atmospheric chemistry on measured fluxes; the companion Signature Edition record specifies the conversation protocol.",
 "key_points": [
  "Chemistry couples to aerosols, clouds, and climate.",
  "Mechanisms (isoprene oxidation) keep being revised.",
  "Emission inventories are approximate.",
  "Component errors compensate, hiding real uncertainty.",
 ],
 "requirements": [
  "Flux-focused chemical observations.",
  "Mechanism testing against measured fluxes.",
  "Exchange-fidelity model evaluation.",
 ],
 "citations": [
  "Brasseur GP, Jacob DJ (2017) Modeling of Atmospheric Chemistry. Cambridge.",
 ],
 "demo": {"t0": 293.15, "gamma": 5.5, "z": 3.0},
},
# ----------------------------------------------------------------- rank 16
{
 "key": "as-methane",
 "name": "The Methane Budget Problem",
 "group": "Atmospheric Chemistry",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Atmospheric methane is rising fast - but how much comes from wetlands, fossil fuels, agriculture, and waste, and why did the rise resume?",
 "background": "Methane - the second greenhouse gas - resumed rapid growth after 2007 for debated reasons: the isotopic signature shifted (suggesting biogenic sources), but fossil-fuel inventories are also suspected underestimates. Top-down (atmospheric inversion) and bottom-up (inventory) budgets disagree by tens of percent; the OH sink (methane's destroyer) is itself uncertain. Super-emitters (a few percent of oil/gas sites) dominate some regions' emissions but are missed by inventories. The budget gap is the mitigation gap: you cannot manage what you cannot attribute.",
 "why_it_matters": "Methane drives near-term warming; cutting it is the fastest climate lever. The unattributed budget is the unmanaged lever.",
 "sig_lens": "The Signature lens reads the methane budget as an accounting scandal: the protocol must audit the books top-down and bottom-up until they agree.",
 "sig_solution": LABEL + " Assumptions: (1) top-down and bottom-up disagree substantially; (2) super-emitters dominate regionally. Reasoning path: reconcile the books - expand isotopic and remote-sensing constraints, and hunt super-emitters directly. Proposed mechanism: an audit protocol with satellite methane mapping (TROPOMI and successors), isotopic source attribution, super-emitter detection and repair programs, and reconciled budgets published with the disagreement shown. Confirm: audited regions show converging budgets. Kill: the OH sink uncertainty defeats reconciliation. Does NOT claim: an exact methane budget - it audits until the books nearly agree.",
 "pointer": "The Signature system's proposed approach reconciles methane budgets with satellite and isotopic constraints; the companion Signature Edition record specifies the audit protocol.",
 "key_points": [
  "Methane growth resumed after 2007 for debated reasons.",
  "Top-down and bottom-up budgets disagree by tens of percent.",
  "The OH sink is itself uncertain.",
  "Super-emitters dominate some regions but evade inventories.",
 ],
 "requirements": [
  "Satellite methane mapping and super-emitter detection.",
  "Isotopic source attribution.",
  "Reconciled budgets with disagreements published.",
 ],
 "citations": [
  "Saunois M et al. (2020) The global methane budget 2000-2017. ESSD 12.",
 ],
 "demo": {"t0": 295.15, "gamma": 6.0, "z": 2.5},
},
# ----------------------------------------------------------------- rank 17
{
 "key": "as-ozone-hole-chem",
 "name": "The Ozone Hole Chemistry Problem",
 "group": "Atmospheric Chemistry",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Polar stratospheric clouds enable the ozone hole's chemistry - but how do the heterogeneous reactions actually proceed on real cloud particles?",
 "background": "The ozone hole's chemistry - chlorine activation on polar stratospheric cloud (PSC) surfaces - was the key discovery (Solomon, 1986), but the heterogeneous reaction rates on real PSC particles (ice, nitric acid trihydrate, supercooled ternary solutions) remain uncertain: laboratory rates on idealized surfaces differ from atmospheric conditions, the particle composition evolves, and denitrification (sedimenting particles removing nitrogen) modulates the chemistry. The Arctic - warmer, more variable - shows different chemistry than the Antarctic. Models reproduce the hole approximately; the surface chemistry details are still parameterized.",
 "why_it_matters": "The ozone hole is chemistry's great solved-then-unsolved problem: the mechanism is known, the surface details that set its depth are not.",
 "sig_lens": "The Signature lens reads PSCs as the hole's reaction vessels: the protocol must sample the vessels in situ and measure the reactions on real surfaces.",
 "sig_solution": LABEL + " Assumptions: (1) lab rates differ from atmospheric conditions; (2) Arctic and Antarctic chemistry differ. Reasoning path: measure the reactions where they happen - in-situ PSC composition and chlorine activation observations. Proposed mechanism: a vessels protocol with polar in-situ PSC campaigns, heterogeneous-rate measurements on real particles, and models keyed to the measured rates. Confirm: measured-rate models reproduce hole depth better. Kill: the in-situ conditions prove unreproducible for rate measurement. Does NOT claim: exact hole prediction - it measures the reactions on real surfaces.",
 "pointer": "The Signature system's proposed approach measures ozone-hole chemistry on real PSC particles; the companion Signature Edition record specifies the vessels protocol.",
 "key_points": [
  "Chlorine activation on PSC surfaces drives the hole.",
  "Lab reaction rates differ from real particle conditions.",
  "Denitrification modulates the chemistry.",
  "Arctic chemistry differs from Antarctic.",
 ],
 "requirements": [
  "In-situ polar PSC composition campaigns.",
  "Heterogeneous rates on real particles.",
  "Models keyed to measured rates.",
 ],
 "citations": [
  "Solomon S et al. (1986) On the depletion of Antarctic ozone. Nature 321.",
 ],
 "demo": {"t0": 283.15, "gamma": 3.5, "z": 10.0},
},
# ----------------------------------------------------------------- rank 18
{
 "key": "as-polar-vortex",
 "name": "The Polar Vortex Disruption Problem",
 "group": "Atmospheric Dynamics",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "The stratospheric polar vortex sometimes collapses, unleashing Arctic cold - but what disrupts it, and can the disruptions be predicted?",
 "background": "The polar vortex - the winter stratospheric cyclone - is disrupted by upward-propagating planetary waves that break in the stratosphere: the disruption's timing and depth determine whether the surface sees a cold-air outbreak. But the wave sources (tropospheric precursors: Ural blocking, North Pacific patterns) are inconsistently predictive, and the downward coupling varies event to event. Forecasting vortex disruptions beyond two weeks is poor - yet they are the best subseasonal predictability source. The vortex is the atmosphere's flywheel; its wobbles are forecasted worse than they should be.",
 "why_it_matters": "Vortex disruptions precede some of the worst winter cold outbreaks. The best subseasonal signal is the worst-forecasted.",
 "sig_lens": "The Signature lens reads the vortex as a spinning top: the protocol must watch the fingers (the waves) that wobble it and predict the wobble.",
 "sig_solution": LABEL + " Assumptions: (1) wave precursors are inconsistently predictive; (2) downward coupling varies. Reasoning path: track the waves and the vortex jointly - monitor precursors and vortex state, and forecast the disruption probabilistically. Proposed mechanism: a top protocol with planetary-wave precursor monitoring, vortex-state forecasting ensembles, and surface-impact probabilities conditioned on disruption forecasts. Confirm: precursor-tracked forecasts beat climatology. Kill: the precursors prove non-predictive. Does NOT claim: exact disruption prediction - it watches the wobble.",
 "pointer": "The Signature system's proposed approach forecasts polar vortex disruptions from wave precursors; the companion Signature Edition record specifies the top protocol.",
 "key_points": [
  "Planetary waves breaking in the stratosphere disrupt the vortex.",
  "Tropospheric precursors are inconsistently predictive.",
  "Downward coupling varies event to event.",
  "Disruptions are the best subseasonal signal, poorly forecast.",
 ],
 "requirements": [
  "Planetary-wave precursor monitoring.",
  "Vortex-state forecast ensembles.",
  "Surface-impact probabilities from disruption forecasts.",
 ],
 "citations": [
  "Charlton AJ, Polvani LM (2007) A new look at stratospheric sudden warmings. J. Climate 20.",
 ],
 "demo": {"t0": 281.15, "gamma": 3.0, "z": 12.0},
},
# ----------------------------------------------------------------- rank 19
{
 "key": "as-ssw",
 "name": "The Sudden Stratospheric Warming Problem",
 "group": "Atmospheric Dynamics",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "The polar stratosphere can warm 50 degrees in days - but what triggers sudden stratospheric warmings, and why do their surface impacts vary?",
 "background": "Sudden stratospheric warmings (SSWs) - dramatic polar-stratosphere warmings with vortex breakdown - are the most spectacular dynamical events in the atmosphere, yet their triggers are debated: tropospheric wave forcing is necessary, but the stratosphere's preconditioning (vortex state, QBO phase) decides the outcome. The surface impacts vary: some SSWs bring European cold snaps, others do little - the downward influence depends on the tropospheric state at the time. Major SSWs occur roughly every other winter in the Arctic; the Antarctic saw its first major in 2002. Prediction skill is limited to ~2 weeks.",
 "why_it_matters": "SSWs are the atmosphere's biggest dynamical events and a prime subseasonal signal. Their variable surface impacts are forecast opportunities wasted.",
 "sig_lens": "The Signature lens reads SSWs as the stratosphere's sneezes: the protocol must learn which sneezes spread the cold (to the surface) and which do not.",
 "sig_solution": LABEL + " Assumptions: (1) triggers debated; preconditioning matters; (2) surface impacts vary with tropospheric state. Reasoning path: forecast the sneeze and its spread jointly - predict the SSW and condition the surface impact on the tropospheric state. Proposed mechanism: a sneeze protocol with SSW forecast ensembles, preconditioning diagnostics (vortex, QBO), and surface-impact forecasts conditioned jointly on the SSW and tropospheric state. Confirm: joint forecasts beat SSW-only guidance. Kill: the conditioning proves unlearnable. Does NOT claim: exact SSW prediction - it forecasts the sneeze and its spread.",
 "pointer": "The Signature system's proposed approach forecasts SSW surface impacts jointly with tropospheric state; the companion Signature Edition record specifies the sneeze protocol.",
 "key_points": [
  "SSWs warm the polar stratosphere ~50 C in days.",
  "Triggers debated; stratospheric preconditioning decides outcomes.",
  "Surface impacts vary with the concurrent tropospheric state.",
  "Prediction skill limited to about two weeks.",
 ],
 "requirements": [
  "SSW forecast ensembles with preconditioning diagnostics.",
  "Joint SSW-troposphere surface-impact forecasts.",
  "Vortex and QBO state monitoring.",
 ],
 "citations": [
  "Butler AH et al. (2015) Defining sudden stratospheric warmings. BAMS 96(11).",
 ],
 "demo": {"t0": 279.15, "gamma": 2.8, "z": 14.0},
},
# ----------------------------------------------------------------- rank 20
{
 "key": "as-qbo",
 "name": "The Quasi Biennial Oscillation Problem",
 "group": "Atmospheric Dynamics",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Tropical stratospheric winds reverse every ~28 months like clockwork - but what keeps the clock, and why did it skip in 2016?",
 "background": "The quasi-biennial oscillation (QBO) - the ~28-month reversal of equatorial stratospheric winds - is driven by wave-mean-flow interaction (Lindzen-Holton theory), and was the atmosphere's most regular oscillation until 2016, when it disrupted unprecedentedly: the expected westerly phase was interrupted by an anomalous easterly jet. The disruption's cause is debated (anomalous wave forcing, possibly climate-change-related). Models struggle to generate a spontaneous QBO (needing high vertical resolution and parameterized gravity waves); the 2016 event raised the question of whether the clock is changing. The QBO modulates the MJO, hurricanes, and ozone - its predictability matters.",
 "why_it_matters": "The QBO organizes tropical variability from hurricanes to ozone. A changing clock changes the organization.",
 "sig_lens": "The Signature lens reads the QBO as the stratosphere's metronome: the protocol must find what keeps the beat and whether the tempo is changing.",
 "sig_solution": LABEL + " Assumptions: (1) wave-mean-flow theory explains the regular QBO; (2) the 2016 disruption's cause debated. Reasoning path: monitor the metronome's drivers - wave forcing and momentum budgets - and test whether disruptions are becoming frequent. Proposed mechanism: a metronome protocol with QBO wave-forcing monitoring, high-resolution model development for spontaneous QBOs, and disruption early-warning from precursor diagnostics. Confirm: monitored precursors anticipate disruptions. Kill: the 2016 event proves singular and the clock is unchanged. Does NOT claim: a new QBO theory - it watches the metronome's beat.",
 "pointer": "The Signature system's proposed approach monitors QBO wave forcing for disruption early warning; the companion Signature Edition record specifies the metronome protocol.",
 "key_points": [
  "The QBO reverses equatorial stratospheric winds ~every 28 months.",
  "Wave-mean-flow interaction drives it (Lindzen-Holton).",
  "The 2016 disruption was unprecedented.",
  "Models struggle to generate spontaneous QBOs.",
 ],
 "requirements": [
  "QBO wave-forcing and momentum-budget monitoring.",
  "High-vertical-resolution model development.",
  "Disruption precursor diagnostics.",
 ],
 "citations": [
  "Baldwin MP et al. (2001) The quasi-biennial oscillation. Reviews of Geophysics 39.",
 ],
 "demo": {"t0": 285.15, "gamma": 4.0, "z": 11.0},
},
# ----------------------------------------------------------------- rank 21
{
 "key": "as-mjo",
 "name": "The Madden Julian Oscillation Problem",
 "group": "Atmospheric Dynamics",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "The MJO - the tropics' 30-60 day pulse - organizes global weather, but why do models simulate it so poorly, and what is its fundamental mechanism?",
 "background": "The Madden-Julian Oscillation - the eastward-propagating tropical convection pulse - is the dominant intraseasonal signal, modulating monsoons, hurricanes, and midlatitude weather, yet its fundamental mechanism is still debated (moisture-mode versus gravity-wave theories compete). Models simulate it poorly: the MJO is too weak, too fast, or absent - the biases trace to convection parameterization and air-sea coupling. The MJO is subseasonal prediction's biggest prize and the models' persistent failure. Field campaigns (DYNAMO) advanced observations without settling the mechanism.",
 "why_it_matters": "The MJO organizes tropical weather on the 2-6 week horizon - the subseasonal gap. Its poor simulation is the gap's cause.",
 "sig_lens": "The Signature lens reads the MJO as the tropics' heartbeat: the protocol must find the heart's mechanism and teach the models to feel the pulse.",
 "sig_solution": LABEL + " Assumptions: (1) mechanism debated (moisture-mode vs gravity-wave); (2) models simulate it poorly. Reasoning path: discriminate the mechanisms observationally, then fix the parameterizations the winning mechanism implicates. Proposed mechanism: a heartbeat protocol with mechanism-discriminating observations (moisture budgets, wave diagnostics), convection-scheme development targeting MJO fidelity, and MJO-skill-weighted subseasonal forecasts. Confirm: mechanism-guided schemes improve MJO simulation. Kill: the mechanisms prove indistinguishable. Does NOT claim: the MJO mechanism - it finds the heartbeat's cause.",
 "pointer": "The Signature system's proposed approach discriminates MJO mechanisms to fix model simulation; the companion Signature Edition record specifies the heartbeat protocol.",
 "key_points": [
  "The MJO is the dominant 30-60 day tropical signal.",
  "Its fundamental mechanism is still debated.",
  "Models simulate it too weak, too fast, or not at all.",
  "It is subseasonal prediction's biggest prize.",
 ],
 "requirements": [
  "Mechanism-discriminating MJO observations.",
  "Convection-scheme development for MJO fidelity.",
  "MJO-skill-weighted subseasonal forecasts.",
 ],
 "citations": [
  "Madden RA, Julian PR (1971) Detection of a 40-50 day oscillation. J. Atmospheric Sciences 28.",
 ],
 "demo": {"t0": 299.15, "gamma": 6.0, "z": 4.0},
},
# ----------------------------------------------------------------- rank 22
{
 "key": "as-blocking",
 "name": "The Blocking Highs Problem",
 "group": "Atmospheric Dynamics",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Blocking highs stall the jet stream for weeks, baking heat waves and flooding - but why do they form, and why do models underpredict them?",
 "background": "Atmospheric blocking - persistent high-pressure systems diverting the jet - causes the worst midlatitude extremes: the 2003 European heat wave, the 2010 Russian heat wave, prolonged floods. But blocking onset is hard to predict (the models' week-2 skill collapses on blocks), and climate models systematically underpredict blocking frequency - the bias with the biggest extreme-weather consequence. Theories (eddy-driven, diabatic, wave-breaking) compete; the predictability limit is unknown. Under warming, blocking trends are uncertain - the models that underpredict blocks cannot project their future.",
 "why_it_matters": "Blocks cause the worst heat waves and floods. The most underpredicted phenomenon causes the most extreme impacts.",
 "sig_lens": "The Signature lens reads blocks as traffic jams in the sky: the protocol must find what causes the jam and warn before the heat builds.",
 "sig_solution": LABEL + " Assumptions: (1) models underpredict blocking frequency; (2) onset theories compete. Reasoning path: diagnose the jam's causes - test onset theories against the observed blocks, and fix the model biases the tests reveal. Proposed mechanism: a traffic-jam protocol with blocking-onset diagnostic studies, targeted model development on the diagnosed deficiencies, and extended-range extreme forecasts conditioned on blocking precursors. Confirm: diagnosed models improve blocking frequency. Kill: the onset proves inherently unpredictable. Does NOT claim: exact blocking prediction - it diagnoses the jam.",
 "pointer": "The Signature system's proposed approach diagnoses blocking onset to fix model biases; the companion Signature Edition record specifies the traffic-jam protocol.",
 "key_points": [
  "Blocking causes the worst midlatitude heat waves and floods.",
  "Models systematically underpredict blocking frequency.",
  "Onset theories (eddy, diabatic, wave-breaking) compete.",
  "Warming trends in blocking are uncertain.",
 ],
 "requirements": [
  "Blocking-onset diagnostic studies.",
  "Targeted model development on diagnosed deficiencies.",
  "Blocking-precursor-conditioned extreme forecasts.",
 ],
 "citations": [
  "Woollings T (2010) Dynamical influences on European climate. Weather 65.",
 ],
 "demo": {"t0": 291.15, "gamma": 5.0, "z": 5.0},
},
# ----------------------------------------------------------------- rank 23
{
 "key": "as-jet",
 "name": "The Jet Stream Meandering Problem",
 "group": "Atmospheric Dynamics",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "The jet stream's waves steer storms - but is Arctic warming making it wavier, and do wavier jets cause more extreme weather?",
 "background": "The jet stream-meandering hypothesis (Francis and Vavrus, 2012) - Arctic amplification weakening the jet, making it wavier and slower, causing persistent extremes - is the most debated idea in modern meteorology: the mechanism is plausible, but the evidence is contested (the waviness trends are sensitive to metric and period; causality is unproven). The debate matters because it links Arctic change to midlatitude extremes directly. Models show mixed responses; the observations are short. The waviness question is the Arctic-midlatitude linkage's central battleground.",
 "why_it_matters": "If Arctic warming waves the jet and the waves cause persistent extremes, the Arctic's fate is the midlatitudes' weather. The contested link is the contested future.",
 "sig_lens": "The Signature lens reads the jet as a river in the sky: the protocol must measure whether the river is truly meandering more, before blaming it for the floods.",
 "sig_solution": LABEL + " Assumptions: (1) waviness trends are metric-sensitive; (2) causality unproven. Reasoning path: settle the measurement first - agree on waviness metrics, then test the Arctic linkage with the agreed measures. Proposed mechanism: a river protocol with standardized waviness metrics, Arctic-midlatitude linkage tests on the standardized measures, and extreme-attribution conditioned on the settled science. Confirm: standardized metrics show consistent trends. Kill: the metrics never agree and the debate persists. Does NOT claim: the waviness answer - it measures the river honestly first.",
 "pointer": "The Signature system's proposed approach standardizes jet-waviness measurement before attributing extremes; the companion Signature Edition record specifies the river protocol.",
 "key_points": [
  "The Francis-Vavrus hypothesis links Arctic warming to wavier jets.",
  "Waviness trends are sensitive to metric and period.",
  "Causality between waviness and extremes is unproven.",
  "Models show mixed jet responses to warming.",
 ],
 "requirements": [
  "Standardized jet-waviness metrics.",
  "Arctic-midlatitude linkage tests on agreed measures.",
  "Attribution conditioned on settled measurement.",
 ],
 "citations": [
  "Francis JA, Vavrus SJ (2012) Evidence linking Arctic amplification to extreme weather. GRL 39.",
 ],
 "demo": {"t0": 289.15, "gamma": 4.8, "z": 6.0},
},
# ----------------------------------------------------------------- rank 24
{
 "key": "as-sensitivity",
 "name": "The Climate Sensitivity Problem",
 "group": "Climate",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "How much will the planet warm for doubled CO2 - and why, after decades, does the answer still span a factor of two?",
 "background": "Equilibrium climate sensitivity (ECS) - warming for doubled CO2 - is the most important number in climate science, yet estimates long spanned 1.5-4.5 C; the Sherwood et al. (2020) assessment narrowed it to 2.6-3.9 C (likely) using multiple lines of evidence. But the narrowing rests on combining paleoclimate, historical, and process evidence whose independence is debated, and CMIP6 models spread wider than the assessed range. The remaining uncertainty is dominated by cloud feedbacks. The most important number is still uncertain by a factor that decides the century.",
 "why_it_matters": "ECS sets the allowable carbon budget. The factor-of-two span is the difference between manageable and catastrophic policy space.",
 "sig_lens": "The Signature lens reads sensitivity as the planet's fever response: the protocol must take the temperature with every thermometer and report the honest range.",
 "sig_solution": LABEL + " Assumptions: (1) evidence lines' independence debated; (2) models spread wider than assessed. Reasoning path: keep constraining with independent evidence - paleoclimate, historical, process - and report the honest range. Proposed mechanism: a fever protocol with multi-evidence sensitivity assessments, cloud-feedback-focused process constraints, and policy guidance carrying the full assessed range. Confirm: new evidence continues narrowing the range. Kill: the evidence lines prove dependent and the range re-widens. Does NOT claim: the exact sensitivity - it takes every thermometer's reading.",
 "pointer": "The Signature system's proposed approach constrains climate sensitivity with multiple independent evidence lines; the companion Signature Edition record specifies the fever protocol.",
 "key_points": [
  "ECS estimates long spanned 1.5-4.5 C; assessed now at 2.6-3.9 C likely.",
  "The narrowing combines evidence lines of debated independence.",
  "CMIP6 models spread wider than the assessed range.",
  "Cloud feedbacks dominate the remaining uncertainty.",
 ],
 "requirements": [
  "Multi-evidence sensitivity assessments.",
  "Cloud-feedback process constraints.",
  "Policy guidance carrying the full range.",
 ],
 "citations": [
  "Sherwood SC et al. (2020) An assessment of Earth's climate sensitivity. Reviews of Geophysics 58.",
 ],
 "demo": {"t0": 294.15, "gamma": 5.5, "z": 4.0},
},
# ----------------------------------------------------------------- rank 25
{
 "key": "as-hydro-amplify",
 "name": "The Hydrological Cycle Amplification Problem",
 "group": "Climate",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Warming should intensify the water cycle - wet gets wetter, dry gets drier - but do the observations actually show it, and where does the paradigm break?",
 "background": "The wet-gets-wetter paradigm - warming intensifies moisture transport, amplifying precipitation contrasts - is thermodynamically robust, but the observations are messy: ocean salinity shows the pattern, yet regional precipitation trends are noisy and some 'dry gets drier' regions are greening. The dynamics (circulation changes) oppose the thermodynamics in places; land-ocean contrasts complicate the pattern. The paradigm works in the zonal mean and breaks regionally - exactly where water planning needs it. The amplification is real in theory, patchy in practice.",
 "why_it_matters": "Water planning assumes wet-wetter/dry-drier. Where the paradigm breaks regionally, the plans misallocate the future's water.",
 "sig_lens": "The Signature lens reads the water cycle as an amplifier with static: the protocol must separate the amplified signal from the regional noise before tuning the plans.",
 "sig_solution": LABEL + " Assumptions: (1) thermodynamics robust; dynamics oppose regionally; (2) observations noisy. Reasoning path: map where the paradigm holds and where it breaks - then plan water on the mapped pattern, not the slogan. Proposed mechanism: an amplifier protocol with regional wet-wetter/dry-drier verification, circulation-aware projections where dynamics dominate, and water plans conditioned on the verified pattern. Confirm: verified-pattern plans outperform slogan plans. Kill: the regional pattern proves unpredictable. Does NOT claim: universal amplification - it maps the signal through the static.",
 "pointer": "The Signature system's proposed approach verifies hydrological amplification regionally for water planning; the companion Signature Edition record specifies the amplifier protocol.",
 "key_points": [
  "Wet-gets-wetter is thermodynamically robust.",
  "Ocean salinity shows the pattern; regional rain trends are noisy.",
  "Circulation changes oppose thermodynamics in places.",
  "The paradigm holds zonally, breaks regionally.",
 ],
 "requirements": [
  "Regional amplification verification.",
  "Circulation-aware projections where dynamics dominate.",
  "Water plans on verified patterns.",
 ],
 "citations": [
  "Held IM, Soden BJ (2006) Robust responses of the hydrological cycle to global warming. J. Climate 19.",
 ],
 "demo": {"t0": 297.15, "gamma": 6.0, "z": 3.5},
},
# ----------------------------------------------------------------- rank 26
{
 "key": "as-cyclone-freq",
 "name": "The Tropical Cyclone Frequency Problem",
 "group": "Climate",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Will warming bring more hurricanes or fewer - and why do the models' answers depend on resolutions they cannot afford?",
 "background": "Tropical cyclone frequency under warming is deeply uncertain: most models project fewer total storms but more intense ones - yet the frequency projection depends on model resolution and convection scheme, and the theories (genesis potential indices, ventilation) disagree. The observations show no clear global frequency trend (the record is short and heterogeneous). Meanwhile the storms that do form carry more rain and intensify faster - the impacts grow even if the count falls. The frequency question that the public asks is the one science answers worst.",
 "why_it_matters": "Coastal planning asks 'more or fewer storms'; science answers best on intensity, worst on frequency. The asked question is the unanswered one.",
 "sig_lens": "The Signature lens reads cyclone frequency as the wrong question asked well: the protocol must answer the impacts (rain, intensity, speed) while honestly bounding the count.",
 "sig_solution": LABEL + " Assumptions: (1) frequency projections are resolution- and scheme-dependent; (2) impacts grow regardless. Reasoning path: plan on the robust impacts - rainfall, intensification, slowdown - and bound the frequency honestly. Proposed mechanism: an impacts protocol with high-resolution cyclone modeling for the robust signals, frequency projections reported with the model-dependence shown, and coastal planning on the impact metrics. Confirm: impact-based plans prove more robust than frequency-based. Kill: the impacts prove as uncertain as the frequency. Does NOT claim: the future storm count - it plans on the robust impacts.",
 "pointer": "The Signature system's proposed approach plans coasts on robust cyclone impact metrics; the companion Signature Edition record specifies the impacts protocol.",
 "key_points": [
  "Models project fewer but more intense storms - uncertainly.",
  "Frequency projections depend on resolution and schemes.",
  "No clear observed global frequency trend exists.",
  "Rainfall and intensification impacts grow regardless.",
 ],
 "requirements": [
  "High-resolution modeling of robust impact signals.",
  "Frequency projections with model-dependence disclosed.",
  "Coastal planning on impact metrics.",
 ],
 "citations": [
  "Knutson T et al. (2020) Tropical cyclones and climate change assessment. BAMS 101(3).",
 ],
 "demo": {"t0": 301.15, "gamma": 6.5, "z": 3.0},
},
# ----------------------------------------------------------------- rank 27
{
 "key": "as-tipping",
 "name": "The Climate Tipping Points Problem",
 "group": "Climate",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Ice sheets, rainforests, and ocean currents may have tipping points - but where are the thresholds, and how close are we?",
 "background": "Climate tipping points - thresholds where subsystems (Greenland ice, Amazon, AMOC, permafrost) shift irreversibly - are the nightmare scenario, but the thresholds are deeply uncertain: the AMOC's stability is debated (models vs. the 'cold blob' observations), Amazon dieback thresholds depend on deforestation-plus-climate interactions, and ice-sheet thresholds span degrees. Early-warning signals (critical slowing down) work in models better than in noisy reality. The tipping discourse runs ahead of the threshold science - the alarm is real, the distances unknown.",
 "why_it_matters": "Tipping points are the irreversible catastrophes. Unknown thresholds mean the safe carbon budget may already be spent - or may have room.",
 "sig_lens": "The Signature lens reads tipping points as cliffs in fog: the protocol must map the fog (the uncertainty) and stop the march before the edge is felt.",
 "sig_solution": LABEL + " Assumptions: (1) thresholds deeply uncertain; (2) early warnings work better in models. Reasoning path: bound the cliffs - use the precautionary margin on the nearest thresholds while improving the threshold science. Proposed mechanism: a cliffs protocol with tipping-element monitoring (AMOC, ice sheets, Amazon), threshold research prioritized by proximity, and carbon budgets carrying tipping-risk margins. Confirm: monitored elements show earlier warnings. Kill: the thresholds prove unknowable and margins are arbitrary. Does NOT claim: the tipping distances - it maps the fog and stops the march early.",
 "pointer": "The Signature system's proposed approach monitors tipping elements with precautionary carbon margins; the companion Signature Edition record specifies the cliffs protocol.",
 "key_points": [
  "Tipping thresholds (AMOC, Amazon, ice sheets) are deeply uncertain.",
  "Early-warning signals work better in models than reality.",
  "The tipping discourse runs ahead of threshold science.",
  "Unknown thresholds make the safe budget unknown.",
 ],
 "requirements": [
  "Tipping-element monitoring systems.",
  "Threshold research prioritized by proximity.",
  "Carbon budgets with tipping-risk margins.",
 ],
 "citations": [
  "Lenton TM et al. (2008) Tipping elements in the Earth's climate system. PNAS 105(6).",
 ],
 "demo": {"t0": 292.15, "gamma": 5.0, "z": 5.0},
},
# ----------------------------------------------------------------- rank 28
{
 "key": "as-paleo-mismatch",
 "name": "The Paleoclimate Data Model Mismatch Problem",
 "group": "Climate",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Models and paleoclimate data disagree on past warm periods - so are the models wrong about the past, or are the proxies misread?",
 "background": "Paleoclimate model-data mismatches - the early Eocene's equable climate, the Holocene temperature conundrum, the Last Glacial Maximum's tropical cooling - challenge the models: either the models miss feedbacks (clouds, vegetation) or the proxies are misread (seasonal biases, calibration). Each mismatch resolved teaches something (the Eocene needed better clouds); each unresolved one questions future projections. The mismatches are the out-of-sample tests the models cannot dodge - the past is the only experiment with a different climate.",
 "why_it_matters": "Future projections rest on models tested against the past. Unresolved mismatches are failed tests - the projections inherit the doubt.",
 "sig_lens": "The Signature lens reads mismatches as failed exams: the protocol must make the models retake them (with better physics) rather than excuse the failures.",
 "sig_solution": LABEL + " Assumptions: (1) mismatches implicate models or proxies; (2) each resolved mismatch teaches. Reasoning path: resolve the mismatches systematically - test whether model physics or proxy interpretation yields, and carry the lesson into projections. Proposed mechanism: an exams protocol with systematic model-data comparison for key periods, targeted physics development on the failures, and projection confidence conditioned on paleoclimate test performance. Confirm: exam-passing models show better-constrained projections. Kill: the mismatches prove irresolvable. Does NOT claim: perfect paleoclimate models - it makes them retake the exams.",
 "pointer": "The Signature system's proposed approach resolves paleoclimate mismatches to condition projection confidence; the companion Signature Edition record specifies the exams protocol.",
 "key_points": [
  "Models and proxies disagree on Eocene, Holocene, and LGM climates.",
  "Mismatches implicate missing feedbacks or misread proxies.",
  "Resolved mismatches (Eocene clouds) improved the models.",
  "The past is the only out-of-sample climate experiment.",
 ],
 "requirements": [
  "Systematic model-data comparison for key periods.",
  "Physics development targeting the failures.",
  "Projection confidence conditioned on paleo performance.",
 ],
 "citations": [
  "Harrison SP et al. (2015) Evaluation of CMIP5 palaeosimulations. Climate of the Past 11.",
 ],
 "demo": {"t0": 290.15, "gamma": 4.5, "z": 6.0},
},
# ----------------------------------------------------------------- rank 29
{
 "key": "as-urban-chem",
 "name": "The Urban Air Chemistry Problem",
 "group": "Atmospheric Chemistry",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "City air chemistry - ozone, particles, toxics - behaves nonlinearly, so why do pollution controls sometimes backfire, and how can the chemistry be managed?",
 "background": "Urban air chemistry is famously nonlinear: cutting NOx can increase ozone (the NOx-saturated regime); particle chemistry depends on the gas-phase mix; and the VOC/NOx ratio decides the ozone response. Controls designed on linear intuition backfire - the weekend ozone effect (lower NOx, higher ozone) is the classic example. Models (chemical transport models) capture the nonlinearity approximately but need emissions inventories that are wrong (missing sources, wrong speciation). Managing urban air needs the chemistry right; the chemistry is the hard part.",
 "why_it_matters": "Billions breathe urban air; controls cost billions. Nonlinear chemistry means the expensive control can worsen the air it was meant to clean.",
 "sig_lens": "The Signature lens reads urban chemistry as a nonlinear machine: the protocol must test the controls on the machine's actual settings before deploying them.",
 "sig_solution": LABEL + " Assumptions: (1) chemistry is nonlinear; linear-intuition controls backfire; (2) emission inventories are wrong. Reasoning path: test controls in the model before the street - run the chemical transport model on the proposed controls with the nonlinearity explicit. Proposed mechanism: a machine protocol with control-scenario modeling before implementation, regime diagnosis (NOx- vs VOC-limited) per city, and post-implementation verification against the modeled outcome. Confirm: modeled-first controls avoid the backfires. Kill: the inventories prove too wrong for useful modeling. Does NOT claim: exact urban chemistry - it tests the machine's settings first.",
 "pointer": "The Signature system's proposed approach tests air-quality controls in chemical models before deployment; the companion Signature Edition record specifies the machine protocol.",
 "key_points": [
  "Cutting NOx can increase ozone in NOx-saturated regimes.",
  "The VOC/NOx ratio decides the ozone response.",
  "Emission inventories miss sources and mis-speciate.",
  "Controls designed linearly backfire nonlinearly.",
 ],
 "requirements": [
  "Pre-implementation control-scenario modeling.",
  "Per-city chemical regime diagnosis.",
  "Post-implementation verification.",
 ],
 "citations": [
  "Haagen-Smit AJ (1952) Chemistry and physiology of Los Angeles smog. Industrial and Engineering Chemistry 44.",
 ],
 "demo": {"t0": 298.15, "gamma": 6.0, "z": 1.5},
},
# ----------------------------------------------------------------- rank 30
{
 "key": "as-geoengineering",
 "name": "The Geoengineering Governance Problem",
 "group": "Climate",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Solar geoengineering could cool the planet - but who decides the thermostat, and how can the science proceed without the governance?",
 "background": "Solar radiation modification (stratospheric aerosol injection) could offset warming cheaply and fast - but the side effects (precipitation shifts, ozone impacts, termination shock) are uncertain, the models disagree, and the governance is absent: no treaty authorizes planetary thermostat-setting, and unilateral deployment is conceivable. The moral hazard (geoengineering talk weakening mitigation) is real. Research itself is contested - field experiments face opposition. The technology that could cool the planet has no legitimate decision process and incomplete science.",
 "why_it_matters": "A cheap planetary thermostat with no governance is the most dangerous technology without an owner. The science-governance gap is the risk.",
 "sig_lens": "The Signature lens reads geoengineering as a thermostat without an owner: the protocol must build the ownership (governance) before the technology, not after.",
 "sig_solution": LABEL + " Assumptions: (1) side effects uncertain; models disagree; (2) no legitimate decision process exists. Reasoning path: govern first - build the decision framework while the research proceeds transparently, with no deployment without it. Proposed mechanism: an ownership protocol with transparent, internationally governed research programs, staged governance (research governance now, deployment governance before any deployment), and mitigation-protection against moral hazard. Confirm: governed research proceeds without deployment pressure. Kill: governance proves impossible and research enables rogue deployment. Does NOT claim: safe geoengineering - it builds the ownership before the thermostat.",
 "pointer": "The Signature system's proposed approach builds geoengineering governance alongside transparent research; the companion Signature Edition record specifies the ownership protocol.",
 "key_points": [
  "Stratospheric aerosol injection could cool fast and cheaply.",
  "Side effects (precipitation, ozone, termination shock) uncertain.",
  "No treaty or process authorizes planetary thermostat-setting.",
  "Moral hazard for mitigation is real.",
 ],
 "requirements": [
  "Internationally governed transparent research.",
  "Staged governance (research now, deployment before deployment).",
  "Mitigation-protection safeguards.",
 ],
 "citations": [
  "NRC (2015) Climate Intervention: Reflecting Sunlight to Cool Earth. National Academies Press.",
 ],
 "demo": {"t0": 293.15, "gamma": 5.5, "z": 7.0},
},
# ----------------------------------------------------------------- rank 31
{
 "key": "as-atmos-elec",
 "name": "The Atmospheric Electricity Problem",
 "group": "Atmospheric Electricity",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "The global electric circuit - thunderstorms charging the ionosphere - couples weather to space, but how does the circuit actually work?",
 "background": "The global electric circuit - thunderstorms as batteries maintaining the ionosphere-Earth potential difference (~250 kV), with fair-weather current closing the loop - is textbook physics with untextbook gaps: the conduction current's variability, the role of electrified shower clouds (not just thunderstorms), and the coupling to cosmic rays and space weather are poorly quantified. The circuit may link solar activity to clouds (the Svensmark hypothesis is contested). Carnegie-curve measurements are sparse; the circuit's monitoring lapsed for decades. The planet's electrical system is the least-monitored global circuit.",
 "why_it_matters": "The circuit couples thunderstorms to the ionosphere and possibly solar activity to clouds. The unmonitored circuit is the unmeasured coupling.",
 "sig_lens": "The Signature lens reads the global circuit as the planet's wiring: the protocol must rewire the monitoring (restore it) before theorizing about the current.",
 "sig_solution": LABEL + " Assumptions: (1) monitoring lapsed for decades; (2) solar-cloud coupling contested. Reasoning path: restore the monitoring first - rebuild the global electric-circuit observatory network, then test the couplings. Proposed mechanism: a wiring protocol with restored fair-weather current and ionospheric potential monitoring, shower-cloud electrification studies, and solar-circuit-cloud tests on the monitored data. Confirm: monitored circuits reveal the couplings' true strength. Kill: the signals prove too weak to detect. Does NOT claim: the solar-cloud link - it rewires the monitoring first.",
 "pointer": "The Signature system's proposed approach restores global electric-circuit monitoring; the companion Signature Edition record specifies the wiring protocol.",
 "key_points": [
  "Thunderstorms maintain ~250 kV ionosphere-Earth potential.",
  "Electrified shower clouds' role is poorly quantified.",
  "Cosmic-ray/solar coupling to clouds is contested.",
  "Circuit monitoring lapsed for decades.",
 ],
 "requirements": [
  "Restored global circuit monitoring network.",
  "Shower-cloud electrification studies.",
  "Solar-circuit-cloud tests on monitored data.",
 ],
 "citations": [
  "Williams ER (2009) The global electrical circuit. Atmospheric Research 91.",
 ],
 "demo": {"t0": 291.15, "gamma": 5.0, "z": 8.0},
},
# ----------------------------------------------------------------- rank 32
{
 "key": "as-nlc",
 "name": "The Noctilucent Clouds Problem",
 "group": "Atmospheric Dynamics",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Noctilucent clouds - the highest clouds on Earth - are spreading, but are they a sign of climate change, and how do they form?",
 "background": "Noctilucent (night-shining) clouds - ice clouds at ~83 km in the polar summer mesopause, the coldest place in the atmosphere - have been observed spreading to lower latitudes and brightening, possibly signaling mesospheric climate change (cooling from CO2, moistening from methane oxidation). But the record is short and observer-biased; the formation microphysics (nucleation on meteoric smoke) is uncertain; and the trend attribution is contested. The AIM satellite advanced the science; the interpretation remains open. The highest clouds may be the mesosphere's climate signal - or observer bias.",
 "why_it_matters": "The mesosphere is climate change's neglected frontier. The highest clouds may be its signal - if the signal is real.",
 "sig_lens": "The Signature lens reads noctilucent clouds as the mesosphere's diary: the protocol must separate the diary's true entries from the observer's handwriting.",
 "sig_solution": LABEL + " Assumptions: (1) record short and observer-biased; (2) formation microphysics uncertain. Reasoning path: standardize the observations - satellite-era homogeneous records - and test the climate attribution on them. Proposed mechanism: a diary protocol with homogenized noctilucent-cloud records, meteoric-smoke nucleation studies, and attribution tests against mesospheric cooling/moistening. Confirm: homogenized records show robust trends. Kill: the trends prove observer bias. Does NOT claim: the climate signal - it separates the diary from the handwriting.",
 "pointer": "The Signature system's proposed approach homogenizes noctilucent-cloud records for attribution; the companion Signature Edition record specifies the diary protocol.",
 "key_points": [
  "Noctilucent clouds form at ~83 km, the coldest atmospheric region.",
  "They appear to be spreading and brightening.",
  "Mesospheric CO2 cooling and methane moistening are candidate drivers.",
  "The record is short and observer-biased.",
 ],
 "requirements": [
  "Homogenized satellite-era cloud records.",
  "Meteoric-smoke nucleation research.",
  "Attribution tests on homogenized data.",
 ],
 "citations": [
  "Russell JM III et al. (2009) The Aeronomy of Ice in the Mesosphere (AIM) mission. J. Atmospheric and Solar-Terrestrial Physics 71.",
 ],
 "demo": {"t0": 278.15, "gamma": 2.5, "z": 15.0},
},
# ----------------------------------------------------------------- rank 33
{
 "key": "as-tides",
 "name": "The Atmospheric Tides Problem",
 "group": "Atmospheric Dynamics",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "The atmosphere has tides like the ocean - but how do the migrating and non-migrating tides shape the upper atmosphere, and why do models miss them?",
 "background": "Atmospheric tides - global-scale waves driven by solar heating (and lunar gravity) - dominate the mesosphere and lower thermosphere's dynamics, modulating the ionosphere and satellite drag. But the non-migrating tides (not sun-synchronous, driven by latent heating and topography) are hard to observe and harder to model: their sources (tropical convection patterns) are the convection-parameterization problem again, at 100 km altitude. Whole-atmosphere models are new and uncertain; the tidal spectrum's variability with the QBO and SSW is observed but unpredicted. The upper atmosphere's weather is tidal - and the tides are under-forecast.",
 "why_it_matters": "Tides modulate the ionosphere (GPS, radio) and satellite drag. The under-forecast tides are space infrastructure's weather.",
 "sig_lens": "The Signature lens reads atmospheric tides as the upper atmosphere's weather: the protocol must observe the tides' sources (the tropical convection) to forecast their effects.",
 "sig_solution": LABEL + " Assumptions: (1) non-migrating tides are hard to observe and model; (2) sources are the convection problem at altitude. Reasoning path: constrain the tidal sources - observe tropical heating patterns and feed them to whole-atmosphere models. Proposed mechanism: a tides protocol with tidal-source observations, whole-atmosphere model development, and ionosphere/drag forecasts carrying tidal variability. Confirm: source-constrained models improve tidal prediction. Kill: the sources prove unobservable usefully. Does NOT claim: exact tidal prediction - it forecasts the upper weather from its sources.",
 "pointer": "The Signature system's proposed approach constrains atmospheric tidal sources for whole-atmosphere forecasting; the companion Signature Edition record specifies the tides protocol.",
 "key_points": [
  "Atmospheric tides dominate mesosphere/lower-thermosphere dynamics.",
  "Non-migrating tides are driven by latent heating and topography.",
  "Tidal sources are the convection problem at 100 km.",
  "Tides modulate GPS, radio, and satellite drag.",
 ],
 "requirements": [
  "Tropical tidal-source heating observations.",
  "Whole-atmosphere model development.",
  "Tidal-variability space-weather forecasts.",
 ],
 "citations": [
  "Forbes JM (1995) Tidal and planetary waves. In The Upper Mesosphere and Lower Thermosphere. AGU.",
 ],
 "demo": {"t0": 283.15, "gamma": 3.5, "z": 12.0},
},
# ----------------------------------------------------------------- rank 34
{
 "key": "as-unified",
 "name": "The Unified Atmosphere Problem",
 "group": "Climate",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "The atmosphere is one fluid from the surface to space - but the science is split into weather, climate, chemistry, and space, so can it be understood as a whole?",
 "background": "The atmosphere's layers and disciplines are studied separately: tropospheric weather, stratospheric dynamics, mesospheric tides, thermospheric space weather, atmospheric chemistry - each with its models and communities. But the couplings cross every boundary: SSWs reach the surface, the QBO modulates the MJO, tides couple to the ionosphere, chemistry feeds back to climate. Whole-atmosphere models (WACCM-X and successors) attempt the union but are young and uncertain. The seamless prediction vision - one model from surface to space, weather to climate - is the aspiration; disciplinary fragmentation is the reality.",
 "why_it_matters": "The couplings cross every disciplinary boundary: the surface feels the stratosphere, the ionosphere feels the tides. Fragmented science misses the connections.",
 "sig_lens": "The Signature lens reads the atmosphere as one ocean of air: the protocol must sail it whole - coupling the layers in models and monitoring the boundaries where they meet.",
 "sig_solution": LABEL + " Assumptions: (1) couplings cross every boundary; (2) whole-atmosphere models are young. Reasoning path: build the union where the couplings matter most - stratosphere-surface, tide-ionosphere - and monitor the layer boundaries. Proposed mechanism: an ocean protocol with whole-atmosphere model development prioritized by coupling strength, boundary-layer (tropopause, mesopause) monitoring, and seamless prediction systems from weather to space weather. Confirm: coupled systems beat fragmented ones on cross-boundary events. Kill: the couplings prove too weak to justify the union. Does NOT claim: a solved atmosphere - it sails the one ocean whole.",
 "pointer": "The Signature system's proposed approach unifies atmospheric layers in whole-atmosphere modeling; the companion Signature Edition record specifies the ocean protocol.",
 "key_points": [
  "Atmospheric couplings cross every disciplinary boundary.",
  "SSWs reach the surface; tides reach the ionosphere.",
  "Whole-atmosphere models are young and uncertain.",
  "Seamless surface-to-space prediction is the aspiration.",
 ],
 "requirements": [
  "Coupling-prioritized whole-atmosphere modeling.",
  "Layer-boundary monitoring networks.",
  "Seamless weather-to-space-weather prediction.",
 ],
 "citations": [
  "Liu HL et al. (2010) Thermosphere extension of the Whole Atmosphere Community Climate Model. JGR 115.",
 ],
 "demo": {"t0": 288.15, "gamma": 4.5, "z": 9.0},
},
]
