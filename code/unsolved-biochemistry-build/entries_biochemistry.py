#!/usr/bin/env python3
"""Entries for The Unsolved Biochemistry Database (unsolved-biochemistry) and its
Signature half (unsolved-biochemistry-signature).

34 famous unsolved problems in biochemistry, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
through the Signature lens, ALWAYS labeled as proposals, never established
science.

ID prefixes JAH-USBC- / JAH-USBCS- verified free in manifest id_prefix
values (exact + substring, both directions).
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

FIELD = {
 "tag": "biochemistry",
 "disp": "biochemistry",
 "name": "The Unsolved Biochemistry Database",
 "sig_name": "The Unsolved Biochemistry Signature Database",
 "prefix": "JAH-USBC-",
 "sig_prefix": "JAH-USBCS-",
 "ai": "JAH Unsolved Biochemistry Archivist",
 "tagline": ("Thirty-four famous open problems in biochemistry, from protein folding to the chemistry of the "
             "origin: real, fact-checked, each with its full story and a clearly labeled Signature proposed solution."),
 "sig_tagline": ("His original Signature solution method applied to all 34 great open problems of biochemistry: "
                 "Signature-generated proposed solutions with assumptions declared, confirm and refute conditions "
                 "stated, and limits honestly marked. Clearly labeled Signature-made, never established science."),
 "pub_line": ("Public records - 34 famous open problems in biochemistry, real and fact-checked: protein folding "
              "pathways, enzyme catalysis, allostery, disordered proteins, membrane proteins, aggregation, "
              "chaperones, metabolic networks, the glycan code, and photosynthesis efficiency - every record "
              "carrying the problem statement, background, why it matters, key points, requirements, standards, "
              "citations, and a working solution-explorer demonstration, organized in the Signature system."),
 "sig_line": ("Signature originals - his original Signature solution method: the same 34 famous unsolved "
              "biochemistry problems approached as a covenant between the known and the unknown, each carrying "
              "the full Signature-generated proposed solution with its assumptions declared, its confirm and "
              "refute conditions stated, and its limits honestly marked. Clearly labeled Signature-made, never "
              "presented as established science or authentic public record."),
 "ladder_text": (" Records are ordered by the teaching ladder: Foundations (folding pathways, protein dynamics, "
                 "enzyme catalysis, allostery, protein interactions, disordered proteins, membrane proteins, "
                 "aggregation, chaperones, metabolic networks, glycan code) -> Compounded (photosynthesis "
                 "efficiency, nitrogen fixation, carbon fixation, oxidative phosphorylation, signal transduction, "
                 "calcium signaling, apoptosis regulation, cell-cycle control, DNA repair choice, epigenetic "
                 "inheritance, histone code, noncoding RNA) -> Advanced (prebiotic chemistry, homochirality, "
                 "minimal genome, synthetic cell, metabolomics identification, proteoforms, PTM code, lipid rafts, "
                 "biomolecular condensates, systems biochemistry, unified biochemistry)."),
 "search_ph": ("Search protein folding, enzymes, allostery, photosynthesis, signaling, epigenetics, origin of "
               "life..."),
 "chat_ph": "Ask about the great open problems of biochemistry...",
 "greet_pub": ("I am the JAH Unsolved Biochemistry Archivist. Ask me about the great open problems of "
               "biochemistry - from protein folding, enzymes, and allostery through photosynthesis and signaling, "
               "to epigenetics, condensates, and the chemistry of the origin of life."),
 "greet_sig": ("I am the JAH Unsolved Biochemistry Archivist (Signature). Ask me about the Signature proposed "
               "solutions to the great open problems of biochemistry - every approach labeled as a proposal, "
               "never established science."),
 "role_pub": ("unsolved biochemistry archivist - the great open problems of biochemistry, from protein folding, "
              "enzymes, and allostery through photosynthesis and signaling, to epigenetics, condensates, and the "
              "chemistry of the origin of life; teaches progressively along the ladder from foundations through "
              "compounded to advanced; answers from many angles - definition, example, analogy, application, "
              "history, math - using only archive data from this system"),
 "role_sig": ("unsolved biochemistry archivist - Signature editions: his original Signature solution method "
              "applied to the 34 great open problems of biochemistry, each carrying the full Signature-generated "
              "proposed solution, clearly labeled Signature-made and never presented as established science; "
              "teaches progressively along the ladder from foundations through compounded to advanced; answers "
              "from many angles - definition, example, analogy, application, history, math - using only archive "
              "data from this system"),
 "gen_desc": "Generate clearly-labeled unsolved biochemistry studies. Seeded archive records are the authoritative entries.",
 "standards": [
  "Problem statements verified against the published literature; open status confirmed as of 2026.",
  "Quantitative claims cross-checked against standard references (Lehninger Principles of Biochemistry; Berg, Tymoczko, and Stryer, Biochemistry).",
  "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
 ],
 "sig_tail": ("Signature editions carry the Signature system's proposed solution approaches to famous "
              "unsolved problems. Every solution is labeled a Signature-generated proposal, never "
              "established science, never peer-accepted, never proof."),
}

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "bc-folding-path",
 "name": "The Protein Folding Pathway Problem",
 "group": "Proteins",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "AlphaFold predicts structures - but how do proteins actually fold, through which pathways and intermediate states?",
 "background": "The folding-pathway problem - the routes proteins take to their native states - persists after AlphaFold's structure-prediction triumph: the endpoint is predicted, but the pathway (intermediates, transition states, timescales) is not. Levinthal's paradox (random search would take forever) is resolved in principle (funneled landscapes) but not in practice for most proteins: single-molecule experiments reveal heterogeneous pathways, and misfolding routes (to amyloid) compete. Structure prediction solved the destination; the journey is still mapped protein by protein.",
 "why_it_matters": "Misfolding causes Alzheimer's, Parkinson's, prion diseases. The pathways - not just the endpoints - are the disease mechanisms.",
 "sig_lens": "The Signature lens reads folding as the journey, not the destination: the protocol must map the roads (pathways) since the map app (AlphaFold) only shows the address.",
 "sig_solution": LABEL + " Assumptions: (1) endpoints predicted; pathways not; (2) misfolding routes compete. Reasoning path: map pathways systematically - single-molecule folding, Markov-state models from simulations, and misfolding-route characterization. Proposed mechanism: a journey protocol with pathway-mapping for disease-relevant proteins, simulation-experiment integration (Markov models validated on single-molecule data), and misfolding-route targeting for therapeutics. Confirm: mapped pathways predict folding kinetics and misfolding. Kill: pathways prove too heterogeneous to generalize. Does NOT claim: universal folding pathways - it maps the roads protein by protein.",
 "pointer": "The Signature system's proposed approach maps protein folding pathways with single-molecule and simulation methods; the companion Signature Edition record specifies the journey protocol.",
 "key_points": [
  "AlphaFold predicts endpoints, not pathways.",
  "Funneled landscapes resolve Levinthal's paradox in principle.",
  "Single-molecule experiments show heterogeneous pathways.",
  "Misfolding routes to amyloid compete with folding.",
 ],
 "requirements": [
  "Single-molecule folding-pathway measurements.",
  "Markov-state models validated on experiments.",
  "Misfolding-route characterization for disease proteins.",
 ],
 "citations": [
  "Dill KA, MacCallum JL (2012) The protein-folding problem, 50 years on. Science 338.",
 ],
 "demo": {"vmax": 100.0, "km": 10.0, "s": [2.0, 10.0, 50.0]},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "bc-dynamics",
 "name": "The Protein Dynamics Problem",
 "group": "Proteins",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Proteins are machines that move - but how do their motions relate to function, and can dynamics be predicted from structure?",
 "background": "The protein-dynamics problem - the relationship between conformational motions and function - is the post-AlphaFold frontier: structures are static snapshots; function lives in the ensemble (allosteric transitions, enzyme conformational changes, induced fit). NMR, cryo-EM classification, and MD simulations probe the dynamics, but the functionally relevant motions are hard to separate from thermal noise, and predicting dynamics from sequence remains out of reach. The structure-function paradigm needs a dynamics-function update.",
 "why_it_matters": "Drug binding, enzyme catalysis, and signaling all depend on protein motions. Static structures miss the moving target.",
 "sig_lens": "The Signature lens reads proteins as machines, not statues: the protocol must film the machine (dynamics) and link each motion to its job.",
 "sig_solution": LABEL + " Assumptions: (1) function lives in the ensemble; (2) relevant motions hard to separate from noise. Reasoning path: link motions to function - correlate dynamics measurements with functional assays, and predict dynamics computationally. Proposed mechanism: a machines protocol with dynamics-function correlation studies (NMR, cryo-EM, single-molecule), MD-based dynamics prediction benchmarked on experiments, and drug design targeting dynamic states. Confirm: dynamics predictions match functional measurements. Kill: the relevant motions prove inseparable from noise. Does NOT claim: dynamics predicted from sequence - it films the machine and links motions to jobs.",
 "pointer": "The Signature system's proposed approach links protein dynamics to function experimentally and computationally; the companion Signature Edition record specifies the machines protocol.",
 "key_points": [
  "Function lives in the conformational ensemble.",
  "NMR, cryo-EM, MD probe dynamics complementarily.",
  "Relevant motions hide in thermal noise.",
  "Dynamics prediction from sequence is out of reach.",
 ],
 "requirements": [
  "Dynamics-function correlation experiments.",
  "MD dynamics benchmarks on measurements.",
  "Drug design on dynamic states.",
 ],
 "citations": [
  "Henzler-Wildman K, Kern D (2007) Dynamic personalities of proteins. Nature 450.",
 ],
 "demo": {"vmax": 80.0, "km": 5.0, "s": [1.0, 5.0, 25.0]},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "bc-catalysis",
 "name": "The Enzyme Catalysis Problem",
 "group": "Enzymes",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Enzymes accelerate reactions by factors of 10^17 - but how, exactly, and how much do dynamics and tunneling contribute?",
 "background": "The enzyme-catalysis problem - the physical origin of enzymatic rate enhancements - is debated after decades: transition-state stabilization (Pauling) is the textbook answer, but the roles of protein dynamics (promoting vibrations?), hydrogen tunneling (large kinetic isotope effects), and electrostatic preorganization are contested. QM/MM simulations reproduce rates but the interpretation varies. The debate matters for enzyme design: the de novo enzymes (Baker lab) work but far below natural efficiencies - the missing catalytic understanding is the design gap.",
 "why_it_matters": "Enzyme design for industry and medicine needs the catalytic principles. The 10^17 acceleration's mechanism is the design manual.",
 "sig_lens": "The Signature lens reads enzymes as the perfect catalysts: the protocol must dissect the acceleration's ingredients - electrostatics, dynamics, tunneling - quantitatively.",
 "sig_solution": LABEL + " Assumptions: (1) transition-state stabilization is the base; (2) dynamics/tunneling roles contested. Reasoning path: quantify each ingredient - electrostatic preorganization, tunneling contributions, dynamical effects - per enzyme class. Proposed mechanism: a catalysts protocol with ingredient-decomposed catalysis studies (KIE, Stark spectroscopy, QM/MM), de novo enzyme benchmarking against the decomposition, and design rules from the quantified ingredients. Confirm: designed enzymes approach natural efficiencies. Kill: the ingredients prove inseparable. Does NOT claim: the catalytic mechanism - it quantifies each ingredient.",
 "pointer": "The Signature system's proposed approach decomposes enzymatic rate enhancements ingredient by ingredient; the companion Signature Edition record specifies the catalysts protocol.",
 "key_points": [
  "Enzymes accelerate reactions up to 10^17-fold.",
  "Transition-state stabilization is the textbook base.",
  "Dynamics, tunneling, electrostatics roles contested.",
  "De novo enzymes work far below natural efficiency.",
 ],
 "requirements": [
  "Ingredient-decomposed catalysis measurements.",
  "De novo enzyme benchmarking.",
  "Design rules from quantified ingredients.",
 ],
 "citations": [
  "Warshel A et al. (2006) Electrostatic basis for enzyme catalysis. Chemical Reviews 106.",
 ],
 "demo": {"vmax": 120.0, "km": 15.0, "s": [3.0, 15.0, 75.0]},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "bc-allostery",
 "name": "The Allostery Problem",
 "group": "Proteins",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Binding at one site changes a distant site - but how does the allosteric signal travel through the protein?",
 "background": "The allostery problem - long-range communication within proteins - has models (MWC concerted, KNF sequential, ensemble/population-shift) but the physical signal's path is elusive: the 'pathways' of correlated motions are statistical, not mechanical linkages, and the energetic contributions (entropy vs enthalpy) vary. Cryptic allosteric sites (hidden pockets) are drug targets - but predicting them is unreliable. Allostery is everywhere in regulation; its mechanism is described, not derived.",
 "why_it_matters": "Allosteric drugs are the precision tools of pharmacology. Unpredictable allosteric sites are missed drug targets.",
 "sig_lens": "The Signature lens reads allostery as the protein's telephone: the protocol must trace the wires (correlated motions) and find the hidden extensions (cryptic sites).",
 "sig_solution": LABEL + " Assumptions: (1) signal paths are statistical, not mechanical; (2) cryptic sites unpredictable. Reasoning path: map the communication - dynamics-based allosteric network analysis validated by mutagenesis - and hunt cryptic sites systematically. Proposed mechanism: a telephone protocol with allosteric-network mapping (NMR, MD, mutagenesis), cryptic-site screening (fragment methods, mixed-solvent MD), and allosteric-drug design on the mapped networks. Confirm: mapped networks predict allosteric mutations. Kill: the networks prove non-predictive. Does NOT claim: the allosteric mechanism - it traces the wires.",
 "pointer": "The Signature system's proposed approach maps allosteric networks and hunts cryptic sites; the companion Signature Edition record specifies the telephone protocol.",
 "key_points": [
  "MWC, KNF, ensemble models describe; mechanism elusive.",
  "Correlated-motion pathways are statistical.",
  "Cryptic allosteric sites are valuable drug targets.",
  "Predicting cryptic sites is unreliable.",
 ],
 "requirements": [
  "Dynamics-based allosteric network mapping.",
  "Mutagenesis validation of networks.",
  "Systematic cryptic-site screening.",
 ],
 "citations": [
  "Changeux JP (2012) Allostery and the Monod-Wyman-Changeux model. Annual Review Biophysics 41.",
 ],
 "demo": {"vmax": 90.0, "km": 8.0, "s": [2.0, 8.0, 40.0]},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "bc-ppi",
 "name": "The Protein Protein Interaction Problem",
 "group": "Proteins",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Proteins work in interaction networks - but how can the interactome be mapped completely, and which interactions actually matter in the cell?",
 "background": "The interactome problem - mapping all protein-protein interactions - is incomplete: high-throughput methods (Y2H, AP-MS) each miss classes (transient, membrane, context-dependent), and the human interactome's size is estimated, not known. Worse, the functional relevance is unclear: many detected interactions are non-functional in vivo. The network's dynamics (interactions changing with cell state) are barely mapped. The wiring diagram is partial and unlabeled.",
 "why_it_matters": "Disease mutations perturb interaction networks. The incomplete, unlabeled wiring diagram limits network medicine.",
 "sig_lens": "The Signature lens reads the interactome as the cell's social network: the protocol must verify the friendships (in vivo) and learn which ones matter.",
 "sig_solution": LABEL + " Assumptions: (1) methods miss interaction classes; (2) functional relevance unclear. Reasoning path: map in vivo and dynamically - context-dependent interactomes with functional readouts. Proposed mechanism: a social-network protocol with in-vivo interaction mapping (proximity labeling), dynamic interactomes across cell states, and functional validation of key interactions. Confirm: validated dynamic networks predict perturbation outcomes. Kill: the interactions prove too context-dependent to map usefully. Does NOT claim: the complete interactome - it verifies the friendships that matter.",
 "pointer": "The Signature system's proposed approach maps dynamic in-vivo interactomes with functional validation; the companion Signature Edition record specifies the social-network protocol.",
 "key_points": [
  "Y2H and AP-MS each miss interaction classes.",
  "Human interactome size estimated, not known.",
  "Many detected interactions non-functional in vivo.",
  "Dynamic (state-dependent) networks barely mapped.",
 ],
 "requirements": [
  "In-vivo proximity-labeling interaction maps.",
  "Dynamic interactomes across cell states.",
  "Functional validation of key interactions.",
 ],
 "citations": [
  "Luck K et al. (2020) A reference map of the human binary protein interactome. Nature 580.",
 ],
 "demo": {"vmax": 110.0, "km": 12.0, "s": [2.5, 12.0, 60.0]},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "bc-idp",
 "name": "The Intrinsically Disordered Proteins Problem",
 "group": "Proteins",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "A third of proteins lack fixed structures - but how do disordered proteins function, and how can their ensembles be described?",
 "background": "The IDP problem - intrinsically disordered proteins/regions function without folding - challenges structure-function: the ensemble (not a structure) is the functional state, described by polymer-physics parameters (Rg, scaling exponents) that are hard to measure and harder to predict. IDPs mediate signaling, phase separation, and regulation; their misbehavior aggregates in disease. The sequence-ensemble-function relationship is the missing theory. Disorder is functional; the function-ensemble map is uncharted.",
 "why_it_matters": "IDPs run signaling and phase separation; their aggregation causes disease. The uncharted ensemble-function map is the drug-design gap.",
 "sig_lens": "The Signature lens reads IDPs as the shapeless workers: the protocol must describe the worker's habits (ensemble) and link them to the job.",
 "sig_solution": LABEL + " Assumptions: (1) ensemble is the functional state; (2) sequence-ensemble-function unmapped. Reasoning path: map ensembles to function - integrative ensemble determination (SAXS, NMR, FRET, simulations) correlated with functional assays. Proposed mechanism: a workers protocol with ensemble-determination pipelines, sequence-ensemble predictors trained on the data, and IDP-targeted drug strategies (ensemble modulators). Confirm: ensemble predictions match functional outcomes. Kill: the ensembles prove too heterogeneous. Does NOT claim: the IDP function code - it charts the habits.",
 "pointer": "The Signature system's proposed approach maps IDP ensembles to function; the companion Signature Edition record specifies the workers protocol.",
 "key_points": [
  "~1/3 of proteins have disordered regions.",
  "The ensemble, not a structure, is functional.",
  "IDPs mediate signaling and phase separation.",
  "Sequence-ensemble-function relationship unmapped.",
 ],
 "requirements": [
  "Integrative ensemble-determination pipelines.",
  "Sequence-ensemble predictors.",
  "IDP ensemble-modulator drug strategies.",
 ],
 "citations": [
  "Wright PE, Dyson HJ (2015) Intrinsically disordered proteins in cellular signalling. Nature Reviews MCB 16.",
 ],
 "demo": {"vmax": 70.0, "km": 6.0, "s": [1.5, 6.0, 30.0]},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "bc-membrane",
 "name": "The Membrane Protein Problem",
 "group": "Proteins",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Membrane proteins are the majority drug target - but why are their structures and mechanisms still the hardest to determine?",
 "background": "The membrane-protein problem - structures and mechanisms of the lipid-embedded majority of drug targets - is easing (cryo-EM revolution: GPCRs, ion channels solved in flurry) but the mechanisms lag: the lipid environment's role, the conformational cycles, and the drug-binding kinetics in native membranes are hard. Expression and purification remain bottlenecks; the structures are detergent-extracted approximations. The drug targets are imaged; their native mechanisms are half-known.",
 "why_it_matters": "Most drugs target membrane proteins. Native mechanisms - not detergent structures - decide drug action.",
 "sig_lens": "The Signature lens reads membrane proteins as machines in their native grease: the protocol must study them in the membrane, not just in the detergent.",
 "sig_solution": LABEL + " Assumptions: (1) cryo-EM eased structures; mechanisms lag; (2) detergent extracts approximate. Reasoning path: go native - in-membrane structural methods (cryo-ET, native MS, nanodiscs) and lipid-dependence studies. Proposed mechanism: a grease protocol with native-membrane structural pipelines, lipid-environment mechanism studies, and drug kinetics measured in native-like systems. Confirm: native mechanisms differ informatively from detergent ones. Kill: native methods never reach the needed resolution. Does NOT claim: all native mechanisms - it studies the machines in their grease.",
 "pointer": "The Signature system's proposed approach studies membrane proteins in native lipid environments; the companion Signature Edition record specifies the grease protocol.",
 "key_points": [
  "Membrane proteins are the majority drug target class.",
  "Cryo-EM solved many structures; mechanisms lag.",
  "Lipid environment's mechanistic role is hard to study.",
  "Detergent extraction approximates the native state.",
 ],
 "requirements": [
  "Native-membrane structural methods.",
  "Lipid-dependence mechanism studies.",
  "Native-like drug kinetics measurements.",
 ],
 "citations": [
  "Cheng Y (2018) Membrane protein structural biology in the era of single particle cryo-EM. Current Opinion Structural Biology 52.",
 ],
 "demo": {"vmax": 95.0, "km": 9.0, "s": [2.0, 9.0, 45.0]},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "bc-aggregation",
 "name": "The Protein Aggregation Problem",
 "group": "Proteins",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Proteins aggregate into amyloids in Alzheimer's, Parkinson's, and prion diseases - but what are the toxic species, and how does aggregation begin?",
 "background": "The aggregation problem - which species (oligomers? fibrils?) are toxic, and how aggregation nucleates - is the neurodegeneration bottleneck: the amyloid hypothesis (fibrils as cause) is challenged by oligomer toxicity evidence and the weak plaque-cognition correlation; secondary nucleation and fragmentation kinetics are modeled but the in-vivo triggers unknown. Anti-amyloid antibodies (aducanumab, lecanemab) show the target matters but modestly. The toxic species is unidentified; the nucleation trigger unknown.",
 "why_it_matters": "Neurodegeneration's mechanism is the aggregation question. The unidentified toxic species is the drug target.",
 "sig_lens": "The Signature lens reads aggregation as the cascade: the protocol must find the toxic link (species) and the first domino (nucleation trigger).",
 "sig_solution": LABEL + " Assumptions: (1) toxic species unidentified; oligomers suspected; (2) in-vivo triggers unknown. Reasoning path: identify the toxic species - isolate and characterize oligomers functionally - and find the nucleation triggers in vivo. Proposed mechanism: a cascade protocol with toxic-species isolation and functional testing, in-vivo nucleation-trigger hunts, and therapeutics targeting the identified species. Confirm: the identified species drives toxicity. Kill: the species prove heterogeneous and untargetable. Does NOT claim: the toxic species - it finds the domino.",
 "pointer": "The Signature system's proposed approach identifies toxic aggregation species and nucleation triggers; the companion Signature Edition record specifies the cascade protocol.",
 "key_points": [
  "Oligomers suspected; fibrils' role challenged.",
  "Plaque-cognition correlation is weak.",
  "In-vivo nucleation triggers unknown.",
  "Anti-amyloid antibodies show modest effects.",
 ],
 "requirements": [
  "Toxic-species isolation and functional testing.",
  "In-vivo nucleation-trigger studies.",
  "Species-targeted therapeutics.",
 ],
 "citations": [
  "Knowles TPJ et al. (2014) The amyloid state and its association with protein misfolding diseases. Nature Reviews MCB 15.",
 ],
 "demo": {"vmax": 60.0, "km": 4.0, "s": [1.0, 4.0, 20.0]},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "bc-chaperone",
 "name": "The Chaperone Mechanism Problem",
 "group": "Proteins",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Chaperones help proteins fold - but how do GroEL, Hsp70, and the chaperone networks actually work?",
 "background": "The chaperone-mechanism problem - how GroEL/GroES (the Anfinsen cage), Hsp70 (the unfoldase/holdase), and TRiC assist folding - is partially solved structurally but mechanistically debated: passive (preventing aggregation) vs active (reshaping the landscape) models compete; the ATP-driven cycles' coupling to folding is unclear; and the cellular chaperone network's coordination (handoff between systems) is unmapped. The folding assistants' methods are half-known.",
 "why_it_matters": "Chaperones are the cell's folding quality control. Their mechanisms are the biotechnology of assisted folding.",
 "sig_lens": "The Signature lens reads chaperones as the folding coaches: the protocol must learn the coaching methods - cage, unfoldase, handoff - play by play.",
 "sig_solution": LABEL + " Assumptions: (1) structures known; mechanisms debated; (2) network coordination unmapped. Reasoning path: watch the coaching - single-molecule chaperone-substrate studies resolving the ATP-coupled steps. Proposed mechanism: a coaches protocol with single-molecule mechanism studies, network-handoff mapping, and chaperone-assisted folding biotechnology. Confirm: the mechanisms predict chaperone function. Kill: the mechanisms prove too complex to generalize. Does NOT claim: the chaperone mechanism - it learns the coaching plays.",
 "pointer": "The Signature system's proposed approach resolves chaperone mechanisms with single-molecule studies; the companion Signature Edition record specifies the coaches protocol.",
 "key_points": [
  "GroEL cage, Hsp70, TRiC mechanisms debated.",
  "Passive vs active assistance models compete.",
  "ATP-cycle coupling to folding unclear.",
  "Chaperone-network handoffs unmapped.",
 ],
 "requirements": [
  "Single-molecule chaperone mechanism studies.",
  "Network-handoff mapping.",
  "Chaperone-assisted folding biotechnology.",
 ],
 "citations": [
  "Hartl FU et al. (2011) Molecular chaperones in protein folding and proteostasis. Nature 475.",
 ],
 "demo": {"vmax": 85.0, "km": 7.0, "s": [1.5, 7.0, 35.0]},
},
# ----------------------------------------------------------------- rank 10
{
 "key": "bc-metabolic-net",
 "name": "The Metabolic Network Problem",
 "group": "Metabolism",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Metabolism is a network of thousands of reactions - but how is the whole network regulated, and can it be modeled predictively?",
 "background": "The metabolic-network problem - whole-cell metabolic regulation and prediction - has tools (flux-balance analysis, kinetic models) but the regulation is distributed: allosteric, transcriptional, post-translational layers interact, and the kinetic parameters for most enzymes are unknown. FBA predicts growth phenotypes but not dynamics; kinetic models need the missing parameters. The metabolome's measurement lags the genome's. The network is mapped; its regulation is half-known.",
 "why_it_matters": "Metabolic engineering (biofuels, drugs) needs predictive network models. The missing kinetics are the engineering gap.",
 "sig_lens": "The Signature lens reads metabolism as the city's traffic: the protocol must learn the traffic lights (regulation) at every layer, not just the road map.",
 "sig_solution": LABEL + " Assumptions: (1) regulation multi-layered; (2) kinetic parameters mostly unknown. Reasoning path: measure the regulation - multi-omics with kinetic parameter determination for key nodes. Proposed mechanism: a traffic protocol with layer-resolved regulation mapping, kinetic-parameter measurement programs, and dynamic metabolic models validated on perturbations. Confirm: the models predict perturbation outcomes. Kill: the parameters stay unmeasurable at scale. Does NOT claim: the whole network modeled - it learns the traffic lights.",
 "pointer": "The Signature system's proposed approach maps multi-layer metabolic regulation with kinetics; the companion Signature Edition record specifies the traffic protocol.",
 "key_points": [
  "Regulation spans allosteric, transcriptional, PTM layers.",
  "Most enzyme kinetic parameters unknown.",
  "FBA predicts growth, not dynamics.",
  "Metabolome measurement lags genome.",
 ],
 "requirements": [
  "Layer-resolved regulation mapping.",
  "Kinetic-parameter measurement programs.",
  "Perturbation-validated dynamic models.",
 ],
 "citations": [
  "Nielsen J, Keasling JD (2016) Engineering cellular metabolism. Cell 164.",
 ],
 "demo": {"vmax": 105.0, "km": 11.0, "s": [2.5, 11.0, 55.0]},
},
# ----------------------------------------------------------------- rank 11
{
 "key": "bc-glycan",
 "name": "The Glycan Code Problem",
 "group": "Carbohydrates",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Sugars coat every cell in complex patterns - but what information does the glycan code carry, and how is it read?",
 "background": "The glycan code - the information in cell-surface glycosylation patterns - is the least-decoded biological code: glycans are not template-encoded (built by enzyme networks), their structures are heterogeneous, and the readers (lectins, antibodies) are promiscuous. Glycosylation affects every therapeutic protein (antibody effector function), viral entry (influenza, SARS-CoV-2), and immune recognition - yet glycan analysis lags genomics/proteomics by decades. The code is written everywhere and read poorly.",
 "why_it_matters": "Glycans control therapeutic antibodies, viral entry, and immunity. The unread code is the biopharmaceutical gap.",
 "sig_lens": "The Signature lens reads glycans as the cell's handwriting: the protocol must learn the script (structures) and the readers (lectins) together.",
 "sig_solution": LABEL + " Assumptions: (1) glycans not template-encoded; heterogeneous; (2) analysis lags decades. Reasoning path: decode systematically - high-throughput glycan sequencing with reader-specificity mapping. Proposed mechanism: a handwriting protocol with glycan-structure determination pipelines, lectin/reader specificity maps, and glyco-engineering for therapeutics. Confirm: decoded patterns predict reader binding and function. Kill: the heterogeneity defeats decoding. Does NOT claim: the glycan code cracked - it learns script and readers.",
 "pointer": "The Signature system's proposed approach decodes glycan patterns with reader-specificity mapping; the companion Signature Edition record specifies the handwriting protocol.",
 "key_points": [
  "Glycans not template-encoded; built by enzyme networks.",
  "Structures heterogeneous; readers promiscuous.",
  "Controls antibody function, viral entry, immunity.",
  "Glycan analysis lags genomics by decades.",
 ],
 "requirements": [
  "High-throughput glycan sequencing.",
  "Reader-specificity maps.",
  "Glyco-engineering for therapeutics.",
 ],
 "citations": [
  "Varki A (2017) Biological roles of glycans. Glycobiology 27.",
 ],
 "demo": {"vmax": 75.0, "km": 6.5, "s": [1.5, 6.5, 32.0]},
},
# ----------------------------------------------------------------- rank 12
{
 "key": "bc-photosynthesis",
 "name": "The Photosynthesis Efficiency Problem",
 "group": "Energy",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Photosynthesis powers the biosphere at ~1% efficiency - but what limits it, and can the efficiency be engineered higher?",
 "background": "The photosynthesis-efficiency problem - crops convert ~1% of sunlight to biomass vs ~4.6% theoretical for C3 - has known loss points: photorespiration (RuBisCO's oxygenase activity wastes ~25%), light-saturation, and canopy architecture. Engineering successes (South et al.'s photorespiration bypass: +40% biomass in trials) prove the headroom; but the gains' field robustness and the regulatory complexity are open. The biosphere's engine has upgrade room - the engineering is young.",
 "why_it_matters": "Crop yields must rise on limited land. Photosynthesis upgrades are the yield frontier.",
 "sig_lens": "The Signature lens reads photosynthesis as the improvable engine: the protocol must fix the known leaks (photorespiration) and test the upgrades in the field.",
 "sig_solution": LABEL + " Assumptions: (1) ~1% realized vs 4.6% theoretical; (2) photorespiration the biggest leak. Reasoning path: engineer the leaks - photorespiration bypasses, RuBisCO improvements, canopy optimization - validated in field trials. Proposed mechanism: an engine protocol with loss-point-targeted engineering, multi-year field validation, and stacked improvements. Confirm: field-validated yield gains stack. Kill: the gains fail in real fields. Does NOT claim: the efficiency limit reached - it fixes the leaks.",
 "pointer": "The Signature system's proposed approach engineers photosynthesis loss points with field validation; the companion Signature Edition record specifies the engine protocol.",
 "key_points": [
  "Crops ~1% efficient vs 4.6% theoretical (C3).",
  "Photorespiration wastes ~25% via RuBisCO oxygenase.",
  "Bypass engineering showed +40% biomass in trials.",
  "Field robustness of gains is open.",
 ],
 "requirements": [
  "Loss-point-targeted photosynthesis engineering.",
  "Multi-year field-trial validation.",
  "Stacked improvement strategies.",
 ],
 "citations": [
  "South PF et al. (2019) Synthetic glycolate metabolism pathways stimulate crop growth. Science 363.",
 ],
 "demo": {"vmax": 130.0, "km": 20.0, "s": [4.0, 20.0, 100.0]},
},
# ----------------------------------------------------------------- rank 13
{
 "key": "bc-nitrogen-fix",
 "name": "The Nitrogen Fixation Problem",
 "group": "Energy",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Nitrogenase fixes nitrogen at room temperature - but how does the enzyme break the N2 triple bond, and can cereals be engineered to fix their own?",
 "background": "The nitrogen-fixation problem - nitrogenase's mechanism (the FeMo cofactor's N2 reduction steps) remains partially unresolved despite structures: the exact intermediates and the ATP-coupling are debated. The applied dream - engineering nitrogen fixation into cereals - faces the oxygen-sensitivity and the 16-ATP cost: the enzyme is poisoned by the oxygen photosynthesis makes. Synthetic biology approaches (minimal nif clusters) progress slowly. The enzyme that feeds half the world is mechanistically half-known.",
 "why_it_matters": "Nitrogen fertilizer feeds billions with huge energy and pollution costs. Self-fertilizing cereals would transform agriculture.",
 "sig_lens": "The Signature lens reads nitrogenase as the priceless catalyst: the protocol must learn its trick (the mechanism) and teach it to cereals.",
 "sig_solution": LABEL + " Assumptions: (1) FeMo-cofactor intermediates debated; (2) oxygen sensitivity blocks cereals. Reasoning path: resolve the mechanism's intermediates (spectroscopy, theory) and engineer oxygen-tolerant minimal systems. Proposed mechanism: a catalyst protocol with intermediate-resolved mechanism studies, minimal-nif synthetic biology, and cereal-engineering on the resolved mechanism. Confirm: the mechanism's intermediates identified; fixation in cereals. Kill: the oxygen problem proves insurmountable. Does NOT claim: the mechanism solved - it learns the trick.",
 "pointer": "The Signature system's proposed approach resolves nitrogenase intermediates toward cereal engineering; the companion Signature Edition record specifies the catalyst protocol.",
 "key_points": [
  "Nitrogenase reduces N2 at ambient conditions.",
  "FeMo-cofactor intermediates debated.",
  "Oxygen poisons the enzyme.",
  "Cereal nitrogen fixation is the applied dream.",
 ],
 "requirements": [
  "Intermediate-resolved mechanism studies.",
  "Minimal-nif synthetic biology.",
  "Oxygen-tolerance engineering.",
 ],
 "citations": [
  "Hoffman BM et al. (2014) Mechanism of nitrogen fixation by nitrogenase. Chemical Reviews 114.",
 ],
 "demo": {"vmax": 65.0, "km": 5.5, "s": [1.0, 5.5, 28.0]},
},
# ----------------------------------------------------------------- rank 14
{
 "key": "bc-rubisco",
 "name": "The Carbon Fixation Problem",
 "group": "Energy",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "RuBisCO - the world's most abundant enzyme - is slow and confused by oxygen, so why has evolution not improved it, and can we?",
 "background": "The RuBisCO problem - the carboxylase's catalytic slowness (~3/s) and oxygenase mistake - is the central carbon-fixation puzzle: the enzyme is constrained by a catalytic tradeoff (specificity vs speed), and its evolution is stuck in a local optimum. Engineering attempts (directed evolution, transplantation of faster variants) show limited gains; the tradeoff may be fundamental. C4 and CAM plants bypass it with CO2-concentrating mechanisms - the engineering template. The bottleneck of the biosphere may be unimprovable - or just unengineered.",
 "why_it_matters": "RuBisCO limits every plant's growth. Its improvement - or bypass - is the carbon-fixation frontier.",
 "sig_lens": "The Signature lens reads RuBisCO as the stuck enzyme: the protocol must test whether the tradeoff is law (fundamental) or habit (evolvable) - by engineering.",
 "sig_solution": LABEL + " Assumptions: (1) speed-specificity tradeoff constrains; (2) engineering gains limited. Reasoning path: test the tradeoff's hardness - directed evolution plus CO2-concentrating-mechanism transplantation (the C4 bypass). Proposed mechanism: a bottleneck protocol with tradeoff-testing enzyme engineering, C4/CAM mechanism transplantation into C3 crops, and field validation of the gains. Confirm: the tradeoff broken or bypassed. Kill: the tradeoff proves fundamental. Does NOT claim: a better RuBisCO - it tests law vs habit.",
 "pointer": "The Signature system's proposed approach tests RuBisCO's tradeoffs and transplants CO2-concentrating mechanisms; the companion Signature Edition record specifies the bottleneck protocol.",
 "key_points": [
  "RuBisCO: ~3 turnovers/s; oxygenase wastes carbon.",
  "Speed-specificity tradeoff hypothesized.",
  "Engineering gains limited so far.",
  "C4/CAM bypass with concentrating mechanisms.",
 ],
 "requirements": [
  "Tradeoff-testing enzyme engineering.",
  "CO2-concentrating-mechanism transplantation.",
  "Field validation of gains.",
 ],
 "citations": [
  "Erb TJ, Zarzycki J (2018) A short history of RubisCO. Current Opinion Chemical Biology 47.",
 ],
 "demo": {"vmax": 55.0, "km": 25.0, "s": [5.0, 25.0, 125.0]},
},
# ----------------------------------------------------------------- rank 15
{
 "key": "bc-oxphos",
 "name": "The Oxidative Phosphorylation Problem",
 "group": "Energy",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Mitochondria make ATP with rotary motors - but how is the proton motive force coupled so efficiently, and what goes wrong in disease?",
 "background": "The oxidative-phosphorylation problem - the exact coupling of electron transport to ATP synthesis - is largely solved in outline (chemiosmotic theory, ATP synthase rotary mechanism - Nobel 1997) but open in detail: the proton pathways through Complexes I, III, IV, the supercomplex organization (respirasomes), and the reactive-oxygen-species production sites in disease. Mitochondrial diseases (mutations in the 13 mtDNA-encoded subunits) lack therapies. The cell's power plants are understood in blueprint, mysterious in operation.",
 "why_it_matters": "Mitochondrial dysfunction underlies metabolic disease, neurodegeneration, and aging. The operational details are the therapeutic targets.",
 "sig_lens": "The Signature lens reads mitochondria as the power grid: the protocol must map the wiring (supercomplexes, proton paths) and find where the grid fails in disease.",
 "sig_solution": LABEL + " Assumptions: (1) outline solved; proton pathways and supercomplex roles open; (2) ROS sites in disease unclear. Reasoning path: map the operational details - proton pathways, supercomplex function, ROS sources - in health and disease. Proposed mechanism: a grid protocol with coupling-mechanism studies (cryo-EM, spectroscopy), supercomplex functional mapping, and disease-mutation mechanism studies toward therapies. Confirm: the operational map predicts disease phenotypes. Kill: the details prove too complex for therapeutic leverage. Does NOT claim: the coupling fully solved - it maps the grid's wiring.",
 "pointer": "The Signature system's proposed approach maps oxidative-phosphorylation coupling details in disease; the companion Signature Edition record specifies the grid protocol.",
 "key_points": [
  "Chemiosmotic theory and rotary ATP synthase established.",
  "Proton pathways through Complexes I/III/IV open in detail.",
  "Supercomplex (respirasome) function debated.",
  "Mitochondrial diseases lack therapies.",
 ],
 "requirements": [
  "Proton-pathway and coupling studies.",
  "Supercomplex functional mapping.",
  "Disease-mutation mechanism studies.",
 ],
 "citations": [
  "Mitchell P (1961) Coupling of phosphorylation to electron transfer. Nature 191.",
 ],
 "demo": {"vmax": 140.0, "km": 18.0, "s": [3.5, 18.0, 90.0]},
},
# ----------------------------------------------------------------- rank 16
{
 "key": "bc-signaling",
 "name": "The Signal Transduction Problem",
 "group": "Signaling",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Cells process signals through kinase cascades - but how is specificity achieved when the components are shared, and how do the networks compute?",
 "background": "The signal-transduction problem - specificity and computation in shared-component networks (MAPK cascades used by many receptors) - is the systems-biochemistry challenge: scaffolds, localization, kinetics, and feedback create specificity from promiscuous parts, but the quantitative mapping (which scaffold does what, how feedback tunes) is incomplete. The networks compute (adaptation, fold-change detection) - the circuit logic is being reverse-engineered. The cell's computers are wired; the logic gates are half-mapped.",
 "why_it_matters": "Cancer drugs target signaling networks; resistance comes from network rewiring. The unmapped logic is the resistance mechanism.",
 "sig_lens": "The Signature lens reads signaling as the cell's circuitry: the protocol must reverse-engineer the gates (scaffolds, feedback) and predict the rewiring.",
 "sig_solution": LABEL + " Assumptions: (1) specificity from scaffolds/localization/kinetics; (2) network rewiring causes drug resistance. Reasoning path: map the circuit logic - quantitative scaffold/feedback studies - and predict rewiring under inhibition. Proposed mechanism: a circuitry protocol with network-logic mapping (perturbation, modeling), rewiring prediction for drug combinations, and scaffold-targeted therapeutics. Confirm: the mapped logic predicts drug responses. Kill: the networks prove too context-dependent. Does NOT claim: the full circuit mapped - it reverse-engineers the gates.",
 "pointer": "The Signature system's proposed approach maps signaling circuit logic to predict drug rewiring; the companion Signature Edition record specifies the circuitry protocol.",
 "key_points": [
  "Shared components (MAPK) serve many receptors.",
  "Specificity from scaffolds, localization, kinetics, feedback.",
  "Networks compute: adaptation, fold-change detection.",
  "Drug resistance comes from network rewiring.",
 ],
 "requirements": [
  "Quantitative network-logic mapping.",
  "Rewiring prediction under inhibition.",
  "Scaffold-targeted therapeutic strategies.",
 ],
 "citations": [
  "Lim WA et al. (2015) Cell signaling principles. Cell 163.",
 ],
 "demo": {"vmax": 100.0, "km": 10.0, "s": [2.0, 10.0, 50.0]},
},
# ----------------------------------------------------------------- rank 17
{
 "key": "bc-calcium",
 "name": "The Calcium Signaling Problem",
 "group": "Signaling",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Calcium signals everything from muscle to memory - but how does one ion encode so many messages without crosstalk?",
 "background": "The calcium-signaling problem - the versatility-specificity paradox of Ca2+ - is solved partially: the code is spatiotemporal (microdomains, puffs, waves, oscillations), with the frequency/amplitude/location encoding the message. But the decoding (how targets read the code), the organelle interplay (ER-mitochondria calcium handshakes), and the dysregulation in disease (neurodegeneration, heart failure) are open. The universal messenger's language is half-deciphered.",
 "why_it_matters": "Calcium dysregulation kills neurons and hearts. The half-deciphered code is the therapeutic dictionary.",
 "sig_lens": "The Signature lens reads calcium as the universal messenger: the protocol must decode the dialects (microdomains, oscillations) and find where the messages garble in disease.",
 "sig_solution": LABEL + " Assumptions: (1) code is spatiotemporal; (2) decoding and organelle interplay open. Reasoning path: decode systematically - map calcium codes to outcomes per cell type, and find the disease garbling. Proposed mechanism: a messenger protocol with spatiotemporal calcium-code mapping, target-decoding studies, and disease-dysregulation characterization toward interventions. Confirm: decoded codes predict cellular outcomes. Kill: the code proves too context-dependent. Does NOT claim: the calcium code cracked - it decodes the dialects.",
 "pointer": "The Signature system's proposed approach decodes calcium signaling spatiotemporally in disease; the companion Signature Edition record specifies the messenger protocol.",
 "key_points": [
  "Ca2+ signals via microdomains, puffs, waves, oscillations.",
  "Frequency/amplitude/location encode messages.",
  "Target decoding mechanisms open.",
  "Dysregulation in neurodegeneration and heart failure.",
 ],
 "requirements": [
  "Spatiotemporal calcium-code mapping.",
  "Target-decoding mechanism studies.",
  "Disease-dysregulation characterization.",
 ],
 "citations": [
  "Berridge MJ et al. (2000) The versatility and universality of calcium signalling. Nature Reviews MCB 1.",
 ],
 "demo": {"vmax": 88.0, "km": 7.5, "s": [1.5, 7.5, 38.0]},
},
# ----------------------------------------------------------------- rank 18
{
 "key": "bc-apoptosis",
 "name": "The Apoptosis Regulation Problem",
 "group": "Signaling",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Cells decide to die through apoptosis - but how is the life-death decision computed, and why do cancer cells evade it?",
 "background": "The apoptosis-regulation problem - the Bcl-2 family rheostat, caspase cascades, and the mitochondrial outer-membrane permeabilization (MOMP) decision - is the cell's life-death computation: the BH3-only proteins' integration of damage signals, the Bax/Bak pore formation, and the point of no return are modeled but the quantitative decision logic is incomplete. Cancer evades via Bcl-2 overexpression (venetoclax targets it); the evasion's network logic is the resistance question. The death decision is computed; the computation is half-mapped.",
 "why_it_matters": "Cancer is apoptosis evaded; neurodegeneration is apoptosis excessive. The decision logic is the therapeutic switch.",
 "sig_lens": "The Signature lens reads apoptosis as the cell's death sentence: the protocol must learn how the jury (Bcl-2 family) votes - to convict cancer cells and acquit neurons.",
 "sig_solution": LABEL + " Assumptions: (1) Bcl-2 rheostat integrates damage; (2) cancer evades via network rewiring. Reasoning path: map the voting - quantitative Bcl-2 family interaction networks - and predict evasion. Proposed mechanism: a jury protocol with life-death decision mapping (BH3 profiling), evasion-mechanism characterization per cancer, and combination therapies on the mapped logic. Confirm: the mapped logic predicts treatment responses. Kill: the decision proves too stochastic. Does NOT claim: the death decision solved - it learns the jury's voting.",
 "pointer": "The Signature system's proposed approach maps the apoptosis decision network for cancer therapy; the companion Signature Edition record specifies the jury protocol.",
 "key_points": [
  "Bcl-2 family integrates damage into the MOMP decision.",
  "Bax/Bak pore formation is the point of no return.",
  "Cancer evades via Bcl-2 overexpression.",
  "Venetoclax proves the target druggable.",
 ],
 "requirements": [
  "Quantitative Bcl-2 network mapping.",
  "BH3 profiling per cancer.",
  "Combination therapies on mapped logic.",
 ],
 "citations": [
  "Czabotar PE et al. (2014) Control of apoptosis by the BCL-2 protein family. Nature Reviews MCB 15.",
 ],
 "demo": {"vmax": 72.0, "km": 6.0, "s": [1.2, 6.0, 30.0]},
},
# ----------------------------------------------------------------- rank 19
{
 "key": "bc-cell-cycle",
 "name": "The Cell Cycle Control Problem",
 "group": "Signaling",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "The cell cycle's checkpoints guard division - but how do they integrate damage signals, and why do they fail in cancer?",
 "background": "The cell-cycle-control problem - the G1/S, G2/M, and spindle checkpoints' signal integration - won Nobels (cyclins, CDKs) but the quantitative control is open: the DNA-damage checkpoint's (ATM/ATR-p53) decision logic, the spindle assembly checkpoint's wait-anaphase signal, and the checkpoint failures in cancer (p53 mutated in half of cancers). CDK inhibitors (palbociclib) work; resistance emerges. The division's guardians are known; their decision algorithms are half-mapped.",
 "why_it_matters": "Checkpoint failure is cancer's license to divide. The guardians' algorithms are the therapy targets.",
 "sig_lens": "The Signature lens reads checkpoints as the division's bouncers: the protocol must learn the guest list (damage signals) and why the bouncers take bribes in cancer.",
 "sig_solution": LABEL + " Assumptions: (1) checkpoint components known; decision logic half-mapped; (2) p53 mutated in ~half of cancers. Reasoning path: map the decision algorithms - quantitative checkpoint modeling - and target the failures. Proposed mechanism: a bouncers protocol with checkpoint decision-logic mapping, cancer-checkpoint-failure characterization, and CDK/checkpoint-targeted combinations. Confirm: the mapped logic predicts checkpoint responses. Kill: the logic proves irreducibly complex. Does NOT claim: the checkpoints solved - it learns the bouncers' rules.",
 "pointer": "The Signature system's proposed approach maps cell-cycle checkpoint decision logic; the companion Signature Edition record specifies the bouncers protocol.",
 "key_points": [
  "Cyclins/CDKs drive the cycle; checkpoints guard it.",
  "ATM/ATR-p53 integrates DNA damage.",
  "Spindle checkpoint's wait signal mechanistically open.",
  "p53 mutated in ~half of human cancers.",
 ],
 "requirements": [
  "Quantitative checkpoint decision modeling.",
  "Cancer checkpoint-failure characterization.",
  "Checkpoint-targeted combination therapies.",
 ],
 "citations": [
  "Hartwell LH, Weinert TA (1989) Checkpoints. Science 246.",
 ],
 "demo": {"vmax": 98.0, "km": 9.5, "s": [2.0, 9.5, 48.0]},
},
# ----------------------------------------------------------------- rank 20
{
 "key": "bc-dna-repair",
 "name": "The DNA Repair Pathway Choice Problem",
 "group": "Nucleic Acids",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "DNA breaks constantly - but how does the cell choose between repair pathways (homologous recombination vs end joining), and what tips the choice?",
 "background": "The repair-pathway-choice problem - HR (accurate, needs sister chromatid) vs NHEJ (fast, error-prone) vs alternatives - is the genome's triage: the choice factors (cell cycle, resection by BRCA1/CtIP, 53BP1's block) are being mapped, but the quantitative decision logic and the therapeutic exploitation (PARP inhibitors in BRCA-mutant cancers: synthetic lethality) are active frontiers. The choice is life-or-mutation; the triage rules are half-written.",
 "why_it_matters": "Repair-choice failure causes cancer; repair-choice exploitation (PARP inhibitors) cures some. The triage rules are the therapy manual.",
 "sig_lens": "The Signature lens reads repair choice as the genome's triage: the protocol must learn the triage rules - to route cancer cells to the lethal choice.",
 "sig_solution": LABEL + " Assumptions: (1) HR vs NHEJ choice factors being mapped; (2) synthetic lethality exploits the choice. Reasoning path: complete the triage rules - quantitative pathway-choice mapping - and expand synthetic-lethal therapies. Proposed mechanism: a triage protocol with repair-choice decision mapping, synthetic-lethal screens per repair defect, and combination therapies routing cancer to lethal choices. Confirm: the mapped rules predict repair outcomes. Kill: the choice proves too stochastic. Does NOT claim: the triage solved - it learns the rules.",
 "pointer": "The Signature system's proposed approach maps DNA repair pathway-choice for synthetic-lethal therapy; the companion Signature Edition record specifies the triage protocol.",
 "key_points": [
  "HR accurate; NHEJ fast and error-prone.",
  "BRCA1/CtIP vs 53BP1 contest resection.",
  "PARP inhibitors exploit BRCA defects (synthetic lethality).",
  "Quantitative choice logic incomplete.",
 ],
 "requirements": [
  "Quantitative repair-choice mapping.",
  "Synthetic-lethal screens per defect.",
  "Choice-routing combination therapies.",
 ],
 "citations": [
  "Chapman JR et al. (2012) Playing the end game: DNA double-strand break repair pathway choice. Molecular Cell 47.",
 ],
 "demo": {"vmax": 82.0, "km": 7.0, "s": [1.4, 7.0, 35.0]},
},
# ----------------------------------------------------------------- rank 21
{
 "key": "bc-epigenetic-inherit",
 "name": "The Epigenetic Inheritance Problem",
 "group": "Nucleic Acids",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Epigenetic marks regulate genes - but which marks are truly inherited across generations, and how?",
 "background": "The epigenetic-inheritance problem - transgenerational epigenetic inheritance (TEI) - is the field's most contested: DNA methylation is largely erased and reset each generation (in mammals), yet some loci escape; histone-mark and small-RNA inheritance is established in worms/plants but debated in mammals. The Lamarckian headlines outrun the evidence: most 'transgenerational' effects are intergenerational (fetal exposure) or unreplicated. The inheritance that survives the reset is the open question.",
 "why_it_matters": "True TEI would reshape heredity and evolution. The contested inheritance is the most oversold and most important epigenetic question.",
 "sig_lens": "The Signature lens reads epigenetic inheritance as the message in the bottle: the protocol must check which messages survive the ocean (the generational reset) - rigorously.",
 "sig_solution": LABEL + " Assumptions: (1) methylation largely reset; some loci escape; (2) headlines outrun evidence. Reasoning path: test rigorously - multi-generation designs excluding fetal exposure, with molecular mechanism required. Proposed mechanism: a bottle protocol with rigorous TEI experimental designs, escapee-locus mechanism studies, and headline-discipline (inter- vs trans-generational distinguished). Confirm: a mark's TEI with mechanism. Kill: all candidates prove intergenerational or unreplicated. Does NOT claim: transgenerational inheritance - it tests the bottle's messages.",
 "pointer": "The Signature system's proposed approach tests transgenerational epigenetic inheritance rigorously; the companion Signature Edition record specifies the bottle protocol.",
 "key_points": [
  "Mammalian methylation largely erased per generation.",
  "Some loci escape the reset.",
  "Worm/plant small-RNA inheritance established; mammals debated.",
  "Intergenerational (fetal) vs transgenerational confused.",
 ],
 "requirements": [
  "Multi-generation TEI experimental designs.",
  "Escapee-locus mechanism studies.",
  "Inter/trans-generational distinction enforced.",
 ],
 "citations": [
  "Heard E, Martienssen RA (2014) Transgenerational epigenetic inheritance. Cell 157.",
 ],
 "demo": {"vmax": 68.0, "km": 5.0, "s": [1.0, 5.0, 25.0]},
},
# ----------------------------------------------------------------- rank 22
{
 "key": "bc-histone-code",
 "name": "The Histone Code Problem",
 "group": "Nucleic Acids",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Histones carry dozens of modifications - but is there really a 'code,' and how do the marks combine to control genes?",
 "background": "The histone-code problem - whether histone modifications form a true code (combinatorial, readable) - is debated: the marks correlate with activity (H3K4me3 at active promoters, H3K27me3 at repressed), and readers/writers/erasers exist, but the causality (marks causing vs reflecting transcription) is contested, and the combinatorial logic is unmapped. The 'code' may be a language or just correlations. The chromatin's annotations are read daily; their grammar is unknown.",
 "why_it_matters": "Epigenetic drugs (HDAC, EZH2 inhibitors) target the writers/erasers. The unmapped grammar is the drug-design dictionary.",
 "sig_lens": "The Signature lens reads histone marks as the genome's annotations: the protocol must learn the grammar - which combinations mean what, causally.",
 "sig_solution": LABEL + " Assumptions: (1) marks correlate; causality contested; (2) combinatorial logic unmapped. Reasoning path: test causality - targeted epigenome editing (dCas9-writers/erasers) with transcriptional readouts. Proposed mechanism: a grammar protocol with causal epigenome-editing screens, combinatorial-mark logic mapping, and epigenetic-drug design on the causal grammar. Confirm: the edited marks cause predicted transcription. Kill: the marks prove purely correlative. Does NOT claim: the histone code cracked - it learns the grammar causally.",
 "pointer": "The Signature system's proposed approach tests histone-mark causality with epigenome editing; the companion Signature Edition record specifies the grammar protocol.",
 "key_points": [
  "Marks correlate with activity states.",
  "Readers, writers, erasers identified.",
  "Causality (cause vs reflect) contested.",
  "Combinatorial logic unmapped.",
 ],
 "requirements": [
  "Causal epigenome-editing screens.",
  "Combinatorial-mark logic mapping.",
  "Drug design on causal grammar.",
 ],
 "citations": [
  "Strahl BD, Allis CD (2000) The language of covalent histone modifications. Nature 403.",
 ],
 "demo": {"vmax": 92.0, "km": 8.5, "s": [1.8, 8.5, 42.0]},
},
# ----------------------------------------------------------------- rank 23
{
 "key": "bc-ncrna",
 "name": "The Noncoding RNA Function Problem",
 "group": "Nucleic Acids",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Most of the genome is transcribed into noncoding RNA - but how much of it is functional, and what does it do?",
 "background": "The noncoding-RNA problem - the function fraction of lncRNAs (tens of thousands annotated) - is genomics' dark matter: some lncRNAs are functional (Xist, HOTAIR), but many may be transcriptional noise; the functional tests (knockouts) often show no phenotype. The classification (functional vs noise) needs systematic perturbation with molecular readouts. The transcribed genome is mostly noncoding; its purpose is mostly unknown.",
 "why_it_matters": "If lncRNAs are largely functional, gene regulation is RNA-run; if noise, the annotation is inflated. The function fraction decides.",
 "sig_lens": "The Signature lens reads lncRNAs as the genome's dark matter: the protocol must weigh it - systematic perturbation - before declaring it functional or noise.",
 "sig_solution": LABEL + " Assumptions: (1) tens of thousands annotated; some functional; (2) knockouts often phenotypeless. Reasoning path: test systematically - high-throughput lncRNA perturbation with molecular (not just viability) readouts. Proposed mechanism: a dark-matter protocol with systematic lncRNA perturbation screens, molecular-phenotype readouts, and function-fraction estimation. Confirm: the functional set identified with mechanisms. Kill: most prove noise. Does NOT claim: lncRNA function generally - it weighs the dark matter.",
 "pointer": "The Signature system's proposed approach systematically perturbs lncRNAs to find the functional set; the companion Signature Edition record specifies the dark-matter protocol.",
 "key_points": [
  "Tens of thousands of lncRNAs annotated.",
  "Xist, HOTAIR functional; many knockouts phenotypeless.",
  "Transcriptional noise vs function debated.",
  "Systematic perturbation with molecular readouts needed.",
 ],
 "requirements": [
  "High-throughput lncRNA perturbation screens.",
  "Molecular (not viability-only) readouts.",
  "Function-fraction estimation.",
 ],
 "citations": [
  "Rinn JL, Chang HY (2012) Genome regulation by long noncoding RNAs. Annual Review Biochemistry 81.",
 ],
 "demo": {"vmax": 78.0, "km": 6.8, "s": [1.4, 6.8, 34.0]},
},
# ----------------------------------------------------------------- rank 24
{
 "key": "bc-prebiotic",
 "name": "The Prebiotic Chemistry Problem",
 "group": "Origins",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Life's building blocks form in simulated early-Earth chemistry - but how did they assemble into the first replicating systems?",
 "background": "The prebiotic-chemistry problem - from building blocks (Miller-Urey amino acids, Sutherland's nucleotide synthesis) to replicating systems - is the gap: the syntheses work in separate flasks under incompatible conditions; the systems chemistry (networks, protocells, non-enzymatic replication) is young. The RNA world's replication (template copying without enzymes) is inefficient; the metabolism-first vs genetics-first debate continues. The building blocks are made; the assembly into life is not.",
 "why_it_matters": "Life's origin is the deepest biochemical question. The assembly gap is between chemistry and biology.",
 "sig_lens": "The Signature lens reads prebiotic chemistry as the parts without the factory: the protocol must build the assembly lines (systems chemistry) that connect parts to replicators.",
 "sig_solution": LABEL + " Assumptions: (1) building-block syntheses work separately; (2) systems chemistry young. Reasoning path: build the assembly - continuous systems-chemistry scenarios linking syntheses to protocells to replication. Proposed mechanism: a factory protocol with compatible-condition synthesis networks, protocell-replication coupling, and non-enzymatic replication improvement. Confirm: a continuous path from chemistry to replicators. Kill: the conditions prove irreconcilable. Does NOT claim: life's origin solved - it builds the assembly lines.",
 "pointer": "The Signature system's proposed approach builds continuous prebiotic systems chemistry; the companion Signature Edition record specifies the factory protocol.",
 "key_points": [
  "Amino acid and nucleotide syntheses work separately.",
  "Conditions for each are mutually incompatible.",
  "Non-enzymatic RNA replication inefficient.",
  "Metabolism-first vs genetics-first debated.",
 ],
 "requirements": [
  "Compatible-condition synthesis networks.",
  "Protocell-replication coupling.",
  "Non-enzymatic replication improvement.",
 ],
 "citations": [
  "Sutherland JD (2016) The origin of life - out of the blue. Angewandte Chemie 55.",
 ],
 "demo": {"vmax": 50.0, "km": 30.0, "s": [6.0, 30.0, 150.0]},
},
# ----------------------------------------------------------------- rank 25
{
 "key": "bc-homochirality",
 "name": "The Homochirality Problem",
 "group": "Origins",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Life uses left-handed amino acids and right-handed sugars exclusively - but how did chemistry choose sides?",
 "background": "The homochirality problem - life's single-handedness - needs a symmetry-breaking mechanism: candidates include circularly polarized starlight, magnetochiral effects, parity-violating weak interactions (tiny), and amplification (Soai autocatalysis, Viedma ripening). But the initial bias's source and the amplification's prebiotic plausibility are debated. The chosen hand (L-amino acids) is universal; its chooser unknown. The mirror world was not taken - why?",
 "why_it_matters": "Homochirality is life's most fundamental asymmetry. Its origin is the symmetry-breaking that made biology possible.",
 "sig_lens": "The Signature lens reads homochirality as the chosen hand: the protocol must find who chose - the bias source - and how the choice amplified.",
 "sig_solution": LABEL + " Assumptions: (1) bias sources each plausible, none proven; (2) amplification demonstrated in models. Reasoning path: test the bias sources prebiotically - measure chiral biases in realistic syntheses and the amplification under prebiotic conditions. Proposed mechanism: a hand protocol with prebiotic chiral-bias measurements, amplification testing (Soai-type, Viedma), and the chosen-hand's universality explained. Confirm: a bias-plus-amplification path demonstrated. Kill: no plausible path found. Does NOT claim: the chooser - it tests the candidates.",
 "pointer": "The Signature system's proposed approach tests homochirality bias sources and amplification prebiotically; the companion Signature Edition record specifies the hand protocol.",
 "key_points": [
  "Life: L-amino acids, D-sugars exclusively.",
  "Starlight, magnetochiral, weak-force biases proposed.",
  "Soai autocatalysis amplifies tiny biases.",
  "Prebiotic plausibility of each debated.",
 ],
 "requirements": [
  "Prebiotic chiral-bias measurements.",
  "Amplification under prebiotic conditions.",
  "Universality explanation.",
 ],
 "citations": [
  "Blackmond DG (2010) The origin of biological homochirality. Cold Spring Harbor Perspectives Biology 2.",
 ],
 "demo": {"vmax": 45.0, "km": 35.0, "s": [7.0, 35.0, 175.0]},
},
# ----------------------------------------------------------------- rank 26
{
 "key": "bc-minimal-genome",
 "name": "The Minimal Genome Problem",
 "group": "Synthetic Biology",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "What is the smallest genome that sustains life - and what do the essential-but-unknown genes do?",
 "background": "The minimal-genome problem - JCVI-syn3.0's 473 genes (149 of unknown function) - is the ignorance quantified: a third of the minimal gene set does nothing we understand, yet the cell dies without them. The unknown-essential genes are the dark matter of the minimal cell. Top-down minimization vs bottom-up synthesis compete; the function assignment for the 149 is the frontier. The simplest life is one-third mystery.",
 "why_it_matters": "The unknown-essential genes are biology's dark matter. Their functions are the missing third of minimal life.",
 "sig_lens": "The Signature lens reads the minimal genome as the parts list with mysteries: the protocol must interrogate each unknown-essential gene until it confesses its function.",
 "sig_solution": LABEL + " Assumptions: (1) 149/473 genes unknown-essential; (2) cell dies without them. Reasoning path: assign functions systematically - knockdown/overexpression with multi-omic readouts per unknown gene. Proposed mechanism: a parts protocol with systematic unknown-essential characterization, multi-omic phenotyping, and minimal-cell engineering on the assigned functions. Confirm: the 149's functions assigned. Kill: the genes prove redundantly essential and unassignable singly. Does NOT claim: all functions known - it interrogates each gene.",
 "pointer": "The Signature system's proposed approach assigns functions to minimal-genome unknowns systematically; the companion Signature Edition record specifies the parts protocol.",
 "key_points": [
  "JCVI-syn3.0: 473 genes; 149 unknown function.",
  "Unknown-essential: dies without them, purpose unknown.",
  "Top-down vs bottom-up minimization compete.",
  "Simplest life one-third mystery.",
 ],
 "requirements": [
  "Systematic unknown-essential characterization.",
  "Multi-omic phenotyping per gene.",
  "Minimal-cell engineering on assignments.",
 ],
 "citations": [
  "Hutchison CA III et al. (2016) Design and synthesis of a minimal bacterial genome. Science 351.",
 ],
 "demo": {"vmax": 40.0, "km": 40.0, "s": [8.0, 40.0, 200.0]},
},
# ----------------------------------------------------------------- rank 27
{
 "key": "bc-synthetic-cell",
 "name": "The Synthetic Cell Problem",
 "group": "Synthetic Biology",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Can a cell be built from scratch - and what would it take to make the built cell truly alive?",
 "background": "The synthetic-cell problem - bottom-up construction of living cells - progresses in modules: PURE translation systems, vesicle growth/division, DNA replication in liposomes - but the integration (a self-reproducing, evolving system from nonliving parts) is distant. The definition of success (replication? evolution? metabolism?) is debated. The BaSyC and other consortia pursue the modular path. The built cell would test our understanding completely - we cannot yet build what we claim to understand.",
 "why_it_matters": "Building a cell tests whether biochemistry truly understands life. The unbuilt cell is the understanding's verdict.",
 "sig_lens": "The Signature lens reads the synthetic cell as the final exam: the protocol must integrate the modules - replication, metabolism, division - until the system lives.",
 "sig_solution": LABEL + " Assumptions: (1) modules progress; integration distant; (2) success criteria debated. Reasoning path: integrate stepwise - couple replication to growth to division in vesicles, adding evolvability. Proposed mechanism: an exam protocol with module-integration milestones, evolvability as the success criterion, and understanding-tests per integration step. Confirm: a self-reproducing evolving synthetic cell. Kill: integration proves intractable. Does NOT claim: a built cell - it works toward the exam.",
 "pointer": "The Signature system's proposed approach integrates synthetic-cell modules toward evolvability; the companion Signature Edition record specifies the exam protocol.",
 "key_points": [
  "Modules: translation, vesicle division, replication progress.",
  "Integration into self-reproducing system distant.",
  "Success criteria (replication? evolution?) debated.",
  "The unbuilt cell tests understanding.",
 ],
 "requirements": [
  "Module-integration milestones.",
  "Evolvability as success criterion.",
  "Understanding-tests per step.",
 ],
 "citations": [
  "Schwille P (2017) Bottom-up synthetic biology. Angewandte Chemie 56.",
 ],
 "demo": {"vmax": 35.0, "km": 45.0, "s": [9.0, 45.0, 225.0]},
},
# ----------------------------------------------------------------- rank 28
{
 "key": "bc-metabolomics",
 "name": "The Metabolomics Identification Problem",
 "group": "Metabolism",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Mass spectrometry sees thousands of metabolite signals - but most cannot be identified, so what are the unknown metabolites?",
 "background": "The metabolomics-identification problem ('dark matter' of metabolomics) - most MS features unidentifiable against spectral libraries - limits the field: the unknowns may be novel metabolites, adducts, or artifacts, and the identification rate (~10-20%) has barely improved. In-silico spectra, molecular networking, and standards synthesis each help partially. The metabolome's dark matter is the measurement's embarrassment: we detect what we cannot name.",
 "why_it_matters": "Unknown metabolites may be biomarkers or new biochemistry. The unnamed signals are the missed discoveries.",
 "sig_lens": "The Signature lens reads metabolomics as the census with unnamed residents: the protocol must name them - by synthesis, networking, and prediction.",
 "sig_solution": LABEL + " Assumptions: (1) identification rate ~10-20%; (2) unknowns mix novel, adduct, artifact. Reasoning path: name systematically - in-silico prediction, molecular networking, and targeted synthesis of candidates. Proposed mechanism: a census protocol with spectral-library expansion, in-silico identification pipelines, and unknown-prioritization by biological signal. Confirm: the dark matter substantially identified. Kill: the unknowns prove mostly artifacts. Does NOT claim: all metabolites named - it names the residents.",
 "pointer": "The Signature system's proposed approach identifies metabolomics dark matter systematically; the companion Signature Edition record specifies the census protocol.",
 "key_points": [
  "Most MS features unidentifiable (~10-20% identified).",
  "Unknowns: novel metabolites, adducts, artifacts.",
  "In-silico spectra and networking help partially.",
  "The dark matter may hold biomarkers.",
 ],
 "requirements": [
  "Spectral-library expansion programs.",
  "In-silico identification pipelines.",
  "Unknown prioritization by biological signal.",
 ],
 "citations": [
  "da Silva RR et al. (2015) Illuminating the dark matter in metabolomics. PNAS 112.",
 ],
 "demo": {"vmax": 115.0, "km": 14.0, "s": [2.8, 14.0, 70.0]},
},
# ----------------------------------------------------------------- rank 29
{
 "key": "bc-proteoform",
 "name": "The Proteoform Problem",
 "group": "Proteins",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "One gene makes many proteoforms - but how many exist in a cell, and which ones actually matter?",
 "background": "The proteoform problem - the combinatorial explosion of protein variants (splice isoforms x PTMs x processing) - dwarfs the genome: millions of possible proteoforms per cell, of which top-down proteomics observes thousands. The functional relevance of most proteoforms is unknown; the 'one gene, many proteins' reality breaks the gene-centric view. The proteoform atlas is being built; the function map lags. The proteome's true complexity is counted, not understood.",
 "why_it_matters": "Drugs target proteoforms, not genes. The unmapped function is the precision-medicine gap.",
 "sig_lens": "The Signature lens reads proteoforms as the gene's many faces: the protocol must catalog the faces and learn which ones the cell actually wears functionally.",
 "sig_solution": LABEL + " Assumptions: (1) millions possible; thousands observed; (2) functional relevance mostly unknown. Reasoning path: catalog and prioritize - top-down proteoform atlases with functional prioritization. Proposed mechanism: a faces protocol with cell-type proteoform atlases, functional screening of variant proteoforms, and proteoform-aware drug targeting. Confirm: the functional proteoforms identified. Kill: the complexity proves intractable. Does NOT claim: all proteoforms mapped - it catalogs the worn faces.",
 "pointer": "The Signature system's proposed approach builds functional proteoform atlases; the companion Signature Edition record specifies the faces protocol.",
 "key_points": [
  "Millions of possible proteoforms per cell.",
  "Top-down proteomics observes thousands.",
  "Functional relevance mostly unknown.",
  "Gene-centric view broken by proteoforms.",
 ],
 "requirements": [
  "Cell-type proteoform atlases.",
  "Functional proteoform screening.",
  "Proteoform-aware drug targeting.",
 ],
 "citations": [
  "Smith LM, Kelleher NL (2013) Proteoform: a single term describing protein complexity. Nature Methods 10.",
 ],
 "demo": {"vmax": 108.0, "km": 13.0, "s": [2.6, 13.0, 65.0]},
},
# ----------------------------------------------------------------- rank 30
{
 "key": "bc-ptm-code",
 "name": "The Post Translational Modification Code Problem",
 "group": "Proteins",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Proteins carry hundreds of modification types in combinations - but is there a PTM code, and how do the marks combine?",
 "background": "The PTM-code problem - 400+ modification types (phosphorylation, ubiquitination, glycosylation, acetylation...) in combinatorial patterns - mirrors the histone code at whole-proteome scale: the modifications crosstalk (phosphorylation gating ubiquitination), but the combinatorial logic is unmapped and the functional annotation lags detection. PTM proteomics identifies sites by the thousands; the code's grammar is unknown. The protein's annotations are catalogued; their language unlearned.",
 "why_it_matters": "PTMs control every signaling pathway; drugs target the writers/erasers. The unlearned language is the pharmacology gap.",
 "sig_lens": "The Signature lens reads PTMs as the proteome's annotations: the protocol must learn the grammar - which combinations mean what - by writing and erasing deliberately.",
 "sig_solution": LABEL + " Assumptions: (1) 400+ PTM types; crosstalk known; (2) combinatorial logic unmapped. Reasoning path: learn the grammar - systematic PTM-combination perturbation with functional readouts. Proposed mechanism: an annotations protocol with combinatorial-PTM screens, crosstalk logic mapping, and PTM-code-based drug design. Confirm: the grammar predicts PTM-function relationships. Kill: the combinations prove idiosyncratic. Does NOT claim: the PTM code cracked - it learns the grammar.",
 "pointer": "The Signature system's proposed approach maps PTM combinatorial logic systematically; the companion Signature Edition record specifies the annotations protocol.",
 "key_points": [
  "400+ PTM types in combinatorial patterns.",
  "Crosstalk (phospho gating ubiquitin) known.",
  "Combinatorial logic unmapped.",
  "Detection outruns functional annotation.",
 ],
 "requirements": [
  "Combinatorial-PTM perturbation screens.",
  "Crosstalk logic mapping.",
  "PTM-grammar-based drug design.",
 ],
 "citations": [
  "Prabakaran S et al. (2012) Post-translational modification: nature's escape from genetic imprisonment. WIREs Systems Biology 4.",
 ],
 "demo": {"vmax": 102.0, "km": 12.5, "s": [2.5, 12.5, 62.0]},
},
# ----------------------------------------------------------------- rank 31
{
 "key": "bc-raft",
 "name": "The Lipid Raft Problem",
 "group": "Membranes",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Membranes may organize into lipid rafts - but do rafts exist in living cells, and what do they do?",
 "background": "The lipid-raft problem - ordered membrane microdomains (sphingolipid/cholesterol) organizing signaling - is the membrane field's long controversy: rafts are well-established in model membranes, but in living cells the evidence is indirect (detergent-resistant membranes are artifactual; super-resolution hints at transient nanodomains). The field split into believers and skeptics; the current synthesis (transient, nanoscale, functional assemblies) satisfies neither fully. The membrane's organization is either raft-structured or not - the cell's surface geography is disputed.",
 "why_it_matters": "Rafts would organize immune signaling, viral entry, and trafficking. The disputed geography is the membrane's map.",
 "sig_lens": "The Signature lens reads rafts as the disputed islands: the protocol must survey them in living cells - without the detergent that creates artifacts.",
 "sig_solution": LABEL + " Assumptions: (1) model-membrane rafts established; (2) live-cell evidence indirect. Reasoning path: observe natively - super-resolution and single-molecule tracking in living cells, artifact-free. Proposed mechanism: an islands protocol with live-cell nanodomain imaging, functional raft-perturbation studies, and artifact-controlled biochemistry. Confirm: functional nanodomains verified in vivo. Kill: the domains prove artifactual. Does NOT claim: rafts exist - it surveys the islands natively.",
 "pointer": "The Signature system's proposed approach images membrane nanodomains in living cells artifact-free; the companion Signature Edition record specifies the islands protocol.",
 "key_points": [
  "Rafts established in model membranes.",
  "Detergent-resistant membranes are artifactual.",
  "Live-cell evidence indirect (super-resolution hints).",
  "Field split; transient-nanodomain synthesis debated.",
 ],
 "requirements": [
  "Live-cell super-resolution nanodomain imaging.",
  "Functional perturbation studies.",
  "Artifact-controlled membrane biochemistry.",
 ],
 "citations": [
  "Simons K, Ikonen E (1997) Functional rafts in cell membranes. Nature 387.",
 ],
 "demo": {"vmax": 66.0, "km": 5.8, "s": [1.2, 5.8, 29.0]},
},
# ----------------------------------------------------------------- rank 32
{
 "key": "bc-condensate",
 "name": "The Biomolecular Condensate Problem",
 "group": "Cellular Organization",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Cells organize chemistry in membraneless condensates - but how do they form, what are the rules, and how do they go wrong in disease?",
 "background": "The condensate problem - liquid-liquid phase separation organizing nucleoli, stress granules, transcriptional hubs - is the cell-biology revolution in progress: the formation rules (multivalent interactions, IDRs), the material states (liquid to gel to solid), and the functional consequences are being mapped, but the in-vivo verification lags the in-vitro demonstrations, and the disease link (ALS/FTD aggregates as aberrant condensates) is correlative. The cell's liquid organization is discovered; its rules half-written.",
 "why_it_matters": "Condensate dysfunction may drive neurodegeneration. The half-written rules are the therapeutic target list.",
 "sig_lens": "The Signature lens reads condensates as the cell's liquid rooms: the protocol must learn the architecture rules - and find where the plumbing floods in disease.",
 "sig_solution": LABEL + " Assumptions: (1) in-vitro LLPS established; in-vivo verification lags; (2) disease link correlative. Reasoning path: verify in vivo - endogenous tagging, material-state measurements in cells - and test the disease causality. Proposed mechanism: a rooms protocol with in-vivo condensate verification, material-state-function mapping, and disease-causality tests (aberrant transitions). Confirm: the rules predict in-vivo organization and disease. Kill: the condensates prove in-vitro artifacts. Does NOT claim: the condensate rules complete - it learns the architecture.",
 "pointer": "The Signature system's proposed approach verifies biomolecular condensates in vivo with material-state mapping; the companion Signature Edition record specifies the rooms protocol.",
 "key_points": [
  "LLPS organizes nucleoli, stress granules, hubs.",
  "Formation via multivalent interactions and IDRs.",
  "In-vivo verification lags in-vitro work.",
  "ALS/FTD aggregates linked correlatively.",
 ],
 "requirements": [
  "In-vivo condensate verification.",
  "Material-state-function mapping.",
  "Disease-causality tests.",
 ],
 "citations": [
  "Shin Y, Brangwynne CP (2017) Liquid phase condensation in cell physiology and disease. Science 357.",
 ],
 "demo": {"vmax": 74.0, "km": 6.2, "s": [1.3, 6.2, 31.0]},
},
# ----------------------------------------------------------------- rank 33
{
 "key": "bc-systems",
 "name": "The Systems Biochemistry Problem",
 "group": "Cellular Organization",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Biochemistry knows the parts - but can the whole cell's chemistry be modeled predictively, from molecules to phenotype?",
 "background": "The systems-biochemistry problem - whole-cell predictive models - has a landmark (Karr's Mycoplasma model, 2012) but the scaling to complex cells is daunting: parameter gaps, multi-scale integration (quantum to cellular), and the data's incompleteness. The models are either detailed-but-narrow or broad-but-coarse. The phenotype-from-molecules prediction - the field's moonshot - is distant. The parts are known; the whole resists computation.",
 "why_it_matters": "Predictive whole-cell models would transform drug design and synthetic biology. The uncomputed whole is the moonshot.",
 "sig_lens": "The Signature lens reads systems biochemistry as the whole symphony: the protocol must score it section by section - and rehearse the sections together.",
 "sig_solution": LABEL + " Assumptions: (1) Mycoplasma landmark; scaling daunting; (2) parameter gaps pervasive. Reasoning path: build modularly - validated module models (metabolism, signaling, gene expression) integrated stepwise. Proposed mechanism: a symphony protocol with module-model validation, integration milestones, and phenotype-prediction benchmarks. Confirm: integrated models predict phenotypes. Kill: the integration proves intractable. Does NOT claim: the whole cell modeled - it scores section by section.",
 "pointer": "The Signature system's proposed approach builds whole-cell models by validated module integration; the companion Signature Edition record specifies the symphony protocol.",
 "key_points": [
  "Karr's Mycoplasma whole-cell model (2012) is the landmark.",
  "Scaling to complex cells daunting.",
  "Parameter gaps pervasive.",
  "Models detailed-but-narrow or broad-but-coarse.",
 ],
 "requirements": [
  "Validated biochemical module models.",
  "Integration milestones.",
  "Phenotype-prediction benchmarks.",
 ],
 "citations": [
  "Karr JR et al. (2012) A whole-cell computational model predicts phenotype from genotype. Cell 150.",
 ],
 "demo": {"vmax": 118.0, "km": 16.0, "s": [3.2, 16.0, 80.0]},
},
# ----------------------------------------------------------------- rank 34
{
 "key": "bc-unified",
 "name": "The Unified Biochemistry Problem",
 "group": "Cellular Organization",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Proteins, nucleic acids, lipids, sugars, metabolites - the molecule classes are studied separately, but can biochemistry be unified as one chemistry of life?",
 "background": "The unified-biochemistry problem - one framework for all biomolecule classes - is the field's synthesis: the classes interact (glycosylated proteins in lipid rafts signaling to nucleic acids via metabolites), but the disciplines are separate (protein science, glycobiology, lipidomics each have journals and cultures). The interactions are the biology; the unification is organizational as much as intellectual. The chemistry of life is one; its science is many.",
 "why_it_matters": "The biology lives in the interactions between molecule classes. The fragmented science misses the unified chemistry.",
 "sig_lens": "The Signature lens reads biochemistry as one language with many dialects: the protocol must write the grammar that covers them all - the interactions, not just the words.",
 "sig_solution": LABEL + " Assumptions: (1) biology in the inter-class interactions; (2) disciplines fragmented. Reasoning path: study the interfaces - glycoproteins in rafts, metabolite signaling, lipid-protein interplay - as the primary objects. Proposed mechanism: a language protocol with interface-focused research programs, cross-class interaction atlases, and unified biochemical education. Confirm: interface studies explain what single-class studies cannot. Kill: the interfaces prove too complex for unification. Does NOT claim: biochemistry unified - it writes the shared grammar.",
 "pointer": "The Signature system's proposed approach studies biomolecular interfaces as primary objects; the companion Signature Edition record specifies the language protocol.",
 "key_points": [
  "Biology lives in inter-class interactions.",
  "Protein, glycan, lipid, metabolite disciplines separate.",
  "Interfaces (glycoproteins in rafts) are primary biology.",
  "Unification is organizational and intellectual.",
 ],
 "requirements": [
  "Interface-focused research programs.",
  "Cross-class interaction atlases.",
  "Unified biochemical frameworks.",
 ],
 "citations": [
  "Lehninger AL et al., Principles of Biochemistry (foundations of unified treatment).",
 ],
 "demo": {"vmax": 125.0, "km": 17.0, "s": [3.4, 17.0, 85.0]},
},
]
