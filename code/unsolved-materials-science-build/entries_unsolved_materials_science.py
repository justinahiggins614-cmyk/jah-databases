#!/usr/bin/env python3
"""Entries for The Unsolved Materials Science Database (unsolved-materials-science)
and its Signature half (unsolved-materials-science-signature).

34 famous unsolved problems in materials science, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
problems through the Signature lens, with Signature-generated proposed
solutions that are ALWAYS labeled as proposals, never established science.

Honesty rule (enforced in every record): never claim proof, never imply
peer acceptance, never present speculation as settled. Signature proposals
are labeled speculation for research discussion only - never engineering
advice, never a materials recommendation; no performance guarantees.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry the Signature system's proposed "
            "solution approaches to famous unsolved problems. Every "
            "solution is labeled a Signature-generated proposal, never "
            "established science, never peer-accepted, never proof, never "
            "engineering advice.")

STD_COMMON = [
    "Problem statements verified against the published materials-science literature; open status confirmed as of 2026.",
    "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
    "Signature proposals are labeled speculation for research discussion only - never engineering advice, never a materials recommendation; no performance guarantees appear.",
]

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "room-temp-superconductor",
 "name": "Room-Temperature Superconductivity",
 "group": "Electronic",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "A room-temperature superconductor would transform civilization - does one exist?",
 "description": "Room-temperature superconductivity - the holy grail of materials science: LK-99 (2023) claimed it and failed; hydrides (LaH10, 2019) superconduct near room temperature but only at extreme pressure. Whether ambient superconductivity is possible remains the field's most famous open question.",
 "background": "Superconductivity (1911, Onnes) required cryogenics; cuprates (1986) raised Tc; hydrides (2015-2019) approached room temperature under pressure; LK-99 (2023) was debunked. As of 2026 ambient superconductivity is unachieved.",
 "why_it_matters": "Room-temperature superconductors would transform power, transport, and computing: the material that changes everything.",
 "sig_pointer": "The Signature system's proposed approach searches for ambient superconductors, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that ambient superconductivity needs guided search: the theoretical guidance (hydride lessons, structure prediction) directing synthesis - with claims rigorously verified. "
  "Assumptions: (1) ambient superconductors exist; (2) theory guides; (3) verification is rigorous. "
  "Reasoning path: a guided-search model explains LK-99's failure and predicts real discovery. "
  "Proposed mechanism: 'theory-guided' superconductor discovery - predicted then verified materials. "
  "What would confirm it: a verified ambient superconductor. "
  "What would kill it: evidence that ambient superconductivity is impossible. "
  "What this does not claim: it does not claim any superconductor exists, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads superconductivity as unguided hype, and asks what theory would direct.",
 "how_it_works": "Researchers study superconductors through hydride synthesis, structure prediction, and rigorous verification.",
 "key_points": [
  "LK-99 (2023) was debunked.",
  "Hydrides superconduct near room temperature under pressure.",
  "Ambient superconductivity is unachieved.",
  "The question is the field's most famous.",
  "Verification standards tightened after LK-99.",
 ],
 "requirements": [
  "Theory-guided material predictions.",
  "Verified ambient superconductors.",
  "Rigorous claim verification.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Drozdov AP et al. Hydride superconductivity. Various; 2015-2019.",
  "Somayazulu M et al. LaH10. Various; 2019-2021.",
  "LK-99 claims and refutations. Various; 2023-2024.",
  "Bednorz JG, Müller KA. Cuprates. Various; 1986-1988.",
 ],
 "demo_data": {"a": ("highest verified Tc at ambient pressure, K (approx)", 138.0),
               "b": ("room temperature, K (approx)", 293.0), "bounds": (0.4, 0.55),
               "step1": "138 kelvin against 293 needed - the most famous gap in materials science",
               "confirm": "a verified ambient superconductor",
               "refute": "ambient superconductivity proves impossible"},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "metallic-glass",
 "name": "Bulk Metallic Glass: The Perfect Metal",
 "group": "Structural",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Metallic glasses are strong and elastic - but they're brittle and hard to make in bulk. Can they be engineered?",
 "description": "Bulk metallic glass - amorphous metals with exceptional strength and elasticity: but they fail catastrophically (shear bands); critical casting thickness is limited; and toughening them without losing their properties is the challenge.",
 "background": "Metallic glasses (1960s, Duwez) were ribbons; bulk glasses (1990s, Johnson, Inoue) enabled applications; but brittleness limited use. As of 2026 BMGs are niche.",
 "why_it_matters": "Tough bulk metallic glass would transform structural materials: the strength of glass with the toughness of metal.",
 "sig_pointer": "The Signature system's proposed approach toughens metallic glasses, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that BMGs need designed toughness: the microstructures (composites, gradients) that arrest shear bands - with properties retained. "
  "Assumptions: (1) shear bands are arrestable; (2) designs work; (3) properties retain. "
  "Reasoning path: a microstructure model explains brittleness and predicts tough glasses. "
  "Proposed mechanism: 'microstructure-designed' tough BMGs - shear-band-arresting metals. "
  "What would confirm it: tough BMGs in structural use. "
  "What would kill it: evidence that amorphous metals are inherently brittle. "
  "What this does not claim: it does not claim tough BMGs exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads metallic glass as brittle promise, and asks what microstructure would toughen.",
 "how_it_works": "Researchers study BMGs through composite design, shear-band research, and casting advances.",
 "key_points": [
  "BMGs are strong and elastic.",
  "They fail via catastrophic shear bands.",
  "Critical casting thickness is limited.",
  "Composites promise toughness.",
  "Applications remain niche.",
 ],
 "requirements": [
  "Shear-band-arresting microstructures.",
  "Tough BMGs in structural use.",
  "Scaled bulk processing.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Johnson WL et al. Bulk metallic glass. Various; 1990s-2010s.",
  "Inoue A et al. BMG development. Various; 1990s-2000s.",
  "Schuh CA et al. Mechanical behavior. Various; 2007-2019.",
  "Hofmann DC et al. BMG composites. Various; 2008-2016.",
 ],
 "demo_data": {"a": ("BMG fracture toughness, MPa√m (approx)", 50.0),
               "b": ("structural steel toughness, MPa√m (approx)", 100.0), "bounds": (0.4, 0.62),
               "step1": "half the toughness of steel - the brittleness behind the strength",
               "confirm": "tough BMGs in structural use",
               "refute": "amorphous metals prove inherently brittle"},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "high-entropy-alloys",
 "name": "High-Entropy Alloys: The Compositional Frontier",
 "group": "Structural",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "High-entropy alloys mix many elements - but the design space is astronomically vast. Can it be navigated?",
 "description": "High-entropy alloys - multi-principal-element materials with exceptional properties: but the compositional space (millions of combinations) is unnavigable by trial; predictive design is the challenge; and the best HEAs may be undiscovered.",
 "background": "HEAs (2004, Yeh, Cantor) launched the field; exceptional cryogenic toughness was found; but design remains Edisonian. As of 2026 the space is largely unexplored.",
 "why_it_matters": "Navigated HEA space would yield transformative alloys: the materials of the unexplored compositions.",
 "sig_pointer": "The Signature system's proposed approach navigates high-entropy alloy space, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that HEA space needs computational navigation: the phase and property predictions - with experiments validating. "
  "Assumptions: (1) predictions are accurate; (2) space is navigable; (3) best alloys are found. "
  "Reasoning path: a computational model explains Edisonian status and predicts designed HEAs. "
  "Proposed mechanism: 'computationally-navigated' HEA design - predicted optimal alloys. "
  "What would confirm it: predicted HEAs outperforming discovered ones. "
  "What would kill it: evidence that HEA space resists prediction. "
  "What this does not claim: it does not claim optimal HEAs are known, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads HEAs as unnavigated vastness, and asks what computation would map.",
 "how_it_works": "Researchers study HEAs through CALPHAD modeling, machine-learning screening, and high-throughput experiments.",
 "key_points": [
  "HEAs mix many principal elements.",
  "The compositional space is vast.",
  "Design is still Edisonian.",
  "Exceptional properties were found.",
  "The best alloys may be undiscovered.",
 ],
 "requirements": [
  "Accurate phase and property prediction.",
  "Predicted HEAs outperforming.",
  "Navigated compositional space.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Yeh JW et al. High-entropy alloys. Various; 2004-2014.",
  "Cantor B et al. HEA development. Various; 2004-2021.",
  "Gludovatz B et al. Cryogenic toughness. Various; 2014-2016.",
  "Miracle DB et al. HEA reviews. Various; 2017-2022.",
 ],
 "demo_data": {"a": ("HEA compositions explored (approx)", 1000.0),
               "b": ("possible HEA compositions (approx)", 1000000.0), "bounds": (0.0005, 0.002),
               "step1": "a thousand explored of a million possible - the unnavigated frontier",
               "confirm": "predicted HEAs outperform discovered ones",
               "refute": "HEA space proves to resist prediction"},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "battery-materials",
 "name": "Battery Materials: Beyond Lithium-Ion",
 "group": "Energy",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Lithium-ion is maturing - what materials enable the next battery revolution?",
 "description": "Battery materials - beyond lithium-ion: solid-state electrolytes, lithium-sulfur, sodium-ion, and multivalent chemistries each promise more; but each faces materials challenges (dendrites, polysulfides, conductivity); and no successor is proven.",
 "background": "Li-ion (1991) transformed storage; solid-state (2010s-2020s) is the leading candidate; sodium-ion commercialized modestly; but Li-ion still dominates. As of 2026 the successor is unproven.",
 "why_it_matters": "Next battery materials would transform transport and grid: the storage revolution's materials.",
 "sig_pointer": "The Signature system's proposed approach discovers next battery materials, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that battery materials need accelerated discovery: the computational screening plus interface engineering - with proven successors. "
  "Assumptions: (1) screening works; (2) interfaces are engineerable; (3) successors prove. "
  "Reasoning path: a discovery model explains Li-ion's persistence and predicts next materials. "
  "Proposed mechanism: 'accelerated-discovery' battery materials - screened proven chemistries. "
  "What would confirm it: successor batteries displacing Li-ion. "
  "What would kill it: evidence that Li-ion is the practical optimum. "
  "What this does not claim: it does not claim successor batteries exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads batteries as Li-ion-locked, and asks what discovery would displace.",
 "how_it_works": "Researchers study battery materials through solid-state development, computational screening, and interface engineering.",
 "key_points": [
  "Li-ion still dominates.",
  "Solid-state is the leading candidate.",
  "Dendrites challenge solid electrolytes.",
  "Sodium-ion commercialized modestly.",
  "No successor is proven.",
 ],
 "requirements": [
  "Proven successor chemistries.",
  "Interface challenges solved.",
  "Successors displacing Li-ion.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Goodenough JB et al. Li-ion history. Various; 1980-2019.",
  "Janek J et al. Solid-state reviews. Various; 2016-2022.",
  "Manthiram A et al. Beyond Li-ion. Various; 2017-2021.",
  "Ceder G et al. Computational screening. Various; 2011-2020.",
 ],
 "demo_data": {"a": ("Li-ion energy density, Wh/kg (approx)", 250.0),
               "b": ("theoretical Li-S density, Wh/kg (approx)", 2600.0), "bounds": (0.07, 0.13),
               "step1": "a tenth of the theoretical - the materials gap in storage",
               "confirm": "successor batteries displace Li-ion",
               "refute": "Li-ion proves the practical optimum"},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "thermoelectrics",
 "name": "Thermoelectrics: Waste Heat to Power",
 "group": "Energy",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Thermoelectrics convert heat to electricity - but efficiency is too low for most uses. Can the figure of merit be raised enough?",
 "description": "Thermoelectric materials - waste-heat recovery: the figure of merit ZT needs to exceed ~3 for broad use; but ZT ~1-2 is typical; and the thermal-electrical tradeoff is fundamental. Nanostructuring raised ZT; the breakthrough is pending.",
 "background": "Thermoelectrics (1950s-60s, Ioffe) were niche; nanostructuring (2000s-2010s) raised ZT; but broad application needs more. As of 2026 thermoelectrics are still niche.",
 "why_it_matters": "Efficient thermoelectrics would harvest the world's waste heat: the power in the discarded.",
 "sig_pointer": "The Signature system's proposed approach raises thermoelectric efficiency, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that thermoelectrics need ZT breakthroughs: the materials decoupling thermal and electrical transport - with ZT above 3. "
  "Assumptions: (1) decoupling is possible; (2) ZT 3 is reachable; (3) applications follow. "
  "Reasoning path: a decoupling model explains the ZT plateau and predicts breakthrough materials. "
  "Proposed mechanism: 'decoupled-transport' thermoelectrics - high-ZT materials. "
  "What would confirm it: ZT above 3 in practical materials. "
  "What would kill it: evidence that the tradeoff is fundamental. "
  "What this does not claim: it does not claim high-ZT materials exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads thermoelectrics as tradeoff-limited, and asks what decoupling would raise.",
 "how_it_works": "Researchers study thermoelectrics through nanostructuring, ZT optimization, and transport theory.",
 "key_points": [
  "ZT ~1-2 is typical; ~3 is needed.",
  "The thermal-electrical tradeoff is fundamental.",
  "Nanostructuring raised ZT.",
  "Applications remain niche.",
  "Waste heat is abundant.",
 ],
 "requirements": [
  "ZT above 3 in practical materials.",
  "Decoupled transport proven.",
  "Broad waste-heat applications.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ioffe AF et al. Thermoelectric foundations. Various; 1950s-1960s.",
  "Snyder GJ et al. ZT reviews. Various; 2008-2021.",
  "Biswas K et al. Nanostructured thermoelectrics. Various; 2012-2019.",
  "He J et al. High-ZT materials. Various; 2016-2022.",
 ],
 "demo_data": {"a": ("typical thermoelectric ZT (approx)", 1.5),
               "b": ("ZT needed for broad use (approx)", 3.0), "bounds": (0.4, 0.62),
               "step1": "half the needed figure of merit - the tradeoff's plateau",
               "confirm": "ZT above 3 in practical materials",
               "refute": "the tradeoff proves fundamental"},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "photovoltaics",
 "name": "Photovoltaics: The Efficiency Limit",
 "group": "Energy",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Solar cells approach theoretical limits - what materials break through?",
 "description": "Photovoltaic materials - the efficiency limit: silicon nears its Shockley-Queisser limit (~29%); perovskites rose spectacularly but degrade; tandems promise more; and the ultimate materials are debated.",
 "background": "Silicon PV (1950s onward) matured; perovskites (2009-2020s) were the sensation; tandems (2020s) push higher. As of 2026 silicon dominates with perovskites pending stability.",
 "why_it_matters": "Breakthrough PV materials would make solar dominant: the efficiency that powers civilization.",
 "sig_pointer": "The Signature system's proposed approach breaks photovoltaic limits, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that PV needs stable breakthroughs: the perovskite stability solved - with tandems exceeding silicon. "
  "Assumptions: (1) stability is solvable; (2) tandems work; (3) limits are breakable. "
  "Reasoning path: a stability model explains perovskite's stall and predicts dominant new PV. "
  "Proposed mechanism: 'stability-solved' photovoltaics - durable high-efficiency cells. "
  "What would confirm it: stable perovskite tandems in production. "
  "What would kill it: evidence that perovskites can't be stabilized. "
  "What this does not claim: it does not claim breakthrough PV exists, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads PV as stability-limited, and asks what durability would make dominant.",
 "how_it_works": "Researchers study PV through perovskite stabilization, tandem development, and limit analyses.",
 "key_points": [
  "Silicon nears its theoretical limit.",
  "Perovskites rose but degrade.",
  "Tandems promise higher efficiency.",
  "Stability is the barrier.",
  "Silicon still dominates.",
 ],
 "requirements": [
  "Stable perovskite materials.",
  "Tandems exceeding silicon.",
  "Production deployment.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Shockley W, Queisser HJ. Efficiency limit. Various; 1961.",
  "Kojima A et al. Perovskites. Various; 2009-2015.",
  "Green MA et al. PV reviews. Various; 2015-2023.",
  "NREL efficiency tables. Various.",
 ],
 "demo_data": {"a": ("silicon cell efficiency, percent (approx)", 26.0),
               "b": ("Shockley-Queisser limit, percent (approx)", 29.0), "bounds": (0.82, 0.97),
               "step1": "ninety percent of the theoretical limit - the matured material",
               "confirm": "stable perovskite tandems in production",
               "refute": "perovskites prove unable to be stabilized"},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "corrosion",
 "name": "Corrosion: The Trillion-Dollar Decay",
 "group": "Structural",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Corrosion costs trillions - can materials be made truly corrosion-proof?",
 "description": "Corrosion - the trillion-dollar decay: it consumes ~3% of GDP; prediction is empirical; and truly corrosion-proof structural materials don't exist. Stainless steels and coatings manage; they don't solve.",
 "background": "Corrosion science (20th century) characterized mechanisms; stainless steels (1910s onward) managed; but prediction remains empirical. As of 2026 corrosion still wins.",
 "why_it_matters": "Corrosion-proof materials would save trillions: the end of the rust tax.",
 "sig_pointer": "The Signature system's proposed approach defeats corrosion, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that corrosion needs predictive prevention: the mechanisms modeled - with immune materials designed. "
  "Assumptions: (1) mechanisms are modelable; (2) immunity is designable; (3) prevention works. "
  "Reasoning path: a mechanism model explains empirical status and predicts corrosion-proof materials. "
  "Proposed mechanism: 'mechanism-designed' corrosion immunity - predictive prevention. "
  "What would confirm it: corrosion-proof structural materials in service. "
  "What would kill it: evidence that corrosion is thermodynamically inevitable. "
  "What this does not claim: it does not claim corrosion-proof materials exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads corrosion as unmanaged decay, and asks what mechanisms would make immune.",
 "how_it_works": "Researchers study corrosion through mechanism modeling, alloy design, and coating research.",
 "key_points": [
  "Corrosion costs ~3% of GDP.",
  "Prediction is empirical.",
  "Stainless steels manage; they don't solve.",
  "Truly immune materials don't exist.",
  "Corrosion still wins.",
 ],
 "requirements": [
  "Predictive corrosion models.",
  "Immune structural materials.",
  "Corrosion-proof service proven.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "NACE corrosion costs. Various; 2016.",
  "Scully JR et al. Corrosion reviews. Various; 2015-2020.",
  "Frankel GS et al. Mechanism research. Various; 2018-2023.",
  "Stainless steel history. Various.",
 ],
 "demo_data": {"a": ("global corrosion cost, trillions (approx)", 2.5),
               "b": ("global GDP, trillions (approx)", 100.0), "bounds": (0.015, 0.038),
               "step1": "two and a half trillion lost to rust - the decay tax",
               "confirm": "corrosion-proof structural materials in service",
               "refute": "corrosion proves thermodynamically inevitable"},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "self-healing-materials",
 "name": "Self-Healing Materials",
 "group": "Functional",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Materials fail by cracking - can they heal themselves like skin?",
 "description": "Self-healing materials - polymers, concrete, and metals that repair damage: microcapsules and reversible bonds work for polymers; but structural self-healing (metals, ceramics) is primitive; and healing is limited.",
 "background": "Self-healing polymers (2000s, White) proved the concept; self-healing concrete (Jonkers, 2010s) followed; but metals lag. As of 2026 healing is polymer-deep.",
 "why_it_matters": "Self-healing structures would end maintenance: the material that repairs itself.",
 "sig_pointer": "The Signature system's proposed approach extends self-healing to structures, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that self-healing needs structural mechanisms: the healing chemistries for metals and ceramics - with strength restored. "
  "Assumptions: (1) mechanisms exist; (2) they restore strength; (3) they scale. "
  "Reasoning path: a mechanism model explains polymer-only status and predicts structural healing. "
  "Proposed mechanism: 'structurally-healing' materials - strength-restoring repair. "
  "What would confirm it: self-healing metals in structural use. "
  "What would kill it: evidence that structural healing is impossible. "
  "What this does not claim: it does not claim self-healing structures exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads healing as polymer-limited, and asks what mechanisms would structuralize.",
 "how_it_works": "Researchers study self-healing through microcapsule systems, reversible chemistry, and metal-healing research.",
 "key_points": [
  "Self-healing polymers work.",
  "Self-healing concrete exists.",
  "Metals and ceramics lag.",
  "Healing is limited in scope.",
  "Structural healing is pending.",
 ],
 "requirements": [
  "Metal and ceramic healing mechanisms.",
  "Strength-restoring repair.",
  "Structural self-healing in use.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "White SR et al. Self-healing polymers. Various; 2001-2014.",
  "Jonkers HM et al. Self-healing concrete. Various; 2011-2018.",
  "Blaiszik BJ et al. Healing reviews. Various; 2010-2015.",
  "Yang Y et al. Metal healing. Various; 2018-2022.",
 ],
 "demo_data": {"a": ("materials with self-healing, classes (approx)", 3.0),
               "b": ("structural material classes (approx)", 10.0), "bounds": (0.2, 0.42),
               "step1": "three healing of ten structural classes - the unhealed majority",
               "confirm": "self-healing metals in structural use",
               "refute": "structural healing proves impossible"},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "glass-strength",
 "name": "Strong Glass: The Transparent Steel",
 "group": "Structural",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Glass is strong in theory but weak in practice - can flaw-tolerant glass be made?",
 "description": "Glass strength - the transparent-steel dream: theoretical strength is enormous, but surface flaws make real glass fail at a hundredth of it. Ion-exchange strengthening toughened surfaces and Gorilla Glass commercialized it, yet bulk flaw tolerance - glass that stays strong despite its flaws - remains unachieved, and every window and screen is still living on borrowed strength.",
 "background": "Glass strengthening (1960s-70s, ion exchange) improved surfaces; Gorilla Glass (2000s) commercialized; but bulk flaw tolerance is pending. As of 2026 glass is still flaw-limited.",
 "why_it_matters": "Strong glass would transform construction and devices: transparency with steel's strength.",
 "sig_pointer": "The Signature system's proposed approach makes glass flaw-tolerant, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that glass needs flaw tolerance: the microstructures that arrest cracks - with transparency retained. "
  "Assumptions: (1) cracks are arrestable; (2) transparency retains; (3) strength follows. "
  "Reasoning path: a microstructure model explains flaw-limited strength and predicts strong glass. "
  "Proposed mechanism: 'flaw-tolerant' glass - crack-arresting transparency. "
  "What would confirm it: flaw-tolerant glass in structural use. "
  "What would kill it: evidence that glass is inherently flaw-limited. "
  "What this does not claim: it does not claim strong glass exists, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads glass as flaw-defeated, and asks what microstructure would make tolerant.",
 "how_it_works": "Researchers study glass strength through ion-exchange research, flaw mechanics, and composite approaches.",
 "key_points": [
  "Theoretical glass strength is enormous.",
  "Surface flaws make real glass weak.",
  "Gorilla Glass toughened surfaces.",
  "Bulk flaw tolerance is unachieved.",
  "Glass is still flaw-limited.",
 ],
 "requirements": [
  "Crack-arresting microstructures.",
  "Transparency retained.",
  "Structural strong glass.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Corning Gorilla Glass. Various; 2007 onward.",
  "Lawn BR et al. Glass fracture. Various; 1993-2017.",
  "Rouxel T et al. Glass mechanics. Various; 2017-2022.",
  "Wondraczek L et al. Strength reviews. Various; 2011-2020.",
 ],
 "demo_data": {"a": ("real glass strength, GPa (approx)", 0.1),
               "b": ("theoretical glass strength, GPa (approx)", 10.0), "bounds": (0.005, 0.018),
               "step1": "a hundredth of theoretical - the flaw's victory",
               "confirm": "flaw-tolerant glass in structural use",
               "refute": "glass proves inherently flaw-limited"},
},
# ------------------------------------------------------------------ rank 10
{
 "key": "shape-memory",
 "name": "Shape-Memory Materials: The Programmable Metal",
 "group": "Functional",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Shape-memory alloys remember shapes - but they're limited to NiTi. Can programmable metals be generalized?",
 "description": "Shape-memory materials - programmable metals that remember their shapes: NiTi (nitinol) dominates the field, but the alloy palette is narrow, fatigue limits how many cycles they survive, and high-temperature shape memory is barely developed. Medical devices made nitinol famous, yet generalization to new compositions with tuned transformations remains stalled.",
 "background": "Nitinol (1960s) was the discovery; medical devices (1990s-2000s) were the application; but generalization stalled. As of 2026 NiTi still dominates.",
 "why_it_matters": "Generalized shape memory would make programmable structures: the metal that remembers.",
 "sig_pointer": "The Signature system's proposed approach generalizes shape-memory materials, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that shape memory needs alloy generalization: the new compositions with tuned transformation - with fatigue solved. "
  "Assumptions: (1) new alloys exist; (2) transformations are tunable; (3) fatigue is solvable. "
  "Reasoning path: an alloy model explains NiTi's dominance and predicts generalized memory. "
  "Proposed mechanism: 'alloy-generalized' shape memory - tuned programmable metals. "
  "What would confirm it: new shape-memory alloys in applications. "
  "What would kill it: evidence that NiTi is the practical optimum. "
  "What this does not claim: it does not claim new alloys exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads shape memory as one-alloy wonder, and asks what compositions would generalize.",
 "how_it_works": "Researchers study shape memory through alloy development, transformation theory, and fatigue research.",
 "key_points": [
  "NiTi dominates shape memory.",
  "The alloy palette is narrow.",
  "Fatigue limits cycle life.",
  "High-temperature memory is undeveloped.",
  "Medical devices are the main use.",
 ],
 "requirements": [
  "New shape-memory compositions.",
  "Tuned transformations.",
  "Fatigue solved.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Nitinol discovery. Various; 1960s.",
  "Otsuka K et al. Shape-memory reviews. Various; 1998-2016.",
  "Ma J et al. High-temperature SMAs. Various; 2010-2020.",
  "Lagoudas DC et al. Modeling. Various; 2008-2018.",
 ],
 "demo_data": {"a": ("shape-memory alloys in wide use (approx)", 3.0),
               "b": ("candidate alloy systems (approx)", 50.0), "bounds": (0.03, 0.1),
               "step1": "three in use of fifty candidates - the unremembered alloys",
               "confirm": "new shape-memory alloys in applications",
               "refute": "NiTi proves the practical optimum"},
},
# ------------------------------------------------------------------ rank 11
{
 "key": "catalyst-design",
 "name": "Catalyst Design: The Rational Catalyst",
 "group": "Functional",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Catalysts are discovered by trial - can they be designed rationally from first principles?",
 "description": "Catalyst design - the rational catalyst: most industrial catalysts are still found by empirical screening, even though computational methods like Nørskov's d-band theory enable semi-rational design. True first-principles design - predicting the active site and synthesizing it - remains unachieved, and industry still screens where theory could design.",
 "background": "Catalysis science (20th century) was empirical; DFT methods (1990s-2000s, Nørskov) enabled rational design; but industry still screens. As of 2026 design is semi-rational.",
 "why_it_matters": "Rational catalysts would transform chemistry: the designed reaction.",
 "sig_pointer": "The Signature system's proposed approach designs catalysts rationally, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that catalysts need first-principles design: the active sites predicted - with industrial catalysts designed. "
  "Assumptions: (1) sites are predictable; (2) design works; (3) industry adopts. "
  "Reasoning path: a design model explains empirical status and predicts rational catalysts. "
  "Proposed mechanism: 'first-principles' catalyst design - predicted active sites. "
  "What would confirm it: designed industrial catalysts in use. "
  "What would kill it: evidence that catalysis resists first-principles design. "
  "What this does not claim: it does not claim rational catalysts exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads catalysis as empirical art, and asks what principles would design.",
 "how_it_works": "Researchers study catalyst design through DFT screening, d-band theory, and industrial collaboration.",
 "key_points": [
  "Most catalysts are found empirically.",
  "DFT enables semi-rational design.",
  "Industry still screens experimentally.",
  "True first-principles design is unachieved.",
  "The d-band model guides.",
 ],
 "requirements": [
  "Predicted active sites.",
  "Designed industrial catalysts.",
  "First-principles design proven.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Nørskov JK et al. d-band theory. Various; 1990s-2010s.",
  "Ertl G et al. Catalysis science. Various; 2008-2015.",
  "Studt F et al. Computational design. Various; 2015-2021.",
  "Schlögl R et al. Industrial catalysis. Various; 2015-2020.",
 ],
 "demo_data": {"a": ("industrial catalysts designed computationally (approx)", 5.0),
               "b": ("industrial catalysts in use (approx)", 100.0), "bounds": (0.03, 0.08),
               "step1": "five designed of a hundred used - the empirical art",
               "confirm": "designed industrial catalysts in use",
               "refute": "catalysis proves to resist first-principles design"},
},
# ------------------------------------------------------------------ rank 12
{
 "key": "materials-genome",
 "name": "The Materials Genome: Computing New Materials",
 "group": "Theory",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Can computation discover materials faster than experiment - the Materials Genome realized?",
 "description": "The Materials Genome Initiative (2011) promised computation that discovers materials faster than experiment: databases like the Materials Project computed thousands of candidates, but computed materials often can't be synthesized, synthesizability prediction is still primitive, and the discovery loop - compute, make, test, learn - remains stubbornly slow.",
 "background": "MGI (2011) launched the vision; the Materials Project computed thousands; but synthesis remains the bottleneck. As of 2026 computation proposes; experiment disposes.",
 "why_it_matters": "Realized materials genomics would accelerate discovery: the computed material made real.",
 "sig_pointer": "The Signature system's proposed approach closes the materials-genome loop, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that materials genomics needs synthesis prediction: the synthesizability computed - with closed discovery loops. "
  "Assumptions: (1) synthesizability is predictable; (2) loops close; (3) discovery accelerates. "
  "Reasoning path: a loop model explains the synthesis bottleneck and predicts realized genomics. "
  "Proposed mechanism: 'loop-closed' materials genomics - predicted synthesizable materials. "
  "What would confirm it: computed materials routinely synthesized. "
  "What would kill it: evidence that synthesis resists prediction. "
  "What this does not claim: it does not claim closed-loop discovery exists, offers no engineering advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads genomics as synthesis-blocked, and asks what prediction would close.",
 "how_it_works": "Researchers study materials genomics through synthesizability prediction, autonomous labs, and database growth.",
 "key_points": [
  "MGI launched in 2011.",
  "The Materials Project computed thousands.",
  "Synthesis is the bottleneck.",
  "Computed materials often can't be made.",
  "The loop is still slow.",
 ],
 "requirements": [
  "Synthesizability prediction.",
  "Closed discovery loops.",
  "Routine computed-to-real materials.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Materials Genome Initiative. 2011.",
  "Jain A et al. Materials Project. Various; 2013-2020.",
  "Ceder G et al. Genomics reviews. Various; 2016-2021.",
  "Szymanski NJ et al. Autonomous labs. Various; 2023-2024.",
 ],
 "demo_data": {"a": ("computed materials synthesized, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.18),
               "step1": "nine in ten computed never made - the unclosed loop",
               "confirm": "computed materials routinely synthesized",
               "refute": "synthesis proves to resist prediction"},
},
# ------------------------------------------------------------------ rank 13
{
 "key": "grain-boundaries",
 "name": "Grain Boundaries: The Weak Links",
 "group": "Structural",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Grain boundaries control strength and failure - but can they be engineered atom by atom?",
 "description": "Grain-boundary engineering - the weak links: boundaries govern creep, fracture, and corrosion; but designing them atomistically is aspirational; and the structure-property relationships are incomplete.",
 "background": "Grain-boundary engineering (1980s-90s, Watanabe) improved properties; atomistic simulations (2000s-2010s) revealed mechanisms; but design is still coarse. As of 2026 boundaries are managed, not designed.",
 "why_it_matters": "Designed grain boundaries would transform metals: strength at the atomic seams.",
 "sig_pointer": "The Signature system's proposed approach engineers grain boundaries atomistically, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that boundaries need atomistic design: the structures predicted and built - with properties controlled. "
  "Assumptions: (1) structures are predictable; (2) they are buildable; (3) properties follow. "
  "Reasoning path: an atomistic model explains coarse control and predicts designed boundaries. "
  "Proposed mechanism: 'atomistically-designed' grain boundaries - built atomic seams. "
  "What would confirm it: designed boundaries in structural metals. "
  "What would kill it: evidence that boundaries resist atomistic control. "
  "What this does not claim: it does not claim designed boundaries exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads boundaries as unmanaged seams, and asks what atomistics would design.",
 "how_it_works": "Researchers study grain boundaries through atomistic simulation, boundary engineering, and property mapping.",
 "key_points": [
  "Boundaries govern creep, fracture, corrosion.",
  "Design is still coarse.",
  "Atomistic simulations revealed mechanisms.",
  "Structure-property relationships are incomplete.",
  "Boundaries are managed, not designed.",
 ],
 "requirements": [
  "Predicted boundary structures.",
  "Built designed boundaries.",
  "Controlled properties.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Watanabe T et al. Boundary engineering. Various; 1984-2011.",
  "Sutton AP et al. Interface science. Various; 1995-2006.",
  "Rohrer GS et al. Boundary character. Various; 2011-2020.",
  "Holm EA et al. Simulation reviews. Various; 2010-2019.",
 ],
 "demo_data": {"a": ("boundaries designed atomistically, percent (approx)", 5.0),
               "b": ("percent scale", 100.0), "bounds": (0.03, 0.08),
               "step1": "one in twenty designed - the unmanaged seams",
               "confirm": "designed boundaries in structural metals",
               "refute": "boundaries prove to resist atomistic control"},
},
# ------------------------------------------------------------------ rank 14
{
 "key": "fatigue",
 "name": "Fatigue: The Unpredictable Failure",
 "group": "Structural",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Fatigue kills structures unpredictably - can failure be predicted from first principles?",
 "description": "Fatigue - the unpredictable failure: S-N curves are empirical; crack initiation is stochastic; and first-principles prediction of fatigue life is unachieved. Structures are overdesigned against the unknown.",
 "background": "Fatigue research (19th-20th century, Wöhler, Paris) was empirical; fracture mechanics (1960s) helped; but initiation remains stochastic. As of 2026 fatigue is still predicted empirically.",
 "why_it_matters": "Predicted fatigue would end overdesign: the failure foreseen.",
 "sig_pointer": "The Signature system's proposed approach predicts fatigue from first principles, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that fatigue needs first-principles prediction: the initiation and growth modeled - with life predicted. "
  "Assumptions: (1) initiation is modelable; (2) stochasticity is tameable; (3) prediction works. "
  "Reasoning path: a physics model explains empirical status and predicts fatigue life. "
  "Proposed mechanism: 'first-principles' fatigue prediction - modeled failure. "
  "What would confirm it: predicted fatigue lives matching service. "
  "What would kill it: evidence that fatigue is inherently stochastic. "
  "What this does not claim: it does not claim fatigue prediction exists, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads fatigue as empirical mystery, and asks what physics would predict.",
 "how_it_works": "Researchers study fatigue through initiation research, crystal-plasticity modeling, and life-prediction methods.",
 "key_points": [
  "S-N curves are empirical.",
  "Crack initiation is stochastic.",
  "First-principles prediction is unachieved.",
  "Structures are overdesigned.",
  "Fracture mechanics helped partially.",
 ],
 "requirements": [
  "Modeled initiation and growth.",
  "Predicted lives matching service.",
  "First-principles prediction proven.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Wöhler A et al. Fatigue foundations. Various; 1850s-1870s.",
  "Paris PC et al. Fracture mechanics. Various; 1961-1971.",
  "Suresh S. Fatigue of Materials. Various; 1991-2004.",
  "McDowell DL et al. Crystal plasticity. Various; 2010-2020.",
 ],
 "demo_data": {"a": ("fatigue-life prediction error, percent (approx)", 100.0),
               "b": ("acceptable error, percent (approx)", 20.0), "bounds": (4.0, 6.5),
               "step1": "five times the acceptable error - the unpredictable failure",
               "confirm": "predicted fatigue lives match service",
               "refute": "fatigue proves inherently stochastic"},
},
# ------------------------------------------------------------------ rank 15
{
 "key": "quasicrystals",
 "name": "Quasicrystals: The Impossible Materials",
 "group": "Structural",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Quasicrystals broke crystallography - but can their unusual properties be exploited?",
 "description": "Quasicrystals - the impossible materials: Shechtman's 1982 discovery broke periodicity; but applications are limited (coatings); and whether their unique properties (low friction, hardness) can be broadly exploited is open.",
 "background": "Shechtman (1982, Nobel 2011) discovered quasicrystals; the field characterized them; but applications lagged. As of 2026 quasicrystals are scientifically fascinating and practically niche.",
 "why_it_matters": "Exploited quasicrystals would open a materials class: the properties of the impossible.",
 "sig_pointer": "The Signature system's proposed approach exploits quasicrystal properties, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that quasicrystals need application engineering: the properties (friction, hardness) exploited - with scalable production. "
  "Assumptions: (1) properties are exploitable; (2) production scales; (3) applications follow. "
  "Reasoning path: an applications model explains niche status and predicts exploited quasicrystals. "
  "Proposed mechanism: 'application-engineered' quasicrystals - scaled useful materials. "
  "What would confirm it: quasicrystals in broad applications. "
  "What would kill it: evidence that quasicrystals are inherently impractical. "
  "What this does not claim: it does not claim broad quasicrystal use exists, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads quasicrystals as unexploited discovery, and asks what engineering would apply.",
 "how_it_works": "Researchers study quasicrystals through property research, coating applications, and production scaling.",
 "key_points": [
  "Shechtman discovered quasicrystals (1982).",
  "They broke crystallographic periodicity.",
  "Applications are limited to coatings.",
  "Unique properties are underexploited.",
  "They remain practically niche.",
 ],
 "requirements": [
  "Exploited unique properties.",
  "Scalable quasicrystal production.",
  "Broad applications.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Shechtman D et al. Quasicrystal discovery. Various; 1982-1984.",
  "Nobel Prize in Chemistry. 2011.",
  "Dubois JM et al. Quasicrystal applications. Various; 2005-2015.",
  "Steurer W et al. Quasicrystal reviews. Various; 2012-2020.",
 ],
 "demo_data": {"a": ("quasicrystal applications in broad use (approx)", 3.0),
               "b": ("promising quasicrystal properties (approx)", 20.0), "bounds": (0.08, 0.25),
               "step1": "three applied of twenty promising - the unexploited impossible",
               "confirm": "quasicrystals in broad applications",
               "refute": "quasicrystals prove inherently impractical"},
},
# ------------------------------------------------------------------ rank 16
{
 "key": "metamaterials",
 "name": "Metamaterials: The Designed Impossible",
 "group": "Functional",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Metamaterials achieve impossible properties - but can they be manufactured at scale?",
 "description": "Metamaterials - designed impossible properties like negative refractive index and cloaking: the physics was demonstrated in the 2000s, but manufacturing at optical scales is brutally hard, losses are high, and real applications remain limited. The field proved the impossible possible, then stalled on making it practical.",
 "background": "Metamaterials (2000s, Pendry, Smith) were the sensation; cloaking was demonstrated; but scale and loss limited them. As of 2026 metamaterials are still seeking applications.",
 "why_it_matters": "Scaled metamaterials would transform optics and more: the designed property made real.",
 "sig_pointer": "The Signature system's proposed approach scales metamaterials, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that metamaterials need scalable manufacturing: the nanostructures built at scale - with losses managed. "
  "Assumptions: (1) manufacturing scales; (2) losses are manageable; (3) applications follow. "
  "Reasoning path: a manufacturing model explains the application gap and predicts scaled metamaterials. "
  "Proposed mechanism: 'scalably-manufactured' metamaterials - low-loss production. "
  "What would confirm it: metamaterials in real products. "
  "What would kill it: evidence that metamaterials can't scale. "
  "What this does not claim: it does not claim scaled metamaterials exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads metamaterials as unmanufacturable physics, and asks what production would scale.",
 "how_it_works": "Researchers study metamaterials through nanofabrication, loss reduction, and application development.",
 "key_points": [
  "Impossible properties were demonstrated.",
  "Manufacturing at optical scales is hard.",
  "Losses are high.",
  "Real applications are limited.",
  "Cloaking was the famous demo.",
 ],
 "requirements": [
  "Scaled nanostructure manufacturing.",
  "Managed losses.",
  "Metamaterials in real products.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Pendry JB et al. Metamaterial theory. Various; 2000-2006.",
  "Smith DR et al. Demonstrations. Various; 2000-2010.",
  "Shalaev VM et al. Optical metamaterials. Various; 2007-2019.",
  "Zheludev NI et al. Reviews. Various; 2015-2021.",
 ],
 "demo_data": {"a": ("metamaterial products in wide use (approx)", 2.0),
               "b": ("metamaterial concepts demonstrated (approx)", 100.0), "bounds": (0.01, 0.035),
               "step1": "two products of a hundred concepts - the unmanufactured impossible",
               "confirm": "metamaterials in real products",
               "refute": "metamaterials prove unable to scale"},
},
# ------------------------------------------------------------------ rank 17
{
 "key": "2d-materials",
 "name": "2D Materials: Beyond Graphene",
 "group": "Electronic",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Graphene is wonderful but hard to use - can 2D materials be manufactured and integrated?",
 "description": "2D materials - beyond graphene: the properties are extraordinary, from ballistic transport to single-atom membranes, but large-area defect-free growth is still hard, integration with silicon manufacturing is unsolved, and the killer application remains debated. Isolated in 2004, the 2D family grew - yet scale still eludes it.",
 "background": "Graphene (2004, Geim, Novoselov) was isolated; the 2D family grew (MoS2, hBN); but manufacturing lagged. As of 2026 2D materials are still seeking scale.",
 "why_it_matters": "Scaled 2D materials would transform electronics: the atom-thin future.",
 "sig_pointer": "The Signature system's proposed approach scales 2D materials, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that 2D materials need manufacturing scale: the defect-free growth at wafer scale - with silicon integration. "
  "Assumptions: (1) growth scales; (2) defects are controllable; (3) integration works. "
  "Reasoning path: a manufacturing model explains the application gap and predicts 2D electronics. "
  "Proposed mechanism: 'wafer-scaled' 2D materials - integrated atom-thin devices. "
  "What would confirm it: 2D materials in commercial electronics. "
  "What would kill it: evidence that 2D materials can't be manufactured. "
  "What this does not claim: it does not claim scaled 2D materials exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads 2D materials as unmanufacturable wonder, and asks what growth would scale.",
 "how_it_works": "Researchers study 2D materials through CVD growth, defect control, and integration research.",
 "key_points": [
  "Graphene was isolated in 2004.",
  "Properties are extraordinary.",
  "Large-area defect-free growth is hard.",
  "Silicon integration is unsolved.",
  "The killer app is debated.",
 ],
 "requirements": [
  "Wafer-scale defect-free growth.",
  "Silicon integration.",
  "Commercial 2D electronics.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Geim AK, Novoselov KS. Graphene. Various; 2004-2010.",
  "Nobel Prize in Physics. 2010.",
  "Akinwande D et al. 2D electronics. Various; 2014-2019.",
  "Lemme MC et al. Integration reviews. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("wafer-scale 2D films defect-free, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.18),
               "step1": "nine in ten wafers defective - the ungrown wonder",
               "confirm": "2D materials in commercial electronics",
               "refute": "2D materials prove unable to be manufactured"},
},
# ------------------------------------------------------------------ rank 18
{
 "key": "topological-materials",
 "name": "Topological Materials: The Protected States",
 "group": "Electronic",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Topological insulators host protected states - but can they be turned into technologies?",
 "description": "Topological materials - protected surface states that won the 2016 Nobel Prize: the physics is profound, promising topological quantum computing and spintronics, but devices remain aspirational and material quality limits progress. The field is rich in physics and poor in technology - the protected states still waiting to be harnessed.",
 "background": "Topological insulators (2000s-2010s, Kane, Mele, Zhang) were discovered; the Nobel (2016) recognized; but applications lag. As of 2026 topology is physics-rich and technology-poor.",
 "why_it_matters": "Topological technologies would be robust by physics: the protected state made useful.",
 "sig_pointer": "The Signature system's proposed approach builds topological technologies, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that topological materials need device engineering: the protected states harnessed - with material quality. "
  "Assumptions: (1) states are harnessable; (2) quality is achievable; (3) devices follow. "
  "Reasoning path: a device model explains the technology gap and predicts topological devices. "
  "Proposed mechanism: 'device-engineered' topological materials - harnessed protection. "
  "What would confirm it: topological devices in applications. "
  "What would kill it: evidence that topology can't be technologized. "
  "What this does not claim: it does not claim topological devices exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads topology as unharnessed physics, and asks what engineering would make useful.",
 "how_it_works": "Researchers study topological materials through crystal growth, device prototyping, and Majorana research.",
 "key_points": [
  "Protected states won the 2016 Nobel.",
  "Devices are aspirational.",
  "Material quality limits progress.",
  "Topological quantum computing is the dream.",
  "Physics is rich; technology is poor.",
 ],
 "requirements": [
  "High-quality topological materials.",
  "Harnessed protected states.",
  "Topological devices in applications.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kane CL, Mele EJ. Topological insulators. Various; 2005-2010.",
  "Nobel Prize in Physics. 2016.",
  "Hasan MZ et al. Reviews. Various; 2010-2021.",
  "Nayak C et al. Topological quantum computing. Various; 2008-2018.",
 ],
 "demo_data": {"a": ("topological devices in applications (approx)", 1.0),
               "b": ("topological material papers (approx)", 10000.0), "bounds": (0.00005, 0.0002),
               "step1": "one device against ten thousand papers - the unharnessed protection",
               "confirm": "topological devices in applications",
               "refute": "topology proves unable to be technologized"},
},
# ------------------------------------------------------------------ rank 19
{
 "key": "ferroelectrics",
 "name": "Ferroelectrics: The Memory Materials",
 "group": "Electronic",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Ferroelectrics could make universal memory - but can they be integrated with silicon?",
 "description": "Ferroelectric materials - universal-memory candidates: HfO2 ferroelectricity (2011) enabled CMOS integration; but endurance, retention, and variability challenge FeRAM/FeFET; and the universal memory is pending.",
 "background": "Ferroelectrics (1920s-50s) were classic; HfO2 (2011, Böscke) revived the field; FeFETs are in development. As of 2026 integration is progressing with reliability pending.",
 "why_it_matters": "Ferroelectric memory would be universal: fast, dense, nonvolatile.",
 "sig_pointer": "The Signature system's proposed approach makes ferroelectric memory universal, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that ferroelectrics need reliability: the endurance and retention proven - with CMOS integration. "
  "Assumptions: (1) reliability is achievable; (2) integration works; (3) memory follows. "
  "Reasoning path: a reliability model explains the pending status and predicts universal memory. "
  "Proposed mechanism: 'reliability-proven' ferroelectrics - integrated universal memory. "
  "What would confirm it: ferroelectric universal memory in products. "
  "What would kill it: evidence that ferroelectrics can't meet reliability. "
  "What this does not claim: it does not claim universal memory exists, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads ferroelectrics as unreliable promise, and asks what proof would make universal.",
 "how_it_works": "Researchers study ferroelectrics through HfO2 research, FeFET development, and reliability studies.",
 "key_points": [
  "HfO2 ferroelectricity enabled CMOS integration.",
  "Endurance and retention are challenges.",
  "FeFETs are in development.",
  "Universal memory is pending.",
  "Reliability is the barrier.",
 ],
 "requirements": [
  "Proven endurance and retention.",
  "CMOS-integrated ferroelectric memory.",
  "Universal memory in products.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Böscke TS et al. HfO2 ferroelectricity. Various; 2011-2012.",
  "Müller J et al. FeFET development. Various; 2012-2020.",
  "Park MH et al. HfO2 reviews. Various; 2015-2021.",
  "Ali T et al. Reliability studies. Various; 2019-2023.",
 ],
 "demo_data": {"a": ("FeFET endurance, cycles (approx)", 10000000000.0),
               "b": ("flash endurance, cycles (approx)", 100000.0), "bounds": (80000.0, 120000.0),
               "step1": "a hundred thousand times flash's endurance - the reliability already demonstrated",
               "confirm": "ferroelectric universal memory in products",
               "refute": "ferroelectrics prove unable to meet reliability"},
},
# ------------------------------------------------------------------ rank 20
{
 "key": "magnetic-materials",
 "name": "Magnetic Materials: Beyond Rare Earths",
 "group": "Functional",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Permanent magnets need rare earths - can high-performance magnets avoid them?",
 "description": "Magnetic materials - beyond rare earths: NdFeB dominates; but supply is concentrated; alternatives (MnBi, FeNi, high-entropy magnets) are inferior; and the rare-earth-free high-performance magnet is unachieved.",
 "background": "NdFeB (1980s, Sagawa) was the breakthrough; supply concerns (2010s) drove the search; but alternatives lag. As of 2026 rare earths still dominate.",
 "why_it_matters": "Rare-earth-free magnets would secure clean energy: the magnet without the monopoly.",
 "sig_pointer": "The Signature system's proposed approach discovers rare-earth-free magnets, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that magnets need computational discovery: the rare-earth-free compositions predicted - with performance proven. "
  "Assumptions: (1) compositions exist; (2) they are predictable; (3) they perform. "
  "Reasoning path: a discovery model explains rare-earth dominance and predicts free magnets. "
  "Proposed mechanism: 'computationally-discovered' rare-earth-free magnets - predicted performance. "
  "What would confirm it: rare-earth-free magnets matching NdFeB. "
  "What would kill it: evidence that rare earths are irreplaceable. "
  "What this does not claim: it does not claim free magnets exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads magnets as monopoly-dependent, and asks what discovery would free.",
 "how_it_works": "Researchers study magnetic materials through computational screening, MnBi/FeNi development, and supply analyses.",
 "key_points": [
  "NdFeB dominates permanent magnets.",
  "Supply is geographically concentrated.",
  "Alternatives are inferior.",
  "Rare-earth-free high performance is unachieved.",
  "Clean energy needs magnets.",
 ],
 "requirements": [
  "Predicted rare-earth-free compositions.",
  "Performance matching NdFeB.",
  "Commercial free magnets.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Sagawa M et al. NdFeB. Various; 1984-1987.",
  "Coey JMD et al. Magnet reviews. Various; 2002-2020.",
  "Lewis LH et al. Rare-earth-free research. Various; 2013-2020.",
  "Skokov KP et al. Alternative magnets. Various; 2015-2022.",
 ],
 "demo_data": {"a": ("rare-earth-free magnet energy product, MGOe (approx)", 15.0),
               "b": ("NdFeB energy product, MGOe (approx)", 50.0), "bounds": (0.2, 0.42),
               "step1": "three-tenths the energy product - the monopoly's moat",
               "confirm": "rare-earth-free magnets match NdFeB",
               "refute": "rare earths prove irreplaceable"},
},
# ------------------------------------------------------------------ rank 21
{
 "key": "solid-electrolytes",
 "name": "Solid Electrolytes: The Battery Bottleneck",
 "group": "Energy",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Solid-state batteries need solid electrolytes - but conductivity, stability, and interfaces all challenge. Can the bottleneck be broken?",
 "description": "Solid electrolytes - the battery bottleneck: sulfides conduct well but are unstable; oxides are stable but resistive; and the lithium-metal interface defeats both. No solid electrolyte does everything.",
 "background": "Solid electrolytes (1970s-80s) were known; the solid-state push (2010s-2020s) intensified research; but the trifecta (conductivity, stability, interface) is unachieved. As of 2026 the bottleneck persists.",
 "why_it_matters": "The complete solid electrolyte would enable solid-state batteries: the bottleneck broken.",
 "sig_pointer": "The Signature system's proposed approach builds the complete solid electrolyte, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that electrolytes need trifecta design: the conductivity, stability, and interface engineered together - not separately. "
  "Assumptions: (1) the trifecta is achievable; (2) joint design works; (3) batteries follow. "
  "Reasoning path: a joint-design model explains the bottleneck and predicts complete electrolytes. "
  "Proposed mechanism: 'trifecta-designed' solid electrolytes - complete materials. "
  "What would confirm it: solid electrolytes enabling commercial solid-state batteries. "
  "What would kill it: evidence that the trifecta is impossible. "
  "What this does not claim: it does not claim complete electrolytes exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads electrolytes as tradeoff-bound, and asks what joint design would complete.",
 "how_it_works": "Researchers study solid electrolytes through sulfide/oxide development, interface engineering, and conductivity research.",
 "key_points": [
  "Sulfides conduct but are unstable.",
  "Oxides are stable but resistive.",
  "The lithium interface defeats both.",
  "No electrolyte does everything.",
  "The trifecta is unachieved.",
 ],
 "requirements": [
  "Conductivity plus stability plus interface.",
  "Complete solid electrolytes.",
  "Commercial solid-state batteries.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kamaya N et al. Sulfide electrolytes. Various; 2011-2014.",
  "Murugan R et al. Garnet oxides. Various; 2007-2013.",
  "Janek J et al. Interface research. Various; 2016-2022.",
  "Manthiram A et al. Electrolyte reviews. Various; 2017-2021.",
 ],
 "demo_data": {"a": ("solid electrolytes meeting all three criteria (approx)", 1.0),
               "b": ("solid electrolytes studied (approx)", 100.0), "bounds": (0.004, 0.02),
               "step1": "one complete of a hundred studied - the unbroken bottleneck",
               "confirm": "solid electrolytes enable commercial solid-state batteries",
               "refute": "the trifecta proves impossible"},
},
# ------------------------------------------------------------------ rank 22
{
 "key": "hydrogen-materials",
 "name": "Hydrogen Storage Materials",
 "group": "Energy",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Hydrogen is hard to store - can materials hold it densely and reversibly?",
 "description": "Hydrogen storage materials - metal hydrides, MOFs, complex hydrides: the DOE targets (5.5 wt%) are unmet by practical materials; kinetics and thermodynamics fight; and no material stores hydrogen well enough.",
 "background": "Hydride research (1970s-80s) found storage; MOFs (2000s-2010s) promised; but practical targets are unmet. As of 2026 hydrogen is stored as compressed gas.",
 "why_it_matters": "Dense hydrogen storage would enable the hydrogen economy: the tank made material.",
 "sig_pointer": "The Signature system's proposed approach stores hydrogen densely, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that storage needs designed thermodynamics: the materials with tuned binding - meeting DOE targets. "
  "Assumptions: (1) thermodynamics are tunable; (2) targets are reachable; (3) materials prove. "
  "Reasoning path: a thermodynamics model explains the target gap and predicts storage materials. "
  "Proposed mechanism: 'thermodynamically-tuned' hydrogen storage - target-meeting materials. "
  "What would confirm it: materials meeting DOE storage targets. "
  "What would kill it: evidence that targets are thermodynamically impossible. "
  "What this does not claim: it does not claim storage materials exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads hydrogen as unstored energy, and asks what thermodynamics would hold.",
 "how_it_works": "Researchers study hydrogen storage through hydride development, MOF research, and thermodynamics modeling.",
 "key_points": [
  "DOE targets (5.5 wt%) are unmet.",
  "Kinetics and thermodynamics fight.",
  "Compressed gas is the current solution.",
  "No material stores well enough.",
  "MOFs promised but underdelivered.",
 ],
 "requirements": [
  "Tuned binding thermodynamics.",
  "DOE targets met.",
  "Practical storage materials.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Schlapbach L et al. Hydride storage. Various; 2001-2009.",
  "DOE storage targets. Various.",
  "Murray LJ et al. MOF storage. Various; 2009-2015.",
  "Allendorf MD et al. Storage reviews. Various; 2018-2022.",
 ],
 "demo_data": {"a": ("practical storage capacity, wt% (approx)", 2.0),
               "b": ("DOE target, wt% (approx)", 5.5), "bounds": (0.25, 0.5),
               "step1": "two percent against five and a half needed - the unstored fuel",
               "confirm": "materials meet DOE storage targets",
               "refute": "targets prove thermodynamically impossible"},
},
# ------------------------------------------------------------------ rank 23
{
 "key": "cement",
 "name": "Green Cement: Decarbonizing Concrete",
 "group": "Structural",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Cement makes 8% of CO2 - can the world's most-used material be decarbonized?",
 "description": "Green cement - decarbonizing concrete: Portland cement's chemistry releases CO2 inherently; alternatives (geopolymers, LC3, carbon capture) help partially; but the scale (4 billion tons) dwarfs solutions.",
 "background": "Cement's emissions were quantified (2000s-2010s); alternatives developed; but Portland still dominates. As of 2026 decarbonization is partial.",
 "why_it_matters": "Green cement would cut 8% of global CO2: the decarbonized foundation.",
 "sig_pointer": "The Signature system's proposed approach decarbonizes cement, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that cement needs chemistry change: the alternative binders scaled - with Portland displaced. "
  "Assumptions: (1) alternatives perform; (2) they scale; (3) displacement happens. "
  "Reasoning path: a chemistry model explains Portland's persistence and predicts green cement. "
  "Proposed mechanism: 'chemistry-changed' green cement - scaled alternative binders. "
  "What would confirm it: green cement displacing Portland at scale. "
  "What would kill it: evidence that Portland is irreplaceable. "
  "What this does not claim: it does not claim green cement exists at scale, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads cement as carbon-locked chemistry, and asks what binders would displace.",
 "how_it_works": "Researchers study green cement through geopolymer development, LC3 deployment, and capture integration.",
 "key_points": [
  "Cement is ~8% of global CO2.",
  "Portland chemistry releases CO2 inherently.",
  "Alternatives help partially.",
  "4 billion tons dwarfs solutions.",
  "Portland still dominates.",
 ],
 "requirements": [
  "Performing alternative binders.",
  "Scaled green cement.",
  "Portland displacement.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Scrivener KL et al. Cement reviews. Various; 2018-2023.",
  "Provis JL et al. Geopolymers. Various; 2014-2019.",
  "LC3 project. Various; 2015 onward.",
  "Andrew RM et al. Cement emissions. Various; 2018-2021.",
 ],
 "demo_data": {"a": ("cement CO2, percent of global (approx)", 8.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.12),
               "step1": "eight percent of all CO2 from one material - the carbon foundation",
               "confirm": "green cement displaces Portland at scale",
               "refute": "Portland proves irreplaceable"},
},
# ------------------------------------------------------------------ rank 24
{
 "key": "additive-materials",
 "name": "Materials for Additive Manufacturing",
 "group": "Processing",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "3D printing needs printable materials - can the materials palette match the process's promise?",
 "description": "Additive-manufacturing materials - the palette problem: printing processes outran materials; high-performance alloys, ceramics, and multi-materials are hard to print; and the materials limit what printing can make.",
 "background": "3D printing (1980s-2010s) grew rapidly; materials lagged processes; but printable superalloys (2020s) are emerging. As of 2026 the palette is still narrow.",
 "why_it_matters": "Printable high-performance materials would unlock additive manufacturing: the palette for the printer.",
 "sig_pointer": "The Signature system's proposed approach expands printable materials, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that printable materials need alloy design: the compositions designed for printing - with properties proven. "
  "Assumptions: (1) printability is designable; (2) properties follow; (3) palette expands. "
  "Reasoning path: a design model explains the palette gap and predicts printable materials. "
  "Proposed mechanism: 'printability-designed' materials - expanded palettes. "
  "What would confirm it: high-performance printed parts in service. "
  "What would kill it: evidence that printing inherently limits materials. "
  "What this does not claim: it does not claim expanded palettes exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads printing as material-starved, and asks what design would expand.",
 "how_it_works": "Researchers study additive materials through printability research, alloy design, and multi-material printing.",
 "key_points": [
  "Printing processes outran materials.",
  "High-performance alloys are hard to print.",
  "The palette is still narrow.",
  "Printable superalloys are emerging.",
  "Materials limit printing's promise.",
 ],
 "requirements": [
  "Printability-designed alloys.",
  "High-performance printed parts.",
  "Expanded material palettes.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "DebRoy T et al. Additive reviews. Various; 2018-2021.",
  "Martin JH et al. Printable alloys. Various; 2017-2020.",
  "Sames WJ et al. Materials challenges. Various; 2016-2019.",
  "Frazier WE et al. Metal printing. Various; 2014-2018.",
 ],
 "demo_data": {"a": ("printable high-performance alloys (approx)", 20.0),
               "b": ("high-performance alloys (approx)", 200.0), "bounds": (0.05, 0.18),
               "step1": "one in ten printable - the starved printer",
               "confirm": "high-performance printed parts in service",
               "refute": "printing proves to inherently limit materials"},
},
# ------------------------------------------------------------------ rank 25
{
 "key": "nuclear-materials",
 "name": "Nuclear Materials: Surviving the Reactor",
 "group": "Structural",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Fusion and advanced fission need materials that survive extreme radiation - do they exist?",
 "description": "Nuclear materials - surviving the reactor: fusion needs plasma-facing materials (tungsten) and structural steels that resist 14-MeV neutrons; but the testing facilities (IFMIF) are incomplete; and the materials are unproven.",
 "background": "Fission materials (1950s-70s) were developed; fusion materials (1980s onward) are still pending; tungsten and RAFM steels are candidates. As of 2026 fusion materials are unproven.",
 "why_it_matters": "Surviving materials would enable fusion power: the wall that holds the star.",
 "sig_pointer": "The Signature system's proposed approach builds reactor-surviving materials, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nuclear materials need radiation-proof design: the alloys engineered for 14-MeV neutrons - with testing proving. "
  "Assumptions: (1) proof is achievable; (2) testing suffices; (3) materials survive. "
  "Reasoning path: a design model explains the unproven status and predicts surviving materials. "
  "Proposed mechanism: 'radiation-proofed' nuclear materials - tested survivors. "
  "What would confirm it: materials surviving fusion-relevant irradiation. "
  "What would kill it: evidence that no material survives. "
  "What this does not claim: it does not claim surviving materials exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads fusion as material-blocked, and asks what alloys would survive.",
 "how_it_works": "Researchers study nuclear materials through irradiation testing, tungsten research, and RAFM development.",
 "key_points": [
  "Fusion needs 14-MeV-neutron-resistant materials.",
  "Testing facilities are incomplete.",
  "Tungsten and RAFM steels are candidates.",
  "Fusion materials are unproven.",
  "Fission materials were developed successfully.",
 ],
 "requirements": [
  "Radiation-proofed alloys.",
  "Fusion-relevant irradiation survival.",
  "Tested surviving materials.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Zinkle SJ et al. Fusion materials. Various; 2005-2019.",
  "Rieth M et al. Tungsten research. Various; 2013-2019.",
  "Bloom EE et al. RAFM steels. Various; 2004-2007.",
  "IFMIF program. Various; 2000s onward.",
 ],
 "demo_data": {"a": ("materials proven for fusion reactors (approx)", 1.0),
               "b": ("candidate fusion materials (approx)", 20.0), "bounds": (0.02, 0.1),
               "step1": "one proven of twenty candidates - the unbuilt wall",
               "confirm": "materials survive fusion-relevant irradiation",
               "refute": "no material proves to survive"},
},
# ------------------------------------------------------------------ rank 26
{
 "key": "biomimetic-materials",
 "name": "Biomimetic Materials: Learning from Nature",
 "group": "Functional",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Nature makes extraordinary materials - can we replicate nacre, spider silk, and bone synthetically?",
 "description": "Biomimetic materials - learning from nature: nacre's toughness, spider silk's strength, and bone's adaptivity inspire; but synthetic replicas underperform; and the hierarchical structures are hard to manufacture.",
 "background": "Biomimetics (1990s-2000s) studied natural materials; replicas were attempted; but hierarchy defeated manufacturing. As of 2026 nature still wins.",
 "why_it_matters": "Replicated natural materials would transform structures: the toughness of the shell made synthetic.",
 "sig_pointer": "The Signature system's proposed approach replicates natural hierarchies, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that biomimetics needs hierarchy manufacturing: the multi-scale structures built synthetically - with properties matching. "
  "Assumptions: (1) hierarchies are buildable; (2) properties follow; (3) manufacturing scales. "
  "Reasoning path: a hierarchy model explains replica failure and predicts natural-matching materials. "
  "Proposed mechanism: 'hierarchy-manufactured' biomimetics - built natural structures. "
  "What would confirm it: synthetic materials matching natural properties. "
  "What would kill it: evidence that hierarchy can't be manufactured. "
  "What this does not claim: it does not claim natural-matching synthetics exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads biomimetics as unmanufacturable hierarchy, and asks what building would replicate.",
 "how_it_works": "Researchers study biomimetics through hierarchy characterization, replica attempts, and manufacturing research.",
 "key_points": [
  "Nacre, silk, and bone inspire.",
  "Synthetic replicas underperform.",
  "Hierarchical structures defeat manufacturing.",
  "Nature still wins.",
  "The field studies more than replicates.",
 ],
 "requirements": [
  "Manufactured multi-scale hierarchies.",
  "Natural-matching properties.",
  "Scaled biomimetic production.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Meyers MA et al. Biological materials. Various; 2008-2013.",
  "Fratzl P et al. Hierarchy reviews. Various; 2007-2016.",
  "Wegst UGK et al. Nacre replicas. Various; 2015-2020.",
  "Heim M et al. Spider silk. Various; 2009-2019.",
 ],
 "demo_data": {"a": ("synthetic replicas matching natural toughness, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "seven-tenths short of nature - the unreplicated hierarchy",
               "confirm": "synthetic materials match natural properties",
               "refute": "hierarchy proves unable to be manufactured"},
},
# ------------------------------------------------------------------ rank 27
{
 "key": "materials-informatics",
 "name": "Materials Informatics: The Data-Driven Discovery",
 "group": "Theory",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Can machine learning discover materials - or does it just interpolate the known?",
 "description": "Materials informatics - data-driven discovery: machine learning predicts materials properties from data, but training sets are sparse and biased, extrapolation beyond them fails, and whether ML truly discovers new materials or merely interpolates the known is hotly debated. The field assists discovery far more than it leads it.",
 "background": "Materials informatics (2010s) grew with data; ML successes were reported; but the interpolation critique persists. As of 2026 ML assists more than discovers.",
 "why_it_matters": "Truly discovering ML would accelerate materials: the intelligence that finds the new.",
 "sig_pointer": "The Signature system's proposed approach makes ML discover new materials, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that materials ML needs extrapolation: the models that predict beyond training - with discoveries validated. "
  "Assumptions: (1) extrapolation is achievable; (2) data suffices; (3) discoveries validate. "
  "Reasoning path: an extrapolation model explains the interpolation critique and predicts discovering ML. "
  "Proposed mechanism: 'extrapolating' materials ML - beyond-training discovery. "
  "What would confirm it: ML-discovered materials in applications. "
  "What would kill it: evidence that ML only interpolates. "
  "What this does not claim: it does not claim discovering ML exists, offers no engineering advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads materials ML as interpolating assistant, and asks what extrapolation would discover.",
 "how_it_works": "Researchers study materials informatics through extrapolation research, dataset growth, and discovery validation.",
 "key_points": [
  "ML predicts properties from data.",
  "Training data is sparse and biased.",
  "Extrapolation fails.",
  "The interpolation critique persists.",
  "ML assists more than discovers.",
 ],
 "requirements": [
  "Extrapolating ML models.",
  "ML-discovered materials validated.",
  "Discoveries in applications.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Butler KT et al. Materials ML. Various; 2018-2022.",
  "Schmidt J et al. ML reviews. Various; 2019-2023.",
  "Himanen L et al. Descriptors. Various; 2019-2021.",
  "Ward L et al. Discovery validation. Various; 2016-2020.",
 ],
 "demo_data": {"a": ("ML-discovered materials in applications (approx)", 5.0),
               "b": ("ML-predicted materials (approx)", 500.0), "bounds": (0.005, 0.018),
               "step1": "five applied of five hundred predicted - the uninterpolated discovery",
               "confirm": "ML-discovered materials in applications",
               "refute": "ML proves only to interpolate"},
},
# ------------------------------------------------------------------ rank 28
{
 "key": "quantum-materials",
 "name": "Quantum Materials: The Correlated Frontier",
 "group": "Electronic",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Quantum materials host exotic states - but can strongly correlated electrons be understood and exploited?",
 "description": "Quantum materials - the correlated frontier: high-temperature superconductors, spin liquids, and strange metals host states that defy theoretical understanding, even as new ones are discovered regularly. Many-body theory lags the experiments, exploitation is aspirational, and the frontier remains one of physics' deepest mysteries.",
 "background": "Correlated electrons (1980s onward) puzzled; new states were found; but theory lags. As of 2026 the frontier is still mysterious.",
 "why_it_matters": "Understood quantum materials would transform electronics: the correlated state made useful.",
 "sig_pointer": "The Signature system's proposed approach understands quantum materials, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that quantum materials need correlated theory: the many-body states understood - with materials designed. "
  "Assumptions: (1) theory is achievable; (2) it predicts; (3) materials follow. "
  "Reasoning path: a theory model explains the mystery and predicts understood materials. "
  "Proposed mechanism: 'theory-understood' quantum materials - designed correlated states. "
  "What would confirm it: predicted quantum materials with exotic states. "
  "What would kill it: evidence that correlations resist understanding. "
  "What this does not claim: it does not claim understood quantum materials exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads quantum materials as theoretically mysterious, and asks what theory would understand.",
 "how_it_works": "Researchers study quantum materials through many-body theory, exotic-state discovery, and materials design.",
 "key_points": [
  "Correlated electrons defy theory.",
  "Exotic states are discovered regularly.",
  "Understanding is incomplete.",
  "Exploitation is aspirational.",
  "The frontier is still mysterious.",
 ],
 "requirements": [
  "Correlated-electron theory.",
  "Predicted exotic materials.",
  "Designed quantum materials.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Keimer B et al. Correlated reviews. Various; 2015-2022.",
  "Savary L et al. Spin liquids. Various; 2016-2021.",
  "Basov DN et al. Quantum materials. Various; 2017-2021.",
  "Tokura Y et al. Correlated oxides. Various; 2017-2022.",
 ],
 "demo_data": {"a": ("quantum materials understood theoretically, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "four in five mysterious - the uncorrelated understanding",
               "confirm": "predicted quantum materials with exotic states",
               "refute": "correlations prove to resist understanding"},
},
# ------------------------------------------------------------------ rank 29
{
 "key": "interface-science",
 "name": "Interface Science: The Boundary Problem",
 "group": "Theory",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Interfaces control devices - but can buried interfaces be characterized and designed?",
 "description": "Interface science - the boundary problem: heterointerfaces govern batteries, electronics, and catalysts, yet buried interfaces are notoriously hard to characterize and interface design remains largely empirical. New operando tools are emerging, but interfaces are still the weak link in nearly every device.",
 "background": "Interface research (20th century) was surface-focused; buried-interface tools (2010s-2020s) are emerging; but design lags. As of 2026 interfaces are still the weak link.",
 "why_it_matters": "Designed interfaces would transform devices: the boundary engineered.",
 "sig_pointer": "The Signature system's proposed approach designs buried interfaces, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that interfaces need buried characterization: the tools seeing buried boundaries - with design following. "
  "Assumptions: (1) characterization is possible; (2) it enables design; (3) devices improve. "
  "Reasoning path: a characterization model explains empirical status and predicts designed interfaces. "
  "Proposed mechanism: 'characterization-enabled' interface design - seen then designed. "
  "What would confirm it: designed interfaces in high-performance devices. "
  "What would kill it: evidence that interfaces resist design. "
  "What this does not claim: it does not claim designed interfaces exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads interfaces as unseen boundaries, and asks what tools would reveal.",
 "how_it_works": "Researchers study interfaces through operando characterization, buried-interface tools, and design research.",
 "key_points": [
  "Heterointerfaces govern devices.",
  "Buried interfaces are hard to characterize.",
  "Design is empirical.",
  "New tools are emerging.",
  "Interfaces are the weak link.",
 ],
 "requirements": [
  "Buried-interface characterization.",
  "Designed interfaces.",
  "High-performance interface devices.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Hwang HY et al. Oxide interfaces. Various; 2012-2019.",
  "Operando characterization literature. Various; 2015-2023.",
  "Strelcov E et al. Interface tools. Various; 2017-2022.",
  "Kortright JB et al. Buried interfaces. Various; 2018-2023.",
 ],
 "demo_data": {"a": ("interfaces designed from characterization, percent (approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.08, 0.25),
               "step1": "eighty-five percent empirical - the unseen boundary",
               "confirm": "designed interfaces in high-performance devices",
               "refute": "interfaces prove to resist design"},
},
# ------------------------------------------------------------------ rank 30
{
 "key": "extreme-materials",
 "name": "Materials for Extremes",
 "group": "Structural",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Hypersonics, deep space, and fusion need materials beyond current limits - can extremes be engineered for?",
 "description": "Extreme-environment materials - for hypersonic leading edges above 2000C, fusion reactors, and deep space: the requirements exceed what current materials survive. Ultra-high-temperature ceramics advanced in the 2000s-2010s, but hypersonic flight needs more, and the gap between environment and material remains the field's hardest frontier.",
 "background": "UHTCs (2000s-2010s, Fahrenholtz) advanced; but hypersonic flight needs more; the extreme gap is the materials frontier. As of 2026 extremes still defeat materials.",
 "why_it_matters": "Extreme materials would enable hypersonics, fusion, and deep space: the material for the impossible environment.",
 "sig_pointer": "The Signature system's proposed approach engineers for extremes, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that extremes need designed materials: the UHTCs and beyond - with environments survived. "
  "Assumptions: (1) design is possible; (2) materials survive; (3) applications follow. "
  "Reasoning path: a design model explains the gap and predicts extreme materials. "
  "Proposed mechanism: 'extreme-designed' materials - environment-surviving. "
  "What would confirm it: materials surviving extreme service. "
  "What would kill it: evidence that extremes defeat materials. "
  "What this does not claim: it does not claim extreme materials exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads extremes as material-defeating, and asks what design would survive.",
 "how_it_works": "Researchers study extreme materials through UHTC development, hypersonic testing, and environment simulation.",
 "key_points": [
  "Hypersonics need 2000C+ materials.",
  "UHTCs advanced but the gap persists.",
  "Fusion and deep space add extremes.",
  "Requirements exceed current materials.",
  "Extremes still defeat materials.",
 ],
 "requirements": [
  "Designed extreme materials.",
  "Survived extreme service.",
  "Enabled extreme applications.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Fahrenholtz WG et al. UHTCs. Various; 2007-2020.",
  "Wuchina E et al. Hypersonic materials. Various; 2007-2018.",
  "Paul A et al. Extreme reviews. Various; 2017-2022.",
  "Glass DE et al. Leading-edge materials. Various; 2008-2016.",
 ],
 "demo_data": {"a": ("hypersonic leading-edge temperature, C (approx)", 2200.0),
               "b": ("best material limit, C (approx)", 2000.0), "bounds": (1.0, 1.25),
               "step1": "hotter than the best material survives - the extreme gap",
               "confirm": "materials survive extreme service",
               "refute": "extremes prove to defeat materials"},
},
# ------------------------------------------------------------------ rank 31
{
 "key": "circular-materials",
 "name": "Circular Materials: The Recycling Problem",
 "group": "Processing",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Materials are used once - can they be designed for infinite recycling?",
 "description": "Circular materials - the recycling problem: most materials degrade when recycled, composites are effectively unrecyclable, and design-for-recycling is still rare. The circular economy needs materials designed for infinite loops, but the vast majority of what civilization makes is linear - used once, then waste.",
 "background": "Recycling (20th century) was downcycling; composites (2000s-2010s) proved unrecyclable; but circular design is emerging. As of 2026 most materials are linear.",
 "why_it_matters": "Circular materials would end waste: the material used forever.",
 "sig_pointer": "The Signature system's proposed approach designs circular materials, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that circularity needs designed materials: the recyclable-by-design compositions - with infinite loops. "
  "Assumptions: (1) design enables circularity; (2) loops are infinite; (3) economics work. "
  "Reasoning path: a design model explains linear status and predicts circular materials. "
  "Proposed mechanism: 'designed-circular' materials - infinitely recyclable. "
  "What would confirm it: circular materials in closed-loop use. "
  "What would kill it: evidence that materials inherently degrade. "
  "What this does not claim: it does not claim circular materials exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads materials as linear waste, and asks what design would circularize.",
 "how_it_works": "Researchers study circular materials through design-for-recycling, composite recycling, and loop analyses.",
 "key_points": [
  "Most materials degrade on recycling.",
  "Composites are unrecyclable.",
  "Design-for-recycling is rare.",
  "Most materials are linear.",
  "The circular economy needs circularity.",
 ],
 "requirements": [
  "Recyclable-by-design materials.",
  "Closed-loop material use.",
  "Infinite recycling proven.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Allwood JM et al. Circular economy. Various; 2011-2017.",
  "Ellen MacArthur Foundation. Various; 2012 onward.",
  "Oliveux G et al. Composite recycling. Various; 2015-2020.",
  "Zhu J et al. Circular design. Various; 2021-2024.",
 ],
 "demo_data": {"a": ("materials recycled without degradation, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.18),
               "step1": "nine in ten degrade - the linear material",
               "confirm": "circular materials in closed-loop use",
               "refute": "materials prove to inherently degrade"},
},
# ------------------------------------------------------------------ rank 32
{
 "key": "materials-theory",
 "name": "A Theory of Materials",
 "group": "Theory",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Materials science is fragmented - can there be a unified theory of materials?",
 "description": "Materials theory - the unified question: the field spans physics, chemistry, and engineering, yet no unified theory connects structure to properties in general. DFT unified the electrons, multiscale modeling connects some scales, but the general predictive theory of materials - the equation that yields properties from structure - remains absent.",
 "background": "Materials theory (20th century) was piecemeal; DFT (1960s-90s) unified electrons; but the general structure-property theory is missing. As of 2026 the field is still fragmented.",
 "why_it_matters": "Unified materials theory would predict everything: the equation of the material.",
 "sig_pointer": "The Signature system's proposed approach unifies materials theory, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that materials theory unifies through multiscale modeling: the scales connected - with properties predicted. "
  "Assumptions: (1) scales are connectable; (2) prediction works; (3) theory unifies. "
  "Reasoning path: a multiscale model explains fragmentation and predicts unified theory. "
  "Proposed mechanism: 'multiscale-unified' materials theory - connected prediction. "
  "What would confirm it: unified predictions across material classes. "
  "What would kill it: evidence that materials resist unification. "
  "What this does not claim: it does not claim a unified theory exists, offers no engineering advice, and does not constitute a theoretical claim."),
 "sig_lens": "The Signature lens reads materials as theoretically fragmented, and asks what multiscale would unify.",
 "how_it_works": "Researchers study materials theory through multiscale modeling, DFT advances, and theory development.",
 "key_points": [
  "The field spans physics, chemistry, engineering.",
  "No unified structure-property theory exists.",
  "DFT unified electrons only.",
  "The general theory is absent.",
  "Fragmentation persists.",
 ],
 "requirements": [
  "Connected multiscale models.",
  "Unified cross-class predictions.",
  "Accepted unified theory.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kohn W et al. DFT foundations. Various; 1964-1998.",
  "Olson GB et al. Materials design. Various; 1997-2015.",
  "van der Giessen E et al. Multiscale reviews. Various; 2020-2024.",
  "Phillips R et al. Theory perspectives. Various; 2001-2015.",
 ],
 "demo_data": {"a": ("material classes with unified theory (approx)", 2.0),
               "b": ("material classes (approx)", 20.0), "bounds": (0.05, 0.18),
               "step1": "two unified of twenty classes - the fragmented theory",
               "confirm": "unified predictions across material classes",
               "refute": "materials prove to resist unification"},
},
# ------------------------------------------------------------------ rank 33
{
 "key": "materials-future",
 "name": "The Future of Materials: A Century Ahead",
 "group": "Theory",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "What materials will define the next century? The field extrapolates poorly - can its future be foreseen?",
 "description": "Materials futurology - predicting the field's century - is speculative: past predictions (room-temperature superconductors by 2000) failed; but structured foresight is absent; whether futures work improves decisions is the meta-question.",
 "background": "Materials predictions have a poor record; scenario methods are unused. As of 2026 the future is debated without discipline.",
 "why_it_matters": "Long-horizon decisions (research, infrastructure) need foresight: the discipline of materials futures.",
 "sig_pointer": "The Signature system's proposed approach builds disciplined materials foresight, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that materials futures need disciplined foresight: the scenario methods and roadmaps - with track records. "
  "Assumptions: (1) foresight is improvable; (2) methods exist; (3) they guide decisions. "
  "Reasoning path: a foresight model explains prediction failures and predicts better futures work. "
  "Proposed mechanism: 'disciplined' materials foresight - tracked scenario methods. "
  "What would confirm it: foresight with validated track records. "
  "What would kill it: evidence that materials futures are unforeseeable. "
  "What this does not claim: it does not claim any future, offers no engineering advice, and does not constitute a prediction."),
 "sig_lens": "The Signature lens reads materials futures as undisciplined speculation, and asks what methods would foresee.",
 "how_it_works": "Researchers study materials futures through scenario methods, technology roadmapping, and prediction tracking.",
 "key_points": [
  "Materials predictions have a poor record.",
  "Superconductors were promised by 2000.",
  "Scenario methods are unused.",
  "Long-horizon decisions need foresight.",
  "The discipline is undeveloped.",
 ],
 "requirements": [
  "Validated foresight methods.",
  "Track records for predictions.",
  "Decisions guided by foresight.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ashby MF et al. Materials futures. Various; 2013-2020.",
  "Foresight methodology literature. Various.",
  "NRC. Materials research agendas. Various; 2000-2020.",
  "Olson GB et al. Design futures. Various; 2015-2022.",
 ],
 "demo_data": {"a": ("materials predictions with validated track records (approx)", 5.0),
               "b": ("materials predictions made (approx)", 200.0), "bounds": (0.015, 0.04),
               "step1": "five tracked of two hundred made - the foresight without a record",
               "confirm": "foresight with validated track records",
               "refute": "materials futures prove unforeseeable"},
},
# ------------------------------------------------------------------ rank 34
{
 "key": "programmable-matter",
 "name": "Programmable Matter",
 "group": "Theory",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Can matter itself be programmed - materials that change properties on command?",
 "description": "Programmable matter - the ultimate materials dream: claytronics, programmable metamaterials, and 4D printing hint; but true programmable matter (arbitrary property change on command) is science fiction with early prototypes.",
 "background": "Programmable matter (1990s-2000s, Toffoli, Margolus) was conceptual; claytronics (Goldstein, 2000s) prototyped; 4D printing (Tibbits, 2013) showed shape change. As of 2026 programming is shape-deep.",
 "why_it_matters": "Programmable matter would end manufacturing: the material that becomes anything.",
 "sig_pointer": "The Signature system's proposed approach programs matter, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that matter is programmable: the unit-cell architectures with commanded properties - scaled from prototypes. "
  "Assumptions: (1) architectures scale; (2) properties are commandable; (3) matter programs. "
  "Reasoning path: a scaling model explains prototype status and predicts programmed matter. "
  "Proposed mechanism: 'architecturally-programmed' matter - commanded properties. "
  "What would confirm it: programmable matter in applications. "
  "What would kill it: evidence that matter resists programming. "
  "What this does not claim: it does not claim programmable matter exists, offers no engineering advice, and does not constitute a materials claim."),
 "sig_lens": "The Signature lens reads matter as unprogrammed, and asks what architecture would command.",
 "how_it_works": "Researchers study programmable matter through claytronics, 4D printing, and architecture research.",
 "key_points": [
  "True programmable matter is science fiction.",
  "Claytronics prototyped the concept.",
  "4D printing showed shape change.",
  "Programming is shape-deep.",
  "The dream is arbitrary property change.",
 ],
 "requirements": [
  "Scaled unit-cell architectures.",
  "Commanded property changes.",
  "Programmable matter in applications.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Toffoli T et al. Programmable matter. Various; 1990s-2000s.",
  "Goldstein SC et al. Claytronics. Various; 2005-2012.",
  "Tibbits S et al. 4D printing. Various; 2013-2019.",
  "Hawkes EW et al. Programmable materials. Various; 2022-2024.",
 ],
 "demo_data": {"a": ("properties programmable on command (approx)", 2.0),
               "b": ("material properties (approx)", 50.0), "bounds": (0.02, 0.08),
               "step1": "two programmable of fifty properties - the unprogrammed matter",
               "confirm": "programmable matter in applications",
               "refute": "matter proves to resist programming"},
},
]
