#!/usr/bin/env python3
"""Entries for The Unsolved Nuclear Engineering Database
(unsolved-nuclear-engineering) and its Signature half
(unsolved-nuclear-engineering-signature).

34 famous unsolved problems in nuclear engineering, ladder-ordered by
accessibility (rank 1 = most approachable, rank 34 = most complex).
Public half: real, fact-checked problems. Signature half: the same 34
through the Signature lens, ALWAYS labeled as proposals, never established
science.

Scope: civilian nuclear engineering knowledge only - power reactors, fusion
energy, materials, safety, waste. No weapons-adjacent content.

ID prefixes JAH-USNE- / JAH-USNES- verified free in manifest id_prefix
values (exact + substring, both directions).
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

FIELD = {
 "tag": "nuclear-engineering",
 "disp": "nuclear engineering",
 "name": "The Unsolved Nuclear Engineering Database",
 "sig_name": "The Unsolved Nuclear Engineering Signature Database",
 "prefix": "JAH-USNE-",
 "sig_prefix": "JAH-USNES-",
 "ai": "JAH Unsolved Nuclear Engineering Archivist",
 "tagline": ("Thirty-four famous open problems in nuclear engineering, from vessel embrittlement to unified "
             "nuclear energy systems: real, fact-checked, each with its full story and a clearly labeled "
             "Signature proposed solution."),
 "sig_tagline": ("His original Signature solution method applied to all 34 great open problems of nuclear "
                 "engineering: Signature-generated proposed solutions with assumptions declared, confirm and "
                 "refute conditions stated, and limits honestly marked. Clearly labeled Signature-made, "
                 "never established science."),
 "pub_line": ("Public records - 34 famous open problems in nuclear engineering, real and fact-checked: reactor "
              "vessel embrittlement, departure from nucleate boiling, two-phase flow, stress corrosion cracking, "
              "CRUD-induced power shift, small modular reactor economics, load following, cogeneration, "
              "decommissioning costs, fuel supply, and accident-tolerant fuel - every record carrying the problem "
              "statement, background, why it matters, key points, requirements, standards, citations, and a "
              "working solution-explorer demonstration, organized in the Signature system."),
 "sig_line": ("Signature originals - his original Signature solution method: the same 34 famous unsolved "
              "nuclear engineering problems approached as a covenant between the known and the unknown, each "
              "carrying the full Signature-generated proposed solution with its assumptions declared, its "
              "confirm and refute conditions stated, and its limits honestly marked. Clearly labeled "
              "Signature-made, never presented as established science or authentic public record."),
 "ladder_text": (" Records are ordered by the teaching ladder: Foundations (vessel embrittlement, nucleate "
                 "boiling departure, two-phase flow, stress corrosion cracking, CRUD power shift, SMR economics, "
                 "load following, cogeneration, decommissioning costs, fuel supply, accident-tolerant fuel) -> "
                 "Compounded (severe accident source term, hydrogen risk, corium coolability, filtered venting, "
                 "risk assessment completeness, human reliability, digital control assurance, molten salt "
                 "corrosion, TRISO fuel, fast reactor cladding, tritium breeding, first wall materials) -> "
                 "Advanced (tokamak disruptions, stellarator optimization, inertial confinement gain, waste "
                 "transmutation, geological repositories, microreactor control, space reactor heat rejection, "
                 "multiphysics coupling, neutron transport, dry cask storage, unified nuclear energy systems)."),
 "search_ph": ("Search embrittlement, nucleate boiling, SMR, fusion, tritium, molten salt, TRISO, decommissioning, "
               "corium, tokamak, microreactor..."),
 "chat_ph": "Ask about the great open problems of nuclear engineering...",
 "greet_pub": ("I am the JAH Unsolved Nuclear Engineering Archivist. Ask me about the great open problems of "
               "nuclear engineering - from vessel embrittlement and thermal hydraulics through SMRs, molten salt, "
               "and fusion materials, to waste transmutation and unified nuclear energy systems."),
 "greet_sig": ("I am the JAH Unsolved Nuclear Engineering Archivist (Signature). Ask me about the Signature "
               "proposed solutions to the great open problems of nuclear engineering - every approach labeled "
               "as a proposal, never established science."),
 "role_pub": ("unsolved nuclear engineering archivist - the great open problems of nuclear engineering, from "
              "vessel embrittlement and thermal hydraulics through SMRs, molten salt, and fusion materials, to "
              "waste transmutation and unified nuclear energy systems; teaches progressively along the ladder "
              "from foundations through compounded to advanced; answers from many angles - definition, example, "
              "analogy, application, history, math - using only archive data from this system"),
 "role_sig": ("unsolved nuclear engineering archivist - Signature editions: his original Signature solution "
              "method applied to the 34 great open problems of nuclear engineering, each carrying the full "
              "Signature-generated proposed solution, clearly labeled Signature-made and never presented as "
              "established science; teaches progressively along the ladder from foundations through compounded "
              "to advanced; answers from many angles - definition, example, analogy, application, history, math "
              "- using only archive data from this system"),
 "gen_desc": "Generate clearly-labeled unsolved nuclear engineering studies. Seeded archive records are the authoritative entries.",
 "standards": [
  "Problem statements verified against the published literature; open status confirmed as of 2026.",
  "Quantitative claims cross-checked against standard references (Lamarsh and Baratta, Introduction to Nuclear Engineering; Todreas and Kazimi, Nuclear Systems).",
  "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
 ],
 "sig_tail": ("Signature editions carry the Signature system's proposed solution approaches to famous "
              "unsolved problems. Every solution is labeled a Signature-generated proposal, never "
              "established science, never peer-accepted, never proof."),
}

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "ne-embrittlement",
 "name": "The Reactor Pressure Vessel Embrittlement Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Neutron bombardment embrittles reactor pressure vessels over decades - but can the embrittlement be predicted accurately enough to justify operating plants for 60 to 80 years?",
 "background": "The reactor pressure vessel is the one component that cannot be replaced: fast neutrons displace atoms in the steel, raising its ductile-to-brittle transition temperature over time. The US NRC's embrittlement trend curves (Regulatory Guide 1.99) and the ASTM E900 correlation predict the shift from copper, nickel, and fluence - but the predictions carry large uncertainties, and surveillance capsules (metal samples irradiated inside the vessel) provide only sparse validation. Annealing can partially recover toughness but is rarely done. License extensions to 80 years hinge on embrittlement margins that the correlations estimate with 1970s-era statistics.",
 "why_it_matters": "Vessel integrity is the ultimate safety barrier: a brittle vessel under pressurized thermal shock is the accident nobody can mitigate. Life-extension decisions worth billions rest on embrittlement predictions.",
 "sig_lens": "The Signature lens reads embrittlement as aging with a meter: the protocol must track the vessel's toughness account continuously and never let the balance go unmeasured.",
 "sig_solution": LABEL + " Assumptions: (1) trend-curve correlations carry large, old uncertainties; (2) surveillance data is sparse but real. Reasoning path: fuse the correlations with surveillance measurements in a Bayesian update, and report the toughness margin as a distribution, not a point. Proposed mechanism: a toughness-ledger protocol that updates embrittlement predictions with each surveillance capsule result, tracks the margin to the screening criterion probabilistically, and flags vessels whose margin distribution dips below the safety threshold. Confirm: ledger-updated predictions match later capsule measurements better than static correlations. Kill: capsule data proves too sparse to move the correlations. Does NOT claim: exact embrittlement prediction - it keeps honest books on the aging.",
 "pointer": "The Signature system's proposed approach fuses embrittlement correlations with surveillance data in a Bayesian toughness ledger; the companion Signature Edition record specifies the ledger protocol.",
 "key_points": [
  "Neutron embrittlement raises the ductile-to-brittle transition temperature over decades.",
  "NRC trend curves and ASTM correlations carry large, dated uncertainties.",
  "Surveillance capsules give sparse but real validation data.",
  "80-year license extensions hinge on these embrittlement margins.",
 ],
 "requirements": [
  "Bayesian fusion of trend correlations with surveillance measurements.",
  "Probabilistic toughness margins, not point estimates.",
  "Threshold flags on margin distributions, not just means.",
 ],
 "citations": [
  "US NRC Regulatory Guide 1.99, Revision 2: Radiation Embrittlement of Reactor Vessel Materials.",
  "ASTM E900-15: Standard Guide for Predicting Radiation-Induced Transition Temperature Shift.",
 ],
 "demo": {"half_life": 5.0, "n0": 1e6},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "ne-dnb",
 "name": "The Departure From Nucleate Boiling Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "When does boiling on a fuel rod switch from efficient nucleate boiling to film boiling that overheats the cladding - and can the crisis be predicted from first principles?",
 "background": "Departure from nucleate boiling (DNB) - the boiling crisis - is the fundamental thermal limit of pressurized water reactors: past the critical heat flux, vapor blankets the rod, heat transfer collapses, and cladding temperatures spike. The industry predicts DNB with empirical correlations (W-3, WRB-1) fitted to thousands of experiments, applied with DNBR safety margins around 1.2-1.3. But the correlations are empirical fits, not physics: they extrapolate poorly to new fuel designs, and the micro-scale physics (bubble crowding, microlayer evaporation) is still debated. Mechanistic DNB prediction from first principles remains an unsolved grand challenge of thermal hydraulics.",
 "why_it_matters": "DNB sets the power limit of every PWR on earth. The margin between operating power and the boiling crisis is the margin between electricity and fuel damage.",
 "sig_lens": "The Signature lens reads DNB as a cliff with a foggy edge: the protocol must map the edge empirically and keep the operation well back from the fog.",
 "sig_solution": LABEL + " Assumptions: (1) DNB correlations are empirical and extrapolate poorly; (2) mechanistic prediction is not yet practical. Reasoning path: bound the crisis empirically with uncertainty-quantified correlations, and keep operations at a measured distance from the bound. Proposed mechanism: a cliff-edge protocol that maintains uncertainty bands on critical heat flux predictions, validates against the experimental database continuously, and requires DNBR margins sized to the band width - widening automatically for new fuel designs. Confirm: band-sized margins prevent DNB events without excessive derating. Kill: the bands prove too wide to operate economically. Does NOT claim: mechanistic DNB prediction - it maps the foggy edge honestly.",
 "pointer": "The Signature system's proposed approach keeps uncertainty-banded DNB margins sized to prediction confidence; the companion Signature Edition record specifies the cliff-edge protocol.",
 "key_points": [
  "DNB is the fundamental thermal limit of PWRs; past it, cladding overheats.",
  "Industry correlations are empirical fits, not mechanistic physics.",
  "Correlations extrapolate poorly to new fuel designs.",
  "First-principles DNB prediction remains a grand challenge.",
 ],
 "requirements": [
  "Uncertainty bands on critical heat flux predictions.",
  "Continuous validation against the experimental database.",
  "DNBR margins sized to band width, widened for new designs.",
 ],
 "citations": [
  "Todreas NE, Kazimi MS (2012) Nuclear Systems, Vol. 1. CRC Press.",
 ],
 "demo": {"half_life": 8.0, "n0": 2e6},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "ne-two-phase",
 "name": "The Two Phase Flow Modeling Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Steam and water flowing together behave nothing like either alone - can two-phase flow be modeled accurately enough for reactor safety analysis?",
 "background": "Two-phase flow - the coupled motion of liquid and vapor - governs reactor thermal hydraulics, yet its modeling rests on flow-regime maps and closure relations that are empirical, discontinuous at regime boundaries, and scale-dependent. System codes (RELAP, TRACE) use six-equation two-fluid models with dozens of closure correlations; CFD with interface tracking resolves the physics but cannot reach system scale. The regime transitions (bubbly to slug to annular) are the crux: the closures change discontinuously where nature changes continuously. Validation against integral experiments shows the codes work for the scenarios tested and unknown fidelity outside them.",
 "why_it_matters": "Loss-of-coolant accidents are two-phase flow events. Safety analysis codes predict them with models whose regime-transition fidelity is unquantified.",
 "sig_lens": "The Signature lens reads two-phase flow as a negotiation between phases: the protocol must track what each closure relation actually buys at each regime.",
 "sig_solution": LABEL + " Assumptions: (1) closure relations are empirical and regime-discontinuous; (2) system-scale CFD is unreachable. Reasoning path: quantify closure uncertainty regime by regime, propagate it through safety calculations, and report safety margins net of modeling uncertainty. Proposed mechanism: a negotiation protocol that maintains uncertainty bands per flow regime from validation data, propagates them through accident analysis, and sizes safety margins to the total uncertainty - flagging regimes where the bands dominate the answer. Confirm: uncertainty-propagated analyses show better agreement with integral tests. Kill: the bands prove too wide for licensing decisions. Does NOT claim: first-principles two-phase prediction - it prices the closure uncertainty.",
 "pointer": "The Signature system's proposed approach propagates regime-by-regime closure uncertainty through safety analysis; the companion Signature Edition record specifies the negotiation protocol.",
 "key_points": [
  "Two-phase closures are empirical and discontinuous at regime boundaries.",
  "System codes work for tested scenarios; fidelity outside is unknown.",
  "Interface-tracking CFD cannot reach system scale.",
  "Regime transitions are the crux where closures fail.",
 ],
 "requirements": [
  "Per-regime closure uncertainty bands from validation data.",
  "Uncertainty propagation through accident analysis.",
  "Safety margins sized to total modeling uncertainty.",
 ],
 "citations": [
  "US NRC TRACE V5.0 Theory Manual.",
 ],
 "demo": {"half_life": 3.0, "n0": 5e5},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "ne-scc",
 "name": "The Stress Corrosion Cracking Problem",
 "group": "Nuclear Materials",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Why do stainless steels and nickel alloys crack in reactor water when stress, material, and environment align - and can the cracking be predicted before it starts?",
 "background": "Stress corrosion cracking (SCC) - the synergistic failure from tensile stress, susceptible material, and corrosive environment - has plagued reactors for decades: primary-water SCC of Alloy 600 steam generator tubes and vessel head penetrations (Davis-Besse, 2002), irradiation-assisted SCC of core internals. The mechanism couples electrochemistry, microstructure, and mechanics across scales, and no predictive model spans them: initiation is stochastic and unobservable, growth rates scatter by orders of magnitude. Mitigation (zinc injection, hydrogen water chemistry, material replacement with Alloy 690) manages the problem empirically. Predicting where the next crack initiates remains beyond reach.",
 "why_it_matters": "SCC has caused some of the industry's costliest outages and nearest misses. Unpredictable cracking in primary pressure boundaries is the integrity threat that never retires.",
 "sig_lens": "The Signature lens reads SCC as a conspiracy of three: the protocol must watch all three conspirators and never trust the absence of evidence.",
 "sig_solution": LABEL + " Assumptions: (1) initiation is stochastic and unobservable; (2) no multi-scale predictive model exists. Reasoning path: manage susceptibility, not prediction - rank components by the three-factor exposure and inspect the highest-ranked on a measured basis. Proposed mechanism: a conspiracy-watch protocol that scores every primary-boundary location on stress, material susceptibility, and environmental aggressiveness, schedules inspection by the combined score, and updates scores with inspection findings - treating uninspected high-score locations as the top risk. Confirm: score-ranked inspection finds cracking earlier than calendar-based programs. Kill: the scores misrank and inspections miss the real cracks. Does NOT claim: crack initiation prediction - it watches the conspirators systematically.",
 "pointer": "The Signature system's proposed approach ranks SCC risk by three-factor exposure and inspects by score; the companion Signature Edition record specifies the conspiracy-watch protocol.",
 "key_points": [
  "SCC needs stress, susceptible material, and environment together.",
  "Alloy 600 PWSCC caused major outages (Davis-Besse vessel head, 2002).",
  "Initiation is stochastic; growth rates scatter by orders of magnitude.",
  "Mitigation is empirical; prediction of initiation is beyond reach.",
 ],
 "requirements": [
  "Three-factor susceptibility scoring of primary-boundary locations.",
  "Inspection scheduling by combined risk score.",
  "Score updates from inspection findings, including null results.",
 ],
 "citations": [
  "Scott PM (1994) A review of irradiation assisted stress corrosion cracking. J. Nuclear Materials 211.",
 ],
 "demo": {"half_life": 12.0, "n0": 8e5},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "ne-crud",
 "name": "The CRUD Induced Power Shift Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Corrosion deposits (CRUD) on fuel rods trap boron and shift power to the top of the core - can this axial offset anomaly be predicted and prevented?",
 "background": "CRUD - Chalk River unidentified deposits - is porous corrosion product that deposits on fuel cladding, and in high-duty PWRs it absorbs boron from the coolant, suppressing power low in the core and shifting it upward: the axial offset anomaly (AOA), or CRUD-induced power shift (CIPS). First widely observed in the 1980s-90s, CIPS forced power derates at multiple plants. The deposition couples thermal hydraulics, chemistry, and neutronics across scales; predictive models (EPRI's BOA code) capture trends but not events. Mitigation - zinc injection, pH control, fuel duty management - works empirically. Predicting which cycle will go anomalous remains unreliable.",
 "why_it_matters": "CIPS has forced multi-million-dollar power derates. The coupling of chemistry to neutronics through a porous deposit is the kind of multi-physics surprise that derates plants.",
 "sig_lens": "The Signature lens reads CRUD as slow poison: the protocol must track the deposit inventory continuously and act before the anomaly, not after.",
 "sig_solution": LABEL + " Assumptions: (1) CRUD deposition couples chemistry, thermal hydraulics, and neutronics; (2) prediction of events is unreliable. Reasoning path: monitor the precursors - coolant chemistry, deposit indicators, axial offset trends - and intervene on precursor thresholds rather than waiting for the anomaly. Proposed mechanism: a slow-poison protocol tracking CRUD precursor indicators through the cycle, with chemistry and duty interventions triggered at measured thresholds, and post-cycle deposit characterization feeding the next cycle's thresholds. Confirm: precursor-triggered intervention prevents AOA events. Kill: precursors prove unreliable and interventions mistime. Does NOT claim: CIPS prediction - it watches the poison accumulate and acts early.",
 "pointer": "The Signature system's proposed approach monitors CRUD precursors and intervenes on measured thresholds; the companion Signature Edition record specifies the slow-poison protocol.",
 "key_points": [
  "CRUD traps boron, shifting core power upward (axial offset anomaly).",
  "CIPS forced power derates at multiple high-duty PWRs.",
  "Deposition couples thermal hydraulics, chemistry, and neutronics.",
  "Predictive codes capture trends but not events.",
 ],
 "requirements": [
  "In-cycle monitoring of CRUD precursor indicators.",
  "Chemistry and duty interventions on measured thresholds.",
  "Post-cycle deposit characterization feeding forward.",
 ],
 "citations": [
  "EPRI BOA (Boron-induced Offset Anomaly) code documentation.",
 ],
 "demo": {"half_life": 6.5, "n0": 1.5e6},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "ne-smr-economics",
 "name": "The Small Modular Reactor Economics Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "SMRs promise cheaper nuclear through factory fabrication - but can the economics work when the first units cost more and the learning curve is unproven?",
 "background": "Small modular reactors - under 300 MWe, factory-built - are the industry's great hope: NuScale's design was the first SMR certified by the US NRC (2023), yet its flagship Utah project was cancelled in 2023 over rising costs. The economic thesis is learning-by-doing: factory production drives costs down the experience curve. But nuclear has historically shown negative learning (costs rising with experience in the US and France), the first-of-a-kind costs are enormous, and the regulatory cost of licensing novel designs is uncertain. Whether SMRs achieve the cost declines their business cases assume is the existential question of the nuclear renaissance.",
 "why_it_matters": "SMR economics will decide whether nuclear scales to meet clean-energy demand or remains a legacy fleet. Billions in investment ride on learning curves that may not exist.",
 "sig_lens": "The Signature lens reads SMR economics as a bet on learning: the protocol must track the learning rate actually achieved and reprice the bet continuously.",
 "sig_solution": LABEL + " Assumptions: (1) nuclear has shown negative learning historically; (2) first-of-a-kind costs dominate early economics. Reasoning path: make the learning bet explicit - track cost versus unit number from the first module, and gate further commitments on measured learning rates. Proposed mechanism: a learning-bet protocol requiring SMR programs to publish cost-learning curves per unit, to trigger go/no-go reviews when measured learning deviates from the business case, and to separate regulatory-driven costs from manufacturing learning. Confirm: protocol-gated programs avoid the sunk-cost escalation of cancelled flagships. Kill: learning rates prove unmeasurable amid cost noise. Does NOT claim: that SMRs will achieve their cost targets - it keeps the bet honest.",
 "pointer": "The Signature system's proposed approach tracks SMR cost-learning per unit and gates commitments on measured rates; the companion Signature Edition record specifies the learning-bet protocol.",
 "key_points": [
  "NuScale's NRC certification (2023) was followed by its flagship project's cancellation.",
  "The economic thesis is factory learning-by-doing.",
  "Nuclear historically showed negative learning in the US and France.",
  "Regulatory costs for novel designs are deeply uncertain.",
 ],
 "requirements": [
  "Published cost-versus-unit-number learning curves.",
  "Go/no-go reviews on measured versus assumed learning rates.",
  "Separation of regulatory costs from manufacturing learning.",
 ],
 "citations": [
  "US NRC NuScale design certification rulemaking (2023).",
 ],
 "demo": {"half_life": 4.0, "n0": 3e6},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "ne-load-follow",
 "name": "The Load Following With Nuclear Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Nuclear plants were built to run flat out - but grids full of renewables need flexible generation, so how can reactors load-follow without breaking fuel or economics?",
 "background": "French PWRs have load-followed for decades (grey rod control, boron adjustments), proving it is technically possible - at a cost: xenon transients complicate the physics, thermal cycling stresses components, and the economics punish it (nuclear's costs are almost all fixed, so running at 70 percent barely saves money). The flexibility value depends on the grid: with high renewable penetration, flexible nuclear displaces storage and curtailment. The optimization - how flexibly to operate given fuel, component, and market effects - has no general solution, and most new designs claim flexibility without demonstrating its economics.",
 "why_it_matters": "Renewable-heavy grids need firm flexible generation. Nuclear that cannot follow load is nuclear that gets curtailed - economics and physics must meet.",
 "sig_lens": "The Signature lens reads flexibility as a product with a cost: the protocol must price every maneuver in fuel, fatigue, and foregone revenue.",
 "sig_solution": LABEL + " Assumptions: (1) load-following is technically proven but economically punished; (2) flexibility value is grid-dependent. Reasoning path: dispatch nuclear flexibility only where it pays - compute the maneuver cost (fuel, fatigue, market) against the grid's flexibility price. Proposed mechanism: a flexibility-market protocol that prices each load maneuver in component-fatigue and fuel terms, bids nuclear flexibility into grid markets at its true cost, and holds baseload where the flexibility price does not clear. Confirm: priced flexibility earns more than blanket load-following. Kill: fatigue costs prove unmeasurable and the pricing is fiction. Does NOT claim: a general flexibility optimum - it trades flexibility where the market pays.",
 "pointer": "The Signature system's proposed approach prices nuclear maneuvers and bids flexibility at true cost; the companion Signature Edition record specifies the flexibility-market protocol.",
 "key_points": [
  "French PWRs prove load-following is technically feasible.",
  "Xenon transients and thermal cycling are the physics and materials costs.",
  "Nuclear costs are mostly fixed, so part-load operation barely saves money.",
  "Flexibility value depends on renewable penetration and market design.",
 ],
 "requirements": [
  "Per-maneuver costing in fuel, fatigue, and market terms.",
  "Flexibility bidding at true cost into grid markets.",
  "Baseload default where flexibility prices do not clear.",
 ],
 "citations": [
  "OECD NEA (2011) Technical and Economic Aspects of Load Following with Nuclear Power Stations.",
 ],
 "demo": {"half_life": 9.0, "n0": 7e5},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "ne-cogeneration",
 "name": "The Nuclear Cogeneration Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Reactors make heat, not just electricity - so why is nuclear cogeneration (desalination, hydrogen, district heat) still mostly PowerPoint, and what would make it real?",
 "background": "Two-thirds of a reactor's energy leaves as waste heat, and the cogeneration case is obvious: desalination (nuclear desalination has run in Kazakhstan and Japan), high-temperature hydrogen (sulfur-iodine, high-temperature electrolysis), district heating (Swiss and Russian experience). But the barriers are structural: electricity markets pay for kilowatt-hours, not heat; coupling a nuclear plant to an industrial process entangles licensing (whose safety case covers the hydrogen plant?); and the economics need heat customers adjacent to the reactor. High-temperature gas reactors would unlock efficient hydrogen, but they are not yet commercial. The integration problem - technical, regulatory, economic - is unsolved as a system.",
 "why_it_matters": "Waste heat is the largest unused energy stream in the power sector. Cogeneration could decarbonize desalination, hydrogen, and industry - if the integration barriers fall.",
 "sig_lens": "The Signature lens reads cogeneration as a marriage: the protocol must arrange the heat match, the license, and the economics together, or not at all.",
 "sig_solution": LABEL + " Assumptions: (1) the barriers are structural (markets, licensing), not just technical; (2) heat customers must be adjacent. Reasoning path: develop the three legs together - anchor heat customers, pre-license the coupled safety case, and contract the heat price before building. Proposed mechanism: a marriage protocol requiring signed heat off-take agreements, a coupled licensing pathway agreed with regulators in advance, and heat pricing that reflects its carbon value - with the project gated on all three legs. Confirm: three-legged projects reach operation more often than heat-first or reactor-first ones. Kill: regulators refuse coupled licensing and the marriage is annulled. Does NOT claim: a general cogeneration optimum - it arranges the specific marriage completely.",
 "pointer": "The Signature system's proposed approach develops heat customers, coupled licensing, and heat pricing together; the companion Signature Edition record specifies the marriage protocol.",
 "key_points": [
  "Two-thirds of reactor energy leaves as waste heat.",
  "Nuclear desalination has operated (Kazakhstan, Japan); hydrogen coupling has not scaled.",
  "Licensing the coupled industrial process is structurally unresolved.",
  "Heat customers must be adjacent; markets pay for electricity, not heat.",
 ],
 "requirements": [
  "Signed heat off-take agreements before construction.",
  "Coupled safety-case licensing pathway agreed in advance.",
  "Heat pricing reflecting carbon value.",
 ],
 "citations": [
  "IAEA (2017) Opportunities for Cogeneration with Nuclear Energy.",
 ],
 "demo": {"half_life": 7.0, "n0": 2.5e6},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "ne-decommissioning",
 "name": "The Decommissioning Cost Estimation Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Dismantling a reactor costs hundreds of millions - but estimates routinely miss by factors of two, so how can the true cost be known before the work begins?",
 "background": "Decommissioning - SAFSTOR (deferred), DECON (immediate dismantling) - has been completed for dozens of reactors, yet cost estimates remain wildly uncertain: actual costs range from a few hundred million to over a billion dollars, driven by waste disposal availability, regulatory changes, and site-specific surprises (contamination finds). The estimation methods extrapolate from the small completed sample to diverse future plants, and the waste-disposal cost - the largest uncertainty - depends on repositories that do not exist. Underfunded decommissioning trusts are the industry's quiet liability.",
 "why_it_matters": "Every operating reactor carries a decommissioning liability. Misestimated by half, the shortfall lands on ratepayers or taxpayers decades after the plant profited.",
 "sig_lens": "The Signature lens reads decommissioning as a bill coming due: the protocol must fund it against the honest cost distribution, not the optimistic point estimate.",
 "sig_solution": LABEL + " Assumptions: (1) the completed sample is small and diverse; (2) waste-disposal cost dominates the uncertainty. Reasoning path: estimate probabilistically from the completed-plant database, stress the waste-disposal assumption, and fund to a high percentile. Proposed mechanism: a bill-due protocol that maintains a decommissioning cost database, produces probabilistic estimates per plant with waste-disposal scenarios, and requires trust funding to the 80th percentile with periodic true-ups. Confirm: probabilistically funded trusts avoid shortfalls better than point-estimated ones. Kill: unprecedented plant designs break the historical database. Does NOT claim: exact decommissioning costs - it funds against the honest distribution.",
 "pointer": "The Signature system's proposed approach funds decommissioning to high-percentile probabilistic estimates; the companion Signature Edition record specifies the bill-due protocol.",
 "key_points": [
  "Actual decommissioning costs range from hundreds of millions past a billion.",
  "Estimates miss by factors of two routinely.",
  "Waste-disposal availability dominates the uncertainty.",
  "Underfunded trusts are a quiet industry liability.",
 ],
 "requirements": [
  "A maintained completed-plant cost database.",
  "Probabilistic per-plant estimates with waste scenarios.",
  "Trust funding to high percentiles with periodic true-ups.",
 ],
 "citations": [
  "OECD NEA (2016) Costs of Decommissioning Nuclear Power Plants.",
 ],
 "demo": {"half_life": 15.0, "n0": 4e5},
},
# ----------------------------------------------------------------- rank 10
{
 "key": "ne-haleu",
 "name": "The High Assay Low Enriched Uranium Supply Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Advanced reactors need HALEU - uranium enriched to 5-20 percent - but the commercial supply chain barely exists, so how can the fuel be available when the reactors are?",
 "background": "Most advanced reactor designs (TRISO-fueled, fast reactors, microreactors) need high-assay low-enriched uranium: enrichment between 5 and 20 percent, above the 5 percent commercial standard but below weapons-usable levels. The problem is supply: enrichment capacity for HALEU is minimal outside limited government programs, the downblending of legacy stocks is finite, and building commercial enrichment takes years and billions. The chicken-and-egg is stark: enrichers will not build without reactor orders, reactors cannot order without fuel assurance. The US DOE's HALEU programs are bridging, but the commercial gap persists.",
 "why_it_matters": "Dozens of advanced reactor designs share one fuel bottleneck. Without HALEU supply, the advanced reactor pipeline is a fleet with no fuel.",
 "sig_lens": "The Signature lens reads HALEU as a bridge that must be built before the traffic: the protocol must secure the fuel path before the reactor orders depend on it.",
 "sig_solution": LABEL + " Assumptions: (1) the chicken-and-egg blocks commercial investment; (2) legacy downblending is finite. Reasoning path: bridge explicitly - quantify the HALEU demand timeline from reactor pipelines, match it against supply projects, and expose the gap years in advance. Proposed mechanism: a bridge protocol maintaining a HALEU demand-supply ledger (reactor pipelines versus enrichment projects and stockpiles), triggering coordinated investment signals when gaps appear, and qualifying alternative fuel forms where HALEU timelines slip. Confirm: ledger-coordinated programs avoid fuel-driven reactor delays. Kill: demand forecasts prove fictional and the ledger misleads. Does NOT claim: a commercial HALEU market - it keeps the bridge-building honest and early.",
 "pointer": "The Signature system's proposed approach maintains a HALEU demand-supply ledger with early gap signals; the companion Signature Edition record specifies the bridge protocol.",
 "key_points": [
  "Advanced reactors need 5-20 percent enrichment; commercial supply is minimal.",
  "Enrichers await reactor orders; reactors await fuel assurance.",
  "Legacy downblend stocks are finite.",
  "Government programs bridge but do not close the commercial gap.",
 ],
 "requirements": [
  "A maintained HALEU demand-supply ledger.",
  "Early gap signals triggering coordinated investment.",
  "Alternative fuel qualification where timelines slip.",
 ],
 "citations": [
  "US DOE HALEU program documentation.",
 ],
 "demo": {"half_life": 5.5, "n0": 9e5},
},
# ----------------------------------------------------------------- rank 11
{
 "key": "ne-atf",
 "name": "The Accident Tolerant Fuel Qualification Problem",
 "group": "Nuclear Materials",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Accident-tolerant fuels promise to survive loss-of-cooling longer - but how can new cladding and fuel be qualified for 60-year service without 60 years of testing?",
 "background": "After Fukushima, the industry pursued accident-tolerant fuel (ATF): coated zirconium cladding, FeCrAl cladding, doped pellets - all aiming to extend coping time in accidents by resisting steam oxidation and ballooning. But qualification is the wall: fuel licensing needs irradiation data to high burnup, which takes a decade in test reactors, and the lead-test-assembly path is slow and expensive. The fundamental problem is accelerated qualification - inferring 60-year behavior from short tests - which materials science cannot yet do reliably. Meanwhile the benefits (extra coping hours) must be weighed against the uncertainties of novel materials.",
 "why_it_matters": "ATF could add critical coping hours in severe accidents. But unqualified fuel in a reactor is an experiment on the public - qualification cannot be shortcut by hope.",
 "sig_lens": "The Signature lens reads qualification as a trust account: every test deposits evidence, and the protocol must show the balance before the fuel earns its place.",
 "sig_solution": LABEL + " Assumptions: (1) accelerated qualification is unreliable; (2) lead assemblies are slow but real. Reasoning path: build the trust account in stages - separate-effects tests, integral tests, then lead assemblies - with explicit evidence thresholds for each stage. Proposed mechanism: a trust-account protocol defining staged qualification gates (each with required evidence types), allowing limited lead-assembly deployment only after gate passage, and requiring full-core deployment to clear the final gate. Confirm: staged qualification catches material issues before full-core commitment. Kill: stage gates prove too slow and ATF never deploys. Does NOT claim: accelerated qualification - it earns trust in stages.",
 "pointer": "The Signature system's proposed approach qualifies ATF through staged evidence gates; the companion Signature Edition record specifies the trust-account protocol.",
 "key_points": [
  "ATF aims to extend coping time via oxidation-resistant cladding and fuels.",
  "Qualification needs high-burnup irradiation data: a decade in test reactors.",
  "Accelerated inference of 60-year behavior is unreliable.",
  "Lead-test assemblies are the slow, real path.",
 ],
 "requirements": [
  "Staged qualification gates with defined evidence types.",
  "Lead-assembly deployment only after gate passage.",
  "Full-core deployment gated on final evidence.",
 ],
 "citations": [
  "US DOE Accident Tolerant Fuel program documentation.",
 ],
 "demo": {"half_life": 11.0, "n0": 6e5},
},
# ----------------------------------------------------------------- rank 12
{
 "key": "ne-source-term",
 "name": "The Severe Accident Source Term Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "If the core melts, what radioactive material escapes, when, and how much - and can the source term be predicted well enough for emergency planning?",
 "background": "The source term - the timing, magnitude, and composition of radioactive release in a severe accident - drives emergency planning zones, containment design, and accident management. The TID-14844 (1961) and NUREG-1465 (1995) source terms bracket the history: from conservative instant-release assumptions to best-estimate phased releases. Mechanistic codes (MELCOR, ASTEC) model the phenomenology - fission product chemistry, aerosol physics, containment transport - but the uncertainties are enormous: iodine chemistry alone can swing releases by orders of magnitude. Fukushima's releases are still being reconstructed. The gap between best-estimate and uncertainty-quantified source terms is the field's open wound.",
 "why_it_matters": "Evacuation zones, potassium iodide distribution, and containment filtered-venting strategies all rest on the source term. An underestimated source term is an unprotected public.",
 "sig_lens": "The Signature lens reads the source term as a forecast that must carry its storm warning: the protocol ships the best estimate with the uncertainty that could change the protective action.",
 "sig_solution": LABEL + " Assumptions: (1) mechanistic models carry order-of-magnitude uncertainties in key phenomena; (2) emergency decisions need bounds, not just best estimates. Reasoning path: compute source terms as distributions via uncertainty propagation, and base protective actions on the distribution's upper tail. Proposed mechanism: a storm-warning protocol that runs best-estimate plus uncertainty (BEPU) source term analysis, identifies the dominant uncertainty contributors (iodine chemistry, leak paths), and sets emergency planning on the upper-confidence release. Confirm: BEPU-based planning covers observed releases in validation exercises. Kill: the uncertainties prove too wide for any planning to be meaningful. Does NOT claim: accurate source term prediction - it plans against the honest upper tail.",
 "pointer": "The Signature system's proposed approach plans emergency response on uncertainty-quantified source term upper tails; the companion Signature Edition record specifies the storm-warning protocol.",
 "key_points": [
  "Source terms evolved from TID-14844 conservatism to NUREG-1465 best estimates.",
  "Iodine chemistry uncertainties swing releases by orders of magnitude.",
  "MELCOR and ASTEC model the phenomenology with large uncertainties.",
  "Fukushima's releases are still being reconstructed.",
 ],
 "requirements": [
  "Best-estimate-plus-uncertainty source term analysis.",
  "Dominant-uncertainty identification per scenario.",
  "Emergency planning based on upper-confidence releases.",
 ],
 "citations": [
  "NUREG-1465: Accident Source Terms for Light-Water Nuclear Power Plants.",
 ],
 "demo": {"half_life": 4.5, "n0": 1.2e6},
},
# ----------------------------------------------------------------- rank 13
{
 "key": "ne-hydrogen",
 "name": "The Hydrogen Risk Mitigation Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Zirconium-steam reaction makes hydrogen in severe accidents - but where does it go, when does it burn, and how can containment-threatening combustion be prevented?",
 "background": "Above about 1200 C, zirconium cladding oxidizes in steam, releasing hydrogen: in a severe accident, hundreds of kilograms can accumulate in containment. Hydrogen burns - deflagration - or detonates if concentrated and mixed, threatening containment integrity (the Fukushima Unit 1 explosion was hydrogen). Mitigation relies on passive autocatalytic recombiners (PARs) and deliberate ignition systems, but the distribution problem is unsolved: hydrogen stratifies and mixes in complex 3D patterns that lumped-parameter codes approximate crudely. Predicting where flammable clouds form, and whether recombiners can prevent them, remains uncertain.",
 "why_it_matters": "Containment is the last barrier; hydrogen combustion is what threatens it from inside. Fukushima showed the explosion is not theoretical.",
 "sig_lens": "The Signature lens reads hydrogen as an invisible accumulation: the protocol must track where it gathers and remove it before it finds a spark.",
 "sig_solution": LABEL + " Assumptions: (1) hydrogen distribution in 3D containments is poorly predicted; (2) recombiners have placement-dependent effectiveness. Reasoning path: design mitigation for the worst credible distribution, not the best-estimate one - place recombiners by 3D analysis and verify with experiments. Proposed mechanism: an accumulation-watch protocol requiring 3D hydrogen distribution analysis for recombiner placement, experimental validation of mixing predictions, and deliberate-ignition backup where recombiners cannot cover. Confirm: 3D-placed mitigation prevents flammable clouds in validation tests. Kill: 3D predictions prove unreliable and placement is guesswork. Does NOT claim: exact hydrogen distribution prediction - it mitigates against the credible worst case.",
 "pointer": "The Signature system's proposed approach places hydrogen mitigation by 3D distribution analysis; the companion Signature Edition record specifies the accumulation-watch protocol.",
 "key_points": [
  "Zirconium-steam reaction above 1200 C generates large hydrogen inventories.",
  "Fukushima Unit 1's explosion was hydrogen combustion.",
  "Hydrogen stratifies in complex 3D patterns codes approximate crudely.",
  "Recombiner effectiveness depends on placement against the distribution.",
 ],
 "requirements": [
  "3D hydrogen distribution analysis for mitigation placement.",
  "Experimental validation of mixing predictions.",
  "Backup deliberate-ignition where recombiners cannot cover.",
 ],
 "citations": [
  "NUREG/CR-2726: Light Water Reactor Hydrogen Manual.",
 ],
 "demo": {"half_life": 6.0, "n0": 1.8e6},
},
# ----------------------------------------------------------------- rank 14
{
 "key": "ne-corium",
 "name": "The Molten Corium Coolability Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "If molten core material (corium) relocates to the containment floor, can water cool it - or does it keep generating heat until it breaches?",
 "background": "Corium - the molten mixture of fuel, cladding, and steel at 2500+ C - is the end state of core melt. Whether flooding it cools it (quenching) or triggers steam explosions is one of severe-accident research's central questions: the FARO and KROTOS experiments showed energetic fuel-coolant interactions are possible, while the COMET and DEFOR programs studied coolability through porous debris beds. Ex-vessel cooling strategies (core catchers in EPR, IVR in some designs) bet on coolability, but the bet's odds are uncertain - debris bed dryout, melt spreading, and concrete ablation (MCCI) each have large uncertainties. The coolability question has no validated general answer.",
 "why_it_matters": "Ex-vessel accident management - core catchers, cavity flooding - bets lives on corium coolability. An unvalidated bet is a hope, not a strategy.",
 "sig_lens": "The Signature lens reads corium as a fire that must be drowned: the protocol must know whether the water will quench it or feed the steam explosion.",
 "sig_solution": LABEL + " Assumptions: (1) coolability depends on debris morphology, which is scenario-dependent; (2) steam explosion risk accompanies flooding. Reasoning path: qualify coolability per design with experiments at representative scale, and manage the explosion risk explicitly. Proposed mechanism: a drowning protocol requiring design-specific coolability demonstration (experiments plus validated models), steam-explosion risk assessment for the flooding strategy, and accident management procedures that condition flooding on the assessed risk. Confirm: protocol-qualified strategies show coolable configurations in integral tests. Kill: scale effects defeat the experiments and the qualification is hollow. Does NOT claim: general corium coolability - it qualifies per design with the explosion risk priced.",
 "pointer": "The Signature system's proposed approach qualifies ex-vessel coolability per design with explosion-risk assessment; the companion Signature Edition record specifies the drowning protocol.",
 "key_points": [
  "Corium at 2500+ C is the end state of core melt.",
  "Flooding can quench or trigger steam explosions (FARO/KROTOS).",
  "Debris-bed dryout and concrete ablation carry large uncertainties.",
  "Core catchers and cavity flooding bet on unvalidated coolability.",
 ],
 "requirements": [
  "Design-specific coolability demonstration at representative scale.",
  "Steam-explosion risk assessment per flooding strategy.",
  "Accident procedures conditioning flooding on assessed risk.",
 ],
 "citations": [
  "OECD/NEA SERENA program on fuel-coolant interactions.",
 ],
 "demo": {"half_life": 3.5, "n0": 2.2e6},
},
# ----------------------------------------------------------------- rank 15
{
 "key": "ne-filtered-venting",
 "name": "The Containment Filtered Venting Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "When containment pressure threatens the structure, venting releases radioactivity deliberately - how can filtered venting be designed and operated to minimize the release?",
 "background": "Filtered containment venting systems (FCVS) - sand-bed or wet-scrubber filters on a vent path - were backfitted widely after Fukushima: vent early through a filter rather than lose containment catastrophically. But the design questions are open: what decontamination factor is achievable under real accident conditions (aerosol loading, hydrogen, high temperature), when exactly to vent (early venting releases more; late venting risks containment), and how do operators decide under stress. The venting decision is the hardest call in accident management - deliberately releasing radioactivity - and the procedures supporting it are thinner than the stakes.",
 "why_it_matters": "Filtered venting is the deliberate-release decision: done right it saves containment; done wrong it releases unnecessarily. Fukushima's venting delays and difficulties showed the gap.",
 "sig_lens": "The Signature lens reads venting as a controlled bleed: the protocol must decide the pressure, the timing, and the filter - before the crisis, not during it.",
 "sig_solution": LABEL + " Assumptions: (1) filter performance under real accident conditions is uncertain; (2) the vent timing decision is the hardest call in accident management. Reasoning path: pre-decide the venting strategy - pressure triggers, filter qualification envelopes, and decision authority - in calm analysis, not in crisis. Proposed mechanism: a controlled-bleed protocol with pre-analyzed venting triggers tied to containment pressure and filter status, filter qualification across the accident envelope, and clear decision authority in procedures. Confirm: pre-decided strategies vent earlier and release less in simulator exercises. Kill: real accidents fall outside the analyzed envelope and the triggers misfire. Does NOT claim: optimal venting - it decides the hard call in advance.",
 "pointer": "The Signature system's proposed approach pre-decides filtered venting triggers and qualifies filters across the envelope; the companion Signature Edition record specifies the controlled-bleed protocol.",
 "key_points": [
  "FCVS backfits spread after Fukushima: vent through filters, not through failure.",
  "Filter decontamination factors under real conditions are uncertain.",
  "Vent timing trades early release against containment risk.",
  "The deliberate-release decision procedures are thinner than the stakes.",
 ],
 "requirements": [
  "Pre-analyzed venting triggers tied to pressure and filter status.",
  "Filter qualification across the accident envelope.",
  "Clear decision authority in accident procedures.",
 ],
 "citations": [
  "OECD/NEA (2014) Status Report on Filtered Containment Venting.",
 ],
 "demo": {"half_life": 8.5, "n0": 1.1e6},
},
# ----------------------------------------------------------------- rank 16
{
 "key": "ne-pra-completeness",
 "name": "The Probabilistic Risk Assessment Completeness Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "PRAs quantify accident risk by enumerating scenarios - but how can anyone know the enumeration is complete, and what about the scenarios nobody thought of?",
 "background": "Probabilistic risk assessment - event trees, fault trees, human reliability - has guided nuclear safety since WASH-1400 (1975) and matured through NUREG-1150. But completeness is the foundational doubt: the PRA quantifies the scenarios modeled, not the ones missed, and history's surprises (Fukushima's multi-unit common-cause tsunami) came from outside the models. Unknown unknowns, model uncertainty, and the treatment of low-probability high-consequence events are handled by judgment. Risk-informed regulation leans on PRA numbers whose completeness cannot be demonstrated - the numbers are conditional on the model being adequate, which is the thing in question.",
 "why_it_matters": "Risk numbers steer regulation and design. A PRA that misses the dominant scenario is precise about the wrong risk - confidence built on an incomplete map.",
 "sig_lens": "The Signature lens reads PRA as a map with blank edges: the protocol must label the blanks and probe them, not pretend the map is the territory.",
 "sig_solution": LABEL + " Assumptions: (1) completeness cannot be demonstrated; (2) surprises come from outside the model. Reasoning path: treat the PRA as conditional - quantify what is modeled rigorously, and probe the blanks with structured searches for missing scenarios. Proposed mechanism: a blank-edges protocol requiring completeness-uncertainty statements on every PRA, structured missing-scenario searches (precursor analysis, cross-industry operating experience, adversarial review), and safety margins sized to the completeness doubt. Confirm: blank-edge probing finds risk-significant missing scenarios. Kill: the searches find nothing and become ritual. Does NOT claim: complete PRAs - it labels the blanks and prices the doubt.",
 "pointer": "The Signature system's proposed approach pairs PRAs with completeness-uncertainty statements and missing-scenario searches; the companion Signature Edition record specifies the blank-edges protocol.",
 "key_points": [
  "PRAs quantify modeled scenarios; completeness cannot be demonstrated.",
  "Historical surprises (Fukushima multi-unit tsunami) came from outside models.",
  "Unknown unknowns and model uncertainty are handled by judgment.",
  "Risk-informed regulation leans on conditional numbers.",
 ],
 "requirements": [
  "Completeness-uncertainty statements on every PRA.",
  "Structured missing-scenario searches (precursors, operating experience).",
  "Safety margins sized to the completeness doubt.",
 ],
 "citations": [
  "NUREG-1150: Severe Accident Risks: An Assessment for Five US Nuclear Power Plants.",
 ],
 "demo": {"half_life": 10.0, "n0": 9e5},
},
# ----------------------------------------------------------------- rank 17
{
 "key": "ne-hra",
 "name": "The Human Reliability Analysis Quantification Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Human actions dominate many accident sequences - but how can the probability of human error be quantified when the data is sparse and context is everything?",
 "background": "Human reliability analysis (HRA) - THERP, ASEP, SPAR-H, and newer methods - assigns error probabilities to operator actions in PRAs, but the numbers rest on thin foundations: expert judgment dominates, the data (simulator studies, rare events) is sparse, and performance-shaping factors (stress, complexity, time pressure) are modeled crudely. The same action gets different probabilities from different methods by orders of magnitude. Post-Fukushima, the multi-unit, long-duration, beyond-design-basis actions that matter most are exactly the ones with no data. HRA is the PRA's largest uncertainty contributor and its least scientific part.",
 "why_it_matters": "Operators are the last line of defense and the largest uncertainty in risk numbers. Unquantified human reliability means unquantified risk.",
 "sig_lens": "The Signature lens reads operators as the adaptive margin: the protocol must measure what crews actually do under pressure, not what task analysis imagines.",
 "sig_solution": LABEL + " Assumptions: (1) HRA numbers rest on expert judgment and sparse data; (2) methods disagree by orders of magnitude. Reasoning path: ground HRA in observed crew performance - simulator data on the actual actions, with uncertainty bands reflecting method disagreement. Proposed mechanism: an adaptive-margin protocol requiring simulator-based human error data for risk-significant actions, multi-method HRA with disagreement reported as uncertainty, and crew performance monitoring feeding back into the numbers. Confirm: simulator-grounded HRA predicts crew performance better than judgment-only. Kill: simulator fidelity is too low for the beyond-design-basis actions that matter. Does NOT claim: true human error probabilities - it grounds the numbers in observation with the disagreement shown.",
 "pointer": "The Signature system's proposed approach grounds HRA in simulator-observed crew performance with method-disagreement bands; the companion Signature Edition record specifies the adaptive-margin protocol.",
 "key_points": [
  "HRA methods (THERP, SPAR-H) rest on expert judgment and sparse data.",
  "Different methods give error probabilities differing by orders of magnitude.",
  "Beyond-design-basis actions have essentially no data.",
  "HRA is the PRA's largest uncertainty and least scientific part.",
 ],
 "requirements": [
  "Simulator-based human error data for risk-significant actions.",
  "Multi-method HRA with disagreement reported as uncertainty.",
  "Crew performance monitoring feeding back into HRA numbers.",
 ],
 "citations": [
  "NUREG-1842: Evaluation of Human Reliability Analysis Methods.",
 ],
 "demo": {"half_life": 7.5, "n0": 1.4e6},
},
# ----------------------------------------------------------------- rank 18
{
 "key": "ne-digital-ic",
 "name": "The Digital Instrumentation and Control Assurance Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Digital control systems bring capability and common-cause software failure risk - how can their safety be assured when testing cannot cover the state space?",
 "background": "Nuclear plants are replacing analog with digital instrumentation and control, gaining diagnostics and flexibility - and inheriting software common-cause failure: a single software defect can disable redundant channels simultaneously, defeating the independence that safety relies on. Diversity (different software, FPGAs, analog backup) is the defense, but diversity's effectiveness is unquantified and its cost is high. Formal verification covers tiny programs, not plant control systems. Cybersecurity adds a new dimension: safety systems are now network-accessible targets. The assurance case for digital safety systems - that they are safe enough - is built on process (standards like IEC 61513) more than on evidence.",
 "why_it_matters": "Digital safety systems will control the next generation of reactors. Unassured software common-cause failure is a single defect away from defeating redundancy.",
 "sig_lens": "The Signature lens reads digital I&C as a single mind in redundant bodies: the protocol must prove the minds are truly different, not just the bodies.",
 "sig_solution": LABEL + " Assumptions: (1) software common-cause failure defeats channel redundancy; (2) diversity effectiveness is unquantified. Reasoning path: require evidence of independence - diverse implementations with measured fault-injection testing - and bound the residual common-cause probability explicitly. Proposed mechanism: a different-minds protocol mandating diverse safety implementations, fault-injection campaigns measuring common-mode susceptibility, and explicit common-cause beta factors in the PRA derived from the testing. Confirm: tested-diverse systems show lower common-mode failure in injection campaigns. Kill: fault injection misses the real defect classes and the testing is theater. Does NOT claim: proven software safety - it measures the independence it claims.",
 "pointer": "The Signature system's proposed approach requires measured evidence of implementation independence; the companion Signature Edition record specifies the different-minds protocol.",
 "key_points": [
  "Software common-cause failure can defeat redundant safety channels at once.",
  "Diversity (software, FPGA, analog) is the defense; its effectiveness is unquantified.",
  "Formal verification does not scale to plant control systems.",
  "Assurance rests on process standards more than on evidence.",
 ],
 "requirements": [
  "Diverse safety implementations with documented differences.",
  "Fault-injection campaigns measuring common-mode susceptibility.",
  "Explicit common-cause factors in PRAs derived from testing.",
 ],
 "citations": [
  "IEC 61513: Nuclear power plants - Instrumentation and control for systems important to safety.",
 ],
 "demo": {"half_life": 5.0, "n0": 2.0e6},
},
# ----------------------------------------------------------------- rank 19
{
 "key": "ne-msr-corrosion",
 "name": "The Molten Salt Reactor Corrosion Problem",
 "group": "Nuclear Materials",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Molten fluoride and chloride salts at 700 C dissolve structural metals - can materials survive decades in the salt, and can the corrosion be predicted?",
 "background": "Molten salt reactors promise high-temperature, low-pressure operation, but the salt is a corrosive medium: chromium leaches from nickel alloys (the MSRE at Oak Ridge showed intergranular attack), tellurium embrittles grain boundaries, and the redox chemistry of the salt controls everything. Modern developers test alloys (Hastelloy N derivatives, stainless steels) in salt loops, but the data is short-term, the mechanisms (dissolution, galvanic, impurity-driven) interact, and extrapolating years of lab data to decades of operation is uncertain. Salt chemistry control (redox buffering) is the mitigation lever, but the control's long-term effectiveness is unproven.",
 "why_it_matters": "MSRs cannot operate without materials that survive the salt. Corrosion is the existential materials question of the entire reactor class.",
 "sig_lens": "The Signature lens reads salt corrosion as slow dissolution: the protocol must track the metal loss account and control the chemistry that drives it.",
 "sig_solution": LABEL + " Assumptions: (1) lab data is short-term; decades of operation must be inferred; (2) redox chemistry controls the attack. Reasoning path: couple corrosion monitoring to chemistry control - measure metal loss in situ and hold the salt redox in the protective window. Proposed mechanism: a dissolution-ledger protocol with in-salt corrosion monitoring (electrochemical probes, sample coupons), redox buffering control with measured effectiveness, and component lifetime estimates updated from the monitoring - replacing components on measured loss, not calendar. Confirm: monitored-and-controlled loops show lower corrosion rates than uncontrolled ones. Kill: in-situ monitoring proves unreliable and the ledger is blind. Does NOT claim: decades of material life proven - it tracks the loss and controls the driver.",
 "pointer": "The Signature system's proposed approach couples in-salt corrosion monitoring with redox control; the companion Signature Edition record specifies the dissolution-ledger protocol.",
 "key_points": [
  "Molten salts leach chromium from nickel alloys; tellurium attacks grain boundaries.",
  "MSRE showed intergranular attack; modern data remains short-term.",
  "Redox chemistry of the salt controls corrosion rates.",
  "Extrapolating lab years to operational decades is uncertain.",
 ],
 "requirements": [
  "In-situ corrosion monitoring in salt loops and plants.",
  "Redox buffering control with measured effectiveness.",
  "Component replacement on measured loss, not calendar age.",
 ],
 "citations": [
  "Williams DF et al. (2006) Assessment of candidate molten salt coolants for the NGNP. ORNL/TM-2006/12.",
 ],
 "demo": {"half_life": 14.0, "n0": 5e5},
},
# ----------------------------------------------------------------- rank 20
{
 "key": "ne-triso",
 "name": "The TRISO Fuel Performance Problem",
 "group": "Nuclear Materials",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "TRISO particles coat uranium kernels in ceramic layers - but do the coatings survive high burnup and temperature, and what is the real failure rate?",
 "background": "TRISO (tristructural isotropic) fuel - uranium kernels coated in pyrolytic carbon and silicon carbide - is the fuel of high-temperature gas reactors and many microreactors, with each particle its own containment. The AGR test program at Idaho National Laboratory demonstrated excellent performance, but the statistical failure rate at high burnup and temperature remains the licensing question: billions of particles per core mean even tiny failure fractions matter, and the failure mechanisms (palladium attack on SiC, kernel migration, pressure vessel failure) are incompletely modeled. Manufacturing quality control at billion-particle scale is its own challenge - the fuel's performance is only as good as its weakest particle batch.",
 "why_it_matters": "TRISO is the safety case of the high-temperature reactor fleet: the fuel IS the containment. Unquantified particle failure rates are unquantified releases.",
 "sig_lens": "The Signature lens reads TRISO as billions of tiny containments: the protocol must count the failures statistically and never trust the average particle.",
 "sig_solution": LABEL + " Assumptions: (1) billions of particles make tiny failure fractions significant; (2) failure mechanisms are incompletely modeled. Reasoning path: qualify statistically - measure failure rates on representative samples at the licensing envelope and bound the core release from the measured distribution. Proposed mechanism: a tiny-containments protocol requiring statistically significant irradiation testing at envelope conditions, failure-rate distributions (not point values) feeding the source term, and manufacturing QC tied to the tested particle populations. Confirm: statistically qualified TRISO shows bounded releases in safety analysis. Kill: test conditions miss the real failure modes and the statistics mislead. Does NOT claim: zero particle failures - it bounds the failures statistically.",
 "pointer": "The Signature system's proposed approach qualifies TRISO by statistical failure-rate distributions; the companion Signature Edition record specifies the tiny-containments protocol.",
 "key_points": [
  "TRISO particles are each their own containment; billions per core.",
  "AGR tests showed excellent performance; high-burnup statistics remain the question.",
  "Palladium attack, kernel migration, and pressure failure mechanisms are incomplete.",
  "Manufacturing QC at billion-particle scale is its own challenge.",
 ],
 "requirements": [
  "Statistically significant irradiation testing at envelope conditions.",
  "Failure-rate distributions feeding source term analysis.",
  "Manufacturing QC tied to tested particle populations.",
 ],
 "citations": [
  "INL AGR Fuel Program technical results.",
 ],
 "demo": {"half_life": 9.5, "n0": 8e5},
},
# ----------------------------------------------------------------- rank 21
{
 "key": "ne-fast-cladding",
 "name": "The Fast Reactor Cladding Compatibility Problem",
 "group": "Nuclear Materials",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Fast reactor cladding faces high-temperature sodium or lead plus intense fast-neutron damage - can any alloy survive the combined assault for economic fuel lifetimes?",
 "background": "Fast reactors need cladding that withstands 550-700 C liquid metal coolant, high fast-neutron fluence (hundreds of dpa), and fuel-cladding chemical interaction: austenitic steels swell, ferritic-martensitic steels embrittle, and oxide-dispersion-strengthened (ODS) alloys are hard to fabricate. Sodium compatibility is manageable; lead and lead-bismuth corrode steels aggressively without oxygen control. The qualification data is thin - few fast test reactors operate - and each coolant-alloy combination needs its own decade of testing. Cladding lifetime sets fuel burnup, which sets fast reactor economics.",
 "why_it_matters": "Fast reactors close the fuel cycle, but only if the cladding survives long enough to make the economics work. Materials are the pacing item of the fast reactor future.",
 "sig_lens": "The Signature lens reads cladding as armor in acid rain: the protocol must test the armor against the actual storm, not a gentler one.",
 "sig_solution": LABEL + " Assumptions: (1) fast-neutron plus liquid-metal damage has no good surrogate; (2) qualification data is thin. Reasoning path: test in the real environment - prioritize fast-spectrum irradiation in representative coolant, and qualify incrementally by burnup. Proposed mechanism: an armor protocol requiring coolant-specific irradiation testing, incremental burnup qualification (each extension earned by data), and swelling/embrittlement monitoring feeding lifetime estimates. Confirm: incrementally qualified cladding reaches higher burnups reliably. Kill: test reactor availability stalls the program. Does NOT claim: a universal fast cladding - it earns each burnup step with data.",
 "pointer": "The Signature system's proposed approach qualifies fast cladding incrementally in representative environments; the companion Signature Edition record specifies the armor protocol.",
 "key_points": [
  "Fast cladding faces 550-700 C liquid metal plus hundreds of dpa.",
  "Austenitics swell; ferritic-martensitics embrittle; ODS is hard to fabricate.",
  "Lead coolants corrode aggressively without oxygen control.",
  "Cladding lifetime sets fuel burnup and fast reactor economics.",
 ],
 "requirements": [
  "Coolant-specific fast-spectrum irradiation testing.",
  "Incremental burnup qualification earned by data.",
  "Swelling and embrittlement monitoring feeding lifetime estimates.",
 ],
 "citations": [
  "Ukai S, Fujiwara M (2002) Perspective of ODS alloys application in nuclear environments. J. Nuclear Materials 307-311.",
 ],
 "demo": {"half_life": 13.0, "n0": 7e5},
},
# ----------------------------------------------------------------- rank 22
{
 "key": "ne-tritium-breeding",
 "name": "The Fusion Tritium Breeding Problem",
 "group": "Fusion Energy",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Fusion reactors burn tritium that barely exists in nature - can breeding blankets make enough to sustain the fuel cycle, and what tritium breeding ratio is truly needed?",
 "background": "Deuterium-tritium fusion consumes tritium; the world's inventory is kilograms (from CANDU reactors), while a power plant burns kilograms per day. Breeding blankets - lithium-bearing structures around the plasma - must breed more tritium than burned: a tritium breeding ratio (TBR) above 1, with margin for losses, decay (5.5 percent per year), and startup inventory. But TBR cannot be measured until a burning plasma device with a full blanket exists - ITER will test modules, not the full cycle. Neutronics calculations predict TBR with uncertainties from nuclear data and geometry; tritium extraction, permeation, and accountancy add engineering unknowns. The closed tritium cycle is unproven at any scale.",
 "why_it_matters": "No tritium, no fusion power: the fuel cycle must breed its own fuel from the first day. An unclosed cycle is a plant that eats its seed corn.",
 "sig_lens": "The Signature lens reads tritium as a currency that must be minted: the protocol must audit every gram bred, burned, lost, and decayed.",
 "sig_solution": LABEL + " Assumptions: (1) TBR cannot be measured before a full-blanket burning device; (2) tritium losses and decay are first-order. Reasoning path: design for margin and audit relentlessly - require calculated TBR well above 1, then measure every tritium account the moment testing allows. Proposed mechanism: a mint-audit protocol requiring TBR margin analysis with nuclear-data uncertainties, tritium accountancy systems designed into blankets from the start, and staged validation (neutronics benchmarks, then module tests, then full-cycle demonstration). Confirm: staged validation converges calculated and measured breeding. Kill: nuclear data uncertainties prove irreducible and margins stay guesswork. Does NOT claim: a closed tritium cycle demonstrated - it audits toward one in stages.",
 "pointer": "The Signature system's proposed approach audits the tritium cycle in staged validation toward closure; the companion Signature Edition record specifies the mint-audit protocol.",
 "key_points": [
  "World tritium inventory is kilograms; a plant burns kilograms per day.",
  "TBR above 1 with margin is required; it cannot yet be measured.",
  "Tritium decays at 5.5 percent per year; losses compound.",
  "The closed tritium fuel cycle is unproven at any scale.",
 ],
 "requirements": [
  "TBR margin analysis with nuclear-data uncertainties.",
  "Tritium accountancy designed into blankets from the start.",
  "Staged validation: benchmarks, modules, full-cycle demonstration.",
 ],
 "citations": [
  "Abdou M et al. (2021) Blanket/first wall challenges and required R&D. Nuclear Fusion 61(1).",
 ],
 "demo": {"half_life": 4.2, "n0": 3.5e6},
},
# ----------------------------------------------------------------- rank 23
{
 "key": "ne-first-wall",
 "name": "The Fusion First Wall Materials Problem",
 "group": "Fusion Energy",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "The first wall faces 14 MeV neutrons, megawatt heat fluxes, and plasma erosion simultaneously - does any material survive a power plant's lifetime?",
 "background": "Fusion's 14 MeV neutrons are uniquely damaging - far above fission spectra - displacing atoms and transmuting elements (helium embrittlement) at rates no current material is qualified for. Tungsten armor handles heat but embrittles; reduced-activation steels (EUROFER) have data only to fission-relevant doses; silicon carbide composites promise much and deliver brittleness. The testing gap is fundamental: no facility reproduces the fusion neutron spectrum at power-plant fluence (IFMIF/DONES is planned, not operating). Materials qualification for fusion is thus extrapolation from fission data and ion beams - educated guessing at the core of the reactor's lifetime.",
 "why_it_matters": "The first wall is the fusion reactor's consumable: if it must be replaced every two years, the plant's economics and availability collapse.",
 "sig_lens": "The Signature lens reads the first wall as a shield against an untestable storm: the protocol must bound the damage with every available surrogate and never promise what the tests cannot show.",
 "sig_solution": LABEL + " Assumptions: (1) no facility reproduces fusion-spectrum damage at plant fluence; (2) extrapolation from fission data is uncertain. Reasoning path: bound the damage with multiple surrogates (ion irradiation, fission neutrons, modeling), design for replaceability, and qualify in stages as facilities come online. Proposed mechanism: a shield protocol requiring multi-surrogate damage assessment, first-wall designs with planned replacement intervals, and staged re-qualification as fusion-spectrum facilities (IFMIF/DONES) deliver data. Confirm: staged re-qualification converges lifetime estimates. Kill: the surrogates miss fusion-specific damage modes entirely. Does NOT claim: qualified fusion first-wall materials - it bounds the storm with honest extrapolation.",
 "pointer": "The Signature system's proposed approach bounds first-wall damage with multi-surrogate assessment and staged re-qualification; the companion Signature Edition record specifies the shield protocol.",
 "key_points": [
  "14 MeV neutrons damage materials far beyond fission spectra.",
  "Helium transmutation embrittles; no material is qualified at plant fluence.",
  "Tungsten, EUROFER, and SiC each have disqualifying weaknesses.",
  "No operating facility reproduces the fusion neutron spectrum at scale.",
 ],
 "requirements": [
  "Multi-surrogate damage assessment (ions, fission neutrons, modeling).",
  "Replaceable first-wall designs with planned intervals.",
  "Staged re-qualification as fusion-spectrum facilities deliver data.",
 ],
 "citations": [
  "Zinkle SJ, Busby JT (2009) Structural materials for fission and fusion energy. Materials Today 12(11).",
 ],
 "demo": {"half_life": 6.8, "n0": 2.8e6},
},
# ----------------------------------------------------------------- rank 24
{
 "key": "ne-disruption",
 "name": "The Tokamak Disruption Prediction Problem",
 "group": "Fusion Energy",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Tokamak disruptions - sudden losses of plasma confinement - can melt walls with electromagnetic and thermal loads, so can they be predicted in time to mitigate?",
 "background": "A major disruption dumps megajoules of plasma energy and drives mega-ampere currents into the vessel in milliseconds: ITER's disruption loads are a design driver, and an unmitigated disruption could damage the machine. Prediction uses MHD stability analysis and, increasingly, machine learning on multi-machine databases - but the warning time needed (tens of milliseconds for massive gas injection) strains every method, false positives waste pulses, and the physics of the thermal quench is incompletely understood. Disruption mitigation (shattered pellet injection) is proven in principle; the prediction-mitigation loop at ITER scale is unproven.",
 "why_it_matters": "One unmitigated disruption at ITER scale could end the experimental program. Prediction is the trigger; mitigation is the shield; both must work the first time.",
 "sig_lens": "The Signature lens reads disruptions as earthquakes: the protocol cannot prevent them, but must give the warning that triggers the mitigation.",
 "sig_solution": LABEL + " Assumptions: (1) warning times of tens of milliseconds strain all methods; (2) false positives waste expensive pulses. Reasoning path: fuse physics stability analysis with ML predictors, and trigger mitigation on the fused alarm with false-positive budgeting. Proposed mechanism: an earthquake protocol combining MHD stability monitors with cross-machine ML predictors, firing shattered-pellet mitigation on fused alarms, and tracking the false-positive versus missed-disruption tradeoff explicitly. Confirm: fused predictors beat either alone on multi-machine databases. Kill: the warning time proves insufficient for mitigation at scale. Does NOT claim: disruption prevention - it buys the warning that triggers the shield.",
 "pointer": "The Signature system's proposed approach fuses physics and ML disruption predictors with budgeted false positives; the companion Signature Edition record specifies the earthquake protocol.",
 "key_points": [
  "Disruptions dump plasma energy and drive vessel currents in milliseconds.",
  "ITER-scale unmitigated disruptions could damage the machine.",
  "Warning times of tens of milliseconds strain prediction methods.",
  "Shattered pellet mitigation is proven in principle, unproven at scale.",
 ],
 "requirements": [
  "Fused physics-plus-ML disruption predictors.",
  "False-positive budgets balancing wasted pulses against missed disruptions.",
  "Mitigation triggering on fused alarms with measured latency.",
 ],
 "citations": [
  "Hender TC et al. (2007) Progress in the ITER Physics Basis: disruptions. Nuclear Fusion 47(6).",
 ],
 "demo": {"half_life": 3.8, "n0": 4.2e6},
},
# ----------------------------------------------------------------- rank 25
{
 "key": "ne-stellarator",
 "name": "The Stellarator Optimization Problem",
 "group": "Fusion Energy",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Stellarators confine plasma with 3D magnetic coils, avoiding disruptions - but can the fiendishly complex coil shapes be optimized for a power plant?",
 "background": "Stellarators trade the tokamak's disruption risk for geometric complexity: the magnetic field must be sculpted in three dimensions by non-planar coils positioned to millimeter precision. Wendelstein 7-X proved the optimized stellarator concept works, but power-plant optimization spans neoclassical transport, MHD stability, fast-particle confinement, and coil manufacturability - a multi-objective nightmare in a huge design space. The coil complexity drives cost: each coil is a unique 3D superconducting sculpture. Whether an economically buildable optimized stellarator exists is unproven - the physics works, the engineering economics are open.",
 "why_it_matters": "Stellarators may be fusion's disruption-free path to power. But a reactor that works physically and bankrupts economically is not a power plant.",
 "sig_lens": "The Signature lens reads the stellarator as a sculpture that must also be a machine: the protocol must optimize the physics and the manufacturability together, not in sequence.",
 "sig_solution": LABEL + " Assumptions: (1) coil complexity drives stellarator cost; (2) physics optimization alone produces unbuildable designs. Reasoning path: optimize jointly - include coil manufacturability and cost in the objective from the start, not as an afterthought. Proposed mechanism: a sculpture protocol with multi-objective optimization spanning plasma performance and coil simplicity metrics, manufacturing trials of candidate coil shapes feeding back into the optimizer, and cost estimates updated per design iteration. Confirm: jointly optimized designs show better cost-performance than physics-first ones. Kill: the objectives prove irreconcilable and every design is either unbuildable or underperforming. Does NOT claim: an economical stellarator design - it searches the joint space honestly.",
 "pointer": "The Signature system's proposed approach optimizes stellarators jointly for physics and coil manufacturability; the companion Signature Edition record specifies the sculpture protocol.",
 "key_points": [
  "Stellarators avoid disruptions via 3D coil-shaped magnetic fields.",
  "Wendelstein 7-X proved the optimized concept works.",
  "Coil shapes need millimeter precision; each is a unique sculpture.",
  "Economic buildability of an optimized stellarator is unproven.",
 ],
 "requirements": [
  "Joint physics-manufacturability multi-objective optimization.",
  "Manufacturing trials feeding back into the optimizer.",
  "Per-iteration cost estimates on candidate designs.",
 ],
 "citations": [
  "Helander P et al. (2012) Stellarator and tokamak plasmas: a comparison. Plasma Phys. Control. Fusion 54(12).",
 ],
 "demo": {"half_life": 7.2, "n0": 3.3e6},
},
# ----------------------------------------------------------------- rank 26
{
 "key": "ne-icf-gain",
 "name": "The Inertial Confinement Ignition Gain Problem",
 "group": "Fusion Energy",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "NIF achieved ignition in 2022 - but can inertial confinement reach the engineering gain needed for power, and what stands between physics breakeven and a power plant?",
 "background": "The National Ignition Facility's December 2022 shot produced more fusion energy than laser energy delivered to the target - scientific breakeven, a historic milestone. But engineering gain (electricity out versus electricity in) needs roughly 100x more: laser efficiency is under 1 percent, target fabrication must go from handcrafted to mass-produced, and the repetition rate must rise from shots-per-day to ten per second. The physics challenges continue too: hydrodynamic instabilities (Rayleigh-Taylor) limit capsule performance, and the ignition margin is thin. Whether ICF can traverse from physics demonstration to power plant is the field's defining open question.",
 "why_it_matters": "NIF proved the physics; the engineering gap is roughly two orders of magnitude. ICF power needs targets, lasers, and repetition rates that do not yet exist.",
 "sig_lens": "The Signature lens reads ignition as the first step of a long staircase: the protocol must price every remaining step, not celebrate the first one as the summit.",
 "sig_solution": LABEL + " Assumptions: (1) scientific breakeven is ~1 percent of engineering breakeven; (2) target fabrication and rep-rate are manufacturing problems, not physics ones. Reasoning path: decompose the gain gap - laser efficiency, target cost, rep-rate, chamber survival - and attack each with its own development program and metrics. Proposed mechanism: a staircase protocol tracking the five gain-gap factors separately with quantitative milestones, funding each factor's program against its milestone progress, and requiring integrated power-plant designs to close all five simultaneously. Confirm: factor-tracked programs show steadier progress than physics-only focus. Kill: one factor (e.g., target cost) proves fundamentally uneconomic. Does NOT claim: ICF power-plant viability - it prices the staircase honestly.",
 "pointer": "The Signature system's proposed approach decomposes the ICF gain gap into five tracked factors; the companion Signature Edition record specifies the staircase protocol.",
 "key_points": [
  "NIF 2022: first scientific breakeven (fusion out exceeded laser in).",
  "Engineering gain needs roughly 100x more; laser efficiency is under 1 percent.",
  "Targets are handcrafted; power needs mass production at 10 Hz.",
  "Hydrodynamic instabilities keep the ignition margin thin.",
 ],
 "requirements": [
  "Separate quantitative milestones for laser, target, rep-rate, chamber, physics.",
  "Per-factor funding gated on milestone progress.",
  "Integrated designs closing all five factors simultaneously.",
 ],
 "citations": [
  "Abu-Shawareb H et al. (2024) Achievement of target gain larger than unity. Physical Review Letters 132(6).",
 ],
 "demo": {"half_life": 5.8, "n0": 5.5e6},
},
# ----------------------------------------------------------------- rank 27
{
 "key": "ne-transmutation",
 "name": "The Nuclear Waste Transmutation Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Can long-lived nuclear waste be transmuted into shorter-lived isotopes - and does the transmutation cure cost more than the disease?",
 "background": "Partitioning and transmutation (P&T) proposes separating minor actinides (neptunium, americium, curium) from spent fuel and fissioning them in fast reactors or accelerator-driven systems, reducing waste lifetimes from hundreds of millennia to centuries. The physics works; the systems analysis is damning: multiple studies (OECD/NEA) find P&T reduces repository burden modestly while multiplying fuel-cycle complexity, cost, and its own waste streams. The separation chemistry is hard, the fast reactors to burn the actinides barely exist, and the net benefit depends on repository assumptions centuries out. Whether P&T is worth doing remains contested after decades of study.",
 "why_it_matters": "Waste lifetimes of 100,000 years strain institutional credibility. Transmutation promises to shrink the problem - if the cure is not worse than the disease.",
 "sig_lens": "The Signature lens reads transmutation as refinancing a long debt: the protocol must show the total cost of the refinancing, not just the shorter term.",
 "sig_solution": LABEL + " Assumptions: (1) the physics of transmutation works; (2) the systems costs may exceed the benefits. Reasoning path: evaluate P&T on full system cost - separation, reactors, new waste streams, repository savings - with honest uncertainty, before building. Proposed mechanism: a refinancing protocol requiring full-fuel-cycle cost-benefit analysis with uncertainty bands, pilot-scale demonstration of the separation chemistry, and a decision gate comparing P&T against direct disposal on equal terms. Confirm: protocol-gated evaluations avoid the cost overruns of premature commitment. Kill: the analysis uncertainties prove too wide for any decision. Does NOT claim: that transmutation is or is not worthwhile - it prices the refinancing completely.",
 "pointer": "The Signature system's proposed approach evaluates transmutation on full system cost with uncertainty; the companion Signature Edition record specifies the refinancing protocol.",
 "key_points": [
  "P&T would fission minor actinides, cutting waste lifetimes to centuries.",
  "OECD/NEA studies find modest repository benefit at large system cost.",
  "Separation chemistry is hard; burner reactors barely exist.",
  "Net benefit hinges on repository assumptions centuries out.",
 ],
 "requirements": [
  "Full-fuel-cycle cost-benefit with uncertainty bands.",
  "Pilot-scale separation chemistry demonstration.",
  "Equal-terms decision gates against direct disposal.",
 ],
 "citations": [
  "OECD/NEA (2002) Accelerator-driven Systems (ADS) and Fast Reactors in Advanced Nuclear Fuel Cycles.",
 ],
 "demo": {"half_life": 11.5, "n0": 1.6e6},
},
# ----------------------------------------------------------------- rank 28
{
 "key": "ne-repository",
 "name": "The Deep Geological Repository Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Can engineered and geological barriers isolate waste for 100,000 years - and how can safety be demonstrated over timescales no institution has ever managed?",
 "background": "Deep geological disposal - waste in engineered canisters, buried in stable rock - is the international scientific consensus (Finland's Onkalo is the first operating facility), but the demonstration problem is philosophical as much as technical: safety cases must argue over 100,000-year timescales using models of geology, climate, and human intrusion that cannot be validated. Copper canister corrosion, bentonite buffer evolution, and glacial-cycle effects each carry uncertainties. The social dimension is harder: no community wants the repository, and the ethics of imposing risks on distant future generations are debated. The technical consensus coexists with political paralysis almost everywhere.",
 "why_it_matters": "Without repositories, waste accumulates at reactor sites indefinitely - the de facto policy of most nuclear nations. The 100,000-year safety case is the credibility of the entire enterprise.",
 "sig_lens": "The Signature lens reads the repository as a promise to the distant future: the protocol must make the promise in layers, each independently credible, and never ask one layer to carry the whole vow.",
 "sig_solution": LABEL + " Assumptions: (1) 100,000-year predictions cannot be validated; (2) social acceptance is the binding constraint. Reasoning path: build safety in defense-in-depth layers (waste form, canister, buffer, geology), argue each layer's performance over its credible timescale, and earn social license through reversibility and consent. Proposed mechanism: a layered-vow protocol with independent safety arguments per barrier, staged repository development (reversible phases before closure), and consent-based siting with community veto rights. Confirm: layered, staged, consent-based programs advance where imposed ones stall. Kill: no community consents and the technical case is moot. Does NOT claim: proven 100,000-year safety - it builds credible layers and earns the social license.",
 "pointer": "The Signature system's proposed approach builds repository safety in independently argued layers with consent-based siting; the companion Signature Edition record specifies the layered-vow protocol.",
 "key_points": [
  "Deep geological disposal is the international scientific consensus.",
  "Finland's Onkalo is the first operating facility; most nations are stalled.",
  "100,000-year safety cases cannot be validated, only argued.",
  "Social acceptance, not technology, is the binding constraint.",
 ],
 "requirements": [
  "Independent safety arguments per barrier layer.",
  "Staged development with reversibility before closure.",
  "Consent-based siting with community veto rights.",
 ],
 "citations": [
  "OECD/NEA (2020) Management of Radioactive Waste: Geological Disposal.",
 ],
 "demo": {"half_life": 16.0, "n0": 6e5},
},
# ----------------------------------------------------------------- rank 29
{
 "key": "ne-microreactor",
 "name": "The Microreactor Autonomous Control Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Microreactors promise power for remote sites with minimal staffing - but can a reactor be trusted to control itself safely with no operators present?",
 "background": "Microreactors (1-20 MWe, transportable, multi-year fuel) target remote communities, mines, and military bases - places with no nuclear workforce. The designs lean on inherent safety (TRISO fuel, heat pipes, negative feedbacks) plus autonomous control: load-following, fault detection, and even startup/shutdown without operators. But autonomous nuclear control has no licensing precedent: regulators license operators, procedures, and organizations, not algorithms. The verification problem - proving the autonomous controller handles the scenarios it was not explicitly programmed for - is unsolved, and cybersecurity for an unstaffed reactor is a new threat surface. The technology is ready before the assurance case.",
 "why_it_matters": "Autonomous microreactors could electrify the remote world - or become unstaffed targets. The assurance case must precede the deployment, not follow it.",
 "sig_lens": "The Signature lens reads autonomy as a pilot who never sleeps: the protocol must prove the pilot's judgment across the scenarios, including the ones nobody scripted.",
 "sig_solution": LABEL + " Assumptions: (1) regulators license organizations, not algorithms; (2) verification of unscripted scenarios is unsolved. Reasoning path: bound the autonomy - give the controller a verified safe envelope and independent hard-wired protection that needs no software. Proposed mechanism: an envelope protocol with a formally verified safe operating envelope, diverse hard-wired protection independent of the autonomous controller, extensive fault-injection testing, and remote human oversight with defined intervention authority. Confirm: envelope-bounded autonomy passes fault-injection campaigns. Kill: the envelope proves too restrictive for useful operation. Does NOT claim: verified autonomous nuclear control - it bounds the pilot and keeps the independent brakes.",
 "pointer": "The Signature system's proposed approach bounds microreactor autonomy in verified envelopes with independent protection; the companion Signature Edition record specifies the envelope protocol.",
 "key_points": [
  "Microreactors target remote sites with no nuclear workforce.",
  "Designs rely on inherent safety plus autonomous control.",
  "No licensing precedent exists for operator-free reactors.",
  "Verification for unscripted scenarios is unsolved.",
 ],
 "requirements": [
  "Formally verified safe operating envelopes.",
  "Diverse hard-wired protection independent of autonomy software.",
  "Fault-injection campaigns plus remote human oversight.",
 ],
 "citations": [
  "US DOE Microreactor Program documentation.",
 ],
 "demo": {"half_life": 4.8, "n0": 7.5e6},
},
# ----------------------------------------------------------------- rank 30
{
 "key": "ne-space-heat",
 "name": "The Space Reactor Heat Rejection Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Space reactors must reject waste heat by radiation alone - but radiators are heavy, huge, and vulnerable, so how can the heat rejection problem be solved for real missions?",
 "background": "In space there is no air or water for cooling: waste heat leaves only by thermal radiation, requiring enormous radiator areas (a megawatt-electric reactor needs thousands of square meters). Radiators dominate the mass budget, are vulnerable to micrometeorites, and their deployment mechanisms are failure-prone. High-temperature operation helps (radiation scales as T^4), which is why space reactors favor refractory materials and Brayton cycles - but high temperature compounds every materials problem. Historical systems (Soviet RORSATs, US SNAP-10A) were small; the megawatt-class systems needed for propulsion or surface power face a heat-rejection wall that no flight program has yet climbed.",
 "why_it_matters": "Nuclear propulsion and lunar surface power both need megawatt-class space reactors. Heat rejection is the mass that eats the mission.",
 "sig_lens": "The Signature lens reads radiators as the mission's skin: the protocol must size the skin for the worst heat, armor it against the environment, and never promise cooling it cannot radiate.",
 "sig_solution": LABEL + " Assumptions: (1) radiation-only cooling sets hard area requirements; (2) radiators dominate mass and vulnerability. Reasoning path: design the power conversion for maximum rejection temperature, segment radiators for damage tolerance, and verify deployment reliability by test. Proposed mechanism: a skin protocol optimizing cycle temperature against materials limits, using segmented redundant radiator panels with micrometeorite-tolerant design, and full-scale deployment testing. Confirm: protocol-designed systems meet mass budgets with margin. Kill: the temperature-materials tradeoff proves irreconcilable at mission power. Does NOT claim: a solved megawatt space reactor - it sizes the skin honestly.",
 "pointer": "The Signature system's proposed approach optimizes space reactors for rejection temperature with segmented radiators; the companion Signature Edition record specifies the skin protocol.",
 "key_points": [
  "Space heat rejection is radiation-only: enormous areas required.",
  "Radiators dominate mass budgets and are micrometeorite-vulnerable.",
  "High-temperature operation helps (T^4) but compounds materials problems.",
  "No megawatt-class system has yet flown.",
 ],
 "requirements": [
  "Cycle-temperature optimization against materials limits.",
  "Segmented redundant radiator panels.",
  "Full-scale deployment mechanism testing.",
 ],
 "citations": [
  "El-Genk MS (2008) Space nuclear reactor power system concepts. AIP Conference Proceedings.",
 ],
 "demo": {"half_life": 6.2, "n0": 9.5e6},
},
# ----------------------------------------------------------------- rank 31
{
 "key": "ne-multiphysics",
 "name": "The Multiphysics Reactor Coupling Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Neutronics, thermal hydraulics, fuel performance, and chemistry all couple in a reactor - but how can the coupled system be simulated with quantified uncertainty?",
 "background": "Modern reactor analysis couples neutron transport, thermal hydraulics, fuel thermomechanics, and sometimes chemistry - the multiphysics vision pursued by DOE's CASL and NEAMS programs. The coupling is where the physics lives (power shapes temperature shapes power), but also where the uncertainties compound: each physics module carries its own approximations, and the coupled uncertainty is not the sum of parts. Verification of coupled codes lags single-physics verification, validation data for coupled effects is sparse, and the computational cost forces coarse coupling that may miss the feedbacks that matter. The dream is a predictive virtual reactor; the reality is coupled codes with unquantified coupled uncertainty.",
 "why_it_matters": "Safety margins are set by coupled phenomena. Unquantified coupled uncertainty means the margins rest on hope where the physics couples most strongly.",
 "sig_lens": "The Signature lens reads coupling as conversation: the protocol must verify each speaker and measure how the conversation changes the message.",
 "sig_solution": LABEL + " Assumptions: (1) coupled uncertainty compounds beyond single-physics bands; (2) validation data for coupled effects is sparse. Reasoning path: verify each physics module separately, then validate the coupled system on integral experiments, propagating uncertainties through the coupling explicitly. Proposed mechanism: a conversation protocol with single-physics verification baselines, coupled uncertainty propagation (not just stacking), and validation against integral tests with the coupled uncertainty reported. Confirm: protocol-coupled analyses match integral experiments within stated bands. Kill: the coupled uncertainties prove too wide for licensing use. Does NOT claim: a predictive virtual reactor - it quantifies the conversation's uncertainty.",
 "pointer": "The Signature system's proposed approach propagates uncertainties explicitly through multiphysics coupling; the companion Signature Edition record specifies the conversation protocol.",
 "key_points": [
  "Reactor physics couples neutronics, thermal hydraulics, fuel, and chemistry.",
  "Coupled uncertainty compounds beyond single-physics bands.",
  "Coupled-code verification lags single-physics verification.",
  "CASL/NEAMS pursue the virtual reactor; coupled uncertainty is unquantified.",
 ],
 "requirements": [
  "Single-physics verification baselines per module.",
  "Explicit coupled uncertainty propagation.",
  "Integral-experiment validation with reported coupled bands.",
 ],
 "citations": [
  "US DOE CASL (Consortium for Advanced Simulation of LWRs) documentation.",
 ],
 "demo": {"half_life": 8.8, "n0": 4.8e6},
},
# ----------------------------------------------------------------- rank 32
{
 "key": "ne-transport",
 "name": "The Neutron Transport Exact Solution Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "The Boltzmann transport equation governs neutrons exactly - but can it be solved accurately enough for design without the approximations that define the field?",
 "background": "Neutron transport - the linear Boltzmann equation in 7 dimensions (space, angle, energy, time) - is solved in practice by approximations: diffusion theory (fast, wrong near boundaries), discrete ordinates (Sn, ray effects), Monte Carlo (exact in the limit, slow to converge). Each approximation has known failure modes, and the choice among them is expertise, not science. High-fidelity Monte Carlo (OpenMC, Serpent) is increasingly the reference, but its convergence for full-core depletion with thermal feedback is slow, and the nuclear data uncertainties feeding it are themselves significant. The exact solution remains computationally unreachable; the approximation-error quantification is the open problem.",
 "why_it_matters": "Every reactor calculation is a transport approximation. Unquantified approximation error is unquantified design margin.",
 "sig_lens": "The Signature lens reads transport approximations as lenses with known distortions: the protocol must calibrate each lens and never trust the view beyond the calibration.",
 "sig_solution": LABEL + " Assumptions: (1) exact 7D transport is computationally unreachable; (2) each approximation has known failure modes. Reasoning path: calibrate approximations against high-fidelity Monte Carlo references on representative problems, and carry the calibration error into design margins. Proposed mechanism: a lens protocol requiring approximation benchmarking against Monte Carlo references, error models per approximation per problem class, and design margins that include the approximation error explicitly. Confirm: calibrated approximations match reference solutions within stated errors. Kill: the reference calculations prove too slow for the needed coverage. Does NOT claim: exact transport solutions - it calibrates the lenses and prices their distortion.",
 "pointer": "The Signature system's proposed approach benchmarks transport approximations against Monte Carlo references; the companion Signature Edition record specifies the lens protocol.",
 "key_points": [
  "The transport equation is 7D; exact solution is unreachable.",
  "Diffusion, Sn, and Monte Carlo each have known failure modes.",
  "Approximation choice is expertise, not quantified science.",
  "Nuclear data uncertainties compound the approximation errors.",
 ],
 "requirements": [
  "Monte Carlo reference benchmarks per problem class.",
  "Per-approximation error models from benchmarking.",
  "Design margins including approximation error explicitly.",
 ],
 "citations": [
  "Lewis EE, Miller WF (1984) Computational Methods of Neutron Transport. ANS.",
 ],
 "demo": {"half_life": 12.5, "n0": 3.8e6},
},
# ----------------------------------------------------------------- rank 33
{
 "key": "ne-dry-cask",
 "name": "The Spent Fuel Dry Cask Storage Problem",
 "group": "Reactor Engineering",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Spent fuel sits in dry casks for decades awaiting repositories - but can the casks and fuel be shown safe for century-scale storage, including the fuel nobody can inspect?",
 "background": "With repositories delayed, dry cask storage - massive steel and concrete canisters, passively cooled - has become the de facto decades-long solution worldwide. The aging questions are open: chloride-induced stress corrosion cracking of stainless canisters (observed in marine environments), fuel cladding embrittlement from hydride reorientation during drying, and the inability to inspect sealed canisters' interiors. License renewals now extend toward a century, but the data covers decades at most. The retrievability requirement - fuel must remain transportable - adds a constraint the aging mechanisms threaten.",
 "why_it_matters": "Dry casks hold the nation's spent fuel at dozens of sites. Century-scale safety argued from decade-scale data is the industry's largest extrapolative bet.",
 "sig_lens": "The Signature lens reads dry casks as time capsules: the protocol must monitor what can be monitored, model what cannot, and never confuse the two.",
 "sig_solution": LABEL + " Assumptions: (1) sealed canisters cannot be internally inspected; (2) aging data covers decades, licenses approach a century. Reasoning path: build an aging management program on external monitoring plus representative demonstration casks that CAN be opened, and keep the safety case tied to measured aging. Proposed mechanism: a time-capsule protocol with external canister monitoring (temperature, dose, visual), periodic opening of demonstration casks to validate aging models, and license extensions gated on the demonstration results. Confirm: demonstration-cask findings track model predictions. Kill: the demonstration casks prove unrepresentative and the models drift. Does NOT claim: century-proven storage - it manages aging with openable witnesses.",
 "pointer": "The Signature system's proposed approach validates cask aging with openable demonstration casks; the companion Signature Edition record specifies the time-capsule protocol.",
 "key_points": [
  "Dry casks are the de facto decades-long storage solution worldwide.",
  "Chloride SCC of canisters and hydride embrittlement of cladding are open risks.",
  "Sealed canisters cannot be internally inspected.",
  "Licenses approach a century on decade-scale data.",
 ],
 "requirements": [
  "External canister monitoring programs.",
  "Openable demonstration casks validating aging models.",
  "License extensions gated on demonstration results.",
 ],
 "citations": [
  "US NRC NUREG-1927: Standard Review Plan for Renewal of Spent Fuel Dry Cask Storage System Licenses.",
 ],
 "demo": {"half_life": 14.5, "n0": 2.6e6},
},
# ----------------------------------------------------------------- rank 34
{
 "key": "ne-unified-system",
 "name": "The Unified Nuclear Energy System Problem",
 "group": "Fusion Energy",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Fission, fusion, fuel cycles, waste, and grids must work as one system - but can nuclear energy be designed as an integrated whole rather than a collection of parts?",
 "background": "Nuclear energy is developed in silos: fission vendors, fusion programs, waste agencies, and grid operators barely coordinate. But the system questions cross every boundary: should fast reactors burn the waste that repositories must otherwise hold for millennia? Can fusion-fission hybrids bridge the fuel cycle? How do reactors, renewables, and storage co-optimize on a decarbonized grid? The integrated assessment - optimizing the nuclear system as a whole across technologies and timescales - has no institutional home and no agreed methodology. Each part optimizes locally; the system-level optimum is nobody's job.",
 "why_it_matters": "The parts are maturing; the system is not designed. A century of nuclear energy decided part-by-part is a century of missed synergies and stranded assets.",
 "sig_lens": "The Signature lens reads the nuclear enterprise as one machine with many builders: the protocol must give the builders a shared blueprint, or accept the machine will never fit together.",
 "sig_solution": LABEL + " Assumptions: (1) institutional silos prevent system optimization; (2) no agreed system methodology exists. Reasoning path: build the shared blueprint first - an integrated system model spanning fission, fusion, fuel cycles, waste, and grids - and evaluate part-level decisions against it. Proposed mechanism: a blueprint protocol maintaining an open integrated nuclear-system model, requiring major program decisions to publish their system-level assessment, and convening cross-silo reviews of the blueprint's conclusions. Confirm: blueprint-assessed programs show better system-level outcomes. Kill: the silos ignore the blueprint and the model is academic. Does NOT claim: an optimized nuclear system - it builds the shared blueprint the builders lack.",
 "pointer": "The Signature system's proposed approach maintains an open integrated nuclear-system model for decision assessment; the companion Signature Edition record specifies the blueprint protocol.",
 "key_points": [
  "Fission, fusion, waste, and grids are developed in institutional silos.",
  "System questions (fast reactors burning waste, hybrids, grid co-optimization) cross all boundaries.",
  "No institutional home or methodology exists for integrated assessment.",
  "Part-level optima can be system-level mistakes.",
 ],
 "requirements": [
  "An open integrated nuclear-system model spanning all parts.",
  "System-level assessments published for major program decisions.",
  "Cross-silo reviews of blueprint conclusions.",
 ],
 "citations": [
  "MIT (2018) The Future of Nuclear Energy in a Carbon-Constrained World.",
 ],
 "demo": {"half_life": 10.5, "n0": 5.2e6},
},
]
