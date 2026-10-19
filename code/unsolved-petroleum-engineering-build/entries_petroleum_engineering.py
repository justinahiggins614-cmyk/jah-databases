#!/usr/bin/env python3
"""Entries for The Unsolved Petroleum Engineering Database
(unsolved-petroleum-engineering) and its Signature half
(unsolved-petroleum-engineering-signature).

34 famous unsolved problems in petroleum engineering, ladder-ordered by
accessibility (rank 1 = most approachable, rank 34 = most complex).
Public half: real, fact-checked problems. Signature half: the same 34
through the Signature lens, ALWAYS labeled as proposals, never established
science.

ID prefixes JAH-USPE- / JAH-USPES- verified free in manifest id_prefix
values (exact + substring, both directions).
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

FIELD = {
 "tag": "petroleum-engineering",
 "disp": "petroleum engineering",
 "name": "The Unsolved Petroleum Engineering Database",
 "sig_name": "The Unsolved Petroleum Engineering Signature Database",
 "prefix": "JAH-USPE-",
 "sig_prefix": "JAH-USPES-",
 "ai": "JAH Unsolved Petroleum Engineering Archivist",
 "tagline": ("Thirty-four famous open problems in petroleum engineering, from multiphase flow to unified "
             "subsurface resources: real, fact-checked, each with its full story and a clearly labeled "
             "Signature proposed solution."),
 "sig_tagline": ("His original Signature solution method applied to all 34 great open problems of petroleum "
                 "engineering: Signature-generated proposed solutions with assumptions declared, confirm and "
                 "refute conditions stated, and limits honestly marked. Clearly labeled Signature-made, "
                 "never established science."),
 "pub_line": ("Public records - 34 famous open problems in petroleum engineering, real and fact-checked: "
              "multiphase flow in porous media, relative permeability hysteresis, wettability alteration, "
              "wellbore stability in shales, lost circulation, drilling fluids, rate of penetration, asphaltene "
              "deposition, scale formation, hydrate prevention, and sour corrosion - every record carrying the "
              "problem statement, background, why it matters, key points, requirements, standards, citations, "
              "and a working solution-explorer demonstration, organized in the Signature system."),
 "sig_line": ("Signature originals - his original Signature solution method: the same 34 famous unsolved "
              "petroleum engineering problems approached as a covenant between the known and the unknown, each "
              "carrying the full Signature-generated proposed solution with its assumptions declared, its "
              "confirm and refute conditions stated, and its limits honestly marked. Clearly labeled "
              "Signature-made, never presented as established science or authentic public record."),
 "ladder_text": (" Records are ordered by the teaching ladder: Foundations (multiphase porous flow, relative "
                 "permeability hysteresis, wettability alteration, shale wellbore stability, lost circulation, "
                 "drilling fluids, rate of penetration, asphaltenes, scale, hydrates, sour corrosion) -> "
                 "Compounded (EOR efficiency limits, sparse reservoir characterization, proppant transport, "
                 "fracture network complexity, induced seismicity, shale desorption, tight oil decline, "
                 "waterflood sweep, CO2 miscibility, SAGD optimization, polymer degradation, produced water) -> "
                 "Advanced (in situ combustion, surfactant cost, microbial EOR, flow assurance, subsea "
                 "processing, offshore decommissioning, methane leaks, flaring, CCS in depleted reservoirs, "
                 "geothermal co-production, unified subsurface resources)."),
 "search_ph": ("Search multiphase flow, EOR, hydraulic fracturing, reservoir, drilling, hydrates, asphaltene, "
               "induced seismicity, CCS, methane..."),
 "chat_ph": "Ask about the great open problems of petroleum engineering...",
 "greet_pub": ("I am the JAH Unsolved Petroleum Engineering Archivist. Ask me about the great open problems of "
               "petroleum engineering - from multiphase flow and drilling through EOR, fracturing, and flow "
               "assurance, to methane leaks, CCS, and unified subsurface resources."),
 "greet_sig": ("I am the JAH Unsolved Petroleum Engineering Archivist (Signature). Ask me about the Signature "
               "proposed solutions to the great open problems of petroleum engineering - every approach labeled "
               "as a proposal, never established science."),
 "role_pub": ("unsolved petroleum engineering archivist - the great open problems of petroleum engineering, "
              "from multiphase flow and drilling through EOR, fracturing, and flow assurance, to methane leaks, "
              "CCS, and unified subsurface resources; teaches progressively along the ladder from foundations "
              "through compounded to advanced; answers from many angles - definition, example, analogy, "
              "application, history, math - using only archive data from this system"),
 "role_sig": ("unsolved petroleum engineering archivist - Signature editions: his original Signature solution "
              "method applied to the 34 great open problems of petroleum engineering, each carrying the full "
              "Signature-generated proposed solution, clearly labeled Signature-made and never presented as "
              "established science; teaches progressively along the ladder from foundations through compounded "
              "to advanced; answers from many angles - definition, example, analogy, application, history, math "
              "- using only archive data from this system"),
 "gen_desc": "Generate clearly-labeled unsolved petroleum engineering studies. Seeded archive records are the authoritative entries.",
 "standards": [
  "Problem statements verified against the published literature; open status confirmed as of 2026.",
  "Quantitative claims cross-checked against standard references (Dake, Fundamentals of Reservoir Engineering; Economides and Nolte, Reservoir Stimulation).",
  "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
 ],
 "sig_tail": ("Signature editions carry the Signature system's proposed solution approaches to famous "
              "unsolved problems. Every solution is labeled a Signature-generated proposal, never "
              "established science, never peer-accepted, never proof."),
}

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "pe-multiphase",
 "name": "The Multiphase Flow in Porous Media Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Oil, water, and gas flow together through rock - but the equations governing their coupled motion remain partly empirical, so where does the physics end and the fitting begin?",
 "background": "Darcy's law (1856) describes single-phase flow; multiphase flow needs relative permeabilities - empirical curves saying how each phase's mobility drops in the presence of others. The curves are measured on core samples, yet they depend on saturation history, wettability, and scale in ways the measurements barely capture. The governing equations (Muskat's extension) assume the phases interfere only through these curves - an assumption with no fundamental derivation. Upscaling from core to reservoir introduces pseudo-functions that are essentially fudge factors. Every reservoir simulator runs on this empirical foundation.",
 "why_it_matters": "Reservoir simulators predict billions in recovery from multiphase equations whose core inputs are empirical curves. The physics-fitting boundary decides how much to trust them.",
 "sig_lens": "The Signature lens reads multiphase flow as three tenants sharing pipes: the protocol must measure how they crowd each other instead of assuming the lease terms.",
 "sig_solution": LABEL + " Assumptions: (1) relative permeability curves are empirical and history-dependent; (2) upscaling adds fudge factors. Reasoning path: measure the interference directly at multiple scales and carry the measurement uncertainty into the simulator. Proposed mechanism: a tenants protocol requiring multi-scale relative permeability measurement (core, block, field), history-dependent curves (drainage and imbibition), and simulator runs with the curve uncertainty propagated to recovery forecasts. Confirm: uncertainty-propagated forecasts match field performance better. Kill: the measurements prove too expensive to gather at scale. Does NOT claim: first-principles multiphase physics - it measures the crowding honestly.",
 "pointer": "The Signature system's proposed approach measures multiphase interference at multiple scales with propagated uncertainty; the companion Signature Edition record specifies the tenants protocol.",
 "key_points": [
  "Relative permeability curves are empirical and history-dependent.",
  "Muskat's extension has no fundamental derivation.",
  "Upscaling introduces pseudo-functions that are essentially fitted.",
  "Every reservoir simulator runs on this empirical foundation.",
 ],
 "requirements": [
  "Multi-scale relative permeability measurement.",
  "History-dependent (drainage and imbibition) curves.",
  "Uncertainty propagation from curves to recovery forecasts.",
 ],
 "citations": [
  "Muskat M (1937) The Flow of Homogeneous Fluids Through Porous Media. McGraw-Hill.",
  "Dake LP (1978) Fundamentals of Reservoir Engineering. Elsevier.",
 ],
 "demo": {"k": 0.2, "area": 50.0, "dp": 300.0, "mu": 1.5, "L": 100.0},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "pe-hysteresis",
 "name": "The Relative Permeability Hysteresis Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Relative permeability depends on whether saturation is rising or falling - but how can hysteresis be modeled when the saturation history of a real reservoir is unknown?",
 "background": "Drainage (non-wetting phase displacing wetting) and imbibition (the reverse) give different relative permeability curves - hysteresis - because the fluid configurations differ. Models (Killough, Carlson) interpolate between the bounding curves, but they need the turning-point saturations: the full saturation history at every point. In a real reservoir with decades of injection and production, that history is unknowable in detail. WAG (water-alternating-gas) processes cycle saturations deliberately, making hysteresis first-order - and the models' errors first-order too. The hysteresis problem is why WAG performance is so hard to predict.",
 "why_it_matters": "WAG and other cyclic processes bet their economics on hysteresis models fed with unknowable histories. The prediction error lands directly on recovery forecasts.",
 "sig_lens": "The Signature lens reads hysteresis as memory in the rock: the protocol must bound what the rock remembers instead of pretending to know its history.",
 "sig_solution": LABEL + " Assumptions: (1) saturation history is unknowable in detail; (2) hysteresis models need turning points. Reasoning path: bound the hysteresis effect - run the bounding drainage and imbibition cases and report the recovery range, rather than a single history-dependent answer. Proposed mechanism: a rock-memory protocol requiring hysteresis models to report bounding-case recoveries, calibrating the interpolation against laboratory cycle experiments, and flagging WAG designs whose economics depend on the uncertain middle. Confirm: bounding-case forecasts bracket actual WAG performance. Kill: the bounds prove too wide for decisions. Does NOT claim: the true saturation history - it bounds what the memory can do.",
 "pointer": "The Signature system's proposed approach bounds hysteresis with drainage-imbibition cases; the companion Signature Edition record specifies the rock-memory protocol.",
 "key_points": [
  "Drainage and imbibition give different relative permeability curves.",
  "Hysteresis models need turning-point saturations: the full history.",
  "Real reservoirs have unknowable detailed saturation histories.",
  "WAG processes make hysteresis first-order and its errors first-order.",
 ],
 "requirements": [
  "Bounding-case (drainage/imbibition) recovery reporting.",
  "Laboratory cycle-experiment calibration of interpolations.",
  "Flags on designs whose economics depend on uncertain hysteresis.",
 ],
 "citations": [
  "Killough JE (1976) Reservoir simulation with history-dependent saturation functions. SPE Journal 16(1).",
 ],
 "demo": {"k": 0.15, "area": 40.0, "dp": 250.0, "mu": 2.0, "L": 120.0},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "pe-wettability",
 "name": "The Wettability Alteration Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Wettability decides which fluid clings to the rock - but reservoir wettability is mixed, fractional, and altered by injections, so how can it be characterized usefully?",
 "background": "Wettability - whether rock prefers water or oil - controls capillary pressure, relative permeability, and recovery: water-wet rock imbibes water and recovers oil efficiently; oil-wet rock traps it. But most reservoirs are mixed-wet or fractional-wet, varying pore by pore, and injections (surfactants, low-salinity water, CO2) alter wettability deliberately or accidentally. Measurement (Amott, USBM indices, contact angles) gives core-scale averages that hide the pore-scale heterogeneity driving the physics. The alteration mechanisms - asphaltene adsorption, mineral reactions - are understood qualitatively and modeled poorly.",
 "why_it_matters": "Wettability is the hidden variable of recovery: the same reservoir recovers 30 or 60 percent depending on it. Uncharacterized wettability is uncharacterized recovery.",
 "sig_lens": "The Signature lens reads wettability as the rock's allegiance: the protocol must map where the allegiance lies and track when injections change it.",
 "sig_solution": LABEL + " Assumptions: (1) reservoir wettability is heterogeneous and partly altered by operations; (2) core averages hide pore-scale reality. Reasoning path: characterize wettability spatially and track its alteration - map the allegiance before and during injections. Proposed mechanism: an allegiance protocol combining multi-scale wettability measurement (pore imaging plus core indices), alteration monitoring during injections, and recovery models conditioned on the measured wettability map. Confirm: wettability-mapped models predict recovery better than uniform assumptions. Kill: the heterogeneity proves unmappable at field scale. Does NOT claim: pore-perfect wettability maps - it measures the allegiance where it matters.",
 "pointer": "The Signature system's proposed approach maps wettability heterogeneity and tracks injection-induced alteration; the companion Signature Edition record specifies the allegiance protocol.",
 "key_points": [
  "Wettability controls capillary pressure, relative permeability, and recovery.",
  "Most reservoirs are mixed- or fractional-wet, varying pore by pore.",
  "Injections alter wettability deliberately or accidentally.",
  "Core-scale indices hide the driving heterogeneity.",
 ],
 "requirements": [
  "Multi-scale wettability measurement (pore to core).",
  "Alteration monitoring during injection operations.",
  "Recovery models conditioned on measured wettability maps.",
 ],
 "citations": [
  "Anderson WG (1986) Wettability literature survey. J. Petroleum Technology 38(11).",
 ],
 "demo": {"k": 0.3, "area": 60.0, "dp": 400.0, "mu": 1.2, "L": 80.0},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "pe-wellbore-shale",
 "name": "The Wellbore Stability in Shales Problem",
 "group": "Drilling Engineering",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Shale wellbores collapse, swell, and slough - but the chemomechanical coupling behind the instability resists prediction, so how can mud weight windows be set reliably?",
 "background": "Shales - the caprock and source rock of petroleum - are chemically reactive: water-based muds invade microfractures, clays swell osmotically, and the wellbore degrades over hours to days. The stability problem couples pore pressure, in-situ stress, and chemical potential, and the models (chemo-poroelasticity) need parameters (membrane efficiency, diffusion coefficients) that are hard to measure on shales. Operators set mud weights by experience and offset-well history; the window between pore pressure (kick) and fracture gradient (losses) narrows with depth until experience fails. Unstable shales cause stuck pipe, sidetracks, and blowouts.",
 "why_it_matters": "Wellbore instability is among drilling's costliest problems: stuck pipe and sidetracks run to millions per event, and narrow-window deep wells have no margin for error.",
 "sig_lens": "The Signature lens reads shale as a reactive wall: the protocol must respect the chemistry, not just the mechanics, and keep the mud window honest.",
 "sig_solution": LABEL + " Assumptions: (1) chemomechanical coupling is real and poorly parameterized; (2) offset-well experience fails in new regimes. Reasoning path: characterize the shale's reactivity directly (membrane tests, swelling tests) and set mud windows from the coupled model with uncertainty. Proposed mechanism: a reactive-wall protocol requiring shale reactivity characterization per formation, coupled-model mud window computation with uncertainty bands, and real-time stability monitoring (torque, drag, cavings) feeding window updates. Confirm: characterized windows show fewer instability events. Kill: the characterization parameters prove unmeasurable on real shales. Does NOT claim: exact stability prediction - it respects the chemistry with honest bands.",
 "pointer": "The Signature system's proposed approach characterizes shale reactivity and sets coupled-model mud windows; the companion Signature Edition record specifies the reactive-wall protocol.",
 "key_points": [
  "Shale instability couples pore pressure, stress, and chemical potential.",
  "Chemo-poroelastic parameters are hard to measure on shales.",
  "Mud windows narrow with depth until experience fails.",
  "Instability causes stuck pipe, sidetracks, and blowouts.",
 ],
 "requirements": [
  "Formation-specific shale reactivity characterization.",
  "Coupled-model mud windows with uncertainty bands.",
  "Real-time stability monitoring feeding window updates.",
 ],
 "citations": [
  "van Oort E (2003) On the physical and chemical stability of shales. J. Petroleum Science and Engineering 38(3-4).",
 ],
 "demo": {"k": 0.1, "area": 30.0, "dp": 500.0, "mu": 3.0, "L": 150.0},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "pe-lost-circulation",
 "name": "The Lost Circulation Control Problem",
 "group": "Drilling Engineering",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Drilling mud vanishes into fractures and caverns - but how can losses be stopped when the thief zone's geometry is unknown and every cure is a gamble?",
 "background": "Lost circulation - mud flowing into the formation instead of returning - costs the industry billions yearly: fractured carbonates and depleted zones swallow mud at hundreds of barrels per hour. The cures (lost circulation materials, cement plugs, crosslinked gels) are chosen by experience against an unknown fracture geometry; particulate LCM bridges fractures only if sized to the aperture, which is unknown. Severe losses force managed-pressure or underbalanced techniques. The fundamental problem is blindness: the thief zone is characterized only by the loss rate, and every treatment is a bet placed in the dark.",
 "why_it_matters": "Lost circulation can kill a well's economics in days: mud costs, rig time, and the risk of going underbalanced into a kick. Blind treatments waste both.",
 "sig_lens": "The Signature lens reads the thief zone as a burglar alarm with no camera: the protocol must size the response to what the loss rate reveals, and escalate by rule.",
 "sig_solution": LABEL + " Assumptions: (1) fracture geometry is unknown; only loss rate is observed; (2) LCM bridging needs aperture sizing. Reasoning path: infer fracture scale from loss dynamics and escalate treatments by a measured ladder, not by hope. Proposed mechanism: a burglar protocol classifying losses by rate and trend (seepage, partial, severe, total), inferring fracture aperture ranges from transient analysis, and escalating LCM-to-gel-to-cement by rule - with each step's success criteria defined before pumping. Confirm: ladder-escalated treatments control losses faster and cheaper. Kill: the inference proves unreliable and escalation mistimes. Does NOT claim: thief-zone characterization - it responds to what the losses reveal.",
 "pointer": "The Signature system's proposed approach escalates lost-circulation treatments by a measured ladder; the companion Signature Edition record specifies the burglar protocol.",
 "key_points": [
  "Lost circulation costs billions yearly; fractured zones swallow mud.",
  "LCM bridging requires aperture sizing against unknown geometry.",
  "Treatments are chosen by experience - bets placed in the dark.",
  "Severe losses force managed-pressure techniques.",
 ],
 "requirements": [
  "Loss classification by rate and trend.",
  "Fracture-aperture inference from loss transients.",
  "Rule-based treatment escalation with predefined success criteria.",
 ],
 "citations": [
  "Lavrov A (2016) Lost Circulation: Mechanisms and Solutions. Gulf Professional.",
 ],
 "demo": {"k": 0.25, "area": 45.0, "dp": 350.0, "mu": 1.8, "L": 90.0},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "pe-drilling-fluid",
 "name": "The Drilling Fluid Optimization Problem",
 "group": "Drilling Engineering",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Drilling fluid must cool, clean, stabilize, and control pressure simultaneously - but how can the formulation be optimized when the objectives conflict downhole?",
 "background": "Drilling mud is a engineered fluid balancing rheology (cuttings transport), density (pressure control), filtration (wall building), lubricity, and shale inhibition - and the optimum shifts with depth, temperature, and formation. High-pressure high-temperature wells degrade polymers; deepwater needs flat rheology; shale sections need inhibition. The formulation science is mature yet the optimization is not: downhole conditions are inferred, fluid properties are measured at surface, and the coupling (temperature-thinned rheology failing to clean the hole) is handled by rules of thumb. Equivalent circulating density management in narrow windows leaves no margin for fluid error.",
 "why_it_matters": "Mud problems cause most non-productive time in drilling. The fluid is the well's lifeblood; misformulated, it poisons everything it touches.",
 "sig_lens": "The Signature lens reads mud as the well's blood: the protocol must monitor its vital signs downhole and transfuse before the patient crashes.",
 "sig_solution": LABEL + " Assumptions: (1) downhole conditions are inferred from surface measurements; (2) objectives conflict and shift with depth. Reasoning path: monitor fluid performance downhole (pressure-while-drilling, cuttings returns) and adjust formulation against measured deficits. Proposed mechanism: a bloodwork protocol with downhole-calibrated hydraulics models, formulation adjustments triggered by measured transport and stability deficits, and narrow-window ECD management with real-time density control. Confirm: monitored formulations show less non-productive time. Kill: downhole inference proves too uncertain to guide formulation. Does NOT claim: optimal mud formulations - it transfuses on measured vital signs.",
 "pointer": "The Signature system's proposed approach adjusts drilling fluids on downhole-measured deficits; the companion Signature Edition record specifies the bloodwork protocol.",
 "key_points": [
  "Mud balances rheology, density, filtration, lubricity, and inhibition.",
  "Optima shift with depth, temperature, and formation.",
  "Downhole conditions are inferred; properties measured at surface.",
  "Narrow-window wells leave no margin for fluid error.",
 ],
 "requirements": [
  "Downhole-calibrated hydraulics models.",
  "Formulation adjustments on measured transport deficits.",
  "Real-time ECD management in narrow windows.",
 ],
 "citations": [
  "Caenn R, Darley HCH, Gray GR (2016) Composition and Properties of Drilling and Completion Fluids, 7th ed. Gulf Professional.",
 ],
 "demo": {"k": 0.18, "area": 55.0, "dp": 280.0, "mu": 2.2, "L": 110.0},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "pe-rop",
 "name": "The Rate of Penetration Limit Problem",
 "group": "Drilling Engineering",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "What fundamentally limits how fast a bit can drill rock - and how close can operations get to the limit without destroying the bit?",
 "background": "Rate of penetration (ROP) is drilling's speedometer, and its limits are murky: the founder point (beyond which more weight-on-bit stops helping), bit-balling, vibrations (stick-slip, whirl) that destroy bits and tools. Drilling optimization (MSE - mechanical specific energy) identifies the founder point from data, but the models are empirical and formation-specific. The deeper limit is the rock-bit interaction physics: cutter-rock fracture mechanics at the microscale, modeled but not validated across lithologies. Automation (drilling advisory systems) pushes toward the limit, but the limit itself moves with the rock.",
 "why_it_matters": "Rig time costs tens to hundreds of thousands per day. The gap between actual and limit ROP is paid daily in rig spread rate.",
 "sig_lens": "The Signature lens reads ROP as a speed limit that moves with the rock: the protocol must find the current limit continuously and drive just under it.",
 "sig_solution": LABEL + " Assumptions: (1) the ROP limit is formation-dependent and moves; (2) vibrations destroy the economics of pushing harder. Reasoning path: detect the founder point and vibration onset in real time, and operate at the constrained optimum. Proposed mechanism: a speed-limit protocol using MSE-based founder detection, real-time vibration monitoring with automatic parameter backoff, and per-formation limit learning feeding the next well's plan. Confirm: limit-operated wells drill faster with fewer bit trips. Kill: the detection lags and bits are destroyed before backoff. Does NOT claim: the fundamental rock-bit limit - it drives at the measured limit.",
 "pointer": "The Signature system's proposed approach operates drilling at real-time-detected ROP limits; the companion Signature Edition record specifies the speed-limit protocol.",
 "key_points": [
  "The founder point marks where more weight stops helping ROP.",
  "Vibrations (stick-slip, whirl) destroy bits when limits are pushed.",
  "MSE identifies founder points empirically and formation-specifically.",
  "Rock-bit fracture physics is modeled but not validated across lithologies.",
 ],
 "requirements": [
  "Real-time founder-point detection via MSE.",
  "Vibration monitoring with automatic parameter backoff.",
  "Per-formation limit learning across wells.",
 ],
 "citations": [
  "Teale R (1965) The concept of specific energy in rock drilling. Int. J. Rock Mechanics 2(1).",
 ],
 "demo": {"k": 0.22, "area": 48.0, "dp": 320.0, "mu": 1.6, "L": 95.0},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "pe-asphaltene",
 "name": "The Asphaltene Deposition Problem",
 "group": "Production Engineering",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Asphaltenes - crude oil's heaviest fraction - precipitate and plug wells and flowlines, but when and where remains hard to predict, so how can deposition be prevented?",
 "background": "Asphaltenes are defined by insolubility (in n-heptane), not by structure - a solubility class, not a molecule - which is why prediction is hard: pressure drops, gas injection, and commingling destabilize them, and the precipitation envelopes (measured by depressurization tests) are expensive and uncertain. Deposition plugs tubing, chokes flowlines, and poisons catalysts; remediation (solvent soaks, mechanical removal) is costly and temporary. Inhibitors exist but their selection is empirical. The molecular-to-deposit scale gap - from nanoaggregates (Yen-Mullins model) to pipeline plugs - is unbridged.",
 "why_it_matters": "Asphaltene plugs have shut in major fields. The deposition is irreversible enough and unpredictable enough to be a flow-assurance nightmare.",
 "sig_lens": "The Signature lens reads asphaltenes as a solubility cliff: the protocol must map the cliff for each crude and keep operations back from the edge.",
 "sig_solution": LABEL + " Assumptions: (1) asphaltenes are a solubility class, not a molecule; (2) precipitation envelopes are expensive and uncertain. Reasoning path: map the envelope per crude, monitor the operating point's distance to it, and intervene (inhibitors, pressure management) before crossing. Proposed mechanism: a cliff protocol with measured precipitation envelopes per crude, real-time tracking of operating conditions against the envelope, and inhibitor programs qualified on the specific crude. Confirm: envelope-tracked operations show fewer deposition events. Kill: the envelopes prove too uncertain to keep distance from. Does NOT claim: molecular prediction of deposition - it maps the cliff and keeps back.",
 "pointer": "The Signature system's proposed approach tracks operations against measured asphaltene envelopes; the companion Signature Edition record specifies the cliff protocol.",
 "key_points": [
  "Asphaltenes are a solubility class, which is why prediction is hard.",
  "Pressure drops and gas injection destabilize them.",
  "Deposition plugs wells and flowlines; remediation is costly and temporary.",
  "The nanoaggregate-to-plug scale gap is unbridged.",
 ],
 "requirements": [
  "Measured precipitation envelopes per crude.",
  "Real-time operating-point versus envelope tracking.",
  "Crude-specific inhibitor qualification.",
 ],
 "citations": [
  "Mullins OC et al. (2007) Asphaltenes, Heavy Oils, and Petroleomics. Springer.",
 ],
 "demo": {"k": 0.12, "area": 38.0, "dp": 420.0, "mu": 2.8, "L": 130.0},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "pe-scale",
 "name": "The Scale Formation Prediction Problem",
 "group": "Production Engineering",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Mixing incompatible waters precipitates mineral scale that chokes production - but can scaling be predicted before the well is drilled, and prevented economically?",
 "background": "Scale - barium sulfate, calcium carbonate, strontium sulfate - precipitates when formation water meets injected seawater: the thermodynamics (saturation indices) are calculable, but the kinetics (where and how fast it deposits) are not. Barium sulfate is nearly insoluble once formed; prevention (scale inhibitors squeezed into the formation) is the only real option, and squeeze lifetimes are uncertain. Prediction tools (ScaleChem, MultiScale) compute saturation but not deposition location or rate. The economic question - inhibitor program cost versus workover cost - is decided on rules of thumb.",
 "why_it_matters": "Scale has killed wells outright: barium sulfate plugs are nearly permanent. Prevention chemistry is cheap; remediation is often impossible.",
 "sig_lens": "The Signature lens reads scale as a chemical ambush: the protocol must predict where the waters meet and lay the inhibitor defense before they do.",
 "sig_solution": LABEL + " Assumptions: (1) thermodynamics predicts saturation, not deposition location or rate; (2) barium sulfate is nearly permanent once formed. Reasoning path: model the mixing front's movement, place inhibitors ahead of it, and verify with produced-water chemistry. Proposed mechanism: an ambush protocol computing saturation along the flow path, scheduling inhibitor squeezes ahead of the scaling front, and monitoring produced-water chemistry for breakthrough. Confirm: front-tracked inhibition prevents scale at lower chemical cost. Kill: the front proves unpredictable and squeezes mistime. Does NOT claim: deposition kinetics prediction - it defends ahead of the front.",
 "pointer": "The Signature system's proposed approach places scale inhibitors ahead of the modeled mixing front; the companion Signature Edition record specifies the ambush protocol.",
 "key_points": [
  "Scale precipitates where incompatible waters mix.",
  "Thermodynamics gives saturation; kinetics of deposition are unmodeled.",
  "Barium sulfate plugs are nearly permanent.",
  "Inhibitor squeeze lifetimes are uncertain.",
 ],
 "requirements": [
  "Saturation modeling along the flow path.",
  "Inhibitor squeezes scheduled ahead of the scaling front.",
  "Produced-water chemistry monitoring for breakthrough.",
 ],
 "citations": [
  "Mackay EJ (2005) Modeling in-situ scale deposition. SPE 100522.",
 ],
 "demo": {"k": 0.16, "area": 42.0, "dp": 380.0, "mu": 2.4, "L": 105.0},
},
# ----------------------------------------------------------------- rank 10
{
 "key": "pe-hydrates",
 "name": "The Hydrate Formation Prevention Problem",
 "group": "Production Engineering",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Gas hydrates - ice-like solids - can plug deepwater flowlines solid, but where exactly will they form, and what is the cheapest reliable prevention?",
 "background": "Gas hydrates form at high pressure and low temperature - exactly deepwater conditions - when water meets light hydrocarbons: the result can be a plug requiring weeks of remediation. Prevention spans thermodynamic inhibitors (methanol, MEG - expensive and logistically heavy), low-dosage hydrate inhibitors (kinetic and anti-agglomerant - cheaper but less certain), and thermal management (insulation, heating). The hydrate equilibrium curve is well known; the operating question - how much margin, which inhibitor, at what cost - is decided per field with incomplete information. Anti-agglomerants let hydrates form but keep them transportable - a paradigm shift with its own uncertainties.",
 "why_it_matters": "A hydrate plug can shut a deepwater field for weeks at millions per day. Prevention chemistry is the operating cost that never ends.",
 "sig_lens": "The Signature lens reads hydrates as frost in the pipes: the protocol must keep the flow warm enough, chemically or thermally, and know exactly where the frost line sits.",
 "sig_solution": LABEL + " Assumptions: (1) the equilibrium curve is known; the operating margin decision is not; (2) LDHIs trade cost against certainty. Reasoning path: manage the subcooling margin explicitly - compute it along the flowline in real time and dose inhibitors to hold it. Proposed mechanism: a frost-line protocol with real-time subcooling computation, inhibitor dosing tied to the measured margin, and thermal design (insulation) sized to the worst-case cooldown. Confirm: margin-managed fields show fewer plug events at lower chemical cost. Kill: the margin computation misses local cold spots. Does NOT claim: a universal prevention optimum - it holds the frost line where measured.",
 "pointer": "The Signature system's proposed approach manages hydrate subcooling margins in real time; the companion Signature Edition record specifies the frost-line protocol.",
 "key_points": [
  "Hydrates form at deepwater pressure-temperature conditions.",
  "Plugs can shut fields for weeks; remediation is slow.",
  "Thermodynamic inhibitors are certain but expensive; LDHIs cheaper but less certain.",
  "Anti-agglomerants shift the paradigm to transportable hydrates.",
 ],
 "requirements": [
  "Real-time subcooling margin computation along flowlines.",
  "Inhibitor dosing tied to measured margins.",
  "Thermal design sized to worst-case cooldowns.",
 ],
 "citations": [
  "Sloan ED, Koh CA (2007) Clathrate Hydrates of Natural Gases, 3rd ed. CRC Press.",
 ],
 "demo": {"k": 0.14, "area": 36.0, "dp": 460.0, "mu": 2.6, "L": 140.0},
},
# ----------------------------------------------------------------- rank 11
{
 "key": "pe-sour-corrosion",
 "name": "The Corrosion in Sour Service Problem",
 "group": "Production Engineering",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Hydrogen sulfide makes steel crack and corrode - but how can materials be qualified for sour service when the cracking depends on the exact service chemistry?",
 "background": "Sour service - H2S-bearing production - brings sulfide stress cracking (SSC), hydrogen-induced cracking, and rapid corrosion: NACE MR0175/ISO 15156 qualifies materials by region and severity, but the boundaries are conservative and contested. The cracking depends on pH, H2S partial pressure, temperature, and stress in coupled ways that lab tests approximate; field failures still occur in qualified materials when conditions drift. Corrosion prediction (de Waard-Milliams and successors) handles CO2 well and H2S poorly. Inhibitors and CRA (corrosion-resistant alloy) upgrades are the defenses; the qualification gap is the residual risk.",
 "why_it_matters": "Sour failures are sudden and catastrophic: SSC gives no warning. The qualification boundaries are where safety meets economics, and both sides are uncertain.",
 "sig_lens": "The Signature lens reads sour service as a corrosive atmosphere: the protocol must monitor the actual chemistry and keep materials qualified for it, not for the design case.",
 "sig_solution": LABEL + " Assumptions: (1) qualification boundaries are conservative and contested; (2) field chemistry drifts from design. Reasoning path: monitor the actual service chemistry continuously and re-qualify materials against it - never assume the design case persists. Proposed mechanism: an atmosphere protocol with continuous H2S/pH/temperature monitoring, material re-qualification triggers on chemistry drift, and corrosion-rate tracking feeding remaining-life estimates. Confirm: monitored systems catch qualification exceedances before failures. Kill: monitoring misses local chemistry (under-deposit, crevice) and failures surprise. Does NOT claim: exact sour-cracking prediction - it keeps the qualification honest to the actual atmosphere.",
 "pointer": "The Signature system's proposed approach re-qualifies sour-service materials against monitored chemistry; the companion Signature Edition record specifies the atmosphere protocol.",
 "key_points": [
  "H2S causes sulfide stress cracking with little warning.",
  "NACE MR0175 boundaries are conservative and contested.",
  "Cracking couples pH, H2S pressure, temperature, and stress.",
  "Field chemistry drifts from design assumptions.",
 ],
 "requirements": [
  "Continuous service-chemistry monitoring.",
  "Material re-qualification triggers on chemistry drift.",
  "Corrosion-rate tracking feeding remaining-life estimates.",
 ],
 "citations": [
  "NACE MR0175/ISO 15156: Materials in sour oilfield environments.",
 ],
 "demo": {"k": 0.2, "area": 52.0, "dp": 300.0, "mu": 1.4, "L": 88.0},
},
# ----------------------------------------------------------------- rank 12
{
 "key": "pe-eor-limit",
 "name": "The Enhanced Oil Recovery Efficiency Limit Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Primary and secondary recovery leave most oil behind - but what is the true efficiency limit of enhanced recovery, and which methods approach it economically?",
 "background": "Conventional recovery leaves 60-80 percent of oil in place; EOR (thermal, gas, chemical) targets the rest, yet global EOR production is a small fraction of output. Each method has a theoretical limit - miscible displacement approaches 100 percent microscopically but sweeps poorly; thermal methods are energy-intensive; chemical methods fight adsorption and degradation. The screening problem (which EOR fits which reservoir) is heuristic, pilot tests are expensive and often inconclusive, and the economic limit (oil price versus EOR cost) moves with markets. The gap between technical potential and economic reality is EOR's defining feature.",
 "why_it_matters": "The world's largest oil resource is the oil already discovered but unrecovered. EOR's efficiency limit decides how much of it is ever produced.",
 "sig_lens": "The Signature lens reads EOR as a second harvest: the protocol must prove the second crop pays before planting it.",
 "sig_solution": LABEL + " Assumptions: (1) technical potential far exceeds economic reality; (2) pilots are expensive and often inconclusive. Reasoning path: screen rigorously on economics first - compute the method's efficiency limit for the specific reservoir, then require the pilot to clear an economic hurdle. Proposed mechanism: a second-harvest protocol with reservoir-specific EOR efficiency modeling, staged pilots gated on economic thresholds, and full-cycle economics (including energy and chemical costs) before scale-up. Confirm: hurdle-gated EOR programs show better returns than technology-pushed ones. Kill: the efficiency models prove unreliable and hurdles mislead. Does NOT claim: the universal EOR limit - it proves the harvest pays per reservoir.",
 "pointer": "The Signature system's proposed approach gates EOR on reservoir-specific economic hurdles; the companion Signature Edition record specifies the second-harvest protocol.",
 "key_points": [
  "Conventional recovery leaves 60-80 percent of oil in place.",
  "Each EOR method has theoretical limits and practical shortfalls.",
  "Screening is heuristic; pilots are expensive and often inconclusive.",
  "The economic limit moves with oil prices and costs.",
 ],
 "requirements": [
  "Reservoir-specific EOR efficiency modeling.",
  "Staged pilots gated on economic thresholds.",
  "Full-cycle economics before scale-up.",
 ],
 "citations": [
  "Lake LW (1989) Enhanced Oil Recovery. Prentice Hall.",
 ],
 "demo": {"k": 0.28, "area": 65.0, "dp": 380.0, "mu": 1.1, "L": 75.0},
},
# ----------------------------------------------------------------- rank 13
{
 "key": "pe-sparse-characterization",
 "name": "The Reservoir Characterization From Sparse Data Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Reservoirs are kilometers wide and sampled by a handful of wells - how can the spaces between wells be characterized well enough to place the next billion-dollar decision?",
 "background": "A reservoir model has millions of cells; the hard data is a few well logs and cores. Geostatistics (kriging, sequential simulation) interpolates with uncertainty, seismic adds soft constraints, and history matching tunes the model to production data - non-uniquely, since many models match the same history. The ensemble methods (ensemble Kalman filter) quantify uncertainty but depend on the prior ensemble's diversity. The fundamental problem is underdetermination: the data cannot distinguish the models, yet decisions (well placement, EOR) need one. Practitioners pick the history-matched model and hope it predicts.",
 "why_it_matters": "Well placement and EOR decisions worth billions rest on models the data cannot uniquely determine. The underdetermination is the industry's open secret.",
 "sig_lens": "The Signature lens reads the reservoir as a dark room mapped by touch: the protocol must carry the uncertainty of every unmapped corner into the decision.",
 "sig_solution": LABEL + " Assumptions: (1) the problem is fundamentally underdetermined; (2) history matching is non-unique. Reasoning path: decide on ensembles, not single models - carry the full range of history-matched realizations into every decision and optimize for robustness across them. Proposed mechanism: a dark-room protocol maintaining diverse model ensembles, requiring decisions to perform acceptably across the ensemble (not just the best-match model), and valuing new data by its uncertainty-reduction. Confirm: ensemble-robust decisions outperform single-model ones out-of-sample. Kill: the ensemble misses the true geology and the robustness is misplaced. Does NOT claim: the true reservoir description - it decides under honest uncertainty.",
 "pointer": "The Signature system's proposed approach decides on diverse model ensembles with robustness requirements; the companion Signature Edition record specifies the dark-room protocol.",
 "key_points": [
  "Million-cell models are constrained by a handful of wells.",
  "History matching is non-unique: many models fit the same data.",
  "Ensemble methods depend on prior diversity.",
  "Decisions need one model; the data supports many.",
 ],
 "requirements": [
  "Diverse history-matched model ensembles maintained.",
  "Decisions robust across the ensemble, not tuned to one model.",
  "New data valued by uncertainty reduction.",
 ],
 "citations": [
  "Oliver DS, Reynolds AC, Liu N (2008) Inverse Theory for Petroleum Reservoir Characterization. Springer.",
 ],
 "demo": {"k": 0.19, "area": 58.0, "dp": 340.0, "mu": 1.9, "L": 92.0},
},
# ----------------------------------------------------------------- rank 14
{
 "key": "pe-proppant",
 "name": "The Hydraulic Fracturing Proppant Transport Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Proppant must ride fracturing fluid deep into cracks and stay there - but how does it actually transport and settle, and why do fractures close on empty rock?",
 "background": "Proppant (sand, ceramic) holds fractures open; its transport - carried by viscous fluid, settling by gravity, bridging at constrictions - determines the productive fracture area. The physics couples slurry rheology, fracture mechanics, and particle settling in narrow, evolving geometries; models (pseudo-3D, planar 3D) approximate aggressively. Field diagnostics (microseismic, fiber, tracers) show proppant often settles near the wellbore while fractures extend far beyond - the industry fractures big and props small. The transport efficiency - what fraction of created area is propped - is the shale industry's central inefficiency.",
 "why_it_matters": "Unpropped fracture area is wasted stimulation: the industry pays to crack rock it then lets close. Transport efficiency is the shale productivity lever.",
 "sig_lens": "The Signature lens reads proppant as cargo on a river that keeps changing course: the protocol must track where the cargo actually lands, not where the river was planned to go.",
 "sig_solution": LABEL + " Assumptions: (1) transport models approximate aggressively; (2) diagnostics show proppant settling near-wellbore. Reasoning path: measure the propped area directly (fiber, tracers, production logs) and redesign the pump schedule to the measured transport, not the modeled one. Proposed mechanism: a cargo protocol requiring propped-area diagnostics per stage, pump-schedule redesign based on measured settling, and fluid/proppant selection tied to the observed transport regime. Confirm: diagnostically redesigned stages show higher propped-area fractions. Kill: diagnostics prove too uncertain to guide redesign. Does NOT claim: exact proppant transport prediction - it lands the cargo where measured.",
 "pointer": "The Signature system's proposed approach redesigns fracturing on measured proppant placement; the companion Signature Edition record specifies the cargo protocol.",
 "key_points": [
  "Proppant transport couples slurry rheology, fracture mechanics, and settling.",
  "Models approximate the evolving narrow geometry aggressively.",
  "Diagnostics show fractures extending far beyond propped regions.",
  "Transport efficiency is the shale industry's central inefficiency.",
 ],
 "requirements": [
  "Propped-area diagnostics per fracturing stage.",
  "Pump-schedule redesign on measured settling.",
  "Fluid and proppant selection tied to observed transport.",
 ],
 "citations": [
  "Economides MJ, Nolte KG (2000) Reservoir Stimulation, 3rd ed. Wiley.",
 ],
 "demo": {"k": 0.24, "area": 44.0, "dp": 360.0, "mu": 1.7, "L": 85.0},
},
# ----------------------------------------------------------------- rank 15
{
 "key": "pe-fracture-network",
 "name": "The Fracture Network Complexity Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Hydraulic fracturing creates complex networks, not planar cracks - but what does the network actually look like, and which parts produce?",
 "background": "The planar-fracture model is dead: microseismic clouds, fiber strain, and core-through studies reveal branching, tortuous networks interacting with natural fractures. Discrete fracture network (DFN) models generate statistically equivalent networks, but the statistics are inferred from indirect data and the flow simulation on DFNs is expensive and uncertain. The stimulated reservoir volume (SRV) concept - the microseismic cloud as productive volume - has been largely discredited: much of the cloud does not produce. Which fractures conduct, which are propped, and which connect to the wellbore remain partially known at best.",
 "why_it_matters": "Fracturing is the shale industry's largest cost. Designing stages for a network nobody can see is designing blind - the complexity is where the money goes.",
 "sig_lens": "The Signature lens reads the fracture network as a root system: the protocol must find which roots drink (produce) rather than admire the whole tangle.",
 "sig_solution": LABEL + " Assumptions: (1) SRV-as-productive-volume is discredited; (2) DFN statistics are inferred indirectly. Reasoning path: identify the productive fractures directly - production logs, tracers, pressure interference - and calibrate the network models to production, not microseismic. Proposed mechanism: a root protocol requiring productive-fracture identification per well, DFN calibration against production data, and stage-design changes tested against the productive network. Confirm: production-calibrated designs outperform microseismic-calibrated ones. Kill: productive fractures prove unidentifiable and calibration is circular. Does NOT claim: the true fracture network - it finds the roots that drink.",
 "pointer": "The Signature system's proposed approach calibrates fracture models to productive fractures, not microseismic clouds; the companion Signature Edition record specifies the root protocol.",
 "key_points": [
  "Fracture networks are branching and tortuous, not planar.",
  "The SRV concept (microseismic cloud equals productive volume) is discredited.",
  "DFN statistics are inferred from indirect data.",
  "Which fractures conduct and connect remains partially known.",
 ],
 "requirements": [
  "Productive-fracture identification per well.",
  "DFN calibration against production data.",
  "Stage designs tested against the productive network.",
 ],
 "citations": [
  "Warpinski NR et al. (2013) Measurements of hydraulic-fracture-induced seismicity. SPE 151597.",
 ],
 "demo": {"k": 0.21, "area": 50.0, "dp": 330.0, "mu": 2.1, "L": 98.0},
},
# ----------------------------------------------------------------- rank 16
{
 "key": "pe-induced-seismicity",
 "name": "The Induced Seismicity Prediction Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Fluid injection can trigger earthquakes - but which injections will, when, and how big, and can the risk be managed without stopping operations?",
 "background": "Wastewater disposal and hydraulic fracturing have induced felt earthquakes (Oklahoma, Texas, UK, Netherlands-Groningen): injection raises pore pressure, unclamping faults. The physics (rate-and-state friction, pressure diffusion) is understood qualitatively; prediction is not: the fault inventory is unknown (most faults are unmapped), the critical pressure is unmeasured, and the maximum magnitude is debated. Traffic-light systems (UK) pause operations on seismicity, but the thresholds are reactive. The Groningen field's induced earthquakes - damaging houses, ending production - showed the social license risk exceeds the technical one.",
 "why_it_matters": "Induced earthquakes have shut down operations and ended fields. The risk is technical, but the consequence is social license - and it is unforgiving.",
 "sig_lens": "The Signature lens reads injection as pressure on unknown faults: the protocol must listen for the rock's complaints and throttle before it shouts.",
 "sig_solution": LABEL + " Assumptions: (1) fault inventories are unknown; (2) critical pressures are unmeasured. Reasoning path: operate adaptively - monitor seismicity in real time, map the pressure front, and throttle injection on measured response. Proposed mechanism: a listening protocol with dense seismic monitoring, pressure-front tracking, and traffic-light thresholds set from the local seismic response (not generic magnitudes) - with automatic throttling. Confirm: adaptive throttling prevents felt events better than fixed schedules. Kill: the first felt event precedes any warning and adaptation is too late. Does NOT claim: earthquake prediction - it listens and throttles.",
 "pointer": "The Signature system's proposed approach throttles injection on real-time seismic response; the companion Signature Edition record specifies the listening protocol.",
 "key_points": [
  "Injection raises pore pressure, unclamping faults (Oklahoma, Groningen).",
  "Fault inventories are unknown; critical pressures unmeasured.",
  "Maximum induced magnitude is debated.",
  "Traffic-light systems are reactive, not predictive.",
 ],
 "requirements": [
  "Dense real-time seismic monitoring around injection.",
  "Pressure-front tracking tied to injection rates.",
  "Adaptive throttling on locally calibrated thresholds.",
 ],
 "citations": [
  "Ellsworth WL (2013) Injection-induced earthquakes. Science 341(6142).",
 ],
 "demo": {"k": 0.17, "area": 47.0, "dp": 390.0, "mu": 2.3, "L": 108.0},
},
# ----------------------------------------------------------------- rank 17
{
 "key": "pe-desorption",
 "name": "The Shale Gas Desorption Kinetics Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Shale gas lives adsorbed on organic matter and in nano-pores - but how fast does it desorb and diffuse, and why do production forecasts keep missing?",
 "background": "Shale stores gas as free gas in pores and adsorbed gas on kerogen (Langmuir isotherms); production needs desorption, diffusion through nano-darcy matrix, and Darcy flow through fractures. The kinetics couple across scales - adsorption equilibrium is fast, matrix diffusion is slow, and the models (dual-porosity, MINC) approximate the coupling. The desorption parameters are measured on crushed samples that destroy the pore structure being measured. Forecasts systematically overestimate late-life production: the long tail of desorption-diffusion is slower than the models say, and the EUR (estimated ultimate recovery) per well keeps being revised.",
 "why_it_matters": "Shale EUR underpins company valuations and energy policy. The desorption tail is where the forecasts meet reality - usually disappointing it.",
 "sig_lens": "The Signature lens reads shale as a slow exhale: the protocol must measure the breath rate directly and never mistake the initial gasp for the lung capacity.",
 "sig_solution": LABEL + " Assumptions: (1) crushed-sample measurements destroy the measured structure; (2) forecasts overestimate the desorption tail. Reasoning path: calibrate desorption-diffusion on intact samples and production data, and forecast with the calibrated tail. Proposed mechanism: an exhale protocol requiring intact-sample desorption measurement, dual-porosity models calibrated to early production, and EUR forecasts with tail-uncertainty bands. Confirm: calibrated-tail forecasts match late-life production better. Kill: the tail proves unmeasurable and bands are too wide. Does NOT claim: exact desorption kinetics - it measures the exhale honestly.",
 "pointer": "The Signature system's proposed approach calibrates shale desorption on intact samples with tail-uncertainty bands; the companion Signature Edition record specifies the exhale protocol.",
 "key_points": [
  "Shale gas is free plus adsorbed; desorption-diffusion is the slow step.",
  "Crushed-sample measurements destroy the pore structure measured.",
  "Forecasts systematically overestimate late-life production.",
  "EUR per well keeps being revised downward.",
 ],
 "requirements": [
  "Intact-sample desorption kinetics measurement.",
  "Dual-porosity calibration to early production.",
  "EUR forecasts with tail-uncertainty bands.",
 ],
 "citations": [
  "Javadpour F (2009) Nanopores and apparent permeability of gas flow in mudrocks. J. Canadian Petroleum Technology 48(8).",
 ],
 "demo": {"k": 0.26, "area": 54.0, "dp": 310.0, "mu": 1.3, "L": 82.0},
},
# ----------------------------------------------------------------- rank 18
{
 "key": "pe-decline-curve",
 "name": "The Tight Oil Decline Curve Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Tight oil wells decline hyperbolically then exponentially - or do they? How can EUR be estimated when the decline model itself is uncertain?",
 "background": "Arps decline curves (1945) - exponential, hyperbolic, harmonic - were derived for boundary-dominated flow; tight oil wells spend years in transient linear flow, where Arps misapplies. The industry fits hyperbolic Arps anyway, with terminal decline rates imposed by rule (5 percent minimum) to prevent infinite reserves. Duong, stretched-exponential, and physics-based models compete; each fits history and diverges on forecast. The SEC reserves booking rests on these curves: the model choice moves booked reserves by factors, yet the choice is more convention than science.",
 "why_it_matters": "Booked reserves are company value. The decline model is the pen that writes the number - and the pen is held by convention.",
 "sig_lens": "The Signature lens reads decline curves as handwriting analysis: the protocol must check the script against the physics of the flow regime, not just the fit.",
 "sig_solution": LABEL + " Assumptions: (1) Arps was derived for boundary-dominated flow; (2) model choice moves reserves by factors. Reasoning path: diagnose the flow regime first (transient versus boundary-dominated), fit only regime-appropriate models, and report the model-spread as uncertainty. Proposed mechanism: a handwriting protocol requiring flow-regime diagnosis (rate-transient analysis) before model selection, multi-model EUR with the spread reported, and terminal-decline assumptions stated explicitly. Confirm: regime-diagnosed forecasts beat blind Arps fits. Kill: regime diagnosis proves ambiguous and the spread is too wide. Does NOT claim: the true decline - it fits the regime honestly and shows the spread.",
 "pointer": "The Signature system's proposed approach diagnoses flow regimes before fitting decline models; the companion Signature Edition record specifies the handwriting protocol.",
 "key_points": [
  "Arps curves assume boundary-dominated flow; tight wells stay transient for years.",
  "Terminal decline floors are imposed by rule to prevent infinite reserves.",
  "Competing models fit history and diverge on forecast.",
  "Model choice moves booked reserves by factors.",
 ],
 "requirements": [
  "Flow-regime diagnosis via rate-transient analysis.",
  "Multi-model EUR with reported spread.",
  "Explicit terminal-decline assumptions.",
 ],
 "citations": [
  "Arps JJ (1945) Analysis of decline curves. Trans. AIME 160(1).",
 ],
 "demo": {"k": 0.23, "area": 49.0, "dp": 345.0, "mu": 1.5, "L": 87.0},
},
# ----------------------------------------------------------------- rank 19
{
 "key": "pe-waterflood",
 "name": "The Waterflooding Sweep Efficiency Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Waterflooding is the workhorse of secondary recovery - but why does injected water channel through high-permeability streaks, leaving oil unswept, and can conformance be fixed?",
 "background": "Water displaces oil, but heterogeneity channels it: the injected water races through high-permeability paths, breaking through early while low-permeability zones stay unswept. The sweep efficiency - areal, vertical, microscopic - multiplies to dismal totals in heterogeneous reservoirs. Conformance control (polymer gels, foam, intelligent wells) tries to block the thief zones, but placement is uncertain and the treatments degrade. Pattern floods, line drives, and peripheral injection each suit some geometries; the optimization of pattern and rate for a heterogeneous reality is heuristic. Most waterfloods recover far less than their volumetric promise.",
 "why_it_matters": "Waterflooding produces most of the world's secondary oil. The sweep shortfall is the difference between the oil contacted and the oil left behind.",
 "sig_lens": "The Signature lens reads waterflooding as irrigation: the protocol must find where the water actually goes and dam the channels that steal it.",
 "sig_solution": LABEL + " Assumptions: (1) heterogeneity channels injection; (2) conformance treatments degrade and misplace. Reasoning path: map the channels with tracers and logs, then place conformance treatments surgically. Proposed mechanism: an irrigation protocol requiring interwell tracer and logging to map thief zones, targeted conformance treatments with placement verification, and pattern/rate re-optimization on the mapped heterogeneity. Confirm: mapped conformance control lifts sweep efficiency measurably. Kill: the channels shift faster than treatments can follow. Does NOT claim: perfect sweep - it dams the measured channels.",
 "pointer": "The Signature system's proposed approach maps thief zones and places conformance treatments surgically; the companion Signature Edition record specifies the irrigation protocol.",
 "key_points": [
  "Heterogeneity channels injected water through high-permeability streaks.",
  "Sweep efficiencies multiply areal, vertical, and microscopic shortfalls.",
  "Conformance treatments (gels, foam) degrade and misplace.",
  "Most waterfloods recover far less than volumetric promise.",
 ],
 "requirements": [
  "Thief-zone mapping via tracers and interwell logging.",
  "Surgically placed conformance treatments with verification.",
  "Pattern and rate re-optimization on mapped heterogeneity.",
 ],
 "citations": [
  "Craig FF (1971) The Reservoir Engineering Aspects of Waterflooding. SPE.",
 ],
 "demo": {"k": 0.27, "area": 62.0, "dp": 290.0, "mu": 1.0, "L": 78.0},
},
# ----------------------------------------------------------------- rank 20
{
 "key": "pe-co2-miscibility",
 "name": "The CO2 EOR Miscibility Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "CO2 can mix miscibly with oil and sweep it nearly completely - but will a given crude achieve miscibility at reservoir pressure, and what does it cost to find out?",
 "background": "Miscible CO2 flooding - the premier EOR method in the Permian - needs the minimum miscibility pressure (MMP) below reservoir pressure: the slim-tube test measures it, but slim tubes are 1D, slow, and expensive, while the reservoir is 3D and heterogeneous. MMP correlations (Yellig-Metcalfe, Cronquist) are crude-specific and often wrong; equation-of-state tuning to PVT data is the modern approach but non-unique. Near-miscible operation is the economic reality - and its efficiency is the least predictable regime. CO2 supply (natural domes, now captured anthropogenic) constrains every project.",
 "why_it_matters": "CO2 EOR is the largest EOR method and the bridge to carbon storage. Miscibility is the binary that decides whether the flood works.",
 "sig_lens": "The Signature lens reads miscibility as a handshake: the protocol must verify the CO2 and oil actually mix at the pressure they will meet.",
 "sig_solution": LABEL + " Assumptions: (1) slim-tube MMP is 1D and expensive; (2) near-miscible is the economic reality. Reasoning path: determine MMP by the most reliable affordable method per project, design for the measured MMP with margin, and monitor miscibility in the field. Proposed mechanism: a handshake protocol combining EOS-tuned MMP prediction with targeted slim-tube validation, operating pressure set above measured MMP with margin, and field monitoring (gas-oil ratio trends) for miscibility confirmation. Confirm: margin-operated floods achieve designed recoveries. Kill: heterogeneity defeats the 1D MMP concept entirely. Does NOT claim: exact MMP prediction - it verifies the handshake where affordable.",
 "pointer": "The Signature system's proposed approach validates CO2 miscibility with margin and field monitoring; the companion Signature Edition record specifies the handshake protocol.",
 "key_points": [
  "Miscible CO2 needs MMP below reservoir pressure.",
  "Slim tubes are 1D, slow, expensive; reservoirs are 3D and heterogeneous.",
  "MMP correlations are crude-specific and often wrong.",
  "Near-miscible operation is the economic reality and least predictable regime.",
 ],
 "requirements": [
  "EOS-tuned MMP with targeted experimental validation.",
  "Operating pressure above measured MMP with margin.",
  "Field miscibility monitoring via production trends.",
 ],
 "citations": [
  "Yellig WF, Metcalfe RS (1980) Determination and prediction of CO2 minimum miscibility pressures. JPT 32(1).",
 ],
 "demo": {"k": 0.25, "area": 56.0, "dp": 410.0, "mu": 0.9, "L": 72.0},
},
# ----------------------------------------------------------------- rank 21
{
 "key": "pe-sagd",
 "name": "The Steam Assisted Gravity Drainage Optimization Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "SAGD made bitumen producible with paired horizontal wells and steam - but the steam-oil ratio decides the economics, so how low can it go?",
 "background": "Butler's SAGD (1980s) - steam injected above, oil drained below by gravity - unlocked Canada's oil sands, but the steam-oil ratio (SOR, typically 2-4) is the economic and carbon crux: each barrel of oil needs barrels of steam, made by burning gas. SOR depends on reservoir quality, well placement, operating pressure, and conformance; solvent co-injection (ES-SAGD) promises lower SOR but adds cost and complexity. The optimization - rate, pressure, solvent, well spacing - is high-dimensional and reservoir-specific. The carbon intensity of high-SOR operations is the existential threat as carbon prices rise.",
 "why_it_matters": "SAGD produces over a million barrels daily. The SOR is its economics and its carbon footprint - the two numbers that decide its future.",
 "sig_lens": "The Signature lens reads SAGD as a steam budget: the protocol must account for every barrel of steam and spend it only where it melts oil.",
 "sig_solution": LABEL + " Assumptions: (1) SOR is the economic and carbon crux; (2) optimization is high-dimensional and reservoir-specific. Reasoning path: optimize the steam budget per well pair - allocate steam where conformance shows it melts oil, starve where it does not. Proposed mechanism: a steam-budget protocol with per-pair SOR tracking, conformance monitoring (temperature observation wells), and rate/pressure/solvent optimization on the measured response. Confirm: budget-optimized pairs beat uniform operations on SOR. Kill: conformance proves unmeasurable and the budget misallocates. Does NOT claim: a universal SAGD optimum - it spends the steam where measured.",
 "pointer": "The Signature system's proposed approach optimizes SAGD steam allocation per well pair on conformance; the companion Signature Edition record specifies the steam-budget protocol.",
 "key_points": [
  "SAGD unlocked bitumen with paired horizontal wells and gravity drainage.",
  "SOR of 2-4 is the economic and carbon crux.",
  "Solvent co-injection promises lower SOR at higher complexity.",
  "Carbon intensity threatens high-SOR operations.",
 ],
 "requirements": [
  "Per-well-pair SOR tracking.",
  "Conformance monitoring via observation wells.",
  "Rate, pressure, and solvent optimization on measured response.",
 ],
 "citations": [
  "Butler RM (1994) Horizontal Wells for the Recovery of Oil, Gas and Bitumen. Gulf Publishing.",
 ],
 "demo": {"k": 0.3, "area": 70.0, "dp": 200.0, "mu": 0.8, "L": 60.0},
},
# ----------------------------------------------------------------- rank 22
{
 "key": "pe-polymer",
 "name": "The Polymer Flooding Degradation Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Polymers thicken injection water to even the flood front - but they shear-degrade, adsorb, and thermally break down, so how much viscosity actually survives to the reservoir?",
 "background": "Polymer flooding (partially hydrolyzed polyacrylamide) improves mobility ratio and sweep; Daqing's massive polymer floods proved the concept at scale. But the polymer that reaches the reservoir is not the polymer injected: mechanical degradation at chokes and perforations shears chains, adsorption strips polymer onto rock, and high temperature and salinity break it down. The in-situ viscosity - the number that matters - is inferred, not measured, and the degradation models are approximate. Associative polymers and HPAM-surfactant blends promise more but complicate the chemistry. The design question - what to inject to get what downhole - is answered by rules with wide bands.",
 "why_it_matters": "Polymer is the injected chemical bill: degraded polymer is money pumped into broken chains. The in-situ viscosity gap is the design's blind spot.",
 "sig_lens": "The Signature lens reads polymer as a chain that frays in transit: the protocol must measure what arrives, not assume what was sent.",
 "sig_solution": LABEL + " Assumptions: (1) injected viscosity is not in-situ viscosity; (2) degradation models are approximate. Reasoning path: measure the surviving viscosity - sample produced and observation-well fluids - and design injection to the measured survival. Proposed mechanism: a fraying protocol with in-situ viscosity inference from produced fluids, degradation-aware injection design (oversizing for measured losses), and polymer selection qualified on survival, not just lab viscosity. Confirm: survival-designed floods show better mobility control. Kill: in-situ measurement proves impractical and design stays blind. Does NOT claim: exact degradation prediction - it measures what arrives.",
 "pointer": "The Signature system's proposed approach designs polymer floods on measured in-situ viscosity survival; the companion Signature Edition record specifies the fraying protocol.",
 "key_points": [
  "Polymers improve mobility ratio; Daqing proved scale.",
  "Shear, adsorption, and thermal breakdown degrade injected polymer.",
  "In-situ viscosity is inferred, not measured.",
  "Design rules for what-to-inject carry wide bands.",
 ],
 "requirements": [
  "In-situ viscosity inference from produced fluids.",
  "Degradation-aware injection design.",
  "Polymer qualification on survival, not lab viscosity.",
 ],
 "citations": [
  "Sorbie KS (1991) Polymer-Improved Oil Recovery. Springer.",
 ],
 "demo": {"k": 0.22, "area": 52.0, "dp": 260.0, "mu": 1.2, "L": 80.0},
},
# ----------------------------------------------------------------- rank 23
{
 "key": "pe-produced-water",
 "name": "The Produced Water Treatment Problem",
 "group": "Production Engineering",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Oilfields produce far more water than oil - but how can the billions of barrels be treated for reuse or disposal when the contaminants keep changing?",
 "background": "Produced water - often 5-10 barrels per barrel of oil - carries oil droplets, dissolved organics, scaling ions, NORM (naturally occurring radioactive material), and now fracking chemicals: the most voluminous waste stream in the industry. Disposal by deep-well injection is cheap where geology allows and seismically fraught where it does not; beneficial reuse (irrigation, industrial) needs treatment trains whose design depends on the specific contaminant mix. The water chemistry evolves over field life, defeating fixed treatment designs. Desalination for reuse is energy-intensive; the economics rarely close without regulatory pressure.",
 "why_it_matters": "Produced water is the industry's largest waste stream and its largest water-management challenge. Mismanaged, it contaminates; well-managed, it could irrigate.",
 "sig_lens": "The Signature lens reads produced water as a changing recipe: the protocol must assay each batch and cook the treatment to match.",
 "sig_solution": LABEL + " Assumptions: (1) water chemistry evolves over field life; (2) fixed treatment trains go obsolete. Reasoning path: characterize continuously and treat modularly - assay the water, then assemble the treatment train from unit operations matched to the assay. Proposed mechanism: a recipe protocol with continuous water-chemistry assay, modular treatment trains reconfigured to the assay, and disposal-versus-reuse economics recomputed as chemistry and regulations evolve. Confirm: assay-matched treatment meets specs at lower cost than fixed trains. Kill: the chemistry shifts faster than modules can reconfigure. Does NOT claim: a universal produced-water solution - it cooks to the assay.",
 "pointer": "The Signature system's proposed approach treats produced water with assay-matched modular trains; the companion Signature Edition record specifies the recipe protocol.",
 "key_points": [
  "Produced water volumes dwarf oil volumes (5-10x).",
  "Contaminants span oil, organics, scale ions, NORM, and frack chemicals.",
  "Deep-well disposal is cheap but seismically fraught.",
  "Chemistry evolves over field life, defeating fixed designs.",
 ],
 "requirements": [
  "Continuous produced-water chemistry assay.",
  "Modular treatment trains reconfigured to the assay.",
  "Recomputed disposal-versus-reuse economics.",
 ],
 "citations": [
  "Fakhru'l-Razi A et al. (2009) Review of technologies for oil and gas produced water treatment. J. Hazardous Materials 170(2-3).",
 ],
 "demo": {"k": 0.18, "area": 46.0, "dp": 300.0, "mu": 1.6, "L": 90.0},
},
# ----------------------------------------------------------------- rank 24
{
 "key": "pe-in-situ-combustion",
 "name": "The In Situ Combustion Control Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Burning part of the oil in place to mobilize the rest is thermodynamically brilliant - but how can the combustion front be controlled when it keeps dying or running away?",
 "background": "In situ combustion (fire flooding) ignites the reservoir and drives a burning front that heats and displaces oil: the most energy-efficient thermal method in principle. In practice the front is unstable - it extinguishes (oxygen bypassing, heat losses) or channels, and the produced gases (CO, H2S) are hazardous. Decades of pilots show spectacular successes and failures with no reliable predictor: the Belridge, Suplacu de Barcau, and Balol experiences each taught different lessons. The kinetics (coke formation and burning) couple to heterogeneity in ways models capture poorly. ISC remains the thermal method that works brilliantly except when it does not.",
 "why_it_matters": "ISC could recover heavy oil with minimal surface footprint. Its unreliability is the reason the industry chose steam instead - at far higher energy cost.",
 "sig_lens": "The Signature lens reads the fire front as a beast to be ridden: the protocol must watch its vital signs and steer with air, not hope.",
 "sig_solution": LABEL + " Assumptions: (1) front stability is the crux and is poorly predicted; (2) pilots give contradictory lessons. Reasoning path: control the front actively - monitor its position and temperature, and modulate air injection to keep it in the stable window. Proposed mechanism: a fire-riding protocol with front tracking (temperature observation, gas analysis), air-rate control laws keeping the front in its stable regime, and automatic shutdown triggers on instability signatures. Confirm: actively controlled pilots sustain fronts longer. Kill: the instability proves faster than any control loop. Does NOT claim: reliable ISC - it rides the front with instruments.",
 "pointer": "The Signature system's proposed approach controls ISC fronts actively with air-rate modulation; the companion Signature Edition record specifies the fire-riding protocol.",
 "key_points": [
  "ISC is the most energy-efficient thermal method in principle.",
  "Fronts extinguish or channel unpredictably.",
  "Pilot history shows spectacular successes and failures without reliable predictors.",
  "Produced gases (CO, H2S) add hazard to instability.",
 ],
 "requirements": [
  "Combustion-front tracking via temperature and gas analysis.",
  "Air-rate control laws for front stability.",
  "Automatic shutdown triggers on instability signatures.",
 ],
 "citations": [
  "Sarathi PS (1999) In-Situ Combustion Handbook. US DOE.",
 ],
 "demo": {"k": 0.2, "area": 40.0, "dp": 480.0, "mu": 2.0, "L": 100.0},
},
# ----------------------------------------------------------------- rank 25
{
 "key": "pe-surfactant-cost",
 "name": "The Surfactant EOR Cost Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Surfactants can wash out nearly all residual oil - but they cost more than the oil they recover, so where is the economic frontier of chemical flooding?",
 "background": "Surfactant flooding reduces interfacial tension to near zero, mobilizing trapped oil ganglia: microscopically the most efficient EOR method. But surfactants adsorb onto rock, degrade, chromatographically separate from co-injected polymer, and cost dollars per barrel of chemical for cents of incremental oil at low prices. The formulation science (microemulsion phase behavior, Huh's correlation) is mature; the economics are not. Low-salinity and surfactant-polymer (SP/ASP) variants improve the odds, but every chemical flood is a bet that the chemical bill stays below the oil value - a bet the industry has often lost.",
 "why_it_matters": "Chemical EOR is the microscopically perfect method with an economic disease. The cost frontier decides whether it stays in the lab or works in the field.",
 "sig_lens": "The Signature lens reads surfactant as soap bought by the barrel: the protocol must prove the wash pays before buying the soap.",
 "sig_solution": LABEL + " Assumptions: (1) the chemistry works; the economics usually do not; (2) adsorption and separation eat the chemical budget. Reasoning path: design to the economic frontier - minimize chemical cost per incremental barrel via formulation optimization against the specific crude and rock. Proposed mechanism: a soap-budget protocol optimizing formulations for cost-per-barrel (not just recovery), with adsorption measured on the actual rock and pilots gated on the chemical economics. Confirm: budget-optimized formulations clear economic hurdles more often. Kill: adsorption proves irreducible and the budget never closes. Does NOT claim: cheap chemical EOR - it proves the wash pays per case.",
 "pointer": "The Signature system's proposed approach optimizes surfactant formulations for cost per incremental barrel; the companion Signature Edition record specifies the soap-budget protocol.",
 "key_points": [
  "Surfactants mobilize trapped oil at near-zero interfacial tension.",
  "Adsorption, degradation, and chromatographic separation eat the chemical budget.",
  "Formulation science is mature; the economics are not.",
  "Chemical floods often lose the bet of chemical cost versus oil value.",
 ],
 "requirements": [
  "Formulation optimization for cost per incremental barrel.",
  "Adsorption measurement on the actual reservoir rock.",
  "Pilots gated on chemical economics, not just recovery.",
 ],
 "citations": [
  "Sheng JJ (2010) Modern Chemical Enhanced Oil Recovery. Gulf Professional.",
 ],
 "demo": {"k": 0.16, "area": 44.0, "dp": 370.0, "mu": 1.4, "L": 85.0},
},
# ----------------------------------------------------------------- rank 26
{
 "key": "pe-meor",
 "name": "The Microbial EOR Mechanisms Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Microbes can make biosurfactants, gases, and acids downhole - but do they actually recover oil in the field, and by which mechanism?",
 "background": "Microbial EOR (MEOR) - injecting nutrients to stimulate indigenous microbes, or injecting microbes directly - promises cheap EOR from biology: biosurfactants, biopolymers, gas pressurization, and selective plugging are all claimed mechanisms. Field trials report successes, but the mechanism attribution is weak: was it the microbes, or the waterflood that carried them? The subsurface microbiology is a black box - which species, doing what, where - and the trials lack the controls to isolate mechanisms. MEOR sits between promising science and unproven technology, with enthusiastic pilots and thin evidence.",
 "why_it_matters": "MEOR promises the cheapest EOR ever - biology does the chemistry. But unproven mechanisms mean unproven economics, and the field cannot tell which it is buying.",
 "sig_lens": "The Signature lens reads MEOR as hiring invisible workers: the protocol must verify the workers exist, what they do, and that the work is theirs.",
 "sig_solution": LABEL + " Assumptions: (1) mechanism attribution in MEOR trials is weak; (2) subsurface microbiology is largely uncharacterized. Reasoning path: prove the mechanism before scaling - run controlled trials with microbial monitoring that isolate the biological effect. Proposed mechanism: a workforce protocol requiring baseline microbiome characterization, controlled pilots (nutrient versus microbe versus waterflood-only), and mechanism-specific measurements (biosurfactant assay, gas composition) before any scale-up claim. Confirm: mechanism-proven MEOR shows repeatable incremental recovery. Kill: no mechanism isolates and the effects prove to be waterflood artifacts. Does NOT claim: working MEOR - it verifies the workers before paying them.",
 "pointer": "The Signature system's proposed approach proves MEOR mechanisms with controlled, monitored pilots; the companion Signature Edition record specifies the workforce protocol.",
 "key_points": [
  "Claimed MEOR mechanisms: biosurfactants, biopolymers, gas, selective plugging.",
  "Field successes lack mechanism attribution and controls.",
  "Subsurface microbiology during MEOR is a black box.",
  "MEOR sits between promising science and unproven technology.",
 ],
 "requirements": [
  "Baseline subsurface microbiome characterization.",
  "Controlled pilots isolating the biological effect.",
  "Mechanism-specific measurements before scale-up claims.",
 ],
 "citations": [
  "Lazar I et al. (2007) The role of microorganisms in enhanced oil recovery. Advances in Applied Microbiology 62.",
 ],
 "demo": {"k": 0.19, "area": 48.0, "dp": 320.0, "mu": 1.8, "L": 92.0},
},
# ----------------------------------------------------------------- rank 27
{
 "key": "pe-flow-assurance",
 "name": "The Integrated Flow Assurance Problem",
 "group": "Production Engineering",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Wax, scale, hydrates, asphaltenes, and corrosion threaten flowlines simultaneously - but how can the integrated risk be managed when each threat is modeled separately?",
 "background": "Flow assurance - keeping hydrocarbons flowing from reservoir to facility - fights five enemies at once: wax deposition, mineral scale, gas hydrates, asphaltenes, and corrosion. Each has its models and chemicals; the integration does not exist: the wax inhibitor affects the hydrate program, the corrosion inhibitor films compete with scale inhibitors, and the operating envelope satisfying all five constraints simultaneously is found by experience. Deepwater and long tiebacks tighten every constraint at once. The industry manages flow assurance by committees of specialists; the integrated optimization - the cheapest reliable operating strategy across all threats - is unsolved.",
 "why_it_matters": "A blocked deepwater flowline is a billion-dollar asset producing nothing. The integrated threat is what actually plugs lines; the separate models miss it.",
 "sig_lens": "The Signature lens reads flow assurance as defending a castle against five armies: the protocol must coordinate the defense, not let each wall fight alone.",
 "sig_solution": LABEL + " Assumptions: (1) threats interact chemically and operationally; (2) specialist silos miss the interactions. Reasoning path: manage the integrated envelope - model the threats jointly, find operating windows satisfying all constraints, and monitor all five continuously. Proposed mechanism: a castle protocol with an integrated threat model (coupled deposition and corrosion), a computed safe operating envelope across all threats, and chemical programs designed jointly for compatibility. Confirm: integrated management shows fewer flowline events at lower chemical cost. Kill: the coupling proves unmodelable and the envelope is fiction. Does NOT claim: a solved integrated model - it coordinates the defense explicitly.",
 "pointer": "The Signature system's proposed approach manages flow assurance through an integrated threat envelope; the companion Signature Edition record specifies the castle protocol.",
 "key_points": [
  "Five simultaneous threats: wax, scale, hydrates, asphaltenes, corrosion.",
  "Inhibitor chemistries interact and compete.",
  "No integrated optimization across threats exists.",
  "Deepwater and long tiebacks tighten all constraints at once.",
 ],
 "requirements": [
  "Coupled multi-threat deposition and corrosion modeling.",
  "Computed safe operating envelopes across all threats.",
  "Jointly designed compatible chemical programs.",
 ],
 "citations": [
  "Kaczmarski AA, Lorimer SE (2001) Emergence of flow assurance as a technical discipline. OTC 13123.",
 ],
 "demo": {"k": 0.15, "area": 42.0, "dp": 440.0, "mu": 2.2, "L": 115.0},
},
# ----------------------------------------------------------------- rank 28
{
 "key": "pe-subsea",
 "name": "The Subsea Processing Reliability Problem",
 "group": "Production Engineering",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Separating oil, gas, and water on the seabed avoids costly platforms - but can subsea processing equipment be reliable enough when intervention costs tens of millions?",
 "background": "Subsea processing - separation, boosting, and compression on the seabed - extends tiebacks and revives marginal fields (Tordis, Marlim, Åsgard proved the concepts). But reliability is the wall: a failed subsea pump needs a vessel, weather window, and weeks - tens of millions per intervention. The equipment (multiphase pumps, subsea separators) operates in an uninspectable environment with limited redundancy, and the reliability data is thin because so few systems operate. The design philosophy - reliability by overengineering versus retrievability by modularity - is unresolved, and each operator chooses differently.",
 "why_it_matters": "Subsea processing unlocks stranded reserves worth billions. But one unrecoverable failure can erase the economics - reliability is the business case.",
 "sig_lens": "The Signature lens reads subsea equipment as unmanned outposts: the protocol must make them either unbreakable or retrievable, and never neither.",
 "sig_solution": LABEL + " Assumptions: (1) intervention costs tens of millions; (2) reliability data is thin. Reasoning path: design for the intervention economics - either prove extreme reliability or make retrieval cheap, and choose explicitly. Proposed mechanism: an outpost protocol requiring reliability demonstration (accelerated testing plus redundancy analysis) OR modular retrievability designed in, with the choice justified by intervention-cost modeling. Confirm: protocol-designed systems show better lifetime economics. Kill: neither reliability nor retrievability proves achievable at acceptable cost. Does NOT claim: proven subsea reliability - it forces the explicit choice.",
 "pointer": "The Signature system's proposed approach forces explicit reliability-versus-retrievability design choices; the companion Signature Edition record specifies the outpost protocol.",
 "key_points": [
  "Subsea processing extends tiebacks and revives marginal fields.",
  "Interventions cost tens of millions and need weather windows.",
  "Equipment operates uninspectable with limited redundancy.",
  "Reliability-by-design versus retrievability is unresolved.",
 ],
 "requirements": [
  "Reliability demonstration or designed modular retrievability.",
  "Intervention-cost modeling justifying the choice.",
  "Redundancy analysis for unretrievable components.",
 ],
 "citations": [
  "Maitland G (2000) Subsea processing: the future. JPT 52(12).",
 ],
 "demo": {"k": 0.13, "area": 38.0, "dp": 520.0, "mu": 2.5, "L": 125.0},
},
# ----------------------------------------------------------------- rank 29
{
 "key": "pe-decommissioning",
 "name": "The Offshore Decommissioning Problem",
 "group": "Production Engineering",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Thousands of offshore platforms must be removed - but how can it be done safely, cheaply, and without ecological harm when each structure is unique?",
 "background": "The North Sea, Gulf of Mexico, and other basins face a decommissioning wave: thousands of platforms at end of life, each a unique structure with unknown structural integrity, residual hydrocarbons, and marine growth ecosystems. Removal options (complete removal, partial, reefing) trade cost against ecological impact; the engineering (heavy lift, cutting, well plugging) is bespoke per platform. Cost estimates routinely double; the UK's decommissioning bill is estimated in tens of billions of pounds. Well plugging and abandonment - the largest cost - has uncertain long-term integrity. The industry is learning on the job at continental scale.",
 "why_it_matters": "Offshore decommissioning is a multi-hundred-billion-dollar global liability. Done badly it pollutes; done expensively it bankrupts; it must be done regardless.",
 "sig_lens": "The Signature lens reads decommissioning as demolishing a city at sea: the protocol must inventory every hazard before the first cut, and price the surprises.",
 "sig_solution": LABEL + " Assumptions: (1) each platform is structurally unique; (2) cost estimates routinely double. Reasoning path: de-risk by characterization - survey structure, wells, and contamination thoroughly before committing to the removal method. Proposed mechanism: a demolition protocol requiring pre-removal characterization (structural, well integrity, contamination), method selection on the characterized inventory, and contingency funding sized to the characterization uncertainty. Confirm: characterized projects overrun less than uncharacterized ones. Kill: characterization proves unable to reveal the critical unknowns. Does NOT claim: cheap decommissioning - it prices the surprises in advance.",
 "pointer": "The Signature system's proposed approach characterizes platforms fully before removal-method selection; the companion Signature Edition record specifies the demolition protocol.",
 "key_points": [
  "Thousands of platforms face end-of-life removal globally.",
  "Each structure is unique with unknown integrity and contamination.",
  "Cost estimates routinely double; the UK bill is tens of billions.",
  "Well plugging integrity is the largest cost and longest risk.",
 ],
 "requirements": [
  "Pre-removal structural, well, and contamination characterization.",
  "Removal-method selection on the characterized inventory.",
  "Contingency funding sized to characterization uncertainty.",
 ],
 "citations": [
  "OECD (2019) Decommissioning of offshore oil and gas installations.",
 ],
 "demo": {"k": 0.11, "area": 34.0, "dp": 480.0, "mu": 2.9, "L": 135.0},
},
# ----------------------------------------------------------------- rank 30
{
 "key": "pe-methane",
 "name": "The Methane Leak Detection Problem",
 "group": "Production Engineering",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Methane leaks erase the climate advantage of gas - but how can leaks be detected and quantified across vast infrastructure when the big emitters are intermittent?",
 "background": "Methane's warming potency (80x CO2 over 20 years) makes leaks the industry's climate crux: studies (Alvarez et al., 2018) put US oil and gas methane emissions at 2.3 percent of production - enough to imperil the gas-over-coal climate benefit. The measurement problem is severe: top-down (satellite, aircraft) and bottom-up (component counts) disagree, super-emitters are intermittent and fat-tailed, and continuous monitors are expensive. New satellites (MethaneSAT) promise facility-level quantification, but attribution to operators and the intermittent-emitter problem remain. Regulations tighten while the measurement science catches up.",
 "why_it_matters": "At 2-3 percent leakage, natural gas loses its climate advantage over coal. The industry's license to operate as a transition fuel hangs on a measurement it cannot yet make reliably.",
 "sig_lens": "The Signature lens reads methane as an invisible tax: the protocol must meter it continuously and charge it to the emitter, or the climate pays.",
 "sig_solution": LABEL + " Assumptions: (1) top-down and bottom-up measurements disagree; (2) super-emitters are intermittent and fat-tailed. Reasoning path: reconcile the scales - combine continuous site monitoring with periodic aerial/satellite surveys, and attribute rigorously. Proposed mechanism: a metering protocol requiring continuous monitoring at facilities, periodic independent surveys, reconciliation of the two scales, and repair mandates on detected super-emitters with deadlines. Confirm: metered-and-repaired sites show lower verified emissions. Kill: attribution proves impossible and the metering is decorative. Does NOT claim: exact methane accounting - it meters continuously and reconciles the scales.",
 "pointer": "The Signature system's proposed approach combines continuous and survey methane monitoring with reconciliation; the companion Signature Edition record specifies the metering protocol.",
 "key_points": [
  "Methane is ~80x CO2 over 20 years; 2.3 percent US leakage is estimated.",
  "Top-down and bottom-up measurements disagree substantially.",
  "Super-emitters are intermittent and fat-tailed.",
  "Satellites promise facility quantification; attribution remains hard.",
 ],
 "requirements": [
  "Continuous facility-level methane monitoring.",
  "Periodic independent aerial/satellite surveys.",
  "Top-down/bottom-up reconciliation with repair mandates.",
 ],
 "citations": [
  "Alvarez RA et al. (2018) Assessment of methane emissions from the US oil and gas supply chain. Science 361(6398).",
 ],
 "demo": {"k": 0.17, "area": 50.0, "dp": 350.0, "mu": 1.7, "L": 95.0},
},
# ----------------------------------------------------------------- rank 31
{
 "key": "pe-flaring",
 "name": "The Flaring Reduction Problem",
 "group": "Production Engineering",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Associated gas is flared for lack of infrastructure - but how can flaring be eliminated when the gas is stranded, intermittent, and uneconomic to gather?",
 "background": "Flaring burns associated gas at the wellhead: 140+ billion cubic meters yearly worldwide (World Bank), a waste and a major CO2 and methane source. The causes are economic, not technical: stranded gas with no pipeline, intermittent volumes, and gas prices below gathering cost. Solutions exist - mini-LNG, compressed gas, gas-to-power, reinjection - but each needs scale the stranded volumes lack. Satellite monitoring (VIIRS) now makes flaring visible globally, and the World Bank's Zero Routine Flaring initiative pushes elimination by 2030. The gap between visibility and elimination is economics.",
 "why_it_matters": "Flaring wastes energy and emits CO2 pointlessly. It is the industry's most visible environmental failure - literally visible from space.",
 "sig_lens": "The Signature lens reads flaring as burning money for lack of a wallet: the protocol must find the wallet (the economic use) or stop producing the money.",
 "sig_solution": LABEL + " Assumptions: (1) the causes are economic, not technical; (2) stranded volumes defeat scale solutions. Reasoning path: match the gas to the smallest economic use - modular solutions sized to the actual volumes, with the economics computed honestly. Proposed mechanism: a wallet protocol assessing each flare stream for modular utilization (mini-LNG, gas-to-power, reinjection), requiring flaring economics disclosure, and gating new developments on gas-utilization plans. Confirm: wallet-matched projects eliminate flaring economically. Kill: no modular use clears the economics and the gas stays stranded. Does NOT claim: universal flaring elimination - it finds the wallet per stream.",
 "pointer": "The Signature system's proposed approach matches flare streams to modular economic uses; the companion Signature Edition record specifies the wallet protocol.",
 "key_points": [
  "140+ bcm flared yearly worldwide; visible from space.",
  "Causes are economic: stranded, intermittent, sub-economic gas.",
  "Modular solutions (mini-LNG, gas-to-power) exist but need scale.",
  "Zero Routine Flaring by 2030 is the industry commitment.",
 ],
 "requirements": [
  "Per-stream modular utilization assessments.",
  "Flaring economics disclosure.",
  "Gas-utilization plans gating new developments.",
 ],
 "citations": [
  "World Bank Global Gas Flaring Reduction Partnership data.",
 ],
 "demo": {"k": 0.21, "area": 54.0, "dp": 300.0, "mu": 1.5, "L": 88.0},
},
# ----------------------------------------------------------------- rank 32
{
 "key": "pe-ccs-depleted",
 "name": "The Carbon Capture and Storage in Depleted Reservoirs Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Depleted oil and gas reservoirs could store CO2 - but will the CO2 stay put for millennia, and can storage be verified without watching every molecule?",
 "background": "Depleted reservoirs offer proven traps, existing wells, and characterization data for CO2 storage - the CCS industry's most accessible sink. But the questions are long-term: caprock integrity under CO2-brine-rock reactions, wellbore leakage through legacy wells (thousands of old penetrations), and induced seismicity from pressure. Monitoring (4D seismic, pressure, tracers) verifies conformance, but millennial containment must be argued, not observed. The Sleipner and Quest projects demonstrate storage works; the scale-up to gigatons needs hundreds of Sleipners, each with its own integrity case. The business model - who pays for millennial stewardship - is as unsolved as the geology.",
 "why_it_matters": "CCS at gigaton scale needs sinks; depleted reservoirs are the nearest. Unverifiable containment is unbankable storage - and the climate needs bankable tons.",
 "sig_lens": "The Signature lens reads storage as a vault for millennia: the protocol must prove the vault's integrity continuously and fund its guardianship permanently.",
 "sig_solution": LABEL + " Assumptions: (1) millennial containment must be argued, not observed; (2) legacy wells are the likely leak paths. Reasoning path: build the integrity case in layers - caprock, wells, monitoring - and fund the stewardship permanently. Proposed mechanism: a vault protocol requiring per-site integrity assessment (caprock geochemistry, legacy-well audit), monitoring matched to the risk profile, and long-term stewardship funding secured before injection. Confirm: vault-assessed sites show conformance in monitoring. Kill: a legacy well leaks and the integrity case collapses. Does NOT claim: proven millennial containment - it layers the argument and funds the watch.",
 "pointer": "The Signature system's proposed approach layers CO2 storage integrity cases with funded stewardship; the companion Signature Edition record specifies the vault protocol.",
 "key_points": [
  "Depleted reservoirs offer proven traps and characterization data.",
  "Caprock reactions, legacy wells, and seismicity are the integrity risks.",
  "Millennial containment must be argued, not observed.",
  "Sleipner and Quest prove storage; gigaton scale needs hundreds more.",
 ],
 "requirements": [
  "Per-site integrity assessment: caprock, wells, seismicity.",
  "Risk-matched monitoring programs.",
  "Funded long-term stewardship before injection.",
 ],
 "citations": [
  "IPCC (2005) Special Report on Carbon Dioxide Capture and Storage.",
 ],
 "demo": {"k": 0.24, "area": 60.0, "dp": 280.0, "mu": 1.1, "L": 75.0},
},
# ----------------------------------------------------------------- rank 33
{
 "key": "pe-geothermal",
 "name": "The Geothermal Co-production Problem",
 "group": "Reservoir Engineering",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Oil wells produce vast hot water - but can the heat be harvested economically, and does co-production pay when the temperatures are marginal?",
 "background": "Produced water is hot: many oilfields produce water at 80-150 C, a geothermal resource already lifted to surface. Co-production - generating power from the heat - has been piloted (Rocky Mountain Oilfield Testing Center, Huabei field in China), but the economics are marginal: low temperatures mean low conversion efficiency (binary ORC plants), the water chemistry fouls heat exchangers, and the power must compete with grid prices. The resource is enormous in aggregate and uneconomic well-by-well - the classic distributed-resource problem. Enhanced co-production (stimulating hotter zones) blurs into EGS with its own risks.",
 "why_it_matters": "Hot produced water is energy already lifted: venting its heat is waste. Co-production could turn water disposal from cost to revenue - if the margin exists.",
 "sig_lens": "The Signature lens reads co-production as harvesting a byproduct: the protocol must prove the harvest pays per well, not in aggregate.",
 "sig_solution": LABEL + " Assumptions: (1) temperatures are marginal for power generation; (2) the resource is huge in aggregate, uneconomic per well. Reasoning path: screen ruthlessly per well - temperature, rate, chemistry, grid price - and build only where the margin clears. Proposed mechanism: a harvest protocol with per-well techno-economic screening, fouling-resistant heat exchanger designs qualified on the actual brine, and modular plants sized to the screened resource. Confirm: screened projects achieve designed paybacks. Kill: fouling defeats the exchangers and the margin evaporates. Does NOT claim: universal co-production economics - it harvests where the margin clears.",
 "pointer": "The Signature system's proposed approach screens geothermal co-production per well on techno-economics; the companion Signature Edition record specifies the harvest protocol.",
 "key_points": [
  "Produced water at 80-150 C is a lifted geothermal resource.",
  "Pilots exist (RMOTC, Huabei); economics remain marginal.",
  "Low temperatures mean low ORC efficiency; brines foul exchangers.",
  "The resource is enormous in aggregate, uneconomic well-by-well.",
 ],
 "requirements": [
  "Per-well techno-economic screening.",
  "Brine-qualified fouling-resistant heat exchangers.",
  "Modular plants sized to screened resources.",
 ],
 "citations": [
  "Tester JW et al. (2006) The Future of Geothermal Energy. MIT.",
 ],
 "demo": {"k": 0.26, "area": 58.0, "dp": 240.0, "mu": 1.0, "L": 70.0},
},
# ----------------------------------------------------------------- rank 34
{
 "key": "pe-unified-subsurface",
 "name": "The Unified Subsurface Resource Problem",
 "group": "Production Engineering",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "The same subsurface holds oil, gas, heat, storage space, and minerals - but can it be managed as one resource system instead of competing single-use claims?",
 "background": "Subsurface use is fragmented: oil operators, geothermal developers, CCS projects, and hydrogen storage compete for the same pore space with separate regulators and no coordination. The conflicts are physical (pressure interference, induced seismicity attribution) and institutional (who owns the pore space? who is liable for migrating CO2?). The Netherlands' Groningen earthquakes showed how uncoordinated extraction creates unassigned liability. Integrated subsurface management - co-optimizing extraction, storage, and heat - has pilot concepts but no working governance. The pore space is one system; the management is many fiefdoms.",
 "why_it_matters": "The energy transition needs the subsurface for everything at once: storage, heat, and remaining hydrocarbons. Uncoordinated claims will collide - physically and legally.",
 "sig_lens": "The Signature lens reads the subsurface as common ground: the protocol must give it one manager with a complete map, or accept the collisions.",
 "sig_solution": LABEL + " Assumptions: (1) pore-space uses conflict physically and legally; (2) no integrated governance exists. Reasoning path: build the shared subsurface model first - geology, pressures, and claims in one registry - then allocate uses against it. Proposed mechanism: a common-ground protocol with a unified subsurface registry (geology plus all claims), interference modeling for new projects against existing uses, and liability frameworks assigned before injection or extraction. Confirm: registry-governed basins show fewer use conflicts. Kill: jurisdictions refuse the registry and fiefdoms persist. Does NOT claim: optimal subsurface allocation - it maps the common ground and assigns the liability.",
 "pointer": "The Signature system's proposed approach governs the subsurface through a unified claims registry; the companion Signature Edition record specifies the common-ground protocol.",
 "key_points": [
  "Oil, geothermal, CCS, and hydrogen storage compete for pore space.",
  "Conflicts are physical (pressure, seismicity) and institutional (ownership, liability).",
  "Groningen showed uncoordinated extraction creates unassigned liability.",
  "No integrated subsurface governance exists.",
 ],
 "requirements": [
  "A unified subsurface registry of geology and claims.",
  "Interference modeling for proposed new uses.",
  "Liability frameworks assigned before operations begin.",
 ],
 "citations": [
  "Benson SM et al. (2005) Underground Geological Storage. IPCC SRCCS Chapter 5.",
 ],
 "demo": {"k": 0.22, "area": 52.0, "dp": 330.0, "mu": 1.3, "L": 80.0},
},
]
