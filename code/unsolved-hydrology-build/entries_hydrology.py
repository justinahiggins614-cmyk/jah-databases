#!/usr/bin/env python3
"""Entries for The Unsolved Hydrology Database (unsolved-hydrology) and its
Signature half (unsolved-hydrology-signature).

34 famous unsolved problems in hydrology, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
through the Signature lens, ALWAYS labeled as proposals, never established
science.

ID prefixes JAH-USHY- / JAH-USHYS- verified free in manifest id_prefix
values (exact + substring, both directions).
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

FIELD = {
 "tag": "hydrology",
 "disp": "hydrology",
 "name": "The Unsolved Hydrology Database",
 "sig_name": "The Unsolved Hydrology Signature Database",
 "prefix": "JAH-USHY-",
 "sig_prefix": "JAH-USHYS-",
 "ai": "JAH Unsolved Hydrology Archivist",
 "tagline": ("Thirty-four famous open problems in hydrology, from ungauged basins to the unified water cycle: "
             "real, fact-checked, each with its full story and a clearly labeled Signature proposed solution."),
 "sig_tagline": ("His original Signature solution method applied to all 34 great open problems of hydrology: "
                 "Signature-generated proposed solutions with assumptions declared, confirm and refute conditions "
                 "stated, and limits honestly marked. Clearly labeled Signature-made, never established science."),
 "pub_line": ("Public records - 34 famous open problems in hydrology, real and fact-checked: predicting ungauged "
              "basins, baseflow separation, the unit hydrograph, evapotranspiration partitioning, aquifer recharge, "
              "snowmelt timing, flash floods, drought propagation, urban hydrology, seawater intrusion, and "
              "environmental flows - every record carrying the problem statement, background, why it matters, key "
              "points, requirements, standards, citations, and a working solution-explorer demonstration, "
              "organized in the Signature system."),
 "sig_line": ("Signature originals - his original Signature solution method: the same 34 famous unsolved "
              "hydrology problems approached as a covenant between the known and the unknown, each carrying the "
              "full Signature-generated proposed solution with its assumptions declared, its confirm and refute "
              "conditions stated, and its limits honestly marked. Clearly labeled Signature-made, never presented "
              "as established science or authentic public record."),
 "ladder_text": (" Records are ordered by the teaching ladder: Foundations (ungauged basins, baseflow "
                 "separation, unit hydrograph, evapotranspiration partitioning, recharge estimation, snowmelt "
                 "timing, flash floods, drought propagation, urban hydrology, seawater intrusion, environmental "
                 "flows) -> Compounded (groundwater-surface water interaction, karst aquifers, fractured rock, "
                 "preferential flow, glacier melt, permafrost thaw, nonstationary flood frequency, drought "
                 "indices, hydrological scaling, equifinality, structural uncertainty, data assimilation) -> "
                 "Advanced (soil moisture remote sensing, GRACE depletion, water quality modeling, sediment "
                 "transport, river morphodynamics, dam removal pulses, managed aquifer recharge, green "
                 "infrastructure, isotope interpretation, paleohydrology, the unified water cycle)."),
 "search_ph": ("Search ungauged basins, baseflow, evapotranspiration, recharge, floods, drought, karst, "
               "groundwater, sediment, GRACE, isotopes..."),
 "chat_ph": "Ask about the great open problems of hydrology...",
 "greet_pub": ("I am the JAH Unsolved Hydrology Archivist. Ask me about the great open problems of hydrology - "
               "from ungauged basins, baseflow, and evapotranspiration through karst, floods, and drought, to "
               "sediment transport, isotopes, and the unified water cycle."),
 "greet_sig": ("I am the JAH Unsolved Hydrology Archivist (Signature). Ask me about the Signature proposed "
               "solutions to the great open problems of hydrology - every approach labeled as a proposal, never "
               "established science."),
 "role_pub": ("unsolved hydrology archivist - the great open problems of hydrology, from ungauged basins, "
              "baseflow, and evapotranspiration through karst, floods, and drought, to sediment transport, "
              "isotopes, and the unified water cycle; teaches progressively along the ladder from foundations "
              "through compounded to advanced; answers from many angles - definition, example, analogy, "
              "application, history, math - using only archive data from this system"),
 "role_sig": ("unsolved hydrology archivist - Signature editions: his original Signature solution method applied "
              "to the 34 great open problems of hydrology, each carrying the full Signature-generated proposed "
              "solution, clearly labeled Signature-made and never presented as established science; teaches "
              "progressively along the ladder from foundations through compounded to advanced; answers from many "
              "angles - definition, example, analogy, application, history, math - using only archive data from "
              "this system"),
 "gen_desc": "Generate clearly-labeled unsolved hydrology studies. Seeded archive records are the authoritative entries.",
 "standards": [
  "Problem statements verified against the published literature; open status confirmed as of 2026.",
  "Quantitative claims cross-checked against standard references (Chow, Maidment and Mays, Applied Hydrology; Freeze and Cherry, Groundwater).",
  "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
 ],
 "sig_tail": ("Signature editions carry the Signature system's proposed solution approaches to famous "
              "unsolved problems. Every solution is labeled a Signature-generated proposal, never "
              "established science, never peer-accepted, never proof."),
}

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "hy-pub",
 "name": "The Ungauged Basin Prediction Problem",
 "group": "Surface Water",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Most of the world's watersheds have no stream gauges - but how can floods, water supply, and drought be predicted where no measurements exist?",
 "background": "The IAHS Predictions in Ungauged Basins (PUB) decade (2003-2012) confronted hydrology's central embarrassment: models are calibrated where gauges exist and needed where they do not. Regionalization - transferring parameters from gauged to ungauged basins by similarity - is the standard answer, but similarity in what? Climate, geology, topography, land use - the relevant attributes are debated, and the transfer errors are large. The PUB synthesis concluded that prediction uncertainty in ungauged basins remains the field's defining challenge. Most flood deaths occur in ungauged basins.",
 "why_it_matters": "Water decisions are made everywhere; gauges exist almost nowhere. The ungauged prediction gap is where floods kill and droughts surprise.",
 "sig_lens": "The Signature lens reads ungauged basins as strangers: the protocol must introduce them by their measurable traits and never pretend the introduction is a friendship.",
 "sig_solution": LABEL + " Assumptions: (1) parameter transfer needs a defensible similarity basis; (2) transfer errors are large. Reasoning path: regionalize on multiple similarity measures, ensemble the transfers, and report the prediction with the ensemble spread. Proposed mechanism: a stranger protocol that characterizes ungauged basins on climate, geology, and topography signatures, transfers parameters from multiple donor sets, and issues predictions as ensembles with the spread shown. Confirm: multi-donor ensembles beat single-donor transfers on test basins. Kill: no similarity measure predicts transferability and the ensembles mislead. Does NOT claim: accurate ungauged prediction - it introduces the stranger honestly.",
 "pointer": "The Signature system's proposed approach predicts ungauged basins with multi-donor ensembles; the companion Signature Edition record specifies the stranger protocol.",
 "key_points": [
  "The PUB decade (2003-2012) made ungauged prediction the field's defining challenge.",
  "Regionalization transfers parameters by similarity; the right similarity is debated.",
  "Transfer errors remain large.",
  "Most flood deaths occur in ungauged basins.",
 ],
 "requirements": [
  "Multi-attribute basin signatures (climate, geology, topography).",
  "Multi-donor parameter transfer ensembles.",
  "Predictions issued with ensemble spreads, not point values.",
 ],
 "citations": [
  "Sivapalan M et al. (2003) IAHS Decade on Predictions in Ungauged Basins (PUB). Hydrological Sciences Journal 48(6).",
 ],
 "demo": {"n": 0.03, "w": 10.0, "d": 2.0, "s": 0.001},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "hy-baseflow",
 "name": "The Baseflow Separation Problem",
 "group": "Surface Water",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Streamflow mixes quick storm runoff with slow groundwater discharge - but how can the two be separated when only their sum is measured?",
 "background": "Baseflow separation - splitting a hydrograph into quickflow and baseflow - underlies groundwater recharge estimation, low-flow forecasting, and water budgets. But the separation is fundamentally non-unique: graphical methods (straight line, recession), digital filters (Lyne-Hollick, Eckhardt), and tracer methods (isotopes, chemistry) give different answers, sometimes wildly so. The filter parameters are tuned, not measured; the tracer methods need data rarely available. There is no ground truth - the separation is a model construct, yet water management treats it as a measurement.",
 "why_it_matters": "Recharge estimates, drought forecasts, and water rights all rest on baseflow separation. A non-unique separation treated as fact is policy built on a construct.",
 "sig_lens": "The Signature lens reads baseflow as two voices in one song: the protocol must admit the harmony cannot be unmixed perfectly, and report the range.",
 "sig_solution": LABEL + " Assumptions: (1) separation is non-unique; (2) management treats it as measurement. Reasoning path: report the ensemble - run multiple defensible separations and carry the range into decisions. Proposed mechanism: a two-voices protocol requiring multi-method baseflow separation (graphical, filter, tracer where available), reporting the method spread, and gating decisions on the spread's width. Confirm: ensemble separations bracket tracer-validated baseflow better than single methods. Kill: the methods disagree so widely the range is useless. Does NOT claim: the true baseflow - it reports the harmony's range.",
 "pointer": "The Signature system's proposed approach reports baseflow as multi-method ensembles; the companion Signature Edition record specifies the two-voices protocol.",
 "key_points": [
  "Baseflow separation methods (graphical, filter, tracer) disagree substantially.",
  "Filter parameters are tuned, not measured.",
  "No ground truth exists; separation is a model construct.",
  "Water management treats the construct as measurement.",
 ],
 "requirements": [
  "Multi-method separation on every analysis.",
  "Reported method spreads, not single separations.",
  "Decisions gated on the spread's width.",
 ],
 "citations": [
  "Eckhardt K (2005) How to construct recursive digital filters for baseflow separation. J. Hydrology 352.",
 ],
 "demo": {"n": 0.035, "w": 8.0, "d": 1.5, "s": 0.002},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "hy-unit-hydrograph",
 "name": "The Unit Hydrograph Universality Problem",
 "group": "Surface Water",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Sherman's 1932 unit hydrograph assumes linear watershed response - but watersheds are nonlinear, so when does the linear fiction work and when does it fail?",
 "background": "The unit hydrograph - the watershed's response to a unit of effective rainfall - assumes linearity and time-invariance: double the rain, double the flow. Real watersheds violate both: response depends on antecedent wetness, rainfall intensity, and spatial pattern. Yet the method persists in engineering practice (SCS, Snyder synthetic hydrographs) because it needs little data. The geomorphologic unit hydrograph (Rodriguez-Iturbe and Valdes) grounds the shape in network geometry but keeps the linearity. Nonlinear alternatives exist but need the data the method was invented to avoid. The linearity fiction survives on convenience.",
 "why_it_matters": "Flood designs across the world rest on unit hydrographs. The linear fiction's failure modes are the flood designs' failure modes.",
 "sig_lens": "The Signature lens reads the unit hydrograph as a useful lie: the protocol must know when the lie is harmless and when it floods the town.",
 "sig_solution": LABEL + " Assumptions: (1) watersheds are nonlinear; (2) the method persists on convenience. Reasoning path: test linearity per event - check whether the watershed's response scales, and use nonlinear methods where it does not. Proposed mechanism: a useful-lie protocol that tests response linearity on available events, applies unit hydrographs only where linearity holds approximately, and routes nonlinear cases to distributed models - with the linearity test reported. Confirm: tested applications show fewer flood-design surprises. Kill: the linearity test needs more data than exists. Does NOT claim: a universal hydrograph - it licenses the lie where harmless.",
 "pointer": "The Signature system's proposed approach tests watershed linearity before applying unit hydrographs; the companion Signature Edition record specifies the useful-lie protocol.",
 "key_points": [
  "The unit hydrograph assumes linear, time-invariant response (Sherman, 1932).",
  "Real response depends on wetness, intensity, and rainfall pattern.",
  "Synthetic hydrographs persist in practice on low data needs.",
  "Nonlinear alternatives need the data the method avoids.",
 ],
 "requirements": [
  "Per-event linearity testing where data allows.",
  "Unit hydrographs restricted to approximately linear cases.",
  "Nonlinear routing for cases failing the test.",
 ],
 "citations": [
  "Sherman LK (1932) Streamflow from rainfall by the unit-graph method. Engineering News Record 108.",
 ],
 "demo": {"n": 0.04, "w": 12.0, "d": 2.5, "s": 0.0008},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "hy-et-partition",
 "name": "The Evapotranspiration Partitioning Problem",
 "group": "Water Cycle",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Evapotranspiration returns most rainfall to the sky - but how much is plant transpiration versus soil evaporation, and why does the split matter?",
 "background": "ET partitioning - splitting evapotranspiration into transpiration (through plants) and evaporation (from soil and surfaces) - matters because transpiration couples to carbon uptake and plant stress while evaporation does not. But the partition is hard to measure: eddy covariance gives total ET, sap flow and isotopes give pieces, and the methods disagree. Models (Penman-Monteith variants) partition by parameterization, not measurement. The global estimates (transpiration 60-80 percent of terrestrial ET) span a range that moves the carbon cycle. In water management, the split decides whether vegetation change saves water.",
 "why_it_matters": "The T/ET split couples the water and carbon cycles. Getting it wrong misattributes both water savings and carbon uptake.",
 "sig_lens": "The Signature lens reads ET as two exhalations: the protocol must separate the plant's breath from the soil's, because only one photosynthesizes.",
 "sig_solution": LABEL + " Assumptions: (1) the partition is hard to measure; methods disagree; (2) models partition by parameterization. Reasoning path: constrain the partition with multiple independent measurements and report the constrained range. Proposed mechanism: a two-exhalations protocol combining eddy covariance, sap flow, and isotope measurements where available, using each to bound the others, and reporting T/ET as a constrained range. Confirm: constrained partitions agree better across methods. Kill: the methods' disagreements prove irreducible. Does NOT claim: the true partition - it bounds the two exhalations.",
 "pointer": "The Signature system's proposed approach constrains ET partitioning with multiple independent measurements; the companion Signature Edition record specifies the two-exhalations protocol.",
 "key_points": [
  "Transpiration couples to carbon; evaporation does not.",
  "Eddy covariance measures total ET; the split needs other methods.",
  "Global T/ET estimates span 60-80 percent.",
  "The split decides whether vegetation change saves water.",
 ],
 "requirements": [
  "Multiple independent partition measurements where available.",
  "Cross-constraint of methods against each other.",
  "T/ET reported as constrained ranges.",
 ],
 "citations": [
  "Jasechko S et al. (2013) Terrestrial water fluxes dominated by transpiration. Nature 496.",
 ],
 "demo": {"n": 0.028, "w": 15.0, "d": 1.8, "s": 0.0012},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "hy-recharge",
 "name": "The Aquifer Recharge Estimation Problem",
 "group": "Groundwater",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Sustainable pumping cannot exceed recharge - but recharge is the hardest term in the water budget to measure, so how can sustainability be judged?",
 "background": "Groundwater recharge - the water reaching the aquifer - is estimated by water-table fluctuations, chloride mass balance, tracers, and models, each with order-of-magnitude uncertainty in arid regions where it matters most. The spatial variability is extreme: focused recharge under ephemeral streams can dominate diffuse recharge, and the methods average over both. Climate change shifts recharge in unmeasured ways. Yet groundwater sustainability plans worldwide set pumping limits against recharge numbers whose uncertainty bands would embarrass the plans. The measurement gap is the governance gap.",
 "why_it_matters": "Aquifers are being mined worldwide on the basis of recharge numbers nobody can measure well. The sustainability verdict rests on the weakest number.",
 "sig_lens": "The Signature lens reads recharge as income: the protocol must audit the income honestly before approving the spending.",
 "sig_solution": LABEL + " Assumptions: (1) recharge uncertainty is order-of-magnitude in arid regions; (2) plans set limits against point estimates. Reasoning path: manage to the uncertainty - set pumping limits against the lower confidence bound of recharge, not the point estimate. Proposed mechanism: an income-audit protocol with multi-method recharge estimation, focused-versus-diffuse decomposition, and pumping limits tied to the lower confidence bound with adaptive updating as monitoring improves. Confirm: bound-managed aquifers show more stable water levels. Kill: the bounds prove too wide for any pumping to be allowed. Does NOT claim: true recharge rates - it audits the income conservatively.",
 "pointer": "The Signature system's proposed approach sets pumping limits against recharge lower-confidence bounds; the companion Signature Edition record specifies the income-audit protocol.",
 "key_points": [
  "Recharge estimation methods carry order-of-magnitude uncertainty.",
  "Focused recharge under streams can dominate diffuse recharge.",
  "Climate shifts recharge in unmeasured ways.",
  "Sustainability plans use point estimates with hidden bands.",
 ],
 "requirements": [
  "Multi-method recharge estimation with uncertainty.",
  "Focused versus diffuse recharge decomposition.",
  "Pumping limits on lower confidence bounds, adaptively updated.",
 ],
 "citations": [
  "Scanlon BR et al. (2006) Global synthesis of groundwater recharge. Water Resources Research 42.",
 ],
 "demo": {"n": 0.032, "w": 9.0, "d": 2.2, "s": 0.0015},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "hy-snowmelt",
 "name": "The Snowmelt Runoff Timing Problem",
 "group": "Surface Water",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Snowpack is the western water tower - but when will it melt, how fast, and how is the timing shifting as the climate warms?",
 "background": "Snowmelt dominates water supply across the western US, Central Asia, and the Himalayas: the timing of melt decides reservoir operations, flood risk, and irrigation. But snowpack measurement (SNOTEL, snow courses) samples points; the basin's snow water equivalent is interpolated. Energy-balance melt models need data (radiation, wind, humidity) rarely available; temperature-index models are calibrated fictions. Warming shifts precipitation from snow to rain and melt earlier - the trends are observed but the future timing is modeled with the same uncertain tools. Dust on snow (accelerating melt) adds an unmodeled forcing.",
 "why_it_matters": "A billion people depend on snowmelt timing. Earlier melt means fuller reservoirs in spring and emptier ones in summer - the timing is the supply.",
 "sig_lens": "The Signature lens reads snowpack as a frozen reservoir with a melting schedule: the protocol must track the schedule as the climate rewrites it.",
 "sig_solution": LABEL + " Assumptions: (1) point measurements interpolate uncertainly; (2) warming rewrites the schedule. Reasoning path: monitor the snowpack as a system - combine point, remote-sensing, and model estimates - and update the melt schedule continuously. Proposed mechanism: a melting-schedule protocol fusing SNOTEL, remote sensing (MODIS, lidar), and energy-balance modeling, with reservoir operations keyed to the fused snow-water-equivalent and its trend. Confirm: fused monitoring improves runoff forecasts. Kill: the fusion cannot beat the interpolation errors. Does NOT claim: exact melt timing - it tracks the rewriting schedule.",
 "pointer": "The Signature system's proposed approach fuses snowpack monitoring for melt scheduling; the companion Signature Edition record specifies the melting-schedule protocol.",
 "key_points": [
  "Snowmelt timing decides reservoir, flood, and irrigation outcomes.",
  "Point measurements interpolate to basins uncertainly.",
  "Warming shifts snow to rain and melt earlier.",
  "Dust-on-snow acceleration is largely unmodeled.",
 ],
 "requirements": [
  "Fused point, remote-sensing, and model snowpack estimates.",
  "Continuous melt-schedule updating.",
  "Reservoir operations keyed to fused estimates and trends.",
 ],
 "citations": [
  "Barnett TP et al. (2005) Potential impacts of a warming climate on water availability in snow-dominated regions. Nature 438.",
 ],
 "demo": {"n": 0.045, "w": 20.0, "d": 1.2, "s": 0.003},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "hy-flash-flood",
 "name": "The Flash Flood Prediction Problem",
 "group": "Surface Water",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Flash floods kill more people than any other flood type - but how can they be predicted with enough lead time when they form in minutes from unmeasured rainfall?",
 "background": "Flash floods - intense rainfall on small, steep, often ungauged catchments - develop in minutes to hours: the 2021 European floods and countless monsoon disasters show the toll. Prediction needs rainfall at kilometer scale (radar, nowcasting) coupled to fast hydrologic models, but radar underestimates intense rain, nowcasts decay within the hour, and the catchments are ungauged. Warning dissemination is the other half: the forecast must reach people who can act. The skill horizon for useful flash-flood warning remains brutally short.",
 "why_it_matters": "Flash floods are the deadliest flood type precisely because warning time is minimal. Every minute of skillful lead time is lives.",
 "sig_lens": "The Signature lens reads flash floods as ambushes: the protocol must watch the sky at the catchment's scale and shout the warning through every channel.",
 "sig_solution": LABEL + " Assumptions: (1) skillful lead times are brutally short; (2) warnings must reach people who can act. Reasoning path: couple nowcast rainfall to fast models at catchment scale, and pre-wire the warning dissemination. Proposed mechanism: an ambush protocol with radar-nowcast-driven flash-flood guidance, impact-based warnings (who floods, not just how much rain), and pre-established dissemination channels tested regularly. Confirm: protocol warnings show longer effective lead times. Kill: nowcast skill decays too fast for useful warning. Does NOT claim: long-lead flash-flood prediction - it maximizes the short warning honestly.",
 "pointer": "The Signature system's proposed approach couples nowcasts to catchment models with pre-wired warnings; the companion Signature Edition record specifies the ambush protocol.",
 "key_points": [
  "Flash floods develop in minutes on small ungauged catchments.",
  "Radar underestimates intense rain; nowcasts decay within the hour.",
  "Warning dissemination is half the problem.",
  "Skillful lead times remain brutally short.",
 ],
 "requirements": [
  "Radar-nowcast-driven guidance at catchment scale.",
  "Impact-based warnings (who floods).",
  "Pre-established, regularly tested dissemination channels.",
 ],
 "citations": [
  "NWS Flash Flood guidance documentation.",
 ],
 "demo": {"n": 0.05, "w": 6.0, "d": 1.0, "s": 0.008},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "hy-drought-prop",
 "name": "The Drought Propagation Problem",
 "group": "Water Cycle",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Meteorological drought becomes hydrological drought becomes socioeconomic drought - but how does the drought propagate through the system, and where can it be interrupted?",
 "background": "Drought propagates: rainfall deficit (meteorological) depletes soil moisture (agricultural), then streamflow and groundwater (hydrological), then water supply and livelihoods (socioeconomic). The propagation timescales - weeks to years - depend on catchment storage in poorly known ways, and the thresholds where one drought type triggers the next are unmapped. Human interventions (reservoirs, pumping) both mitigate and mask propagation: reservoir releases hide hydrological drought until the reservoir itself fails. The propagation science is descriptive; the interruption points are unidentified.",
 "why_it_matters": "Droughts kill through the propagation chain: the rain fails first, the wells fail last, and the interruption must happen between.",
 "sig_lens": "The Signature lens reads drought as a contagion moving through the water system: the protocol must track its spread and quarantine it at the choke points.",
 "sig_solution": LABEL + " Assumptions: (1) propagation timescales depend on poorly known storage; (2) human interventions mask and mitigate. Reasoning path: monitor the propagation chain stage by stage, and intervene at the choke points where one stage feeds the next. Proposed mechanism: a contagion protocol tracking meteorological, soil-moisture, hydrological, and supply indicators jointly, with staged interventions (demand management, conjunctive use) triggered at propagation thresholds. Confirm: staged interventions reduce socioeconomic drought severity. Kill: the thresholds prove unidentifiable and interventions mistime. Does NOT claim: drought prevention - it quarantines the propagation.",
 "pointer": "The Signature system's proposed approach tracks drought propagation stage-by-stage with staged interventions; the companion Signature Edition record specifies the contagion protocol.",
 "key_points": [
  "Drought propagates across types on timescales of weeks to years.",
  "Propagation depends on poorly known catchment storage.",
  "Reservoirs mask hydrological drought until they fail.",
  "Interruption points in the chain are unidentified.",
 ],
 "requirements": [
  "Joint multi-stage drought indicator monitoring.",
  "Propagation-threshold-triggered staged interventions.",
  "Conjunctive surface-groundwater management during propagation.",
 ],
 "citations": [
  "Van Loon AF (2015) Hydrological drought explained. WIREs Water 2(4).",
 ],
 "demo": {"n": 0.033, "w": 11.0, "d": 1.6, "s": 0.0011},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "hy-urban",
 "name": "The Urban Hydrology Problem",
 "group": "Surface Water",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Cities pave their watersheds and flood themselves - but how can urban flood risk be predicted when every city is a unique maze of pipes, pavement, and blockage?",
 "background": "Urbanization replaces infiltration with runoff: the same storm that once soaked in now floods streets. Urban hydrology models (SWMM and successors) route water through pipe networks, but the networks are incompletely mapped, inlets block with debris unpredictably, and the surface-subsurface interactions (basement flooding, surcharging manholes) defeat the models. Pluvial flooding - rain overwhelming drainage - is the growing urban risk, unmapped by river flood maps. Green infrastructure changes the hydrology parcel by parcel; the cumulative effect is unmeasured.",
 "why_it_matters": "Urban flooding damages homes that never knew they were in a floodplain. The unmapped risk is where the surprise - and the damage - concentrates.",
 "sig_lens": "The Signature lens reads the city as a watershed wearing concrete: the protocol must map the actual drainage, not the designed one.",
 "sig_solution": LABEL + " Assumptions: (1) pipe networks are incompletely mapped; (2) blockage is unpredictable. Reasoning path: map the real drainage (survey plus sensors), model pluvial flooding explicitly, and maintain the inlets. Proposed mechanism: a concrete-watershed protocol with drainage-asset mapping, pluvial flood modeling on the mapped network, inlet-maintenance programs, and green infrastructure sited by modeled benefit. Confirm: mapped-and-maintained systems flood less. Kill: the mapping never completes and the models stay fictional. Does NOT claim: exact urban flood prediction - it maps the real drainage.",
 "pointer": "The Signature system's proposed approach maps actual urban drainage and models pluvial flooding on it; the companion Signature Edition record specifies the concrete-watershed protocol.",
 "key_points": [
  "Urbanization converts infiltration to runoff.",
  "Pipe networks are incompletely mapped; inlets block unpredictably.",
  "Pluvial flooding is unmapped by river flood maps.",
  "Green infrastructure effects accumulate unmeasured.",
 ],
 "requirements": [
  "Drainage-asset mapping programs.",
  "Pluvial flood modeling on mapped networks.",
  "Inlet maintenance and benefit-sited green infrastructure.",
 ],
 "citations": [
  "Fletcher TD et al. (2013) SUDS, LID, BMPs, WSUD and more. Urban Water Journal 10(1).",
 ],
 "demo": {"n": 0.02, "w": 5.0, "d": 1.0, "s": 0.005},
},
# ----------------------------------------------------------------- rank 10
{
 "key": "hy-seawater",
 "name": "The Seawater Intrusion Control Problem",
 "group": "Groundwater",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Coastal pumping pulls seawater into freshwater aquifers - but where is the saltwater front, how fast does it move, and can it be pushed back?",
 "background": "Seawater intrusion - the landward migration of the saltwater-freshwater interface under pumping - threatens coastal water supplies worldwide (from California to Chennai). The Ghyben-Herzberg lens approximation is a crude guide; real interfaces are diffuse transition zones shaped by heterogeneity, tides, and pumping history. Monitoring (electrical resistivity, well sampling) locates the front approximately; the movement rate depends on unmeasured aquifer properties. Control (reduced pumping, injection barriers, scavenger wells) works but the sustainable yield - the pumping rate that holds the front - is uncertain. Sea-level rise pushes the boundary landward regardless.",
 "why_it_matters": "Once intruded, an aquifer is ruined for decades: the salt does not flush easily. Coastal cities are pumping toward a boundary they cannot see.",
 "sig_lens": "The Signature lens reads the saltwater front as an invading tide: the protocol must watch the shoreline underground and hold it with measured pumping.",
 "sig_solution": LABEL + " Assumptions: (1) the interface is a diffuse, heterogeneous transition zone; (2) sustainable yield is uncertain. Reasoning path: monitor the front continuously, model its movement, and pump adaptively to hold it. Proposed mechanism: a tide-watch protocol with interface monitoring (resistivity, wells), adaptive pumping limits tied to front movement, and barrier wells where the front advances. Confirm: adaptively managed coasts hold their fronts. Kill: the front moves faster than monitoring detects. Does NOT claim: exact interface prediction - it watches the tide and holds the line.",
 "pointer": "The Signature system's proposed approach monitors saltwater fronts and adapts pumping to hold them; the companion Signature Edition record specifies the tide-watch protocol.",
 "key_points": [
  "Pumping pulls the saltwater interface landward; recovery takes decades.",
  "Real interfaces are diffuse zones, not sharp fronts.",
  "Sustainable pumping rates are uncertain.",
  "Sea-level rise pushes the boundary regardless of pumping.",
 ],
 "requirements": [
  "Continuous saltwater-front monitoring.",
  "Adaptive pumping limits tied to front movement.",
  "Barrier wells where fronts advance.",
 ],
 "citations": [
  "Werner AD et al. (2013) Seawater intrusion processes, investigation and management. Advances in Water Resources 51.",
 ],
 "demo": {"n": 0.03, "w": 14.0, "d": 2.0, "s": 0.0009},
},
# ----------------------------------------------------------------- rank 11
{
 "key": "hy-eflows",
 "name": "The Environmental Flows Problem",
 "group": "Surface Water",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Rivers need water for ecosystems, not just people - but how much, when, and with what variability does a river need to stay a river?",
 "background": "Environmental flows (e-flows) - the quantity, timing, and quality of water needed to sustain ecosystems - are now legally required in many jurisdictions, but the science of how much is enough is young: the natural flow paradigm (Poff et al., 1997) says ecosystems need the natural variability, not just a minimum flow, yet implementing variability means releasing floods that water managers hoard. Methods range from hydrological rules of thumb (Tennant) to holistic habitat modeling (IFIM), each with gaps. The climate shifts the baseline: the natural flow being mimicked is itself changing. E-flow science advises; water allocation decides.",
 "why_it_matters": "Dammed and diverted rivers are dying worldwide. E-flows are the legal and scientific instrument for keeping rivers alive - if the numbers are right.",
 "sig_lens": "The Signature lens reads the river as a patient with a prescription: the protocol must write the prescription in flows, not just volumes, and fill it.",
 "sig_solution": LABEL + " Assumptions: (1) ecosystems need variability, not just minimums; (2) the baseline is shifting with climate. Reasoning path: prescribe the flow regime - magnitudes, timing, and variability - and adapt it as the climate shifts the baseline. Proposed mechanism: a prescription protocol defining e-flows as regime components (baseflows, pulses, floods), implementing them through reservoir reoperation, and monitoring ecological response to adapt the prescription. Confirm: regime-prescribed rivers show better ecological outcomes. Kill: water allocation politics overrides the prescription. Does NOT claim: the perfect e-flow - it prescribes the regime and adapts.",
 "pointer": "The Signature system's proposed approach prescribes environmental flow regimes adaptively; the companion Signature Edition record specifies the prescription protocol.",
 "key_points": [
  "Ecosystems need flow variability, not just minimum flows.",
  "Methods range from Tennant rules to holistic habitat models.",
  "Climate shifts the natural baseline being mimicked.",
  "Water allocation politics often overrides e-flow science.",
 ],
 "requirements": [
  "E-flow regimes defined by magnitude, timing, and variability.",
  "Reservoir reoperation implementing the regimes.",
  "Ecological monitoring adapting the prescription.",
 ],
 "citations": [
  "Poff NL et al. (1997) The natural flow regime. BioScience 47(11).",
 ],
 "demo": {"n": 0.036, "w": 18.0, "d": 2.4, "s": 0.0007},
},
# ----------------------------------------------------------------- rank 12
{
 "key": "hy-gw-sw",
 "name": "The Groundwater Surface Water Interaction Problem",
 "group": "Groundwater",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Rivers gain from and lose to aquifers along every reach - but where, how much, and how can the exchange be measured when it hides beneath the streambed?",
 "background": "Groundwater-surface water exchange - the hyporheic flow through streambeds - controls baseflow, stream temperature, and nutrient processing, yet it is measured at points (seepage meters, piezometers, temperature profiles) while varying over meters. The exchange direction flips with stage and season; losing reaches become gaining and back. Models couple surface and subsurface (HydroGeoSphere, ParFlow) but need streambed conductivities that are effectively unknowable at scale. Water rights treat surface and groundwater separately where they are one system - the legal fiction compounds the measurement gap.",
 "why_it_matters": "Pumping near streams dries them; the exchange is the connection. Managing the two waters separately while they are one is the governance failure.",
 "sig_lens": "The Signature lens reads the streambed as a breathing membrane: the protocol must measure its breath at the reach scale and manage the two waters as one.",
 "sig_solution": LABEL + " Assumptions: (1) exchange varies at meter scales; point measurements under-sample; (2) law treats the waters separately. Reasoning path: characterize exchange at reach scale (distributed temperature sensing, geophysics) and manage conjunctively. Proposed mechanism: a membrane protocol with reach-scale exchange characterization, coupled management of pumping and streamflow, and stream-depletion accounting for nearby wells. Confirm: conjunctively managed reaches maintain baseflow better. Kill: the exchange proves too variable to characterize usefully. Does NOT claim: exact exchange fluxes - it measures the membrane's breath at scale.",
 "pointer": "The Signature system's proposed approach characterizes streambed exchange at reach scale for conjunctive management; the companion Signature Edition record specifies the membrane protocol.",
 "key_points": [
  "Hyporheic exchange controls baseflow, temperature, and nutrients.",
  "Exchange direction flips with stage and season.",
  "Streambed conductivities are effectively unknowable at scale.",
  "Water law treats surface and groundwater as separate systems.",
 ],
 "requirements": [
  "Reach-scale exchange characterization (DTS, geophysics).",
  "Conjunctive pumping and streamflow management.",
  "Stream-depletion accounting for nearby wells.",
 ],
 "citations": [
  "Winter TC et al. (1998) Ground Water and Surface Water: A Single Resource. USGS Circular 1139.",
 ],
 "demo": {"n": 0.038, "w": 13.0, "d": 1.9, "s": 0.0013},
},
# ----------------------------------------------------------------- rank 13
{
 "key": "hy-karst",
 "name": "The Karst Aquifer Modeling Problem",
 "group": "Groundwater",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Karst aquifers - caves, conduits, sinkholes - move water at wildly different speeds through the same rock, so how can flow be modeled when the conduits are unmappable?",
 "background": "Karst aquifers underlie 15 percent of ice-free land and supply a quarter of the world's drinking water, yet their dual-porosity behavior - slow matrix flow plus fast conduit flow - defeats standard groundwater models. The conduits are unmappable (caves known at points, inferred elsewhere); tracer tests reveal connections but not geometry; and spring hydrographs show flashy responses no porous-medium model reproduces. Modeling approaches (equivalent porous medium, discrete conduit networks, hybrid) each fail differently. Contamination in karst travels fast and far - the vulnerability is extreme and the models are approximate.",
 "why_it_matters": "A quarter of humanity drinks karst water. Contamination in karst moves at cave-stream speed through models built for sand.",
 "sig_lens": "The Signature lens reads karst as plumbing hidden in rock: the protocol must map the pipes by what flows through them, not by drilling blind.",
 "sig_solution": LABEL + " Assumptions: (1) conduits are unmappable by drilling; (2) contamination travels fast. Reasoning path: map the plumbing functionally - tracers, spring responses, and geophysics locate the fast paths; protect them as the vulnerability. Proposed mechanism: a hidden-plumbing protocol with tracer-based conduit mapping, spring-hydrograph-calibrated hybrid models, and protection zones drawn on the fast paths, not on porous-medium assumptions. Confirm: functionally mapped karsts show better contamination early warning. Kill: the conduits reorganize (collapse, sediment) faster than mapping. Does NOT claim: complete conduit maps - it maps the plumbing by flow.",
 "pointer": "The Signature system's proposed approach maps karst conduits functionally for protection zoning; the companion Signature Edition record specifies the hidden-plumbing protocol.",
 "key_points": [
  "Karst supplies a quarter of global drinking water.",
  "Dual-porosity behavior defeats porous-medium models.",
  "Conduits are unmappable by conventional means.",
  "Contamination travels at cave-stream speed.",
 ],
 "requirements": [
  "Tracer-based conduit mapping programs.",
  "Hybrid models calibrated on spring responses.",
  "Protection zones drawn on fast paths.",
 ],
 "citations": [
  "Ford D, Williams P (2007) Karst Hydrogeology and Geomorphology. Wiley.",
 ],
 "demo": {"n": 0.025, "w": 7.0, "d": 1.4, "s": 0.004},
},
# ----------------------------------------------------------------- rank 14
{
 "key": "hy-fractured",
 "name": "The Fractured Rock Flow Problem",
 "group": "Groundwater",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Crystalline bedrock carries water only in fractures - but how can flow be predicted when the fracture network is sampled at boreholes and the rock between is unknown?",
 "background": "Fractured-rock aquifers - granites, basalts, shales - supply water across Africa, India, and Scandinavia, yet flow occurs in discrete fractures whose geometry is known only where boreholes intersect them. The upscaling problem is severe: a pumping test samples the fractures near the well, but the regional flow depends on the network's connectivity - percolation-like behavior where a few fractures carry everything. Discrete fracture network (DFN) models need statistics the data cannot supply; equivalent-continuum models smooth away the very heterogeneity that matters. Dry boreholes sit meters from productive ones.",
 "why_it_matters": "Millions depend on fractured-rock wells; drilling success is a lottery. The connectivity science is the difference between water and a dry hole.",
 "sig_lens": "The Signature lens reads fractured rock as a maze with few corridors: the protocol must find the corridors with geophysics before drilling, not after.",
 "sig_solution": LABEL + " Assumptions: (1) boreholes sample fractures sparsely; (2) connectivity dominates productivity. Reasoning path: target the corridors - use surface geophysics and lineament analysis to site wells on connected fracture zones. Proposed mechanism: a corridors protocol with pre-drilling geophysical surveys, DFN models conditioned on the surveys, and drilling success tracked to improve the targeting. Confirm: geophysically sited wells show higher success rates. Kill: the geophysics cannot resolve the productive fractures. Does NOT claim: certain well success - it plays the lottery with loaded dice.",
 "pointer": "The Signature system's proposed approach sites fractured-rock wells with pre-drilling geophysics; the companion Signature Edition record specifies the corridors protocol.",
 "key_points": [
  "Flow occurs in discrete fractures; boreholes sample sparsely.",
  "Network connectivity dominates well productivity.",
  "DFN models need statistics the data cannot supply.",
  "Dry boreholes sit meters from productive ones.",
 ],
 "requirements": [
  "Pre-drilling geophysical fracture surveys.",
  "DFN models conditioned on survey data.",
  "Drilling-success tracking to improve targeting.",
 ],
 "citations": [
  "NRC (1996) Rock Fractures and Fluid Flow. National Academies Press.",
 ],
 "demo": {"n": 0.042, "w": 9.0, "d": 1.7, "s": 0.0022},
},
# ----------------------------------------------------------------- rank 15
{
 "key": "hy-preferential",
 "name": "The Preferential Flow Problem",
 "group": "Water Cycle",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Water bypasses the soil matrix through macropores - wormholes, cracks, root channels - so how can infiltration be modeled when the fast lanes carry most of the flow?",
 "background": "Preferential flow - water racing through macropores past the soil matrix - explains why contaminants arrive at depth years before matrix-flow models predict, and why irrigation water bypasses the root zone. The macropore network is unmappable (dye tracers reveal it destructively, at points); its activation depends on rainfall intensity and antecedent wetness in threshold-like ways. Dual-permeability models represent the fast lanes but need parameters that are effectively fitted, not measured. The matrix-flow Richards equation - hydrology's workhorse - is wrong where macropores dominate, which is often.",
 "why_it_matters": "Contaminants outrun the models through macropores; irrigation misses the roots the same way. The fast lanes decide what the matrix never sees.",
 "sig_lens": "The Signature lens reads soil as a highway system with unmapped express lanes: the protocol must assume the express lanes are open during storms.",
 "sig_solution": LABEL + " Assumptions: (1) macropore networks are unmappable non-destructively; (2) matrix models fail where macropores dominate. Reasoning path: model the fast lanes explicitly - dual-permeability with macropore activation thresholds, calibrated on dye-tracer and breakthrough data. Proposed mechanism: an express-lanes protocol requiring dual-permeability modeling for contaminant transport, macropore-sensitive irrigation scheduling, and conservative (fast) travel-time estimates for wellhead protection. Confirm: dual-permeability models predict breakthrough better than matrix models. Kill: the activation thresholds prove unidentifiable. Does NOT claim: mapped macropores - it assumes the express lanes are open.",
 "pointer": "The Signature system's proposed approach models preferential flow with dual-permeability methods; the companion Signature Edition record specifies the express-lanes protocol.",
 "key_points": [
  "Macropores carry contaminants years ahead of matrix predictions.",
  "The network is unmappable except destructively.",
  "Activation is threshold-like in intensity and wetness.",
  "The Richards equation fails where macropores dominate.",
 ],
 "requirements": [
  "Dual-permeability modeling for contaminant transport.",
  "Macropore-sensitive irrigation scheduling.",
  "Conservative travel-time estimates for wellhead protection.",
 ],
 "citations": [
  "Jarvis NJ (2007) A review of non-equilibrium water flow and solute transport in soil macropores. J. Contaminant Hydrology 90.",
 ],
 "demo": {"n": 0.034, "w": 10.0, "d": 1.5, "s": 0.0018},
},
# ----------------------------------------------------------------- rank 16
{
 "key": "hy-glacier",
 "name": "The Glacier Melt Contribution Problem",
 "group": "Water Cycle",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Glaciers feed rivers across the Himalayas, Andes, and Alps - but how much of the river is glacier melt versus snow and rain, and how will the mix change as glaciers retreat?",
 "background": "Glacier melt sustains dry-season flows for hundreds of millions (the Indus, Ganges, Brahmaputra headwaters), but the melt fraction is contested: hydrograph separation by isotopes and chemistry gives one answer, glacier mass-balance models give another, and the monsoon complicates both. As glaciers retreat, the melt contribution first rises (more melt) then falls (less ice) - the peak-water timing is the planning question, and it varies glacier by glacier. Debris-covered glaciers melt differently; the data is thinnest where the dependence is greatest (High Mountain Asia).",
 "why_it_matters": "Hundreds of millions depend on the melt fraction. Peak water - the turn from rising to falling melt - is the planning deadline nobody can date.",
 "sig_lens": "The Signature lens reads glaciers as melting savings accounts: the protocol must track the withdrawals and date the account's peak.",
 "sig_solution": LABEL + " Assumptions: (1) melt fractions are method-dependent; (2) peak-water timing varies by glacier. Reasoning path: date peak water per basin - combine mass-balance, isotope separation, and modeling to project each basin's melt trajectory. Proposed mechanism: a savings-account protocol with per-basin peak-water dating, melt-fraction monitoring (isotopes, mass balance), and water planning keyed to the post-peak decline. Confirm: dated basins plan adaptations earlier. Kill: the methods never converge on the trajectory. Does NOT claim: exact peak-water dates - it dates the account's turn honestly.",
 "pointer": "The Signature system's proposed approach dates glacier peak water per basin; the companion Signature Edition record specifies the savings-account protocol.",
 "key_points": [
  "Glacier melt sustains dry-season flows for hundreds of millions.",
  "Melt fractions differ between isotope and model methods.",
  "Melt rises then falls as glaciers retreat; timing varies.",
  "Data is thinnest in High Mountain Asia where dependence is greatest.",
 ],
 "requirements": [
  "Per-basin peak-water dating.",
  "Melt-fraction monitoring via isotopes and mass balance.",
  "Water planning keyed to post-peak decline.",
 ],
 "citations": [
  "Immerzeel WW et al. (2010) Climate change will affect the Asian water towers. Science 328.",
 ],
 "demo": {"n": 0.048, "w": 16.0, "d": 1.3, "s": 0.006},
},
# ----------------------------------------------------------------- rank 17
{
 "key": "hy-permafrost",
 "name": "The Permafrost Thaw Hydrology Problem",
 "group": "Water Cycle",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Thawing permafrost rewrites Arctic hydrology - but how do groundwater, runoff, and carbon release change as the frozen ground that organized them disappears?",
 "background": "Permafrost underlies a quarter of Northern Hemisphere land; its thaw is reorganizing Arctic hydrology: the active layer deepens, new groundwater pathways open, thermokarst lakes drain catastrophically, and winter baseflows rise as stored water releases. The carbon feedback - thaw releasing CO2 and methane - couples hydrology to climate. But permafrost hydrology is data-poor (few gauges, harsh conditions), the thaw is heterogeneous (ice content varies wildly), and models built for temperate soils misbehave in thawing ground. The Arctic's water future is being written in unmonitored terrain.",
 "why_it_matters": "Permafrost thaw couples water and carbon: the hydrology decides how fast the carbon escapes, and the carbon decides how fast the thaw proceeds.",
 "sig_lens": "The Signature lens reads permafrost as a frozen dam system: the protocol must watch the dams fail and track where the released water - and carbon - goes.",
 "sig_solution": LABEL + " Assumptions: (1) thaw is heterogeneous and data-poor; (2) hydrology and carbon are coupled. Reasoning path: monitor the thaw's hydrological signature - baseflow trends, thermokarst drainage, active-layer deepening - as the early warning. Proposed mechanism: a failing-dams protocol with Arctic hydrological monitoring focused on thaw signatures, coupled hydro-carbon modeling, and infrastructure adaptation to the reorganized drainage. Confirm: signature-monitored regions anticipate drainage changes. Kill: the heterogeneity defeats regional prediction. Does NOT claim: exact thaw trajectories - it watches the dams fail systematically.",
 "pointer": "The Signature system's proposed approach monitors permafrost thaw's hydrological signatures; the companion Signature Edition record specifies the failing-dams protocol.",
 "key_points": [
  "Permafrost underlies a quarter of Northern Hemisphere land.",
  "Thaw deepens active layers, opens groundwater paths, drains lakes.",
  "The carbon feedback couples hydrology to climate.",
  "Arctic hydrology is data-poor; models misbehave in thawing ground.",
 ],
 "requirements": [
  "Thaw-signature hydrological monitoring (baseflow, thermokarst, active layer).",
  "Coupled hydrological-carbon modeling.",
  "Infrastructure adaptation to reorganized drainage.",
 ],
 "citations": [
  "Schuur EAG et al. (2015) Climate change and the permafrost carbon feedback. Nature 520.",
 ],
 "demo": {"n": 0.055, "w": 8.0, "d": 1.1, "s": 0.0025},
},
# ----------------------------------------------------------------- rank 18
{
 "key": "hy-nonstationary",
 "name": "The Flood Frequency Under Nonstationarity Problem",
 "group": "Surface Water",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Flood frequency analysis assumes the past predicts the future - but the climate is changing, so how can the 100-year flood be estimated when the record is obsolete?",
 "background": "Flood frequency analysis (Bulletin 17C, Log-Pearson III) fits distributions to annual maxima under stationarity - the assumption that the flood regime is unchanging. Climate change breaks it: intensifying rainfall, earlier snowmelt, and land-use change shift flood distributions within the record. Nonstationary frequency analysis (time-varying parameters) exists but needs long records to detect trends that the records are too short to show; the trend estimates are uncertain and the projections depend on climate models. Engineers need a number for the bridge; the science offers a moving target with wide bands.",
 "why_it_matters": "Every bridge, levee, and floodplain map rests on flood frequency. Designing to an obsolete 100-year flood is designing to fail.",
 "sig_lens": "The Signature lens reads the flood record as a history book in a changing language: the protocol must translate the past into the future's climate, with the translation uncertainty shown.",
 "sig_solution": LABEL + " Assumptions: (1) stationarity is broken; (2) nonstationary estimates are uncertain. Reasoning path: design to the projected regime - use nonstationary analysis with climate-informed covariates, and build safety margins for the uncertainty. Proposed mechanism: a translation protocol requiring nonstationary flood frequency with climate covariates, design values taken at upper confidence bounds, and adaptive design (foundations for future raising) where uncertainty is widest. Confirm: translated designs survive observed flood shifts better. Kill: the covariates prove unpredictive and the translation misleads. Does NOT claim: the true future 100-year flood - it translates with the uncertainty shown.",
 "pointer": "The Signature system's proposed approach estimates flood frequency nonstationarily with climate covariates; the companion Signature Edition record specifies the translation protocol.",
 "key_points": [
  "Stationarity assumptions underlie all standard flood frequency.",
  "Climate shifts flood distributions within the gauged record.",
  "Nonstationary methods need longer records than exist.",
  "Engineers need numbers; the science offers moving targets.",
 ],
 "requirements": [
  "Nonstationary frequency analysis with climate covariates.",
  "Design values at upper confidence bounds.",
  "Adaptive design where uncertainty is widest.",
 ],
 "citations": [
  "Milly PCD et al. (2008) Stationarity is dead. Science 319.",
 ],
 "demo": {"n": 0.037, "w": 22.0, "d": 3.0, "s": 0.0006},
},
# ----------------------------------------------------------------- rank 19
{
 "key": "hy-drought-index",
 "name": "The Hydrological Drought Indices Problem",
 "group": "Water Cycle",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Dozens of drought indices exist - SPI, SPEI, PDSI, and more - but they disagree, so which index actually measures the drought that matters?",
 "background": "Drought indices compress the water deficit into numbers for triggering aid, insurance, and restrictions - but the indices disagree: SPI (precipitation only) misses evaporative demand that SPEI captures; PDSI has calibration quirks; none was designed for the hydrological drought (streamflow, groundwater) that water managers face. The index choice decides who gets drought relief: the same event is moderate on one index, severe on another. Under warming, temperature-driven indices (SPEI) show drying that precipitation indices miss - the index debate is now a climate debate. There is no agreed measure of the thing being managed.",
 "why_it_matters": "Drought aid, insurance payouts, and water restrictions trigger on indices. The index choice is a policy decision wearing a technical costume.",
 "sig_lens": "The Signature lens reads drought indices as thermometers that disagree: the protocol must read several, and act on what they agree the patient has.",
 "sig_solution": LABEL + " Assumptions: (1) indices disagree; the choice is policy; (2) warming splits precipitation and evaporative-demand signals. Reasoning path: trigger on index ensembles - require agreement among complementary indices before declaring drought stages. Proposed mechanism: a thermometers protocol using multi-index drought assessment (precipitation, evaporative demand, hydrological), staged triggers requiring index agreement, and published index-choice justification for every declaration. Confirm: ensemble-triggered declarations face fewer disputes. Kill: the indices never agree and the ensemble paralyzes response. Does NOT claim: the true drought measure - it acts on the thermometers' agreement.",
 "pointer": "The Signature system's proposed approach triggers drought response on multi-index agreement; the companion Signature Edition record specifies the thermometers protocol.",
 "key_points": [
  "SPI, SPEI, PDSI and others disagree on the same events.",
  "Index choice decides drought relief eligibility.",
  "Warming splits precipitation-based and demand-based signals.",
  "No index was designed for hydrological drought specifically.",
 ],
 "requirements": [
  "Multi-index drought assessment per event.",
  "Staged triggers requiring index agreement.",
  "Published justification of index choices.",
 ],
 "citations": [
  "Mishra AK, Singh VP (2010) A review of drought concepts. J. Hydrology 391.",
 ],
 "demo": {"n": 0.031, "w": 12.0, "d": 1.8, "s": 0.001},
},
# ----------------------------------------------------------------- rank 20
{
 "key": "hy-scaling",
 "name": "The Scaling in Hydrology Problem",
 "group": "Water Cycle",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Hydrological processes measured at points must predict catchments - but how do point physics scale to basins when heterogeneity rules at every scale?",
 "background": "The scaling problem - from soil core to hillslope to catchment - is hydrology's version of the micro-macro gap: Darcy's law works in the lab; the catchment's effective conductivity is a different beast. Heterogeneity (soil, geology, vegetation) varies at all scales with no representative elementary volume in sight. Upscaling by averaging destroys the connectivity that controls flow; downscaling disaggregates without physics. The PUB decade's scaling synthesis concluded that scale remains the field's unsolved core. Models calibrated at one scale fail at others.",
 "why_it_matters": "Every catchment prediction scales point physics up. The scaling gap is the hidden error in every distributed model.",
 "sig_lens": "The Signature lens reads scaling as translation between languages: the protocol must test the translation at intermediate scales, not just the endpoints.",
 "sig_solution": LABEL + " Assumptions: (1) no representative elementary volume exists in heterogeneous catchments; (2) models fail across scales. Reasoning path: validate at nested scales - require models to perform at point, hillslope, and catchment scales simultaneously. Proposed mechanism: a translation protocol with nested-scale monitoring (points within hillslopes within catchments), multi-scale model validation, and effective parameters reported with their scale dependence. Confirm: nested-validated models transfer across scales better. Kill: the heterogeneity defeats every upscaling rule. Does NOT claim: a universal scaling law - it tests the translation at every step.",
 "pointer": "The Signature system's proposed approach validates hydrological models at nested scales; the companion Signature Edition record specifies the translation protocol.",
 "key_points": [
  "Point physics (Darcy) does not scale to catchments by averaging.",
  "Heterogeneity varies at all scales; no representative volume exists.",
  "Upscaling destroys controlling connectivity.",
  "Models calibrated at one scale fail at others.",
 ],
 "requirements": [
  "Nested-scale monitoring networks.",
  "Multi-scale model validation.",
  "Scale-dependent effective parameters.",
 ],
 "citations": [
  "Bloschl G, Sivapalan M (1995) Scale issues in hydrological modelling. Hydrological Processes 9.",
 ],
 "demo": {"n": 0.039, "w": 14.0, "d": 2.1, "s": 0.0014},
},
# ----------------------------------------------------------------- rank 21
{
 "key": "hy-equifinality",
 "name": "The Equifinality Problem",
 "group": "Surface Water",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Many different parameter sets fit the same streamflow record - so which model is right, and what does 'calibrated' even mean?",
 "background": "Equifinality (Beven, 1993) - the observation that many parameter sets are equally consistent with the data - undermines the idea of an optimal calibrated model: the 'best' parameters are an artifact of the objective function, and different objectives crown different winners. GLUE (Generalized Likelihood Uncertainty Estimation) embraces the multiplicity with behavioral parameter sets, but critics call it statistically incoherent. The practical consequence: calibrated models predict the calibration period well and the future poorly, because the right answer for the wrong reasons fails under change. Equifinality is hydrology's replication crisis in miniature.",
 "why_it_matters": "Calibrated models underpin flood forecasts and water plans. If calibration cannot identify the right model, the forecasts rest on the wrong reasons.",
 "sig_lens": "The Signature lens reads equifinality as many suspects with the same alibi: the protocol must keep all suspects under watch and never convict one on a fitted alibi.",
 "sig_solution": LABEL + " Assumptions: (1) many parameter sets fit equally; (2) best-fit is objective-function artifact. Reasoning path: predict with the ensemble of behavioral sets, and test the models under change (differential split-sample). Proposed mechanism: a suspects protocol requiring behavioral-ensemble prediction (GLUE-style), rejection of sets failing under changed conditions, and reported prediction bands from the surviving sets. Confirm: ensemble predictions bracket observations better than best-fit. Kill: all sets fail under change and the ensemble is decorative. Does NOT claim: the true parameters - it keeps every suspect watched.",
 "pointer": "The Signature system's proposed approach predicts with behavioral parameter ensembles tested under change; the companion Signature Edition record specifies the suspects protocol.",
 "key_points": [
  "Many parameter sets fit the same record equally (Beven, 1993).",
  "Best-fit parameters are objective-function artifacts.",
  "Right answers for wrong reasons fail under change.",
  "GLUE embraces multiplicity; critics dispute its statistics.",
 ],
 "requirements": [
  "Behavioral-ensemble prediction, not best-fit.",
  "Differential split-sample testing under changed conditions.",
  "Prediction bands from surviving parameter sets.",
 ],
 "citations": [
  "Beven K, Binley A (1992) The future of distributed models. Hydrological Processes 6(3).",
 ],
 "demo": {"n": 0.036, "w": 11.0, "d": 2.0, "s": 0.0016},
},
# ----------------------------------------------------------------- rank 22
{
 "key": "hy-structural",
 "name": "The Model Structural Uncertainty Problem",
 "group": "Surface Water",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Different model structures - different equations for the same watershed - give different answers, so how can the structural uncertainty be quantified when the true structure is unknown?",
 "background": "Hydrological models differ structurally: in how they represent runoff generation, routing, and storage - and the structural choice often matters more than the parameters. But structural uncertainty is hard to quantify: multi-model ensembles (like FUSE, SUMMA frameworks) sample the structural space incompletely, and the true structure is unknown, so the ensemble may miss it entirely. Model intercomparison (MOPEX) shows models disagree most where data is scarcest - exactly where decisions need them. The structural uncertainty is the largest and least quantified.",
 "why_it_matters": "The equation choice can matter more than the parameter values. Unquantified structural uncertainty is the largest hidden error in water prediction.",
 "sig_lens": "The Signature lens reads model structures as competing blueprints: the protocol must build from several and report where the blueprints disagree.",
 "sig_solution": LABEL + " Assumptions: (1) structure matters more than parameters; (2) the true structure is unknown. Reasoning path: sample the structural space deliberately - run modular frameworks spanning runoff-generation and routing hypotheses, and report the structural spread. Proposed mechanism: a blueprints protocol with multi-structural ensembles (FUSE/SUMMA-style), structural hypotheses tied to catchment characteristics, and decisions conditioned on the structural spread. Confirm: structural ensembles bracket observations better than single structures. Kill: the structural space is too large to sample usefully. Does NOT claim: the true structure - it reports where blueprints disagree.",
 "pointer": "The Signature system's proposed approach quantifies structural uncertainty with multi-model frameworks; the companion Signature Edition record specifies the blueprints protocol.",
 "key_points": [
  "Structural choice often matters more than parameter values.",
  "Multi-model ensembles sample structural space incompletely.",
  "Models disagree most where data is scarcest.",
  "Structural uncertainty is the largest, least quantified error.",
 ],
 "requirements": [
  "Multi-structural ensemble modeling.",
  "Structural hypotheses tied to catchment traits.",
  "Decisions conditioned on structural spreads.",
 ],
 "citations": [
  "Clark MP et al. (2008) Framework for Understanding Structural Errors (FUSE). Water Resources Research 44.",
 ],
 "demo": {"n": 0.04, "w": 13.0, "d": 2.3, "s": 0.0012},
},
# ----------------------------------------------------------------- rank 23
{
 "key": "hy-assimilation",
 "name": "The Data Assimilation in Hydrology Problem",
 "group": "Surface Water",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Satellites and sensors flood hydrology with data - but how can the data be merged into models when the models' states are unobserved and their errors are unknown?",
 "background": "Data assimilation - merging observations into running models (EnKF, particle filters) - transformed weather forecasting, but hydrology lags: the states (soil moisture profiles, groundwater storages) are largely unobserved, the observation operators (satellite soil moisture to model layers) are uncertain, and the model errors are unknown and probably biased. Assimilating biased observations into biased models can degrade forecasts. The promise (real-time flood updating, drought monitoring) is real; the error characterization needed to fulfill it is missing. Hydrologic data assimilation is a field awaiting its error models.",
 "why_it_matters": "Real-time flood and drought prediction needs models corrected by data. Assimilation without error models is correction by rumor.",
 "sig_lens": "The Signature lens reads assimilation as steering by instruments: the protocol must calibrate the instruments' errors before trusting the steering.",
 "sig_solution": LABEL + " Assumptions: (1) states are unobserved; errors unknown and probably biased; (2) biased assimilation can degrade forecasts. Reasoning path: characterize the errors first - estimate observation and model error statistics before operational assimilation. Proposed mechanism: an instruments protocol with error-characterization studies (triple collocation, innovations), bias-aware assimilation methods, and forecast-skill verification against non-assimilated baselines. Confirm: error-characterized assimilation improves forecast skill. Kill: the errors prove uncharacterizable and assimilation stays experimental. Does NOT claim: optimal assimilation - it calibrates the instruments first.",
 "pointer": "The Signature system's proposed approach characterizes errors before operational hydrologic assimilation; the companion Signature Edition record specifies the instruments protocol.",
 "key_points": [
  "Hydrologic states are largely unobserved; errors unknown.",
  "Observation operators (satellite to model) are uncertain.",
  "Biased assimilation can degrade forecasts.",
  "Weather forecasting's success has not transferred.",
 ],
 "requirements": [
  "Error characterization before operational use.",
  "Bias-aware assimilation methods.",
  "Skill verification against non-assimilated baselines.",
 ],
 "citations": [
  "Liu Y et al. (2012) Advancing data assimilation in operational hydrologic forecasting. Reviews of Geophysics 50.",
 ],
 "demo": {"n": 0.035, "w": 15.0, "d": 2.2, "s": 0.001},
},
# ----------------------------------------------------------------- rank 24
{
 "key": "hy-soil-moisture-rs",
 "name": "The Remote Sensing of Soil Moisture Problem",
 "group": "Water Cycle",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Soil moisture controls floods, droughts, and weather - but satellites see only the top centimeters, so how can the root zone be observed from space?",
 "background": "Soil moisture is the water cycle's memory, but the root zone (the top meter, where plants drink) is invisible to satellites: microwave sensors (SMAP, SMOS, ASCAT) sense the top 2-5 cm, and the profile below is inferred by models with uncertain physics. The spatial mismatch is severe: satellite footprints (tens of kilometers) versus the field scale where decisions happen. Downscaling needs the very heterogeneity data that is missing. Data assimilation merges the surface observations into models, but the model errors dominate. The root zone remains hydrology's unobserved reservoir.",
 "why_it_matters": "Drought early warning, flood forecasting, and irrigation all need root-zone moisture. The unobserved reservoir is the missing state in every water forecast.",
 "sig_lens": "The Signature lens reads satellites as seeing only the skin: the protocol must diagnose the body's hydration from the skin, the symptoms, and the history.",
 "sig_solution": LABEL + " Assumptions: (1) satellites sense centimeters; decisions need meters; (2) model errors dominate the inference. Reasoning path: fuse the skin observation with models and in-situ networks, and validate the root-zone inference where probes exist. Proposed mechanism: a diagnosis protocol combining satellite surface moisture, land-surface models, and in-situ networks (ISMN), with root-zone products validated against probe networks and uncertainty reported per pixel. Confirm: fused products beat model-only root-zone estimates at probe sites. Kill: the inference errors dominate and the products mislead. Does NOT claim: observed root-zone moisture - it diagnoses from skin, symptoms, and history.",
 "pointer": "The Signature system's proposed approach fuses satellite, model, and in-situ data for root-zone moisture; the companion Signature Edition record specifies the diagnosis protocol.",
 "key_points": [
  "Microwave satellites sense only the top 2-5 cm of soil.",
  "Root-zone moisture (top meter) is inferred, not observed.",
  "Footprints (tens of km) mismatch decision scales.",
  "In-situ validation networks are sparse.",
 ],
 "requirements": [
  "Fusion of satellite, model, and in-situ soil moisture.",
  "Root-zone products validated at probe networks.",
  "Per-pixel uncertainty reporting.",
 ],
 "citations": [
  "Entekhabi D et al. (2010) The Soil Moisture Active Passive (SMAP) Mission. Proc. IEEE 98(5).",
 ],
 "demo": {"n": 0.033, "w": 10.0, "d": 1.5, "s": 0.0017},
},
# ----------------------------------------------------------------- rank 25
{
 "key": "hy-grace",
 "name": "The GRACE Groundwater Depletion Problem",
 "group": "Groundwater",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "GRACE satellites weigh Earth's water from space and show aquifers depleting - but how much of the signal is groundwater versus soil, snow, and surface water?",
 "background": "The GRACE (and GRACE-FO) missions measure gravity anomalies that reveal total water-storage change - famously showing depletion in the Central Valley, North China Plain, and northwest India. But GRACE sees the total column: separating groundwater from soil moisture, snow, and surface water needs land-surface models whose own errors are large. The leakage problem (signals bleeding across regions) and the coarse resolution (~300 km) limit attribution. The depletion numbers that make headlines rest on model-assisted disaggregation that the models cannot validate. Groundwater depletion is observed from space through a model-shaped lens.",
 "why_it_matters": "GRACE depletion maps drive global groundwater alarm. If the disaggregation misattributes the signal, the alarm points at the wrong water.",
 "sig_lens": "The Signature lens reads GRACE as weighing the whole patient: the protocol must separate the organs' weights before diagnosing which one is losing mass.",
 "sig_solution": LABEL + " Assumptions: (1) GRACE sees total storage; (2) disaggregation models have large errors. Reasoning path: constrain the disaggregation with independent data - well levels, soil moisture networks, snow surveys - and report the groundwater component with the constraint spread. Proposed mechanism: a weighing protocol disaggregating GRACE with multi-source constraints, validating against well networks where available, and reporting depletion with disaggregation uncertainty. Confirm: constrained disaggregation matches well trends better. Kill: the constraints are too sparse and the groundwater signal stays ambiguous. Does NOT claim: exact groundwater depletion - it separates the organs' weights honestly.",
 "pointer": "The Signature system's proposed approach constrains GRACE disaggregation with independent data; the companion Signature Edition record specifies the weighing protocol.",
 "key_points": [
  "GRACE measures total water-storage change from gravity.",
  "Groundwater separation needs land-surface models with large errors.",
  "Coarse resolution (~300 km) and signal leakage limit attribution.",
  "Headline depletion numbers rest on model-assisted disaggregation.",
 ],
 "requirements": [
  "Multi-source constraints on GRACE disaggregation.",
  "Validation against well-level networks.",
  "Depletion reported with disaggregation uncertainty.",
 ],
 "citations": [
  "Tapley BD et al. (2004) The Gravity Recovery and Climate Experiment. Geophysical Research Letters 31.",
 ],
 "demo": {"n": 0.032, "w": 12.0, "d": 1.9, "s": 0.0011},
},
# ----------------------------------------------------------------- rank 26
{
 "key": "hy-water-quality",
 "name": "The Water Quality Modeling Problem",
 "group": "Surface Water",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Nutrients, sediments, and contaminants move through watersheds in pulses - but how can water quality be modeled when the sources are diffuse and the monitoring is sparse?",
 "background": "Water-quality modeling (SWAT, HSPF, SPARROW) routes nutrients and contaminants through watersheds, but nonpoint sources (fields, streets, septic) are diffuse and episodic: most of the annual load moves in a few storms that monitoring misses. The models have dozens of water-quality parameters that are unidentifiable from sparse data - equifinality squared. Legacy nutrients (stored in soils and groundwater) delay the response to management by decades, defeating before-after evaluation. TMDLs (pollution diets) are set by models whose uncertainty would void the diet if disclosed.",
 "why_it_matters": "Dead zones, algal blooms, and drinking-water contamination are modeled problems. The models' hidden uncertainty is the policy's hidden risk.",
 "sig_lens": "The Signature lens reads water quality as crime-scene forensics with few witnesses: the protocol must sample the storms (when the crime happens) and admit what the lab cannot prove.",
 "sig_solution": LABEL + " Assumptions: (1) loads move in missed storms; parameters unidentifiable; (2) legacy stores delay response decades. Reasoning path: monitor the events, model the uncertainty, and set expectations on decadal timescales. Proposed mechanism: a forensics protocol with storm-targeted water-quality monitoring, ensemble water-quality modeling with reported spreads, and TMDLs carrying uncertainty bands and legacy-adjusted timelines. Confirm: storm-monitored models predict loads better. Kill: the monitoring never captures the critical events. Does NOT claim: exact load attribution - it forensically samples the crime.",
 "pointer": "The Signature system's proposed approach targets water-quality monitoring at storm events with ensemble modeling; the companion Signature Edition record specifies the forensics protocol.",
 "key_points": [
  "Most annual loads move in a few unmonitored storms.",
  "Water-quality parameters are unidentifiable from sparse data.",
  "Legacy nutrients delay management response by decades.",
  "TMDLs rest on undisclosed model uncertainty.",
 ],
 "requirements": [
  "Storm-targeted water-quality monitoring.",
  "Ensemble modeling with reported spreads.",
  "TMDLs with uncertainty bands and legacy timelines.",
 ],
 "citations": [
  "Arnold JG et al. (1998) Large area hydrologic modeling and assessment (SWAT). JAWRA 34(1).",
 ],
 "demo": {"n": 0.038, "w": 11.0, "d": 2.0, "s": 0.0015},
},
# ----------------------------------------------------------------- rank 27
{
 "key": "hy-sediment",
 "name": "The Sediment Transport Prediction Problem",
 "group": "Surface Water",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Rivers move sediment in formulas that disagree by orders of magnitude - but which transport equation, if any, predicts the load?",
 "background": "Sediment-transport formulas (Meyer-Peter and Muller, Engelund-Hansen, Yang, Wilcock-Crowe) predict bedload and suspended load from hydraulics - and disagree by orders of magnitude on the same river. The formulas are empirical fits to flume data extrapolated to rivers they were never tested on; the threshold of motion, hiding effects, and supply limitation each break the formulas differently. Bedload measurement itself is uncertain (Helley-Smith samplers disturb the flow they measure). Reservoir sedimentation, channel restoration, and dam removal all need numbers the formulas cannot reliably give.",
 "why_it_matters": "Reservoirs fill with sediment; restorations fail on wrong transport predictions. Order-of-magnitude formula disagreement is engineering without a number.",
 "sig_lens": "The Signature lens reads transport formulas as weather vanes pointing different ways: the protocol must measure the wind (the actual load) and use the formulas as hypotheses, not answers.",
 "sig_solution": LABEL + " Assumptions: (1) formulas disagree by orders of magnitude; (2) bedload measurement disturbs the flow. Reasoning path: measure the load directly (acoustics, tracers, repeated surveys) and use formulas as hypotheses to be tested, not answers to be trusted. Proposed mechanism: a wind protocol with direct sediment-load measurement programs, formula testing against the measurements, and designs using measured loads with formula ensembles as bounds. Confirm: measured-load designs outperform formula-only designs. Kill: direct measurement proves too costly for routine use. Does NOT claim: a universal transport law - it measures the wind.",
 "pointer": "The Signature system's proposed approach measures sediment loads directly and tests formulas against them; the companion Signature Edition record specifies the wind protocol.",
 "key_points": [
  "Transport formulas disagree by orders of magnitude on the same river.",
  "Formulas are flume fits extrapolated beyond their data.",
  "Bedload samplers disturb the flow they measure.",
  "Reservoir and restoration designs need reliable numbers.",
 ],
 "requirements": [
  "Direct sediment-load measurement programs.",
  "Formula testing against measurements.",
  "Designs on measured loads with formula-ensemble bounds.",
 ],
 "citations": [
  "Gomez B, Church M (1989) An assessment of bed load sediment transport formulae. Water Resources Research 25(6).",
 ],
 "demo": {"n": 0.041, "w": 17.0, "d": 2.6, "s": 0.0019},
},
# ----------------------------------------------------------------- rank 28
{
 "key": "hy-morphodynamics",
 "name": "The River Morphodynamics Problem",
 "group": "Surface Water",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Rivers reshape their channels - meandering, braiding, avulsing - but can the evolution be predicted when the physics spans grains to valleys?",
 "background": "River morphodynamics - the co-evolution of flow, sediment, and channel form - spans scales from grain entrainment to valley evolution over millennia. Models (Delft3D, HEC-RAS 2D sediment) couple hydraulics to bed updating, but the morphologic acceleration tricks, the bank-erosion physics, and the vegetation feedbacks are parameterized crudely. Avulsions (channel jumps) and meander cutoffs are threshold events the models miss. Restoration designs assume equilibrium the rivers never reach. The channel's future is computed from physics that breaks at the event scale.",
 "why_it_matters": "Levees, bridges, and restorations assume channel positions the river will abandon. Unpredicted avulsions are the floodplain's surprise.",
 "sig_lens": "The Signature lens reads rivers as restless sculptors: the protocol must map where the sculptor has moved before and design for the movement, not the moment.",
 "sig_solution": LABEL + " Assumptions: (1) models miss threshold events (avulsions, cutoffs); (2) restorations assume false equilibrium. Reasoning path: design for mobility - map historical channel movement, model the envelope of plausible evolution, and keep infrastructure out of the migration zone. Proposed mechanism: a sculptor protocol with historical channel-migration mapping, morphodynamic modeling of the evolution envelope, and setback/room-for-the-river designs. Confirm: mobility-designed reaches suffer less infrastructure damage. Kill: the historical record proves unrepresentative under change. Does NOT claim: exact channel prediction - it designs for the sculptor's range.",
 "pointer": "The Signature system's proposed approach designs for channel mobility using historical migration mapping; the companion Signature Edition record specifies the sculptor protocol.",
 "key_points": [
  "Morphodynamics spans grains to valleys, events to millennia.",
  "Models miss avulsions and meander cutoffs.",
  "Bank erosion and vegetation feedbacks are crudely parameterized.",
  "Restorations assume equilibria rivers never reach.",
 ],
 "requirements": [
  "Historical channel-migration mapping.",
  "Evolution-envelope morphodynamic modeling.",
  "Setback and room-for-the-river designs.",
 ],
 "citations": [
  "Church M (2006) Bed material transport and the morphology of alluvial river channels. Annual Review EPS 34.",
 ],
 "demo": {"n": 0.036, "w": 25.0, "d": 2.8, "s": 0.0008},
},
# ----------------------------------------------------------------- rank 29
{
 "key": "hy-dam-removal",
 "name": "The Dam Removal Sediment Pulse Problem",
 "group": "Surface Water",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Dam removals release decades of trapped sediment downstream - but how big is the pulse, where does it go, and how long does the river take to recover?",
 "background": "Dam removal is accelerating (hundreds in the US), each releasing the reservoir's sediment legacy: the Elwha removals freed 20+ million cubic meters, reshaping the river and delta. But the pulse's magnitude, timing, and downstream fate are hard to predict: the reservoir sediment's erodibility, the release sequencing, and the downstream transport capacity interact. Contaminated reservoir sediments add a toxic dimension. The recovery trajectory - how the river finds its new equilibrium - is observed post hoc, not predicted. Each removal is an experiment the science watches but cannot fully forecast.",
 "why_it_matters": "Dam removals are the century's river-restoration tool. Unpredicted sediment pulses bury the habitat the removal was meant to restore.",
 "sig_lens": "The Signature lens reads dam removal as surgery: the protocol must image the mass to be removed (the sediment), plan the incision (the release), and monitor the recovery.",
 "sig_solution": LABEL + " Assumptions: (1) pulse magnitude and fate are hard to predict; (2) contaminated sediments add toxic risk. Reasoning path: characterize the reservoir sediment fully, model the release scenarios, and stage the removal to meter the pulse. Proposed mechanism: a surgery protocol with pre-removal sediment characterization (volume, grain size, contamination), scenario modeling of release sequencing, staged removals metering the pulse, and downstream monitoring with adaptive management. Confirm: staged removals show more predictable downstream recovery. Kill: the sediment erodibility proves unpredictable. Does NOT claim: exact pulse prediction - it plans the surgery and monitors recovery.",
 "pointer": "The Signature system's proposed approach stages dam removals on sediment characterization; the companion Signature Edition record specifies the surgery protocol.",
 "key_points": [
  "Removals release decades of trapped sediment (Elwha: 20M+ m3).",
  "Pulse magnitude, timing, and fate resist prediction.",
  "Contaminated reservoir sediments add toxic dimensions.",
  "Recovery trajectories are observed, not predicted.",
 ],
 "requirements": [
  "Pre-removal sediment characterization.",
  "Release-sequencing scenario modeling.",
  "Staged removals with downstream adaptive monitoring.",
 ],
 "citations": [
  "East AE et al. (2015) Large-scale dam removal on the Elwha River. Geomorphology 246.",
 ],
 "demo": {"n": 0.044, "w": 19.0, "d": 2.2, "s": 0.0028},
},
# ----------------------------------------------------------------- rank 30
{
 "key": "hy-mar",
 "name": "The Managed Aquifer Recharge Problem",
 "group": "Groundwater",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Storing floodwater underground (MAR) could bank water for droughts - but where does the recharged water go, does it stay, and does it stay clean?",
 "background": "Managed aquifer recharge - infiltrating surplus surface water (spreading basins, injection wells, dry wells) - is the water bank for a volatile climate, practiced from Orange County to Rajasthan. But the banked water's fate is uncertain: it migrates with regional gradients, mixes with native groundwater of different quality, and can mobilize contaminants (arsenic, uranium) from the aquifer matrix. Clogging (physical, biological, chemical) degrades infiltration rates. Recovery efficiency - the fraction banked that can be pumped back - varies widely. MAR is water banking without audited accounts.",
 "why_it_matters": "MAR is the climate-adaptation water bank. Unrecovered or contaminated banked water is the adaptation that fails when the drought comes.",
 "sig_lens": "The Signature lens reads MAR as banking: the protocol must audit the deposits - where they went, what they mixed with, and what can be withdrawn.",
 "sig_solution": LABEL + " Assumptions: (1) banked water migrates and mixes; (2) recharge can mobilize native contaminants. Reasoning path: audit the bank - trace the recharged water, monitor the mixing, and test recovery before counting on it. Proposed mechanism: a banking protocol with recharge-water tracing, geochemical compatibility testing before injection, clogging management, and recovery-efficiency verification before the banked water enters supply plans. Confirm: audited MAR systems show verified recovery efficiencies. Kill: the banked water proves unrecoverable and MAR is recharge without banking. Does NOT claim: guaranteed recovery - it audits the deposits.",
 "pointer": "The Signature system's proposed approach audits managed aquifer recharge with tracing and recovery verification; the companion Signature Edition record specifies the banking protocol.",
 "key_points": [
  "Banked water migrates, mixes, and can mobilize contaminants.",
  "Clogging degrades infiltration over time.",
  "Recovery efficiency varies widely and is often unverified.",
  "Geochemical incompatibility (arsenic, uranium) is a real risk.",
 ],
 "requirements": [
  "Recharge-water tracing programs.",
  "Geochemical compatibility testing pre-injection.",
  "Recovery-efficiency verification before supply planning.",
 ],
 "citations": [
  "Dillon P et al. (2009) Managed aquifer recharge: an introduction. Waterlines Report 13.",
 ],
 "demo": {"n": 0.03, "w": 12.0, "d": 2.0, "s": 0.0012},
},
# ----------------------------------------------------------------- rank 31
{
 "key": "hy-green-infra",
 "name": "The Green Infrastructure Performance Problem",
 "group": "Surface Water",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Bioswales, rain gardens, and permeable pavements promise urban runoff control - but how do they actually perform over years, and does the maintenance ever happen?",
 "background": "Green infrastructure (GI) - distributed stormwater controls mimicking natural hydrology - is the policy darling for urban runoff, but the performance evidence is thin: most studies monitor the first year, while clogging, sedimentation, and vegetation change degrade performance over years. Maintenance - the unglamorous determinant - is underfunded and unmonitored; failed GI looks green while infiltrating nothing. The cumulative watershed-scale effect of parcel-scale GI is modeled, not measured. Design standards assume maintained performance that the maintenance budgets do not deliver.",
 "why_it_matters": "Cities are spending billions on green infrastructure. Unmaintained GI is landscaping billed as flood control - the performance gap is the public's money.",
 "sig_lens": "The Signature lens reads green infrastructure as a living machine: the protocol must maintain the machine and measure its work, not admire its looks.",
 "sig_solution": LABEL + " Assumptions: (1) performance degrades without maintenance; (2) most monitoring covers year one only. Reasoning path: maintain and monitor for the long term - fund maintenance as infrastructure, and measure infiltration over years. Proposed mechanism: a living-machine protocol with dedicated GI maintenance funding, long-term infiltration monitoring, and performance-based design standards (credit only verified performance). Confirm: maintained GI sustains infiltration over years. Kill: the maintenance funding never materializes. Does NOT claim: perpetual GI performance - it maintains the machine and measures the work.",
 "pointer": "The Signature system's proposed approach funds and monitors green infrastructure as maintained infrastructure; the companion Signature Edition record specifies the living-machine protocol.",
 "key_points": [
  "GI performance degrades via clogging and sedimentation over years.",
  "Most performance studies cover only the first year.",
  "Maintenance is underfunded; failed GI looks green.",
  "Watershed-scale cumulative effects are modeled, not measured.",
 ],
 "requirements": [
  "Dedicated long-term GI maintenance funding.",
  "Multi-year infiltration monitoring.",
  "Performance-based design crediting.",
 ],
 "citations": [
  "Eckart K et al. (2017) Performance and implementation of low impact development. J. Environmental Management 198.",
 ],
 "demo": {"n": 0.028, "w": 8.0, "d": 1.2, "s": 0.002},
},
# ----------------------------------------------------------------- rank 32
{
 "key": "hy-isotope",
 "name": "The Isotope Hydrology Interpretation Problem",
 "group": "Water Cycle",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Water isotopes trace the water cycle's pathways - but how can the isotopic signals be interpreted when fractionation, mixing, and seasonality entangle them?",
 "background": "Stable isotopes (oxygen-18, deuterium) fingerprint water sources: the meteoric water line, d-excess, and seasonal cycles let hydrologists separate event from pre-event water (the famous finding that storms mostly push out old water). But interpretation is entangled: fractionation during evaporation, mixing of sources, and seasonal damping each alter the signal, and the end-member mixing models need end-members that vary in time. New tools (continuous laser spectroscopy, triple oxygen isotopes) add resolution and new puzzles. Isotope hydrology reads the water's diary - in a cipher with multiple keys.",
 "why_it_matters": "Isotopes revealed that stormflow is mostly old water - the field's deepest insight. Misread isotopes misattribute the water's origins and age.",
 "sig_lens": "The Signature lens reads isotopes as the water's diary in cipher: the protocol must decode with multiple keys (tracers) and never trust a single entry.",
 "sig_solution": LABEL + " Assumptions: (1) fractionation, mixing, and seasonality entangle signals; (2) end-members vary in time. Reasoning path: decode with multiple tracers - combine stable isotopes, tritium, and chemistry, and model the time-varying end-members. Proposed mechanism: a diary protocol with multi-tracer hydrograph separation, time-varying end-member characterization, and uncertainty on every source attribution. Confirm: multi-tracer separations agree better than single-isotope ones. Kill: the entanglement proves irreducible and attributions stay qualitative. Does NOT claim: exact water ages - it decodes with multiple keys.",
 "pointer": "The Signature system's proposed approach interprets water isotopes with multi-tracer, time-varying methods; the companion Signature Edition record specifies the diary protocol.",
 "key_points": [
  "Isotopes revealed stormflow is mostly pre-event (old) water.",
  "Fractionation, mixing, and seasonality entangle the signals.",
  "End-members vary in time, breaking static mixing models.",
  "New tools add resolution and new puzzles.",
 ],
 "requirements": [
  "Multi-tracer hydrograph separation.",
  "Time-varying end-member characterization.",
  "Uncertainty on every source attribution.",
 ],
 "citations": [
  "Kendall C, McDonnell JJ (1998) Isotope Tracers in Catchment Hydrology. Elsevier.",
 ],
 "demo": {"n": 0.034, "w": 10.0, "d": 1.6, "s": 0.0014},
},
# ----------------------------------------------------------------- rank 33
{
 "key": "hy-paleo",
 "name": "The Paleohydrology Reconstruction Problem",
 "group": "Water Cycle",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Tree rings, lake sediments, and corals record past water - but how can centuries of drought and flood be reconstructed when every proxy is an imperfect witness?",
 "background": "Paleohydrology reconstructs past water from proxies: tree rings (precipitation, streamflow), lake sediments (levels, salinity), speleothems, and corals. The reconstructions revealed megadroughts dwarfing the instrumental record (the medieval megadroughts of the western US) - reshaping water planning. But every proxy is imperfect: tree rings record growing-season moisture, not annual flow; dating has errors; and the calibration (proxy to water) assumes stationarity of the proxy relationship. Multi-proxy synthesis helps but the witnesses still disagree on details. The deep past is hydrology's only long experiment, read through frosted glass.",
 "why_it_matters": "Megadroughts in the proxy record exceed anything planned for. The imperfect witnesses are the only evidence of what the water system can do.",
 "sig_lens": "The Signature lens reads proxies as witnesses with biases: the protocol must cross-examine several and convict only on their agreement.",
 "sig_solution": LABEL + " Assumptions: (1) every proxy is seasonally and mechanistically biased; (2) calibration assumes proxy stationarity. Reasoning path: reconstruct with multi-proxy synthesis, calibrate transparently, and plan to the reconstructed extremes. Proposed mechanism: a witnesses protocol with multi-proxy reconstructions, published calibration with uncertainty, and water planning stress-tested against reconstructed megadroughts. Confirm: stress-tested plans survive proxy-record extremes in simulation. Kill: proxy disagreements prove too wide for planning use. Does NOT claim: exact past flows - it cross-examines the witnesses.",
 "pointer": "The Signature system's proposed approach reconstructs past water with multi-proxy synthesis for planning stress-tests; the companion Signature Edition record specifies the witnesses protocol.",
 "key_points": [
  "Proxies revealed megadroughts exceeding the instrumental record.",
  "Tree rings record growing-season moisture, not annual flow.",
  "Proxy-calibration assumes stationarity of the proxy relationship.",
  "Multi-proxy witnesses disagree on details.",
 ],
 "requirements": [
  "Multi-proxy reconstruction synthesis.",
  "Transparent calibration with uncertainty.",
  "Planning stress-tests against reconstructed extremes.",
 ],
 "citations": [
  "Cook ER et al. (2004) Long-term aridity changes in the western US. Science 306.",
 ],
 "demo": {"n": 0.037, "w": 14.0, "d": 2.0, "s": 0.001},
},
# ----------------------------------------------------------------- rank 34
{
 "key": "hy-unified",
 "name": "The Unified Water Cycle Problem",
 "group": "Water Cycle",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "The water cycle is one system - atmosphere, surface, subsurface, ocean, ice - but the science is fragmented across disciplines, so can the cycle be understood and managed as a whole?",
 "background": "The water cycle's branches are studied by different sciences: atmospheric scientists own precipitation, hydrologists own runoff, hydrogeologists own groundwater, oceanographers own the marine source - each with its own models, data, and journals. But the cycle is coupled: groundwater pumping reduces streamflow and evapotranspiration, feeding back to rainfall; land-use change alters the atmospheric branch. Earth system models couple the branches crudely; the human water system (pumping, dams, irrigation) is bolted on. Integrated water prediction - one system, one forecast - is the aspiration; disciplinary fragmentation is the reality.",
 "why_it_matters": "The branches interact: pumping changes rain, dams change coasts. Fragmented science mismanages the coupled system - the whole is more than the managed parts.",
 "sig_lens": "The Signature lens reads the water cycle as one body with many physicians: the protocol must give them a shared chart and treat the interactions, not just the organs.",
 "sig_solution": LABEL + " Assumptions: (1) branch coupling is real and policy-relevant; (2) disciplines fragment the science. Reasoning path: couple the branches where the coupling matters most - groundwater-atmosphere, land-use-precipitation - and manage the interactions. Proposed mechanism: a shared-chart protocol with coupled human-natural water-cycle modeling, interaction-focused monitoring (where branches meet), and management that accounts for cross-branch effects. Confirm: coupled management avoids the surprises of fragmented management. Kill: the couplings prove too weak or uncertain to manage on. Does NOT claim: a solved water cycle - it charts the one body jointly.",
 "pointer": "The Signature system's proposed approach couples water-cycle branches in modeling and management; the companion Signature Edition record specifies the shared-chart protocol.",
 "key_points": [
  "Water-cycle branches are owned by different disciplines.",
  "Groundwater pumping feeds back to rainfall via evapotranspiration.",
  "Earth system models couple branches crudely.",
  "The human water system is bolted onto natural models.",
 ],
 "requirements": [
  "Coupled human-natural water-cycle modeling.",
  "Interaction-focused monitoring at branch boundaries.",
  "Management accounting for cross-branch effects.",
 ],
 "citations": [
  "Oki T, Kanae S (2006) Global hydrological cycles and world water resources. Science 313.",
 ],
 "demo": {"n": 0.035, "w": 16.0, "d": 2.4, "s": 0.0013},
},
]
