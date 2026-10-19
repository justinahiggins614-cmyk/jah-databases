#!/usr/bin/env python3
"""Entries for The Unsolved Environmental Engineering Database
(unsolved-environmental-engineering) and its Signature half
(unsolved-environmental-engineering-signature).

34 famous unsolved problems in environmental engineering, ladder-ordered by
accessibility (rank 1 = most approachable, rank 34 = most complex).
Public half: real, fact-checked problems. Signature half: the same 34
through the Signature lens, ALWAYS labeled as proposals, never established
science.

ID prefixes JAH-USVE- / JAH-USVES- verified free in manifest id_prefix
values (exact + substring, both directions).
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

FIELD = {
 "tag": "environmental-engineering",
 "disp": "environmental engineering",
 "name": "The Unsolved Environmental Engineering Database",
 "sig_name": "The Unsolved Environmental Engineering Signature Database",
 "prefix": "JAH-USVE-",
 "sig_prefix": "JAH-USVES-",
 "ai": "JAH Unsolved Environmental Engineering Archivist",
 "tagline": ("Thirty-four famous open problems in environmental engineering, from PFAS destruction to unified "
             "environmental systems: real, fact-checked, each with its full story and a clearly labeled "
             "Signature proposed solution."),
 "sig_tagline": ("His original Signature solution method applied to all 34 great open problems of environmental "
                 "engineering: Signature-generated proposed solutions with assumptions declared, confirm and "
                 "refute conditions stated, and limits honestly marked. Clearly labeled Signature-made, "
                 "never established science."),
 "pub_line": ("Public records - 34 famous open problems in environmental engineering, real and fact-checked: "
              "PFAS destruction, microplastic removal, pharmaceutical contaminants, algal bloom prediction, "
              "disinfection byproducts, lead service lines, distribution biofilms, stormwater treatment, "
              "combined sewer overflows, membrane fouling, and desalination brine - every record carrying the "
              "problem statement, background, why it matters, key points, requirements, standards, citations, "
              "and a working solution-explorer demonstration, organized in the Signature system."),
 "sig_line": ("Signature originals - his original Signature solution method: the same 34 famous unsolved "
              "environmental engineering problems approached as a covenant between the known and the unknown, "
              "each carrying the full Signature-generated proposed solution with its assumptions declared, its "
              "confirm and refute conditions stated, and its limits honestly marked. Clearly labeled "
              "Signature-made, never presented as established science or authentic public record."),
 "ladder_text": (" Records are ordered by the teaching ladder: Foundations (PFAS destruction, microplastic "
                 "removal, pharmaceutical contaminants, algal blooms, disinfection byproducts, lead lines, "
                 "biofilms, stormwater, sewer overflows, membrane fouling, desalination brine) -> Compounded "
                 "(antibiotic resistance, nutrient recovery, desalination energy, oxidation byproducts, urban "
                 "heat islands, source apportionment, indoor air, mixed-contaminant soil, brownfields, landfill "
                 "leachate, landfill gas, e-waste) -> Advanced (plastic circularity, construction waste, life "
                 "cycle uncertainty, carbon allocation, environmental justice, climate adaptation, nature-based "
                 "solutions, ultrafine particulates, VOC removal, contaminated sediments, unified environmental "
                 "systems)."),
 "search_ph": ("Search PFAS, microplastics, desalination, algal blooms, lead, stormwater, air quality, brownfields, "
               "landfill, e-waste, environmental justice..."),
 "chat_ph": "Ask about the great open problems of environmental engineering...",
 "greet_pub": ("I am the JAH Unsolved Environmental Engineering Archivist. Ask me about the great open problems "
               "of environmental engineering - from PFAS, microplastics, and desalination through air quality, "
               "brownfields, and e-waste, to environmental justice and unified environmental systems."),
 "greet_sig": ("I am the JAH Unsolved Environmental Engineering Archivist (Signature). Ask me about the Signature "
               "proposed solutions to the great open problems of environmental engineering - every approach labeled "
               "as a proposal, never established science."),
 "role_pub": ("unsolved environmental engineering archivist - the great open problems of environmental "
              "engineering, from PFAS, microplastics, and desalination through air quality, brownfields, and "
              "e-waste, to environmental justice and unified environmental systems; teaches progressively along "
              "the ladder from foundations through compounded to advanced; answers from many angles - definition, "
              "example, analogy, application, history, math - using only archive data from this system"),
 "role_sig": ("unsolved environmental engineering archivist - Signature editions: his original Signature solution "
              "method applied to the 34 great open problems of environmental engineering, each carrying the full "
              "Signature-generated proposed solution, clearly labeled Signature-made and never presented as "
              "established science; teaches progressively along the ladder from foundations through compounded "
              "to advanced; answers from many angles - definition, example, analogy, application, history, math "
              "- using only archive data from this system"),
 "gen_desc": "Generate clearly-labeled unsolved environmental engineering studies. Seeded archive records are the authoritative entries.",
 "standards": [
  "Problem statements verified against the published literature; open status confirmed as of 2026.",
  "Quantitative claims cross-checked against standard references (Peavy, Rowe and Tchobanoglous, Environmental Engineering; Crittenden et al., Water Treatment).",
  "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
 ],
 "sig_tail": ("Signature editions carry the Signature system's proposed solution approaches to famous "
              "unsolved problems. Every solution is labeled a Signature-generated proposal, never "
              "established science, never peer-accepted, never proof."),
}

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "ee-pfas",
 "name": "The PFAS Destruction Problem",
 "group": "Water Treatment",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Per- and polyfluoroalkyl substances resist every natural breakdown - but how can the carbon-fluorine bond, among the strongest in chemistry, be broken at water-treatment scale?",
 "background": "PFAS - the forever chemicals in nonstick coatings, firefighting foam, and waterproofing - now contaminate water supplies globally; the carbon-fluorine bond resists heat, microbes, and oxidants. Treatment today mostly moves PFAS around: granular activated carbon and ion exchange capture them, then the spent media needs disposal or regeneration. Destruction technologies - electrochemical oxidation, supercritical water oxidation, plasma, UV-sulfite - work in labs but face energy costs, fluoride byproducts, and scale-up gaps. EPA's 2024 drinking-water standards (4 ppt for PFOA/PFOS) turned the science problem into a compliance emergency with no proven destruction workhorse.",
 "why_it_matters": "PFAS are in the blood of nearly everyone tested. Capture without destruction is postponement; the bond must be broken or the problem is inherited forever.",
 "sig_lens": "The Signature lens reads PFAS as a debt that cannot be refinanced: the protocol must destroy the bond, not move the molecule, and prove the destruction.",
 "sig_solution": LABEL + " Assumptions: (1) capture-only treatment postpones the problem; (2) destruction methods are lab-proven but unscaled. Reasoning path: pair capture with destruction - concentrate PFAS from water, then destroy the concentrate where energy-per-molecule is affordable. Proposed mechanism: a bond-breaking protocol combining high-efficiency capture (targeted sorbents) with concentrate destruction (electrochemical or supercritical), verified by fluoride mass balance proving mineralization. Confirm: paired systems show verified destruction at acceptable energy cost. Kill: destruction energy proves uneconomic at scale and capture remains postponement. Does NOT claim: a proven PFAS destruction workhorse - it pairs capture with verified destruction.",
 "pointer": "The Signature system's proposed approach pairs PFAS capture with verified concentrate destruction; the companion Signature Edition record specifies the bond-breaking protocol.",
 "key_points": [
  "The carbon-fluorine bond resists natural breakdown processes.",
  "Current treatment captures PFAS; spent media needs disposal.",
  "Destruction methods work in labs with energy and scale-up gaps.",
  "EPA 2024 standards (4 ppt PFOA/PFOS) created a compliance emergency.",
 ],
 "requirements": [
  "High-efficiency capture concentrating PFAS from water.",
  "Destruction verified by fluoride mass balance (mineralization proof).",
  "Energy-per-molecule accounting for the destruction step.",
 ],
 "citations": [
  "US EPA (2024) National Primary Drinking Water Regulation for PFAS.",
 ],
 "demo": {"cin": 120.0, "cout": 6.0, "k": 0.8, "t": 3.0},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "ee-microplastic",
 "name": "The Microplastic Removal Problem",
 "group": "Water Treatment",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Microplastics pervade water from wastewater to drinking water - but how can particles spanning six orders of magnitude be removed reliably, and measured honestly?",
 "background": "Microplastics (under 5 mm) and nanoplastics shed from textiles, tires, and packaging into every water stream; drinking-water plants remove much via coagulation and filtration, but the removal efficiency for the smallest fractions is poorly quantified - because measurement itself is the problem. Counting methods (FTIR, Raman) have size detection limits, recovery rates vary, and nanoplastics largely evade quantification. Treatment claims therefore rest on shaky measurement: you cannot prove removal of what you cannot count. Membrane processes remove more but foul faster and cost more.",
 "why_it_matters": "Microplastics are in drinking water worldwide. Unmeasurable removal is unmanageable pollution - the treatment gap hides inside the measurement gap.",
 "sig_lens": "The Signature lens reads microplastics as dust of many sizes: the protocol must count honestly before claiming to clean.",
 "sig_solution": LABEL + " Assumptions: (1) measurement limits define the problem; (2) removal claims exceed measurement capability. Reasoning path: standardize measurement first (size-fractionated recovery rates), then optimize treatment against the measured fractions. Proposed mechanism: a counting protocol requiring size-fractionated microplastic measurement with reported recovery rates, treatment trains optimized per size fraction, and removal claims bounded by the measurement limits. Confirm: fraction-optimized treatment shows verified removal across sizes. Kill: nanoplastics prove unmeasurable and the smallest fraction stays unknown. Does NOT claim: complete microplastic removal - it counts honestly and cleans what is counted.",
 "pointer": "The Signature system's proposed approach standardizes size-fractionated microplastic measurement before optimizing removal; the companion Signature Edition record specifies the counting protocol.",
 "key_points": [
  "Microplastics span six orders of magnitude in size.",
  "Measurement methods have size limits and variable recovery.",
  "Nanoplastics largely evade quantification.",
  "Removal claims exceed measurement capability.",
 ],
 "requirements": [
  "Size-fractionated measurement with reported recovery rates.",
  "Per-fraction treatment optimization.",
  "Removal claims bounded by measurement limits.",
 ],
 "citations": [
  "Koelmans AA et al. (2019) Microplastics in freshwaters and drinking water. Water Research 155.",
 ],
 "demo": {"cin": 85.0, "cout": 12.0, "k": 0.6, "t": 2.5},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "ee-pharma",
 "name": "The Pharmaceutical Contaminant Treatment Problem",
 "group": "Water Treatment",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Pharmaceuticals and personal-care products pass through wastewater plants into rivers - but how can hundreds of trace contaminants be removed without knowing which matter most?",
 "background": "Wastewater treatment was designed for organics and nutrients, not for the hundreds of pharmaceuticals, hormones, and personal-care chemicals now detected downstream: conventional plants remove 20-90 percent depending on the compound, and the rest feminizes fish, breeds resistance, and enters drinking water. Advanced treatment (ozone, activated carbon, membranes) removes more at higher cost, but the prioritization problem is unsolved - which of the hundreds of compounds drive ecological risk? Effect-based monitoring is emerging but unstandardized. Regulators watch lists grow faster than treatment budgets.",
 "why_it_matters": "Trace pharmaceuticals are restructuring aquatic ecosystems. Treatment upgrades cost billions; spending them on the wrong compounds wastes the investment.",
 "sig_lens": "The Signature lens reads trace contaminants as a crowd of suspects: the protocol must identify the ringleaders before arresting everyone.",
 "sig_solution": LABEL + " Assumptions: (1) hundreds of compounds, unknown risk ranking; (2) advanced treatment is expensive. Reasoning path: prioritize by effect - use bioassays to find which effluent fractions drive toxicity, then target treatment at those. Proposed mechanism: a ringleader protocol combining effect-directed analysis (fractionate effluent, test fractions) with targeted advanced treatment for the identified drivers, verified by downstream bioassays. Confirm: effect-targeted upgrades cut ecological risk per dollar better than blanket upgrades. Kill: mixture effects defeat the fractionation and the drivers stay hidden. Does NOT claim: a complete risk ranking - it finds the ringleaders measurably.",
 "pointer": "The Signature system's proposed approach prioritizes pharmaceutical treatment by effect-directed analysis; the companion Signature Edition record specifies the ringleader protocol.",
 "key_points": [
  "Conventional plants remove 20-90 percent of pharmaceuticals, compound-dependent.",
  "Hundreds of compounds detected; risk ranking unknown.",
  "Advanced treatment works but is expensive.",
  "Effect-based monitoring is emerging but unstandardized.",
 ],
 "requirements": [
  "Effect-directed analysis identifying toxicity drivers.",
  "Targeted advanced treatment for identified drivers.",
  "Downstream bioassay verification of risk reduction.",
 ],
 "citations": [
  "Luo Y et al. (2014) A review on the occurrence of micropollutants in the aquatic environment. STOTEN 473-474.",
 ],
 "demo": {"cin": 200.0, "cout": 25.0, "k": 0.7, "t": 4.0},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "ee-algal-bloom",
 "name": "The Algal Bloom Prediction Problem",
 "group": "Water Treatment",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Harmful algal blooms shut down drinking water for cities - but can they be predicted days ahead, and what triggers the toxin production that makes them dangerous?",
 "background": "Cyanobacterial blooms (Microcystis, Anabaena) produce microcystins and other toxins: Toledo's 2014 do-not-drink order (400,000 people) showed the stakes. Prediction couples nutrient loading, hydrology, temperature, and ecology; models exist but the toxin trigger is poorly understood - the same bloom may or may not produce toxin, and the switch is unmapped. Remote sensing detects blooms; forecasting their toxicity does not follow. Nutrient reduction (the Lake Erie phosphorus saga) works slowly against legacy loads. Drinking-water plants need days of warning; the science gives hours of detection.",
 "why_it_matters": "A toxic bloom is a city's water supply turned poison. Prediction buys treatment time; detection alone buys panic.",
 "sig_lens": "The Signature lens reads blooms as a loaded weapon: the protocol must watch the trigger (toxin production), not just the gun (the bloom).",
 "sig_solution": LABEL + " Assumptions: (1) bloom presence does not imply toxicity; (2) the toxin trigger is unmapped. Reasoning path: forecast toxicity, not just biomass - monitor the gene expression and conditions correlated with toxin production. Proposed mechanism: a trigger-watch protocol combining bloom forecasting (nutrients, temperature, hydrology) with toxin-gene monitoring and treatment-plant early warning tied to toxin risk, not cell counts. Confirm: trigger-watched systems give earlier effective warnings. Kill: the toxin switch proves unpredictable and warnings stay unreliable. Does NOT claim: bloom toxicity prediction solved - it watches the trigger measurably.",
 "pointer": "The Signature system's proposed approach forecasts algal toxicity via trigger monitoring; the companion Signature Edition record specifies the trigger-watch protocol.",
 "key_points": [
  "Toledo 2014: 400,000 people under do-not-drink orders from microcystins.",
  "Blooms may or may not produce toxin; the switch is unmapped.",
  "Remote sensing detects blooms, not toxicity.",
  "Nutrient reduction works slowly against legacy loads.",
 ],
 "requirements": [
  "Toxin-gene and toxin monitoring alongside bloom forecasting.",
  "Early-warning triggers tied to toxin risk, not cell counts.",
  "Treatment-plant response plans keyed to warning tiers.",
 ],
 "citations": [
  "Paerl HW, Paul VJ (2012) Climate change: links to global expansion of harmful cyanobacteria. Water Research 46(5).",
 ],
 "demo": {"cin": 150.0, "cout": 30.0, "k": 0.5, "t": 3.5},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "ee-dbp",
 "name": "The Disinfection Byproduct Minimization Problem",
 "group": "Water Treatment",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Disinfection kills pathogens but creates byproducts that may cause cancer - how can both risks be minimized when they pull in opposite directions?",
 "background": "Chlorination's triumph over waterborne disease created its own problem: trihalomethanes and haloacetic acids, regulated as probable carcinogens (EPA Stage 2 DBP Rule). The tradeoff is fundamental - less disinfectant means fewer byproducts but more pathogens - and the unregulated byproducts (haloacetonitriles, NDMA) may be more toxic than the regulated ones. Alternative disinfectants (chloramine, ozone, UV) shift the byproduct profile rather than eliminating it. The risk-risk tradeoff has no agreed optimum: the pathogen risk is acute and visible, the DBP risk chronic and statistical.",
 "why_it_matters": "Every chlorinated water system navigates this tradeoff daily. Optimizing one risk while ignoring the other is not public health - it is risk transfer.",
 "sig_lens": "The Signature lens reads disinfection as a balance with two pans: the protocol must weigh the pathogen pan against the byproduct pan explicitly.",
 "sig_solution": LABEL + " Assumptions: (1) the pathogen-DBP tradeoff is fundamental; (2) unregulated byproducts may dominate toxicity. Reasoning path: optimize the total health risk - model pathogen and DBP risks jointly and find the operating point minimizing their sum. Proposed mechanism: a balance protocol with quantitative microbial risk assessment plus DBP toxicity modeling (including unregulated species), multi-objective optimization of disinfectant type and dose, and monitoring of both risk pans. Confirm: jointly optimized systems show lower total risk estimates. Kill: the toxicity models prove too uncertain to optimize on. Does NOT claim: a risk-free disinfectant - it balances the pans explicitly.",
 "pointer": "The Signature system's proposed approach jointly optimizes pathogen and byproduct risks; the companion Signature Edition record specifies the balance protocol.",
 "key_points": [
  "DBPs (THMs, HAAs) are regulated as probable carcinogens.",
  "Less disinfectant means fewer byproducts but more pathogens.",
  "Unregulated byproducts may be more toxic than regulated ones.",
  "Alternative disinfectants shift profiles rather than eliminating risk.",
 ],
 "requirements": [
  "Joint pathogen-plus-DBP quantitative risk modeling.",
  "Multi-objective disinfectant optimization.",
  "Monitoring of both regulated and unregulated byproducts.",
 ],
 "citations": [
  "US EPA Stage 2 Disinfectants and Disinfection Byproducts Rule.",
 ],
 "demo": {"cin": 90.0, "cout": 8.0, "k": 0.9, "t": 2.0},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "ee-lead-lines",
 "name": "The Lead Service Line Replacement Problem",
 "group": "Water Treatment",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Millions of lead service lines still deliver drinking water - but how can they all be found and replaced when records are missing and the money is short?",
 "background": "Flint made lead service lines infamous: an estimated 9 million remain in the US, and the EPA's 2024 Lead and Copper Rule Improvements mandate replacement within a decade. But utilities do not know where the lines are - records are paper, lost, or never existed - and verification means digging. Replacement prioritization (which neighborhoods first) is an environmental justice question: the lines concentrate in poor and minority communities. Partial replacements can spike lead levels by disturbing pipes. The inventory, prioritization, and funding problems are unsolved at national scale.",
 "why_it_matters": "Lead damages children's brains irreversibly. Every year of delay is measured in IQ points across exposed children.",
 "sig_lens": "The Signature lens reads lead lines as buried hazards: the protocol must map them, prioritize the vulnerable, and replace completely - never partially.",
 "sig_solution": LABEL + " Assumptions: (1) line inventories are incomplete; (2) partial replacement can worsen exposure. Reasoning path: inventory aggressively (predictive modeling plus verification digs), prioritize by vulnerability, and replace full lines only. Proposed mechanism: a buried-hazard protocol with machine-learning line-material prediction from records, targeted verification, vulnerability-weighted replacement sequencing, and mandatory full (never partial) replacement. Confirm: protocol-driven programs replace more high-risk lines per dollar. Kill: prediction proves unreliable and verification digs bankrupt the program. Does NOT claim: a complete national inventory - it maps aggressively and replaces completely.",
 "pointer": "The Signature system's proposed approach inventories lead lines predictively and replaces by vulnerability; the companion Signature Edition record specifies the buried-hazard protocol.",
 "key_points": [
  "An estimated 9 million lead service lines remain in the US.",
  "EPA 2024 rules mandate replacement within a decade.",
  "Utility records are incomplete; verification requires digging.",
  "Partial replacements can spike lead exposure.",
 ],
 "requirements": [
  "Predictive line-material modeling with verification digs.",
  "Vulnerability-weighted replacement sequencing.",
  "Full-line replacement mandates; partial replacements prohibited.",
 ],
 "citations": [
  "US EPA (2024) Lead and Copper Rule Improvements.",
 ],
 "demo": {"cin": 60.0, "cout": 3.0, "k": 1.0, "t": 2.5},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "ee-biofilm",
 "name": "The Drinking Water Distribution Biofilm Problem",
 "group": "Water Treatment",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Pipes grow biofilms that shelter pathogens and corrode infrastructure - but how can the living pipe wall be managed when it cannot be seen?",
 "background": "Distribution-system biofilms - microbial communities on pipe walls - harbor opportunistic pathogens (Legionella, Mycobacterium), accelerate corrosion, and consume disinfectant residual: the water leaving the plant is not the water reaching the tap. Biofilm monitoring is indirect (heterotrophic plate counts, ATP), the ecology is complex, and disinfectant penetration into biofilms is poor. Flushing and disinfectant boosts manage symptoms; the underlying ecology is unmanaged. Premise plumbing (building pipes) adds stagnation zones where biofilms thrive - the Legionella problem is substantially a biofilm problem.",
 "why_it_matters": "Distribution biofilms are where treated water gets recontaminated. Legionella outbreaks trace substantially to biofilm ecology nobody manages.",
 "sig_lens": "The Signature lens reads biofilms as cities in the pipes: the protocol must govern the cities, not just poison the water flowing past.",
 "sig_solution": LABEL + " Assumptions: (1) biofilms shelter pathogens from disinfectants; (2) monitoring is indirect. Reasoning path: manage the pipe ecology - control nutrients and disinfectant residual jointly, and flush strategically. Proposed mechanism: a pipe-city protocol with biofilm monitoring (ATP, sequencing), nutrient limitation strategies, targeted flushing programs, and premise-plumbing guidance for stagnation control. Confirm: ecologically managed systems show lower opportunistic pathogen detection. Kill: the ecology proves unmanageable and interventions are cosmetic. Does NOT claim: biofilm elimination - it governs the cities measurably.",
 "pointer": "The Signature system's proposed approach manages distribution biofilm ecology jointly with disinfectant strategy; the companion Signature Edition record specifies the pipe-city protocol.",
 "key_points": [
  "Biofilms shelter Legionella and Mycobacterium from disinfectants.",
  "Biofilms accelerate corrosion and consume disinfectant residual.",
  "Monitoring is indirect; disinfectant penetration is poor.",
  "Premise plumbing stagnation zones amplify the problem.",
 ],
 "requirements": [
  "Biofilm monitoring via ATP and sequencing.",
  "Joint nutrient and disinfectant-residual management.",
  "Strategic flushing and premise-plumbing guidance.",
 ],
 "citations": [
  "Wingender J, Flemming HC (2011) Biofilms in drinking water. Water Research 45(18).",
 ],
 "demo": {"cin": 110.0, "cout": 15.0, "k": 0.55, "t": 3.0},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "ee-stormwater",
 "name": "The Stormwater Runoff Treatment Problem",
 "group": "Water Treatment",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Rain washes oil, metals, and trash off cities into waterways - but how can diffuse, episodic stormwater be treated when it arrives all at once and then not at all?",
 "background": "Stormwater is the largest unregulated water pollution source in many cities: first-flush flows carry the accumulated load of streets - hydrocarbons, heavy metals (tire wear is now known as a major microplastic and 6PPD-quinone source, lethal to salmon), nutrients, trash. Treatment must handle extreme flow variability: green infrastructure (bioswales, permeable pavement) treats small storms and bypasses large ones. The performance data is scattered, maintenance is neglected, and the regulatory framework (MS4 permits) manages programs, not outcomes. Climate change intensifies the storms the infrastructure was not designed for.",
 "why_it_matters": "Urban runoff is now the dominant water-quality problem in many watersheds. The first flush carries the city's accumulated filth straight to the river.",
 "sig_lens": "The Signature lens reads stormwater as a flash flood of pollution: the protocol must catch the first flush, which carries the load, and maintain what catches it.",
 "sig_solution": LABEL + " Assumptions: (1) first flush carries the load; (2) green infrastructure performance degrades without maintenance. Reasoning path: design for the first flush, monitor performance continuously, and maintain relentlessly. Proposed mechanism: a first-flush protocol sizing treatment for initial runoff volumes, with performance monitoring (influent/effluent sampling) and maintenance schedules tied to measured performance decline. Confirm: maintained first-flush systems meet load-reduction targets. Kill: maintenance proves unfundable and systems degrade. Does NOT claim: treatment of extreme events - it catches the first flush reliably.",
 "pointer": "The Signature system's proposed approach sizes stormwater treatment for first-flush capture with maintained performance; the companion Signature Edition record specifies the first-flush protocol.",
 "key_points": [
  "Stormwater is the largest unregulated urban pollution source.",
  "First-flush flows carry the accumulated street load.",
  "Tire wear (6PPD-quinone) is acutely toxic to salmon.",
  "Green infrastructure bypasses large storms and degrades without maintenance.",
 ],
 "requirements": [
  "First-flush-volume-based treatment sizing.",
  "Influent/effluent performance monitoring.",
  "Maintenance schedules tied to measured performance.",
 ],
 "citations": [
  "Tian Z et al. (2021) A ubiquitous tire rubber-derived chemical induces acute mortality in coho salmon. Science 371(6525).",
 ],
 "demo": {"cin": 180.0, "cout": 40.0, "k": 0.45, "t": 2.0},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "ee-cso",
 "name": "The Combined Sewer Overflow Problem",
 "group": "Water Treatment",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Combined sewers carry sewage and stormwater in one pipe - but when it rains hard, they overflow raw sewage into rivers, so how can overflows be eliminated affordably?",
 "background": "Combined sewer systems (older cities worldwide) overflow during wet weather: billions of gallons of dilute sewage enter waterways yearly in the US alone. The fixes are capital-intensive: deep tunnel storage (Chicago's TARP, London's Tideway), sewer separation (digging up cities), and green infrastructure to reduce inflow. Consent decrees drive multi-billion-dollar programs with decades-long timelines. Real-time control (smart sewers that route flow to available capacity) promises cheaper reduction but is operationally immature. Climate-intensified rainfall moves the goalposts continuously.",
 "why_it_matters": "CSOs dump pathogens and floatables into urban waterways billions of gallons at a time. The rivers cannot wait decades for the tunnels.",
 "sig_lens": "The Signature lens reads CSOs as a bathtub with one drain: the protocol must add storage, reduce the inflow, and steer the water smartly - in that order of cost.",
 "sig_solution": LABEL + " Assumptions: (1) fixes are capital-intensive with decade timelines; (2) rainfall intensification moves the goalposts. Reasoning path: layer the defenses - green infrastructure to cut inflow, real-time control to use existing capacity, storage tunnels for the remainder. Proposed mechanism: a bathtub protocol sequencing green inflow reduction first, smart-sewer real-time control second, and storage sized to the residual - with overflow monitoring verifying each layer's contribution. Confirm: layered programs cut overflow volumes per dollar better than tunnel-only. Kill: real-time control proves operationally unreliable. Does NOT claim: CSO elimination on a budget - it layers the defenses by cost-effectiveness.",
 "pointer": "The Signature system's proposed approach layers green infrastructure, smart control, and storage against CSOs; the companion Signature Edition record specifies the bathtub protocol.",
 "key_points": [
  "CSOs discharge billions of gallons of dilute sewage yearly in the US.",
  "Deep tunnels and separation cost billions with decade timelines.",
  "Green infrastructure and real-time control promise cheaper reductions.",
  "Climate-intensified rainfall moves the targets.",
 ],
 "requirements": [
  "Green infrastructure inflow reduction as first layer.",
  "Real-time control using existing system capacity.",
  "Storage sized to the residual with overflow verification.",
 ],
 "citations": [
  "US EPA (2004) Report to Congress on CSOs.",
 ],
 "demo": {"cin": 250.0, "cout": 60.0, "k": 0.4, "t": 1.5},
},
# ----------------------------------------------------------------- rank 10
{
 "key": "ee-membrane-fouling",
 "name": "The Membrane Fouling Prediction Problem",
 "group": "Water Treatment",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Membranes foul - biological, organic, colloidal, scaling layers choke flux - but can fouling be predicted from feedwater, or only discovered by watching pressure rise?",
 "background": "Membrane processes (MF/UF/NF/RO) are the treatment frontier, and fouling is their tax: flux declines, energy rises, cleaning cycles interrupt production, membranes die young. Fouling indices (SDI, MFI) predict poorly - they measure the wrong things (SDI famously fails to predict RO fouling). The fouling mechanisms interact: biofouling feeds on the organics that coagulation missed. Cleaning restores partially and ages membranes. The models (resistance-in-series, CFD) describe but do not predict field fouling rates. Operators learn each plant's fouling personality by experience - the science lags the operations.",
 "why_it_matters": "Membranes are the future of water treatment; fouling is their operating cost. Unpredictable fouling makes membrane economics a gamble.",
 "sig_lens": "The Signature lens reads fouling as a slow siege: the protocol must watch the walls (flux and pressure) and sally forth (clean) before the breach.",
 "sig_solution": LABEL + " Assumptions: (1) fouling indices predict poorly; (2) mechanisms interact. Reasoning path: monitor fouling directly and clean on measured state, not schedule - and characterize the feed to anticipate. Proposed mechanism: a siege protocol with direct fouling monitoring (normalized flux, differential pressure trends), clean-in-place triggered on measured thresholds, and feedwater characterization feeding fouling-rate models calibrated per plant. Confirm: state-triggered cleaning extends membrane life versus scheduled. Kill: the monitoring cannot distinguish fouling types and cleaning mistargets. Does NOT claim: fouling prediction from first principles - it watches the siege and sorties on measurement.",
 "pointer": "The Signature system's proposed approach triggers membrane cleaning on measured fouling state; the companion Signature Edition record specifies the siege protocol.",
 "key_points": [
  "Fouling taxes flux, energy, cleaning downtime, and membrane life.",
  "SDI and MFI predict RO fouling poorly.",
  "Biofouling, organic, colloidal, and scaling mechanisms interact.",
  "Operators learn fouling by experience; science lags.",
 ],
 "requirements": [
  "Direct fouling-state monitoring (flux, pressure trends).",
  "Threshold-triggered (not scheduled) cleaning.",
  "Per-plant calibrated fouling-rate models from feedwater data.",
 ],
 "citations": [
  "Flemming HC (1997) Reverse osmosis membrane biofouling. Experimental Thermal and Fluid Science 14(4).",
 ],
 "demo": {"cin": 140.0, "cout": 20.0, "k": 0.65, "t": 2.8},
},
# ----------------------------------------------------------------- rank 11
{
 "key": "ee-brine",
 "name": "The Desalination Brine Management Problem",
 "group": "Water Treatment",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Desalination makes freshwater and concentrated brine - but what can be done with the brine when ocean discharge harms ecosystems and inland plants have no ocean?",
 "background": "Every liter of desalinated water makes ~1.5 liters of brine: hypersaline, chemical-laden, denser than seawater - it sinks and smothers benthic ecosystems at outfalls. Inland desalination (brackish groundwater) has no ocean option: evaporation ponds need vast land, deep-well injection faces the same seismicity questions as oilfield water. Zero-liquid-discharge (ZLD) crystallizes the salts but at steep energy cost. Brine mining (lithium, magnesium) promises revenue but remains mostly pilot-scale. The brine problem grows with every new desalination plant - the freshwater solution creates a salt problem.",
 "why_it_matters": "Desalination is water security for arid regions; its brine is an environmental liability that scales with every plant. The salt must go somewhere.",
 "sig_lens": "The Signature lens reads brine as concentrated consequence: the protocol must account for every ton of salt, not just every liter of water.",
 "sig_solution": LABEL + " Assumptions: (1) ocean discharge harms benthic ecosystems; (2) ZLD is energy-steep. Reasoning path: minimize brine first (high-recovery designs), then valorize or dispose by the least-harm path per site. Proposed mechanism: a consequence protocol requiring brine management plans with every desalination project - high-recovery process design, outfall diffusion modeling with ecological monitoring, and brine-mining pilots where economics approach viability. Confirm: planned brine management shows less ecological impact. Kill: brine mining never clears economics and ZLD stays unaffordable. Does NOT claim: a universal brine solution - it accounts for the salt per site.",
 "pointer": "The Signature system's proposed approach requires brine management plans with every desalination project; the companion Signature Edition record specifies the consequence protocol.",
 "key_points": [
  "Desalination makes ~1.5 liters of brine per liter of freshwater.",
  "Dense brine plumes smother benthic ecosystems at outfalls.",
  "Inland plants lack ocean discharge; ZLD is energy-steep.",
  "Brine mining remains mostly pilot-scale.",
 ],
 "requirements": [
  "Brine management plans with every new desalination project.",
  "High-recovery process designs minimizing brine volume.",
  "Outfall ecological monitoring and brine-mining pilots.",
 ],
 "citations": [
  "Jones E et al. (2019) The state of desalination and brine production. Science of the Total Environment 657.",
 ],
 "demo": {"cin": 300.0, "cout": 45.0, "k": 0.5, "t": 3.2},
},
# ----------------------------------------------------------------- rank 12
{
 "key": "ee-amr-wastewater",
 "name": "The Antibiotic Resistance in Wastewater Problem",
 "group": "Water Treatment",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Wastewater plants mix antibiotics, bacteria, and genes - but do they breed resistance, and can treatment be redesigned to stop it?",
 "background": "Wastewater treatment plants are hypothesized hotspots for antibiotic resistance: sub-lethal antibiotic concentrations, dense bacterial populations, and mobile genetic elements create ideal conditions for horizontal gene transfer. Studies detect resistance genes in effluents and downstream sediments, but the quantitative contribution of WWTPs versus agriculture and medicine to environmental resistance is contested. Treatment upgrades (disinfection, advanced oxidation) reduce bacterial loads but may select for resistant survivors. The surveillance (which genes, where, how much) is unstandardized, and the risk link from environmental genes to human infections is the missing epidemiological step.",
 "why_it_matters": "Antibiotic resistance kills over a million yearly. If treatment plants amplify it, the infrastructure meant to protect health is spreading the threat.",
 "sig_lens": "The Signature lens reads the treatment plant as a potential academy for resistance: the protocol must graduate fewer resistant bacteria, not more.",
 "sig_solution": LABEL + " Assumptions: (1) WWTPs are plausible resistance hotspots; (2) the human-health link is unquantified. Reasoning path: measure resistance through the plant (influent, process, effluent), identify the amplifying stages, and redesign those stages. Proposed mechanism: an academy protocol with resistance-gene monitoring across treatment stages, process modifications targeting gene transfer hotspots, and effluent disinfection validated against resistance (not just indicator bacteria). Confirm: redesigned plants show lower effluent resistance-gene loads. Kill: resistance proves driven by upstream sources and plant redesign is futile. Does NOT claim: a quantified human-health benefit - it graduates fewer resistant bacteria measurably.",
 "pointer": "The Signature system's proposed approach monitors resistance genes across treatment stages and redesigns hotspots; the companion Signature Edition record specifies the academy protocol.",
 "key_points": [
  "WWTPs combine antibiotics, dense bacteria, and mobile genes.",
  "Resistance genes are detected in effluents and sediments.",
  "The WWTP contribution versus agriculture and medicine is contested.",
  "Disinfection may select for resistant survivors.",
 ],
 "requirements": [
  "Resistance-gene monitoring across treatment stages.",
  "Process redesign targeting gene-transfer hotspots.",
  "Effluent standards validated against resistance, not indicators.",
 ],
 "citations": [
  "Rizzo L et al. (2013) Urban wastewater treatment plants as hotspots for antibiotic resistant bacteria. STOTEN 447.",
 ],
 "demo": {"cin": 170.0, "cout": 35.0, "k": 0.48, "t": 2.6},
},
# ----------------------------------------------------------------- rank 13
{
 "key": "ee-nutrient-recovery",
 "name": "The Nutrient Recovery From Wastewater Problem",
 "group": "Water Treatment",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Wastewater holds phosphorus and nitrogen worth recovering - but can recovery pay for itself, and will farmers trust fertilizer made from sewage?",
 "background": "Phosphorus is a finite resource (Morocco holds most reserves) and nitrogen production is energy-intensive; wastewater contains both. Recovery technologies - struvite precipitation, ammonia stripping, membrane concentration - work technically, but the economics are marginal: recovered struvite competes with cheap mined phosphorus, and the product quality (contaminants, consistency) worries farmers. The regulatory status of sewage-derived fertilizer varies. The paradigm shift - treatment plants as resource factories - is philosophically embraced and economically stalled. The question is not can we recover, but can we sell.",
 "why_it_matters": "Phosphorus scarcity threatens future food security; nitrogen recovery saves energy. The nutrients are in the water; the market is not.",
 "sig_lens": "The Signature lens reads nutrients as money in the wastewater: the protocol must mint it into a product farmers actually buy.",
 "sig_solution": LABEL + " Assumptions: (1) recovery technology works; economics do not; (2) product acceptance is the binding constraint. Reasoning path: design the product for the market - certify quality, guarantee consistency, and price against mined alternatives honestly. Proposed mechanism: a minting protocol with product certification standards (contaminant limits, nutrient guarantees), offtake agreements before plant investment, and process selection on full economics including avoided disposal costs. Confirm: certified products with offtake agreements achieve viable recovery economics. Kill: farmers reject the product regardless of certification. Does NOT claim: universal recovery economics - it mints what the market will buy.",
 "pointer": "The Signature system's proposed approach certifies recovered nutrients and secures offtake before investment; the companion Signature Edition record specifies the minting protocol.",
 "key_points": [
  "Phosphorus reserves are concentrated; nitrogen production is energy-intensive.",
  "Struvite and ammonia recovery work technically.",
  "Recovered products compete with cheap mined phosphorus.",
  "Farmer acceptance and regulatory status are binding constraints.",
 ],
 "requirements": [
  "Product certification standards for recovered nutrients.",
  "Offtake agreements secured before recovery investment.",
  "Full economics including avoided disposal costs.",
 ],
 "citations": [
  "Cordell D et al. (2009) The story of phosphorus. Global Environmental Change 19(2).",
 ],
 "demo": {"cin": 130.0, "cout": 18.0, "k": 0.62, "t": 3.4},
},
# ----------------------------------------------------------------- rank 14
{
 "key": "ee-desal-energy",
 "name": "The Desalination Energy Reduction Problem",
 "group": "Water Treatment",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Reverse osmosis is near its thermodynamic limit - so where can the next halving of desalination energy come from?",
 "background": "Seawater RO now uses ~3 kWh per cubic meter, approaching the thermodynamic minimum (~1 kWh/m3) for 50 percent recovery: the technology is mature, and the remaining energy goes to pretreatment, pumping, and brine disposal. Breakthrough claims (graphene membranes, biomimetic aquaporins) promise leaps but face fouling, manufacturing, and scale realities - the history of membrane breakthroughs is long on papers and short on plants. The realistic frontiers are system-level: renewable-powered desalination, high-recovery designs, and brine concentration. The energy problem is increasingly not the membrane but everything around it.",
 "why_it_matters": "Desalination's energy cost is its carbon footprint and its operating bill. The next halving decides whether desalination scales sustainably.",
 "sig_lens": "The Signature lens reads desalination energy as a budget with a floor: the protocol must spend the remaining budget where the physics still allows savings.",
 "sig_solution": LABEL + " Assumptions: (1) RO approaches thermodynamic limits; (2) breakthrough membranes face scale realities. Reasoning path: optimize the system, not the membrane - cut pretreatment, pumping, and brine-handling energy where the physics allows. Proposed mechanism: an energy-budget protocol auditing desalination plants by stage, targeting the largest non-membrane energy uses, and qualifying novel membranes on fouled, manufactured, scaled performance - not lab flux. Confirm: system-optimized plants beat membrane-focused R&D on energy per dollar. Kill: the system overhead proves irreducible and the floor is the ceiling. Does NOT claim: a breakthrough membrane - it spends the budget where physics allows.",
 "pointer": "The Signature system's proposed approach optimizes desalination energy at the system level; the companion Signature Edition record specifies the energy-budget protocol.",
 "key_points": [
  "Seawater RO uses ~3 kWh/m3, near the ~1 kWh/m3 thermodynamic limit.",
  "Remaining energy goes to pretreatment, pumping, and brine handling.",
  "Breakthrough membrane claims face fouling and manufacturing realities.",
  "The frontier is system-level, not membrane-level.",
 ],
 "requirements": [
  "Stage-by-stage energy audits of desalination plants.",
  "Novel membranes qualified on fouled, scaled performance.",
  "Renewable integration and high-recovery designs.",
 ],
 "citations": [
  "Elimelech M, Phillip WA (2011) The future of seawater desalination. Science 333(6043).",
 ],
 "demo": {"cin": 220.0, "cout": 28.0, "k": 0.58, "t": 3.8},
},
# ----------------------------------------------------------------- rank 15
{
 "key": "ee-aop-byproducts",
 "name": "The Advanced Oxidation Byproduct Problem",
 "group": "Water Treatment",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Advanced oxidation destroys micropollutants with radicals - but the radicals also make new byproducts, some worse than the originals, so how can the cure be verified better than the disease?",
 "background": "Advanced oxidation processes (ozone/H2O2, UV/H2O2, Fenton) generate hydroxyl radicals that mineralize pharmaceuticals and PFAS-precursors - and also bromate (a carcinogen) from bromide, NDMA, and unknown transformation products. The byproduct profile depends on the water matrix in ways that resist prediction: the same AOP makes different byproducts in different waters. Effect-based monitoring (bioassays on treated water) is the honest check but is unstandardized for regulation. The field destroys the target compounds triumphantly while the transformation products go unmeasured.",
 "why_it_matters": "AOPs are the upgrade path for micropollutant removal. Trading known contaminants for unknown byproducts is not treatment - it is transformation.",
 "sig_lens": "The Signature lens reads oxidation as fire: the protocol must check what the smoke contains, not just that the fuel burned.",
 "sig_solution": LABEL + " Assumptions: (1) byproduct profiles are matrix-dependent and unpredictable; (2) target destruction is routinely verified while byproducts are not. Reasoning path: verify the treated water, not just the destroyed targets - require effect-based testing of AOP effluents. Proposed mechanism: a smoke-check protocol mandating bioassay batteries on AOP-treated water, byproduct monitoring for known bad actors (bromate, NDMA), and process selection on the total toxicity reduction, not target removal. Confirm: smoke-checked AOPs show verified toxicity reduction. Kill: bioassays prove too variable for process control. Does NOT claim: byproduct-free oxidation - it checks the smoke.",
 "pointer": "The Signature system's proposed approach verifies AOP effluents with bioassay batteries; the companion Signature Edition record specifies the smoke-check protocol.",
 "key_points": [
  "AOPs mineralize micropollutants but create bromate, NDMA, and unknowns.",
  "Byproduct profiles depend on the water matrix unpredictably.",
  "Target destruction is verified; transformation products often are not.",
  "Effect-based monitoring is the honest check but unstandardized.",
 ],
 "requirements": [
  "Bioassay batteries on AOP-treated effluents.",
  "Monitoring for known bad-actor byproducts.",
  "Process selection on total toxicity reduction.",
 ],
 "citations": [
  "von Gunten U (2003) Ozonation of drinking water: part II disinfection and by-product formation. Water Research 37(7).",
 ],
 "demo": {"cin": 95.0, "cout": 10.0, "k": 0.75, "t": 2.2},
},
# ----------------------------------------------------------------- rank 16
{
 "key": "ee-uhi",
 "name": "The Urban Heat Island Mitigation Problem",
 "group": "Air Quality",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Cities run degrees hotter than their surroundings, killing the vulnerable in heat waves - but which cooling interventions actually work at city scale?",
 "background": "Urban heat islands (Oke, 1982) - cities 2-10 C hotter than rural surroundings - amplify heat-wave mortality: the 2003 European heat wave killed 70,000, disproportionately in hot neighborhoods. Mitigations (cool roofs, street trees, permeable pavements, green corridors) each have evidence, but the city-scale effectiveness is uncertain: cool roofs cool buildings more than streets, trees need water cities lack, and the interventions interact. The equity dimension is stark - the hottest neighborhoods are the poorest - yet cooling investments follow political, not thermal, maps. Heat action plans exist; their effectiveness is largely unevaluated.",
 "why_it_matters": "Heat kills more Americans than all other weather combined, and the toll concentrates in poor neighborhoods. Unproven cooling spends the adaptation budget on hope.",
 "sig_lens": "The Signature lens reads the heat island as a fever map: the protocol must cool the hottest patients first and verify the fever broke.",
 "sig_solution": LABEL + " Assumptions: (1) intervention evidence is building-scale; city-scale effects uncertain; (2) heat burden is inequitable. Reasoning path: map the heat at neighborhood resolution, deploy cooling where the burden is highest, and verify with temperature monitoring. Proposed mechanism: a fever-map protocol with high-resolution urban temperature monitoring, vulnerability-weighted intervention targeting, and before-after verification of cooling effectiveness. Confirm: targeted interventions show measured temperature and health improvements. Kill: city-scale effects prove undetectable against weather noise. Does NOT claim: city-scale cooling solved - it treats the hottest patients first with verification.",
 "pointer": "The Signature system's proposed approach targets urban cooling by vulnerability-weighted heat maps; the companion Signature Edition record specifies the fever-map protocol.",
 "key_points": [
  "Cities run 2-10 C hotter than surroundings; heat kills disproportionately.",
  "Cool roofs, trees, and permeable pavements each have partial evidence.",
  "City-scale effectiveness of interventions is uncertain.",
  "The hottest neighborhoods are the poorest; investments follow politics.",
 ],
 "requirements": [
  "High-resolution urban temperature monitoring.",
  "Vulnerability-weighted intervention targeting.",
  "Before-after verification of cooling effectiveness.",
 ],
 "citations": [
  "Oke TR (1982) The energetic basis of the urban heat island. QJRMS 108(455).",
 ],
 "demo": {"cin": 75.0, "cout": 9.0, "k": 0.68, "t": 2.4},
},
# ----------------------------------------------------------------- rank 17
{
 "key": "ee-source-apportionment",
 "name": "The Air Pollution Source Apportionment Problem",
 "group": "Air Quality",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "A city's air is a cocktail from traffic, industry, cooking, and dust - but how much comes from each source, and which controls will actually clean the air?",
 "background": "Source apportionment - attributing PM2.5 to its sources - uses chemical mass balance, positive matrix factorization, and emissions inventories, but the answers disagree: inventories miss sources (cooking, brake wear), receptor models have rotational ambiguity, and secondary aerosol (formed in the atmosphere) resists attribution entirely. The policy stakes are high: control strategies target the apportioned sources, and misapportionment wastes billions. Low-cost sensor networks promise hyperlocal data but bring calibration chaos. The cocktail's recipe remains contested in every megacity.",
 "why_it_matters": "Air pollution kills millions yearly. Controls aimed at misapportioned sources clean the wrong air while the real sources keep emitting.",
 "sig_lens": "The Signature lens reads the cocktail as a recipe to be reverse-engineered: the protocol must triangulate the sources with multiple independent methods.",
 "sig_solution": LABEL + " Assumptions: (1) inventories miss sources; receptor models have ambiguity; (2) secondary aerosol resists attribution. Reasoning path: triangulate - require agreement among inventory, receptor, and dispersion modeling before targeting controls. Proposed mechanism: a recipe protocol mandating multi-method apportionment (inventory plus PMF plus modeling), control strategies targeting only triangulated sources, and accountability monitoring verifying the predicted air-quality improvement. Confirm: triangulated controls deliver predicted improvements. Kill: the methods never agree and triangulation paralyzes action. Does NOT claim: exact source attribution - it acts on triangulated agreement.",
 "pointer": "The Signature system's proposed approach triangulates pollution sources with multiple methods before targeting controls; the companion Signature Edition record specifies the recipe protocol.",
 "key_points": [
  "Inventories miss sources; receptor models have rotational ambiguity.",
  "Secondary aerosol formation resists source attribution.",
  "Misapportionment wastes control investments.",
  "Low-cost sensors add data with calibration chaos.",
 ],
 "requirements": [
  "Multi-method apportionment (inventory, receptor, dispersion).",
  "Controls targeting only triangulated sources.",
  "Accountability monitoring of predicted improvements.",
 ],
 "citations": [
  "Hopke PK (2016) Review of receptor modeling methods for source apportionment. JAWMA 66(3).",
 ],
 "demo": {"cin": 65.0, "cout": 7.0, "k": 0.72, "t": 2.1},
},
# ----------------------------------------------------------------- rank 18
{
 "key": "ee-iaq",
 "name": "The Indoor Air Quality Problem",
 "group": "Air Quality",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "People spend 90 percent of time indoors breathing air worse than outside - but what is in it, and how can buildings be ventilated without wasting energy?",
 "background": "Indoor air concentrates cooking emissions, cleaning chemicals, off-gassing materials, radon, and bioaerosols - often at levels exceeding outdoor standards, yet indoor air is largely unregulated. The ventilation-energy tradeoff is the crux: more fresh air means healthier air and higher HVAC bills. CO2 as a ventilation proxy is crude; the actual contaminants (formaldehyde, PM2.5, VOCs) need direct sensing that is expensive. The pandemic made ventilation a public-health priority overnight, but the standards (ASHRAE 62.1) balance health against energy with thin evidence. Smart ventilation - ventilating on measured need - is the aspiration without the sensors.",
 "why_it_matters": "Indoor air is the air most breathed and least regulated. The ventilation-energy tradeoff is decided daily in every building, mostly by default.",
 "sig_lens": "The Signature lens reads buildings as lungs: the protocol must ventilate on measured need, not on schedule, and never trade health for energy silently.",
 "sig_solution": LABEL + " Assumptions: (1) indoor air is largely unregulated and under-measured; (2) ventilation trades health against energy. Reasoning path: ventilate smart - measure the actual contaminants and ventilate to the need, with the tradeoff made explicit. Proposed mechanism: a lungs protocol with multi-pollutant indoor sensing in representative buildings, demand-controlled ventilation tied to measured contaminants, and health-energy tradeoff reporting per building. Confirm: smart-ventilated buildings show better air at equal or lower energy. Kill: sensing proves too expensive and the protocol never deploys. Does NOT claim: optimal indoor air - it ventilates on measured need.",
 "pointer": "The Signature system's proposed approach ventilates buildings on measured contaminant need; the companion Signature Edition record specifies the lungs protocol.",
 "key_points": [
  "Indoor air often exceeds outdoor pollution levels; it is largely unregulated.",
  "Ventilation trades health against HVAC energy directly.",
  "CO2 is a crude proxy for the actual contaminants.",
  "Smart ventilation needs sensors that are still expensive.",
 ],
 "requirements": [
  "Multi-pollutant indoor sensing in representative buildings.",
  "Demand-controlled ventilation tied to measured contaminants.",
  "Health-energy tradeoff reporting per building.",
 ],
 "citations": [
  "ASHRAE Standard 62.1: Ventilation for Acceptable Indoor Air Quality.",
 ],
 "demo": {"cin": 55.0, "cout": 6.0, "k": 0.7, "t": 2.3},
},
# ----------------------------------------------------------------- rank 19
{
 "key": "ee-soil-mixed",
 "name": "The Soil Remediation of Mixed Contaminants Problem",
 "group": "Waste Management",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Real contaminated sites hold mixtures - solvents, metals, PCBs together - but remediation technologies each target one contaminant, so how can mixtures be cleaned?",
 "background": "Contaminated sites rarely hold single contaminants: chlorinated solvents plus heavy metals plus PCBs is the typical brownfield cocktail. But remediation technologies are single-target: bioremediation eats organics (metals poison the microbes), soil washing moves metals (leaving organics), thermal treatment handles organics (volatilizing metals). Treatment trains - sequences of technologies - are designed by experience, and the interactions (one step's residue poisoning the next) are learned the hard way. The characterization problem compounds it: the mixture's spatial distribution is under-sampled. Most cleanups address the regulated driver and leave the rest.",
 "why_it_matters": "Mixed-contaminant sites are the norm, not the exception. Single-target cleanups leave the other contaminants for the next generation.",
 "sig_lens": "The Signature lens reads mixed contamination as a knot: the protocol must untangle it in the right order, or each pull tightens another loop.",
 "sig_solution": LABEL + " Assumptions: (1) technologies are single-target; (2) treatment interactions are learned painfully. Reasoning path: sequence the treatment train by compatibility - characterize the mixture fully, then order technologies so each step's residue feeds the next. Proposed mechanism: a knot protocol with full mixture characterization (not just the regulated driver), compatibility-tested treatment sequences, and verification of all contaminants (not just the driver) at completion. Confirm: sequenced trains achieve multi-contaminant cleanup goals. Kill: the interactions prove unpredictable and sequences fail. Does NOT claim: a universal mixed-waste solution - it untangles in the tested order.",
 "pointer": "The Signature system's proposed approach sequences remediation trains by tested compatibility; the companion Signature Edition record specifies the knot protocol.",
 "key_points": [
  "Real sites hold contaminant mixtures; technologies target singles.",
  "Bioremediation microbes are poisoned by co-contaminant metals.",
  "Treatment-train interactions are learned the hard way.",
  "Cleanups typically address only the regulated driver.",
 ],
 "requirements": [
  "Full mixture characterization beyond the regulated driver.",
  "Compatibility-tested treatment sequences.",
  "Multi-contaminant verification at completion.",
 ],
 "citations": [
  "US EPA (2004) Treatment Technologies for Site Cleanup.",
 ],
 "demo": {"cin": 190.0, "cout": 28.0, "k": 0.52, "t": 3.0},
},
# ----------------------------------------------------------------- rank 20
{
 "key": "ee-brownfield",
 "name": "The Brownfield Redevelopment Risk Problem",
 "group": "Waste Management",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Brownfields - abandoned contaminated sites - could be redeveloped, but the liability and cleanup uncertainty freeze them, so how can the risk be priced to unlock reuse?",
 "background": "The US has an estimated 450,000+ brownfields: former factories and gas stations whose contamination is uncertain, whose liable parties are gone, and whose cleanup costs are unknowable until excavation. Liability regimes (CERCLA's joint and several liability) freeze transactions: buyers fear the unknown cleanup bill. Risk assessment for redevelopment must predict future exposure under future land use - a chain of assumptions. Insurance products (environmental liability) exist but are expensive and incomplete. The result is urban decay amid housing shortages: the land is needed, the risk is unpriced, and nothing moves.",
 "why_it_matters": "Brownfields blight cities while greenfields get developed. The frozen land is a housing and economic crisis wearing a contamination costume.",
 "sig_lens": "The Signature lens reads brownfields as locked value: the protocol must appraise the lock (the risk) honestly so the key (the investment) can turn.",
 "sig_solution": LABEL + " Assumptions: (1) cleanup costs are unknowable until excavation; (2) liability freezes transactions. Reasoning path: bound the risk - characterize to the decision's needs, cap the liability contractually, and insure the residual. Proposed mechanism: a locked-value protocol with decision-grade site characterization, contractual liability caps (prospective purchaser agreements), and residual-risk insurance - each redevelopment carrying its priced risk. Confirm: protocol-unlocked sites redevelop faster with fewer surprises. Kill: the characterization misses the critical contamination and caps are breached. Does NOT claim: risk-free brownfields - it prices the lock honestly.",
 "pointer": "The Signature system's proposed approach bounds brownfield risk with characterization, caps, and insurance; the companion Signature Edition record specifies the locked-value protocol.",
 "key_points": [
  "450,000+ brownfields estimated in the US alone.",
  "Liability regimes freeze transactions on unknown cleanup bills.",
  "Risk assessment chains assumptions about future land use.",
  "Insurance exists but is expensive and incomplete.",
 ],
 "requirements": [
  "Decision-grade site characterization.",
  "Contractual liability caps for purchasers.",
  "Residual-risk insurance on the priced remainder.",
 ],
 "citations": [
  "US EPA Brownfields Program data.",
 ],
 "demo": {"cin": 160.0, "cout": 22.0, "k": 0.56, "t": 2.9},
},
# ----------------------------------------------------------------- rank 21
{
 "key": "ee-leachate",
 "name": "The Landfill Leachate Treatment Problem",
 "group": "Waste Management",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Rain through garbage makes leachate - ammonia, organics, metals, PFAS - but how can the changing cocktail be treated as the landfill ages over decades?",
 "background": "Landfill leachate evolves: young landfills leach biodegradable organics (treatable biologically), old ones leach ammonia and refractory organics (needing physical-chemical treatment), and now PFAS rides along at every age. The treatment must adapt over the landfill's decades-long life, but plants are built once: biological plants go obsolete as leachate ages, and the ammonia (often thousands of mg/L) defeats conventional nitrification. Recirculation (bioreactor landfills) accelerates stabilization but risks seeps and instability. The leachate problem is a decades-long moving target.",
 "why_it_matters": "Every landfill makes leachate for decades after closure. The moving target defeats fixed treatment - and the PFAS rides along throughout.",
 "sig_lens": "The Signature lens reads leachate as a aging patient: the protocol must change the treatment as the patient ages, not prescribe once for life.",
 "sig_solution": LABEL + " Assumptions: (1) leachate chemistry evolves over decades; (2) fixed plants go obsolete. Reasoning path: treat in phases matched to leachate age - biological for young, physical-chemical for old, with PFAS treatment throughout. Proposed mechanism: an aging-patient protocol with leachate-age monitoring, phased treatment trains that reconfigure as chemistry evolves, and PFAS removal integrated at every phase. Confirm: phased treatment meets discharge limits across landfill ages. Kill: the transitions prove unpredictable and phases mistime. Does NOT claim: a universal leachate solution - it treats the patient's current age.",
 "pointer": "The Signature system's proposed approach phases leachate treatment to the landfill's age; the companion Signature Edition record specifies the aging-patient protocol.",
 "key_points": [
  "Leachate evolves: young (biodegradable) to old (ammonia, refractory).",
  "Ammonia at thousands of mg/L defeats conventional treatment.",
  "PFAS contaminates leachate at every landfill age.",
  "Fixed plants go obsolete as the leachate ages.",
 ],
 "requirements": [
  "Leachate-age monitoring driving treatment selection.",
  "Reconfigurable phased treatment trains.",
  "PFAS removal integrated at every phase.",
 ],
 "citations": [
  "Kjeldsen P et al. (2002) Present and long-term composition of MSW landfill leachate. Critical Reviews in Env. Sci. Tech. 32(4).",
 ],
 "demo": {"cin": 400.0, "cout": 50.0, "k": 0.42, "t": 3.6},
},
# ----------------------------------------------------------------- rank 22
{
 "key": "ee-landfill-gas",
 "name": "The Landfill Gas Capture Problem",
 "group": "Waste Management",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Landfills are among the largest methane sources - but how much gas escapes uncaptured, and can capture be verified rather than assumed?",
 "background": "Landfill gas (roughly half methane) is captured by well fields for flaring or energy - where installed. But collection efficiency is the open number: EPA defaults assume 75 percent, while field studies (tracer releases, drone surveys) find wide variation, with cracks, cover failures, and edge leaks. The uncollected methane - a potent greenhouse gas - is the industry's invisible emission. Verification is hard: the landfill is heterogeneous, emissions are diffuse, and the business case for better capture depends on carbon prices that wobble. The gap between assumed and actual capture is the climate question.",
 "why_it_matters": "Landfills are top methane emitters. The assumed 75 percent capture may be fiction - and the climate pays for the fiction.",
 "sig_lens": "The Signature lens reads landfill gas as an invisible leak: the protocol must measure what escapes, not assume what is caught.",
 "sig_solution": LABEL + " Assumptions: (1) collection efficiency is assumed more than measured; (2) emissions are diffuse and heterogeneous. Reasoning path: verify capture directly - measure surface emissions and reconcile with collected gas to compute the true efficiency. Proposed mechanism: a leak-meter protocol with periodic surface-emission surveys (drones, tracers), reconciliation against collected volumes, and capture-system upgrades targeted at the measured leaks. Confirm: verified systems show higher true capture efficiencies. Kill: the surveys prove too uncertain for reconciliation. Does NOT claim: complete capture - it measures the escape honestly.",
 "pointer": "The Signature system's proposed approach verifies landfill gas capture by surface-emission reconciliation; the companion Signature Edition record specifies the leak-meter protocol.",
 "key_points": [
  "Landfills are among the largest methane sources.",
  "EPA assumes 75 percent collection; field studies vary widely.",
  "Cover cracks and edge leaks defeat assumed efficiencies.",
  "The verification gap is the climate question.",
 ],
 "requirements": [
  "Periodic surface-emission surveys (drones, tracers).",
  "Reconciliation of emissions against collected volumes.",
  "Capture upgrades targeted at measured leaks.",
 ],
 "citations": [
  "US EPA Landfill Methane Outreach Program data.",
 ],
 "demo": {"cin": 120.0, "cout": 14.0, "k": 0.6, "t": 2.7},
},
# ----------------------------------------------------------------- rank 23
{
 "key": "ee-ewaste",
 "name": "The E-Waste Recycling Problem",
 "group": "Waste Management",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Electronics hold precious metals and toxic substances together - but how can e-waste be recycled economically without exporting the hazard to the informal sector?",
 "background": "E-waste is the fastest-growing waste stream (62 million tonnes in 2022, Global E-waste Monitor): phones hold gold, palladium, and rare earths alongside lead, mercury, and brominated flame retardants. Formal recycling recovers a fraction at high cost; the informal sector (Agbogbloshie, Guiyu) recovers more by burning and acid-stripping - poisoning workers and land. Extended producer responsibility schemes shift costs but not design: products are still unmade for disassembly. The material complexity defeats automated sorting; the economics defeat formal processing. The loop stays open.",
 "why_it_matters": "E-waste is toxic wealth: the metals are needed for the energy transition, the toxins poison the poor. The recycling gap is an environmental justice crisis.",
 "sig_lens": "The Signature lens reads e-waste as a mine above ground: the protocol must make formal mining pay, or the informal miners pay with their health.",
 "sig_solution": LABEL + " Assumptions: (1) formal recycling loses economically to informal; (2) products are not designed for disassembly. Reasoning path: close the loop at both ends - design for disassembly upstream, and make formal recovery pay downstream. Proposed mechanism: a mine-above-ground protocol with design-for-disassembly standards, formal recovery subsidized to outcompete informal (funded by producer fees), and material passports tracking substances through the product life. Confirm: protocol regions show higher formal recovery rates. Kill: the subsidy proves insufficient and informal processing persists. Does NOT claim: a closed e-waste loop - it makes formal mining competitive.",
 "pointer": "The Signature system's proposed approach pairs design-for-disassembly with subsidized formal recovery; the companion Signature Edition record specifies the mine-above-ground protocol.",
 "key_points": [
  "62 million tonnes of e-waste in 2022, fastest-growing stream.",
  "Devices mix precious metals with lead, mercury, and flame retardants.",
  "Informal recycling recovers more by poisoning workers.",
  "Products are not designed for disassembly.",
 ],
 "requirements": [
  "Design-for-disassembly product standards.",
  "Producer-fee-funded formal recovery subsidies.",
  "Material passports tracking substances through life.",
 ],
 "citations": [
  "Global E-waste Monitor 2024 (UNITAR).",
 ],
 "demo": {"cin": 100.0, "cout": 11.0, "k": 0.64, "t": 2.5},
},
# ----------------------------------------------------------------- rank 24
{
 "key": "ee-plastic-circularity",
 "name": "The Plastic Recycling Circularity Problem",
 "group": "Waste Management",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Less than 10 percent of plastic is recycled - but can the loop actually be closed when the material degrades, the streams mix, and virgin plastic stays cheap?",
 "background": "Mechanical recycling downgrades plastic (downcycling); the streams mix polymers that contaminate each other; and virgin resin - tied to oil prices - usually undercuts recycled. Chemical recycling (pyrolysis, depolymerization) promises virgin-quality output but faces energy costs, yield questions, and greenwashing accusations. The system problems dwarf the technical: collection rates, sorting economics, and product design (multi-layer films are unrecyclable by design). The circular economy for plastics is mostly linear with better PR.",
 "why_it_matters": "Plastic production keeps growing; the ocean keeps filling. An unclosed loop is a linear waste economy wearing circular language.",
 "sig_lens": "The Signature lens reads plastic as a material with amnesia: the protocol must give it memory (tracking) and a reason to return (economics).",
 "sig_solution": LABEL + " Assumptions: (1) technical recycling exists; the system economics do not; (2) downcycling is the norm. Reasoning path: fix the economics first - make virgin plastic carry its externalities and pay for collection infrastructure. Proposed mechanism: a memory protocol with extended producer responsibility funding collection, recycled-content mandates creating demand, and design standards banning unrecyclable formats. Confirm: protocol jurisdictions show rising true recycling rates. Kill: the mandates prove unenforceable and the loop stays rhetorical. Does NOT claim: a closed plastic loop - it builds the economics the technology needs.",
 "pointer": "The Signature system's proposed approach builds plastic circularity on producer responsibility and content mandates; the companion Signature Edition record specifies the memory protocol.",
 "key_points": [
  "Under 10 percent of plastic is recycled globally.",
  "Mechanical recycling downcycles; streams contaminate each other.",
  "Chemical recycling faces energy, yield, and credibility questions.",
  "Virgin resin usually undercuts recycled on price.",
 ],
 "requirements": [
  "Extended producer responsibility funding collection.",
  "Recycled-content mandates creating demand.",
  "Design standards banning unrecyclable formats.",
 ],
 "citations": [
  "OECD (2022) Global Plastics Outlook.",
 ],
 "demo": {"cin": 80.0, "cout": 9.0, "k": 0.66, "t": 2.2},
},
# ----------------------------------------------------------------- rank 25
{
 "key": "ee-construction-waste",
 "name": "The Construction Waste Valorization Problem",
 "group": "Waste Management",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Construction and demolition waste is the largest waste stream by mass - but how can concrete, wood, and gypsum be valorized when the material is mixed and the markets are local?",
 "background": "C&D waste - concrete, asphalt, wood, drywall, metals - is roughly a third of all waste by mass, and most of it is downcycled (road base) or landfilled. The valorization barriers are practical: mixed debris is costly to sort, recycled aggregates face quality skepticism, and the markets are hyperlocal (heavy materials do not travel). Deconstruction (careful disassembly for reuse) beats demolition environmentally but loses economically on labor. Building passports (material inventories) would enable future reuse but barely exist. The circular construction economy is a concept awaiting logistics.",
 "why_it_matters": "Concrete alone is 8 percent of global CO2; reusing it avoids new production. The largest waste stream is also the largest missed material bank.",
 "sig_lens": "The Signature lens reads buildings as material banks: the protocol must inventory the deposits before demolition withdraws them as rubble.",
 "sig_solution": LABEL + " Assumptions: (1) C&D markets are hyperlocal; (2) deconstruction loses to demolition on labor cost. Reasoning path: bank the materials - require pre-demolition inventories and match them to local demand before rubble is made. Proposed mechanism: a material-bank protocol mandating building material passports for new construction, pre-demolition audits matching materials to buyers, and deconstruction incentives where reuse value exceeds the labor premium. Confirm: banked projects achieve higher valorization rates. Kill: the matching logistics prove too costly and audits gather dust. Does NOT claim: universal C&D circularity - it banks what the local market will take.",
 "pointer": "The Signature system's proposed approach banks construction materials via pre-demolition audits; the companion Signature Edition record specifies the material-bank protocol.",
 "key_points": [
  "C&D waste is roughly a third of all waste by mass.",
  "Most is downcycled or landfilled; markets are hyperlocal.",
  "Deconstruction beats demolition environmentally, loses economically.",
  "Building material passports barely exist.",
 ],
 "requirements": [
  "Material passports for new construction.",
  "Pre-demolition audits matching materials to local buyers.",
  "Deconstruction incentives where reuse value clears the premium.",
 ],
 "citations": [
  "EU Construction and Demolition Waste Protocol.",
 ],
 "demo": {"cin": 90.0, "cout": 12.0, "k": 0.6, "t": 2.4},
},
# ----------------------------------------------------------------- rank 26
{
 "key": "ee-lca-uncertainty",
 "name": "The Life Cycle Assessment Uncertainty Problem",
 "group": "Waste Management",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Life cycle assessment compares products' environmental footprints - but how can the comparisons be trusted when the uncertainty bands are wider than the differences?",
 "background": "LCA (ISO 14040) tallies impacts from cradle to grave, guiding eco-design and procurement - but the results carry enormous uncertainty: allocation choices (how to split impacts among co-products), system boundary decisions, and database gaps each swing results. Comparative LCAs routinely claim product A beats B by 10 percent with uncertainty bands of 50 percent. The practitioner degrees of freedom (boundary, allocation, impact method) make LCA results negotiable - the same comparison can favor either product. Decision-makers get point estimates; the science has distributions.",
 "why_it_matters": "LCAs steer procurement, eco-labels, and policy. Point-estimate comparisons with hidden uncertainty are decisions built on negotiated numbers.",
 "sig_lens": "The Signature lens reads LCA as accounting with choices: the protocol must show the ledger's sensitivity to every choice, not just the bottom line.",
 "sig_solution": LABEL + " Assumptions: (1) practitioner choices swing results more than product differences; (2) uncertainty is usually hidden. Reasoning path: report the distribution, not the point - propagate uncertainty through every LCA and show the choice sensitivity. Proposed mechanism: a choices protocol requiring Monte Carlo uncertainty propagation in comparative LCAs, sensitivity analysis on allocation and boundary choices, and claims of superiority only where the distributions separate. Confirm: protocol LCAs reverse fewer procurement decisions on re-analysis. Kill: the uncertainty proves too wide for any comparison to clear. Does NOT claim: precise footprints - it shows the ledger's sensitivity honestly.",
 "pointer": "The Signature system's proposed approach reports LCAs as distributions with choice-sensitivity; the companion Signature Edition record specifies the choices protocol.",
 "key_points": [
  "LCA uncertainty bands routinely exceed the claimed product differences.",
  "Allocation and boundary choices are practitioner degrees of freedom.",
  "The same comparison can favor either product depending on choices.",
  "Decision-makers receive point estimates; the science has distributions.",
 ],
 "requirements": [
  "Monte Carlo uncertainty propagation in comparative LCAs.",
  "Sensitivity analysis on allocation and boundary choices.",
  "Superiority claims only where distributions separate.",
 ],
 "citations": [
  "ISO 14040:2006 Environmental management - Life cycle assessment.",
 ],
 "demo": {"cin": 70.0, "cout": 8.0, "k": 0.63, "t": 2.6},
},
# ----------------------------------------------------------------- rank 27
{
 "key": "ee-carbon-allocation",
 "name": "The Carbon Footprint Allocation Problem",
 "group": "Air Quality",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "A product's carbon footprint must be allocated among co-products, life stages, and actors - but every allocation rule is a value judgment, so which one is honest?",
 "background": "Carbon footprints allocate shared emissions: a refinery's crude unit serves gasoline, diesel, and jet; a cow gives milk and meat; a data center serves many users. Allocation rules (by mass, energy, economic value) give different answers - economic allocation makes luxury co-products carry the carbon, mass allocation spreads it evenly. Scope 3 accounting chains these allocations across supply networks, compounding the judgments. The GHG Protocol gives guidance, not answers. Carbon border adjustments and procurement standards need numbers; the numbers embed unacknowledged ethics.",
 "why_it_matters": "Carbon prices, border taxes, and procurement all run on allocated footprints. The allocation rule is a hidden tax code - and nobody voted on it.",
 "sig_lens": "The Signature lens reads allocation as taxation: the protocol must publish the tax code (the rule) with the bill (the footprint).",
 "sig_solution": LABEL + " Assumptions: (1) every allocation rule embeds values; (2) Scope 3 chains compound the judgments. Reasoning path: disclose the rule with the number - report footprints under multiple allocation rules and let the user see the spread. Proposed mechanism: a tax-code protocol requiring footprint reports to state the allocation rule, show sensitivity to alternative rules, and justify the choice in writing. Confirm: disclosed footprints face fewer disputes. Kill: users ignore the disclosure and treat the number as physical. Does NOT claim: the true carbon footprint - it publishes the tax code with the bill.",
 "pointer": "The Signature system's proposed approach discloses carbon allocation rules with footprint numbers; the companion Signature Edition record specifies the tax-code protocol.",
 "key_points": [
  "Co-product allocation rules (mass, energy, economic) give different answers.",
  "Scope 3 accounting chains allocations across supply networks.",
  "The GHG Protocol guides but does not resolve the judgments.",
  "Border taxes and procurement need numbers that embed ethics.",
 ],
 "requirements": [
  "Stated allocation rules with every footprint report.",
  "Multi-rule sensitivity showing the spread.",
  "Written justification of the chosen rule.",
 ],
 "citations": [
  "GHG Protocol Corporate Value Chain (Scope 3) Standard.",
 ],
 "demo": {"cin": 85.0, "cout": 10.0, "k": 0.61, "t": 2.5},
},
# ----------------------------------------------------------------- rank 28
{
 "key": "ee-justice",
 "name": "The Environmental Justice Quantification Problem",
 "group": "Air Quality",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Pollution burdens fall hardest on poor and minority communities - but how can the disparity be measured rigorously enough to drive remediation?",
 "background": "Environmental justice research documents disproportionate exposure: hazardous facilities cluster in minority neighborhoods (the landmark UCC 1987 report; Bullard's work), and the disparities persist after controlling for income. But quantification for action is hard: exposure models lack neighborhood resolution, cumulative impacts (multiple stressors) have no agreed metric, and the counterfactual (what would equitable siting look like?) is contested. EJSCREEN and CalEnviroScreen map vulnerability, yet the leap from maps to remediation priorities needs dose-response and accountability that the science strains to provide. Justice delayed by measurement gaps is still injustice.",
 "why_it_matters": "The disparity is documented; the remediation lags. Measurement gaps become delay tactics - rigor must serve justice, not postpone it.",
 "sig_lens": "The Signature lens reads EJ as a debt ledger: the protocol must quantify who paid (in health) and direct the repayment (remediation) accordingly.",
 "sig_solution": LABEL + " Assumptions: (1) disparities are documented; remediation lags; (2) cumulative-impact metrics are unagreed. Reasoning path: measure what is measurable now - facility proximity, monitored pollution, health outcomes - and act on the convergence while improving the metrics. Proposed mechanism: a debt-ledger protocol with triangulated disparity measurement (proximity, monitoring, health), remediation prioritization on the triangulated burden, and cumulative-impact research running parallel to (not gating) action. Confirm: ledger-prioritized remediation reaches burdened communities faster. Kill: the metrics prove too contested to prioritize on. Does NOT claim: a perfect EJ metric - it quantifies the debt and directs repayment.",
 "pointer": "The Signature system's proposed approach triangulates EJ burdens and prioritizes remediation on them; the companion Signature Edition record specifies the debt-ledger protocol.",
 "key_points": [
  "Hazardous facilities disproportionately cluster in minority neighborhoods.",
  "Disparities persist after income controls.",
  "Cumulative multi-stressor impacts lack agreed metrics.",
  "Screening tools map vulnerability; remediation prioritization lags.",
 ],
 "requirements": [
  "Triangulated burden measurement (proximity, monitoring, health).",
  "Remediation prioritization on triangulated burdens.",
  "Cumulative-impact research parallel to, not gating, action.",
 ],
 "citations": [
  "Bullard RD (1990) Dumping in Dixie. Westview Press.",
  "US EPA EJSCREEN technical documentation.",
 ],
 "demo": {"cin": 105.0, "cout": 13.0, "k": 0.59, "t": 2.8},
},
# ----------------------------------------------------------------- rank 29
{
 "key": "ee-adaptation",
 "name": "The Climate Adaptation Infrastructure Problem",
 "group": "Waste Management",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Infrastructure must survive climates decades out - but how can it be designed for futures whose probabilities are unknown and whose extremes keep breaking records?",
 "background": "Bridges, levees, and water systems are built for 50-100 years under stationary-climate assumptions that no longer hold: design storms are exceeded regularly, and the exceedances are accelerating. Deep uncertainty (unknown probabilities) defeats expected-value optimization; robust decision-making (Lempert) and adaptive pathways (Haasnoot) offer frameworks - design for flexibility, upgrade as the climate reveals itself. But the methods need decision-makers comfortable with ambiguity, and the infrastructure politics wants single numbers. The adaptation deficit grows: every year of stationary design is a year of future retrofit.",
 "why_it_matters": "Infrastructure failures in climate extremes kill and cost billions. Designing for the past climate is designing for failure.",
 "sig_lens": "The Signature lens reads adaptation as building for a moving target: the protocol must buy flexibility now and upgrade on the climate's actual trajectory.",
 "sig_solution": LABEL + " Assumptions: (1) stationary design assumptions are obsolete; (2) deep uncertainty defeats single-number optimization. Reasoning path: design adaptive pathways - build the foundation for upgrades now, trigger them on observed climate signals. Proposed mechanism: a moving-target protocol with adaptive-pathway designs (staged upgrades), climate-signal triggers for each stage, and robustness testing across deep-uncertainty scenarios. Confirm: pathway-designed infrastructure adapts cheaper than retrofitted. Kill: the signals prove ambiguous and triggers never fire. Does NOT claim: optimal adaptation - it buys flexibility and upgrades on evidence.",
 "pointer": "The Signature system's proposed approach designs infrastructure on adaptive pathways with climate triggers; the companion Signature Edition record specifies the moving-target protocol.",
 "key_points": [
  "Design storms are exceeded regularly; stationarity is obsolete.",
  "Deep uncertainty defeats expected-value infrastructure optimization.",
  "Adaptive pathways stage upgrades on observed climate signals.",
  "Infrastructure politics wants single numbers the science cannot give.",
 ],
 "requirements": [
  "Adaptive-pathway designs with staged upgrades.",
  "Climate-signal triggers per stage.",
  "Robustness testing across deep-uncertainty scenarios.",
 ],
 "citations": [
  "Lempert RJ et al. (2003) Shaping the Next One Hundred Years. RAND.",
 ],
 "demo": {"cin": 140.0, "cout": 18.0, "k": 0.55, "t": 3.1},
},
# ----------------------------------------------------------------- rank 30
{
 "key": "ee-nbs",
 "name": "The Nature Based Solutions Performance Problem",
 "group": "Waste Management",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Wetlands, forests, and reefs promise flood control and water treatment - but how much protection does nature actually provide, and can it be credited like concrete?",
 "background": "Nature-based solutions (NBS) - restored wetlands for flood attenuation, oyster reefs for storm protection, forests for water treatment - are fashionable in policy, but the performance evidence is thin: flood-reduction claims rest on models, not measurements; the protection varies with storm size in unmapped ways; and the maintenance (a wetland needs tending like infrastructure) is unfunded. The crediting problem is central: engineers size concrete to standards, but there are no standards for how many centimeters of flood a hectare of wetland buys. Without creditable performance, NBS stays in pilot-land.",
 "why_it_matters": "NBS could protect coasts and cities cheaper and greener than concrete - if the protection can be credited. Uncredited nature gets paved.",
 "sig_lens": "The Signature lens reads nature as infrastructure that grows: the protocol must measure its protection like concrete's, and maintain it like concrete's.",
 "sig_solution": LABEL + " Assumptions: (1) NBS performance evidence is model-based; (2) no crediting standards exist. Reasoning path: measure protection directly - instrument NBS sites for flood attenuation and treatment performance, and build the crediting standards from measurement. Proposed mechanism: a growing-infrastructure protocol with performance monitoring at NBS sites, engineering-equivalent crediting standards derived from the measurements, and maintenance funding tied to the credited protection. Confirm: credited NBS attracts infrastructure-scale investment. Kill: the protection proves too variable to credit. Does NOT claim: nature-as-concrete equivalence - it measures and credits what is measured.",
 "pointer": "The Signature system's proposed approach measures NBS performance toward engineering-equivalent crediting; the companion Signature Edition record specifies the growing-infrastructure protocol.",
 "key_points": [
  "NBS flood and treatment claims rest on models, not measurements.",
  "Protection varies with event size in unmapped ways.",
  "No engineering-equivalent crediting standards exist.",
  "Maintenance of living infrastructure is unfunded.",
 ],
 "requirements": [
  "Performance monitoring at NBS sites (flood, treatment).",
  "Crediting standards derived from measurements.",
  "Maintenance funding tied to credited protection.",
 ],
 "citations": [
  "IUCN Global Standard for Nature-based Solutions.",
 ],
 "demo": {"cin": 115.0, "cout": 16.0, "k": 0.57, "t": 2.9},
},
# ----------------------------------------------------------------- rank 31
{
 "key": "ee-ultrafine",
 "name": "The Ultrafine Particulate Measurement Problem",
 "group": "Air Quality",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Ultrafine particles (under 100 nm) may be the most toxic fraction - but they are unregulated and barely measured, so how can the risk be assessed?",
 "background": "Ultrafine particles (UFP) - from combustion, especially traffic - penetrate deep into lungs and possibly the bloodstream; toxicology suggests outsized harm per mass. But regulation counts PM2.5 mass, which UFP barely register on: a million ultrafines weigh less than one coarse particle. Measurement (condensation particle counters) is research-grade, not routine; no ambient standard exists anywhere; and the epidemiology is thin because the exposure data is thin. The regulatory gap is circular: no standard because no data, no data because no standard.",
 "why_it_matters": "The most toxic fraction may be the unmeasured one. Mass-based standards are blind to number-based harm - the regulation measures the wrong thing.",
 "sig_lens": "The Signature lens reads ultrafines as an invisible army: the protocol must count the soldiers (number), not weigh the battalion (mass).",
 "sig_solution": LABEL + " Assumptions: (1) mass standards miss number-based harm; (2) the measurement-regulatory gap is circular. Reasoning path: break the circle - deploy number-based monitoring at scale and build the epidemiology on it. Proposed mechanism: a counting protocol with ultrafine number monitoring networks, epidemiological studies on the number metric, and interim guidance values while standards develop. Confirm: number-monitored areas show actionable exposure patterns. Kill: the health evidence stays thin and the monitoring is precaution without proof. Does NOT claim: a UFP standard - it counts the army so the risk can be assessed.",
 "pointer": "The Signature system's proposed approach builds ultrafine number monitoring toward future standards; the companion Signature Edition record specifies the counting protocol.",
 "key_points": [
  "UFP penetrate deep; toxicology suggests outsized harm per mass.",
  "PM2.5 mass standards barely register ultrafines.",
  "Measurement is research-grade; no ambient standard exists.",
  "The no-standard/no-data circle blocks progress.",
 ],
 "requirements": [
  "Ultrafine number-concentration monitoring networks.",
  "Epidemiology on the number metric.",
  "Interim guidance values during standard development.",
 ],
 "citations": [
  "HEI (2013) Understanding the Health Effects of Ambient Ultrafine Particles.",
 ],
 "demo": {"cin": 45.0, "cout": 5.0, "k": 0.69, "t": 2.0},
},
# ----------------------------------------------------------------- rank 32
{
 "key": "ee-voc",
 "name": "The VOC Removal Efficiency Problem",
 "group": "Air Quality",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Volatile organic compounds drive ozone and carry toxics - but control devices claim efficiencies the field rarely verifies, so what do they actually remove?",
 "background": "VOC controls - thermal oxidizers, carbon adsorbers, biofilters - are permitted at 95-99 percent destruction efficiency, but the numbers come from stack tests under ideal conditions: real operation with varying loads, startup/shutdown, and aging media performs worse, unmeasured. Fugitive emissions (leaks, the largest source in many sectors) evade the control devices entirely. The verification gap means permitted reductions exceed actual ones - the air-quality plans rest on fiction. Continuous monitoring is expensive; periodic testing is gameable.",
 "why_it_matters": "Ozone nonattainment plans assume VOC reductions that may not exist. The verification gap is the difference between the plan and the air.",
 "sig_lens": "The Signature lens reads controls as promises: the protocol must verify the promise in operation, not just at the permit hearing.",
 "sig_solution": LABEL + " Assumptions: (1) permitted efficiencies exceed field performance; (2) fugitives evade controls entirely. Reasoning path: verify continuously - require operational monitoring of control performance and fugitive surveys. Proposed mechanism: a promise protocol with continuous parametric monitoring of control devices, periodic fugitive detection (optical gas imaging), and permitted efficiencies discounted to verified levels. Confirm: verified programs show real emission reductions. Kill: monitoring costs exceed the regulatory will to require it. Does NOT claim: exact VOC accounting - it verifies the promise operationally.",
 "pointer": "The Signature system's proposed approach verifies VOC controls operationally with fugitive surveys; the companion Signature Edition record specifies the promise protocol.",
 "key_points": [
  "Controls are permitted at 95-99 percent; field performance is worse.",
  "Stack tests occur under ideal, gameable conditions.",
  "Fugitive emissions evade control devices entirely.",
  "Air-quality plans rest on unverified reductions.",
 ],
 "requirements": [
  "Continuous parametric monitoring of control devices.",
  "Periodic fugitive-emission surveys.",
  "Permitted efficiencies discounted to verified levels.",
 ],
 "citations": [
  "US EPA Control Techniques Guidelines for VOC sources.",
 ],
 "demo": {"cin": 68.0, "cout": 4.0, "k": 0.78, "t": 1.8},
},
# ----------------------------------------------------------------- rank 33
{
 "key": "ee-sediment",
 "name": "The Contaminated Sediment Remediation Problem",
 "group": "Waste Management",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "River and harbor sediments hold legacy PCBs, mercury, and PAHs - but should they be dredged, capped, or left alone when each option risks spreading the contamination?",
 "background": "Contaminated sediments (Hudson River PCBs, Fox River, harbor Superfund sites) present a trilemma: dredging removes mass but resuspends contaminants during the work; capping isolates but can fail; monitored natural recovery is slow and uncertain. The remedies cost hundreds of millions and take decades; the resuspension during dredging has sometimes worsened conditions temporarily. The bioavailability question - how much of the sediment contaminant actually enters the food web - should drive the remedy but is hard to measure. Each site relitigates the trilemma with incomplete science.",
 "why_it_matters": "Sediment remedies are among the costliest cleanups, and the wrong choice spreads contamination or wastes hundreds of millions. The trilemma has no general answer.",
 "sig_lens": "The Signature lens reads sediments as a sleeping hazard: the protocol must decide whether to operate, sedate, or watch - based on the bioavailable risk, not the total mass.",
 "sig_solution": LABEL + " Assumptions: (1) dredging resuspends; capping can fail; natural recovery is slow; (2) bioavailability should drive the remedy. Reasoning path: remedy to the bioavailable risk - measure what enters the food web, and choose the option minimizing it. Proposed mechanism: a sleeping-hazard protocol with bioavailability assessment (porewater, tissue), remedy selection on bioavailable-risk reduction, and resuspension controls plus monitoring during active remedies. Confirm: bioavailability-driven remedies achieve risk goals at lower cost. Kill: bioavailability proves unmeasurable and the trilemma persists. Does NOT claim: a universal sediment remedy - it remedies the risk, not the mass.",
 "pointer": "The Signature system's proposed approach selects sediment remedies on bioavailable risk; the companion Signature Edition record specifies the sleeping-hazard protocol.",
 "key_points": [
  "Dredging removes mass but resuspends contaminants.",
  "Capping isolates but can fail; natural recovery is slow.",
  "Remedies cost hundreds of millions over decades.",
  "Bioavailability, not total mass, should drive remedy choice.",
 ],
 "requirements": [
  "Bioavailability assessment via porewater and tissue.",
  "Remedy selection on bioavailable-risk reduction.",
  "Resuspension controls and monitoring during active remedies.",
 ],
 "citations": [
  "US EPA (2005) Contaminated Sediment Remediation Guidance for Hazardous Waste Sites.",
 ],
 "demo": {"cin": 210.0, "cout": 32.0, "k": 0.5, "t": 3.3},
},
# ----------------------------------------------------------------- rank 34
{
 "key": "ee-unified-systems",
 "name": "The Unified Environmental Systems Problem",
 "group": "Air Quality",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Air, water, waste, and climate are managed in silos - but the problems cross every boundary, so can environmental protection be designed as one system?",
 "background": "Environmental management is siloed by medium: air offices, water offices, waste offices - each with its own laws, each optimizing its own medium. But the problems cross: air controls make solid waste, water treatment makes air emissions, waste decisions affect climate. The multimedia tradeoff is handled by nobody: a regulation that cleans water by dirtying air is a success in one office and a failure in the next. Integrated assessment (life-cycle thinking, multimedia modeling) exists academically; institutionally, the silos are law. The system optimum is nobody's mandate.",
 "why_it_matters": "Siloed optimization manufactures problem-shifting: solved in one medium, created in another. The planet is one system; the management is many fiefdoms.",
 "sig_lens": "The Signature lens reads the environment as one patient with many specialists: the protocol must give the specialists a shared chart, or accept contradictory treatments.",
 "sig_solution": LABEL + " Assumptions: (1) multimedia tradeoffs are real and unmanaged; (2) institutional silos are legal, not just cultural. Reasoning path: assess multimedia consequences for every major decision - require the cross-medium ledger before approval. Proposed mechanism: a shared-chart protocol mandating multimedia impact assessment for major environmental decisions, cross-office review of medium-shifting rules, and a unified environmental accounting framework. Confirm: charted decisions show less problem-shifting. Kill: the silos reject the shared chart and the accounting is decorative. Does NOT claim: unified environmental management - it builds the shared chart the system lacks.",
 "pointer": "The Signature system's proposed approach mandates multimedia ledgers for environmental decisions; the companion Signature Edition record specifies the shared-chart protocol.",
 "key_points": [
  "Environmental management is siloed by medium with separate laws.",
  "Air controls make waste; water treatment makes emissions.",
  "No institution owns the multimedia tradeoff.",
  "Integrated assessment exists academically, not institutionally.",
 ],
 "requirements": [
  "Multimedia impact assessment for major decisions.",
  "Cross-office review of medium-shifting rules.",
  "A unified environmental accounting framework.",
 ],
 "citations": [
  "US EPA (1992) Safeguarding the Future: Credible Science, Credible Decisions (multimedia).",
 ],
 "demo": {"cin": 125.0, "cout": 15.0, "k": 0.58, "t": 3.0},
},
]
