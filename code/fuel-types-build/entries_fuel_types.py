#!/usr/bin/env python3
"""Entries for The Fuel Types Database (public + Signature), track 1 of 3:
ESTABLISHED fuel types. Manon's order 2026-10-17 17:55 EDT.

34 ladder-ordered records, simple fuels to complex systems: what a fuel is,
wood, charcoal, the coal family (basics, grades, coke, peat), petroleum
distillates (kerosene, heating oil, fuel oil grades), gaseous fuels (natural
gas, propane), liquid transport fuels (gasoline/octane, diesel/cetane),
biofuels (ethanol blends, E85, biodiesel, biodiesel blends), methanol,
aviation fuels (avgas, jet fuel), LNG, CNG, hydrogen (established
production via steam methane reforming; storage, handling, fuel cells),
nuclear fuels (natural uranium, enriched uranium pellets/assemblies, the
fuel cycle), refining systems (naphtha streams, the refinery, blending and
additives), and fuel systems (bunker fuel, storage/transport/safety, the
energy-density comparison framework).

Public records carry real, fact-checked fuel knowledge - properties,
production, uses, handling and safety, energy density - organized in the
Signature system. Signature editions carry the same ladder through his
original Signature fuel-system designs, optimization frameworks, and
comparative analyses, clearly labeled Signature-made, never presented as
authentic public record.

Dedupe: 2026-10-17 - all 68 titles checked against the whole system via
code/dedupe_gate.py (manifest 2,602 databases + global exact shards):
zero collisions, zero refusals.

No website references. No Facebook. Screened per the canon.
"""

SIG_TAIL = ("Signature edition: his original Signature fuel-system design, "
            "optimization framework, and comparative analysis for this fuel - "
            "a Signature-generated engineering interpretation, clearly labeled "
            "Signature-made, never presented as authentic public record.")

ENTRIES = [
{
 "key": "fuel-what-is",
 "name": "What a fuel is: stored chemical energy",
 "group": "fuel-basics",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "description": ("A fuel is any material that stores chemical energy and "
  "releases it in a controlled way, usually as heat, when it reacts with an "
  "oxidizer - most often the oxygen in air. Wood, coal, gasoline, natural "
  "gas, and uranium all qualify, though nuclear fuel releases energy by "
  "splitting atoms rather than by burning. What makes a substance useful as "
  "a fuel is a practical combination of four things: high energy density "
  "(energy per kilogram or per liter), availability at scale, safe and "
  "controllable release, and an acceptable cost per unit of energy. This "
  "record defines the vocabulary every later record uses: combustion, "
  "oxidation, energy density in megajoules per kilogram (MJ/kg) and per "
  "liter (MJ/L), flash point, and the difference between a fuel, an "
  "oxidizer, and an energy carrier."),
 "how_it_works": ("Chemical fuels store energy in molecular bonds. Burning "
  "rearranges those bonds - hydrocarbon plus oxygen becomes carbon dioxide "
  "plus water - and the new bonds hold less energy than the old ones, so "
  "the difference escapes as heat. A simple comparison makes the ladder "
  "concrete: one kilogram of gasoline holds about 46 MJ, one kilogram of "
  "dry wood about 19 MJ, and one kilogram of coal about 24 to 30 MJ. "
  "Nuclear fuel is in another league entirely: one kilogram of uranium-235 "
  "fissioned releases about 82 terajoules, roughly two million times the "
  "energy of a kilogram of gasoline. The record walks through the "
  "combustion equation for methane (CH4 + 2O2 -> CO2 + 2H2O), shows why "
  "incomplete combustion makes carbon monoxide, and explains why energy "
  "density is quoted both per mass and per volume - hydrogen wins per "
  "kilogram and loses badly per liter."),
 "key_points": [
  "A fuel stores energy and releases it in a controlled reaction with an oxidizer, usually oxygen.",
  "Energy density is quoted in MJ/kg and MJ/L; mass and volume rankings often disagree.",
  "Gasoline holds about 46 MJ/kg; dry wood about 19 MJ/kg; fissioned uranium-235 about 82 TJ/kg.",
  "Complete combustion of hydrocarbons yields carbon dioxide and water; incomplete combustion yields carbon monoxide.",
  "Nuclear fuel is an established fuel that releases energy by fission, not by burning."],
 "requirements": [
  "Learner must state the four practical qualities of a useful fuel in their own words.",
  "Learner must write the balanced combustion equation for methane.",
  "Learner must explain why hydrogen ranks first by mass but near last by volume.",
  "Learner must distinguish a fuel from an oxidizer and from an energy carrier."],
 "standards": [
  "Energy quantities in SI units: joules, megajoules, terajoules.",
  "Combustion chemistry: balanced stoichiometric equations.",
  "Safety vocabulary: flash point, flammability limits, complete vs incomplete combustion."],
 "citations": [
  "Smil V. Energy and Civilization: A History. MIT Press; 2017 (fuels as stored energy through history).",
  "Heywood JB. Internal Combustion Engine Fundamentals. McGraw-Hill; 1988 (combustion chemistry and energy release).",
  "U.S. DOE Energy Information Administration. Energy units and calculators: heat content of fuels (reference energy-density values)."],
 "sig_lens": ("Signature reframing: the Signature fuel taxonomy ranks every "
  "established fuel on a four-axis Signature chart - mass density, volume "
  "density, controllability, and civilization-scale availability - so a "
  "newcomer can place any fuel at a glance. The Signature Energy Ledger "
  "method teaches learners to convert any fuel quantity into megajoules "
  "first and only then into dollars, gallons, or BTUs, which is the "
  "Signature discipline behind every optimization framework later in this "
  "database."),
},
{
 "key": "wood-fuel",
 "name": "Wood fuel: the original fuel",
 "group": "solid-fuels",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "description": ("Wood is the oldest fuel humans have used, and it remains "
  "an established fuel worldwide: roughly two billion people still cook "
  "and heat with it. Dry wood is about half carbon, six percent hydrogen, "
  "and most of the rest oxygen bound in cellulose, hemicellulose, and "
  "lignin. Air-dried firewood (about 20 percent moisture) delivers roughly "
  "15 to 16 megajoules per kilogram; oven-dry wood delivers about 18 to 19 "
  "MJ/kg. Moisture is the enemy of efficiency: every kilogram of water in "
  "the wood must be boiled off, stealing about 2.4 MJ before any useful "
  "heat reaches the room. Hardwoods (oak, maple, ash) burn slower and "
  "denser than softwoods (pine, fir), but per dry kilogram their energy "
  "content is nearly identical - density changes the burn rate, not the "
  "energy per kilogram."),
 "how_it_works": ("Burning wood happens in four overlapping stages. First "
  "drying: heat drives off water below 100 C. Then pyrolysis: between about "
  "200 and 400 C the wood breaks down into flammable gases (the visible "
  "flames are burning gas, not burning solid). Then gas-phase combustion: "
  "those gases mix with air and burn. Finally char burnout: the remaining "
  "charcoal glows and burns with little flame. A modern wood stove "
  "separates these stages with secondary air tubes that re-burn the smoke, "
  "which is why an EPA-certified stove extracts far more heat and far less "
  "pollution from the same log than an open fireplace. The record includes "
  "the moisture penalty calculation: net heating value falls almost "
  "linearly as moisture rises, which is why properly seasoned wood is the "
  "single biggest efficiency measure in wood heating."),
 "key_points": [
  "Wood is the oldest established fuel; about two billion people still rely on it.",
  "Oven-dry wood holds about 18-19 MJ/kg; air-dried firewood about 15-16 MJ/kg.",
  "Moisture steals roughly 2.4 MJ per kilogram of water before useful heat appears.",
  "Visible flames are burning pyrolysis gases, not burning solid wood.",
  "Hardwood and softwood hold nearly equal energy per dry kilogram; density changes burn rate, not energy."],
 "requirements": [
  "Learner must compute the moisture penalty for a stated moisture content.",
  "Learner must name the four stages of wood combustion in order.",
  "Learner must explain why a modern stove beats an open fireplace on the same log.",
  "Learner must state the approximate MJ/kg of dry wood from memory."],
 "standards": [
  "Moisture content quoted on a wet basis unless stated otherwise.",
  "Heating values: higher heating value (HHV) vs lower heating value (LHV) distinguished.",
  "Wood stove efficiency and emissions: EPA certification method 28."],
 "citations": [
  "Reed TB, Das A. Handbook of Biomass Downdraft Gasifier Engine Systems. Solar Energy Research Institute; 1988 (wood composition and combustion stages).",
  "FAO Forestry Paper. Unified Bioenergy Terminology (wood fuel definitions and moisture conventions).",
  "Smil V. Energy and Civilization: A History. MIT Press; 2017 (wood as the foundational fuel)."],
 "sig_lens": ("Signature reframing: the Signature Wood Ledger treats a "
  "woodpile as an energy bank account - every cord logged with species, "
  "moisture reading, and megajoules on deposit. The Signature seasoning "
  "rule (split, stack, sun, one full summer) is presented as a "
  "deterministic protocol: follow it and the moisture meter reads under 20 "
  "percent, no judgment calls. The Signature stove-tuning framework maps "
  "the four combustion stages to four damper settings."),
},
{
 "key": "charcoal",
 "name": "Charcoal: wood concentrated by fire",
 "group": "solid-fuels",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("Charcoal is wood that has been baked in low oxygen until "
  "most of the water and volatile compounds are driven off, leaving mostly "
  "pure carbon. Traditional charcoal making converts about 100 kilograms of "
  "dry wood into 20 to 25 kilograms of charcoal - a mass yield of roughly "
  "one quarter - but because the energy concentrates, charcoal delivers "
  "about 29 to 30 megajoules per kilogram, nearly double wood per "
  "kilogram, and burns with almost no smoke or flame. That combination "
  "made charcoal the established fuel of blacksmiths, smelters, and "
  "cooking across every civilization: it burns hot (over 1,000 C in a "
  "forge), clean, and controllably. Modern uses include metallurgy, "
  "activated-carbon filtration, and cooking - from backyard grills to the "
  "charcoal stoves still common across much of the world."),
 "how_it_works": ("Charcoal is made by pyrolysis: wood is heated to 400-500 "
  "C with restricted air so it cannot burst into flame. Water boils off "
  "first, then volatile gases (methanol, acetic acid, tar vapors - the "
  "basis of the old wood-chemicals industry) escape and are burned or "
  "collected, leaving a carbon skeleton that keeps the shape of the wood. "
  "The record works the energy balance: 100 kg of dry wood at 19 MJ/kg "
  "holds 1,900 MJ; 22 kg of charcoal at 29.5 MJ/kg holds about 650 MJ - "
  "roughly one third of the energy is kept in the charcoal and two thirds "
  "leaves as heat and volatiles during making. Burning charcoal reverses "
  "only the last step: carbon plus oxygen becomes carbon dioxide, with "
  "almost no smoke because the smoke-making volatiles were already "
  "removed. The danger is carbon monoxide: charcoal burning in a closed "
  "room is a classic CO poisoning source."),
 "key_points": [
  "Charcoal is wood pyrolyzed in low oxygen: mostly pure carbon, about 29-30 MJ/kg.",
  "Traditional yield is about 20-25 kg of charcoal per 100 kg of dry wood.",
  "Charcoal burns hot, clean, and nearly smokeless because the volatiles were already driven off.",
  "It was the established fuel of forges and smelters for millennia before coke and coal.",
  "Charcoal in enclosed spaces produces deadly carbon monoxide."],
 "requirements": [
  "Learner must compute the energy balance of a charcoal burn (100 kg wood in, charcoal energy out).",
  "Learner must explain why charcoal burns with almost no flame.",
  "Learner must state the CO danger rule for indoor charcoal use.",
  "Learner must give the approximate MJ/kg of charcoal from memory."],
 "standards": [
  "Charcoal quality: fixed-carbon content and volatile-matter limits.",
  "Cooking charcoal vs metallurgical charcoal distinguished by density and ash.",
  "CO safety: ventilation requirements for indoor solid-fuel use."],
 "citations": [
  "Reed TB, Das A. Handbook of Biomass Downdraft Gasifier Engine Systems. Solar Energy Research Institute; 1988 (pyrolysis and charcoal yields).",
  "Smil V. Energy and Civilization: A History. MIT Press; 2017 (charcoal in metallurgy).",
  "FAO Forestry Paper 41. Simple technologies for charcoal making (traditional kiln yields)."],
 "sig_lens": ("Signature reframing: the Signature Carbon Concentration "
  "protocol presents charcoal making as the first fuel-upgrading technology "
  "in history - energy densification by removing everything that is not "
  "fuel. The Signature forge-fuel specification (dense hardwood charcoal, "
  "low ash, uniform lump size) is framed as a quality standard any "
  "blacksmith can verify by eye and by scale, with the CO rule stated as "
  "an absolute: charcoal never burns indoors without engineered "
  "ventilation."),
},
{
 "key": "coal-basics",
 "name": "Coal: ancient sunlight in rock",
 "group": "coal-family",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "description": ("Coal is fossilized plant matter: swamps buried hundreds "
  "of millions of years ago, compressed and heated until the plant "
  "structure collapsed into carbon-rich rock. It is the established fuel "
  "that powered the Industrial Revolution and still generates roughly a "
  "third of the world's electricity. A kilogram of typical bituminous coal "
  "holds about 24 to 30 megajoules - more than wood, less than oil - and "
  "the world burns on the order of eight billion tonnes of it per year. "
  "Coal's advantages are energy density, abundance, and ease of storage; "
  "its costs are mining impacts, ash and sulfur, and the highest carbon "
  "dioxide output per unit of energy of any major fuel - about 94 to 96 "
  "kilograms of CO2 per gigajoule, versus about 73 for gasoline."),
 "how_it_works": ("Coal formed in stages: peat compacted into lignite, "
  "lignite squeezed into sub-bituminous and bituminous coal, bituminous "
  "metamorphosed into anthracite - each step driving off water and "
  "volatiles and raising the carbon fraction. Burning coal is solid-fuel "
  "combustion: the coal is pulverized to powder in a power station, blown "
  "into the furnace with air, and burns in suspension at over 1,400 C, "
  "boiling water into the steam that drives the turbine. The record "
  "explains the two great coal technologies - the pulverized-coal power "
  "plant and the coke oven plus blast furnace that makes steel - and shows "
  "the CO2 arithmetic: coal is mostly carbon, carbon plus oxygen becomes "
  "CO2 at a mass ratio of 44 to 12, so a tonne of carbon-rich coal yields "
  "roughly 2.4 to 2.9 tonnes of CO2."),
 "key_points": [
  "Coal is fossilized plant matter; typical bituminous coal holds 24-30 MJ/kg.",
  "It powered the Industrial Revolution and still generates about a third of world electricity.",
  "Coal has the highest CO2 per unit energy of any major fuel: about 94-96 kg CO2 per gigajoule.",
  "Power stations burn it pulverized, in suspension, above 1,400 C.",
  "One tonne of carbon-rich coal yields roughly 2.4-2.9 tonnes of CO2."],
 "requirements": [
  "Learner must name the coalification sequence from peat to anthracite.",
  "Learner must compute CO2 from a stated mass of coal using the 44/12 ratio.",
  "Learner must explain why coal is pulverized before burning in a power station.",
  "Learner must state coal's CO2 intensity relative to gasoline."],
 "standards": [
  "Coal rank classification: ASTM D388.",
  "Coal sampling and analysis: ASTM D2013 / D3172 proximate analysis.",
  "Emission factors: IPCC default 94.6 kg CO2/GJ for bituminous coal."],
 "citations": [
  "ASTM D388-19a. Standard Classification of Coals by Rank (the coalification sequence).",
  "Speight JG. The Chemistry and Technology of Coal. 3rd ed. CRC Press; 2013 (coal formation and combustion).",
  "Smil V. Energy and Civilization: A History. MIT Press; 2017 (coal and industrialization)."],
 "sig_lens": ("Signature reframing: the Signature Coal Ledger converts any "
  "coal shipment into three Signature numbers - megajoules on the pile, "
  "tonnes of CO2 committed, and dollars per megajoule delivered - so buyer "
  "and burner see the same truth. The Signature rank ladder (peat to "
  "anthracite) is taught as a single slider: carbon up, water down, "
  "volatiles down, energy up. The Signature rule for coal is stated "
  "plainly: it is the cheapest dense fuel and the dirtiest per joule - "
  "plan both."),
},
{
 "key": "coal-grades",
 "name": "Coal grades: lignite, bituminous, anthracite",
 "group": "coal-family",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "description": ("Not all coal is the same fuel. Rank - the industry's "
  "grading scale - runs from lignite (brown coal, the youngest) through "
  "sub-bituminous and bituminous to anthracite (hard coal, the oldest). "
  "Lignite is brown, crumbly, up to 60 percent water, and delivers only "
  "about 10 to 20 megajoules per kilogram; it is usually burned at the "
  "mine mouth because shipping water is uneconomical. Bituminous is the "
  "workhorse: black, 24 to 30 MJ/kg, the standard steam coal for power "
  "stations and the parent of metallurgical coke. Anthracite is hard, "
  "glassy, over 86 percent fixed carbon, 30 to 33 MJ/kg, and burns with a "
  "short blue flame and almost no smoke - the premium home-heating coal "
  "where it is still used. Rank is set by fixed carbon, volatile matter, "
  "and heating value under ASTM D388."),
 "how_it_works": ("Rank is measured by proximate analysis: a coal sample "
  "is heated in stages to measure moisture, volatile matter, fixed "
  "carbon, and ash. High volatile matter (bituminous, 15-40 percent) "
  "means long yellow flames - good for steam raising. Low volatile matter "
  "and high fixed carbon (anthracite, under 8 percent volatiles) means "
  "hard ignition and a short hot flame. The record gives the classifier "
  "demo: feed in moisture, volatiles, and heating value, and the rank "
  "falls out. It also explains the economic logic: lignite's water makes "
  "it a local fuel, bituminous's balance makes it the traded fuel, and "
  "anthracite's hardness makes it the specialty fuel. Sulfur content cuts "
  "across rank - low-sulfur coal of any rank commands a premium where "
  "sulfur dioxide limits apply."),
 "key_points": [
  "Coal rank runs lignite -> sub-bituminous -> bituminous -> anthracite, set by ASTM D388.",
  "Lignite: 10-20 MJ/kg, high moisture, burned near the mine.",
  "Bituminous: 24-30 MJ/kg, the standard steam coal and coking coal.",
  "Anthracite: 30-33 MJ/kg, over 86 percent fixed carbon, nearly smokeless.",
  "Sulfur content cuts across rank and sets the environmental premium."],
 "requirements": [
  "Learner must place a coal sample in its rank from proximate-analysis numbers.",
  "Learner must explain why lignite is rarely shipped far.",
  "Learner must state the heating-value ranges of the three main ranks.",
  "Learner must explain what volatile matter does to flame character."],
 "standards": [
  "ASTM D388: classification of coals by rank.",
  "ASTM D3172: proximate analysis (moisture, volatiles, fixed carbon, ash).",
  "Sulfur forms and limits: ASTM D4239."],
 "citations": [
  "ASTM D388-19a. Standard Classification of Coals by Rank.",
  "Speight JG. The Chemistry and Technology of Coal. 3rd ed. CRC Press; 2013 (rank properties and analysis).",
  "ASTM D3172-13. Standard Practice for Proximate Analysis of Coal and Coke."],
 "sig_lens": ("Signature reframing: the Signature Rank Slider is a single "
  "visual scale from wet brown lignite to glassy black anthracite with "
  "carbon, water, volatiles, and megajoules marked at every stop - one "
  "glance replaces a table. The Signature buying rule: never pay "
  "bituminous prices for lignite energy; the ledger converts every offer "
  "to dollars per delivered megajoule at the boiler, water included. The "
  "Signature sulfur screen flags any coal above the local SO2 limit before "
  "it is bought."),
},
{
 "key": "coke",
 "name": "Coke: coal baked for the furnace",
 "group": "coal-family",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "description": ("Coke is coal that has been baked at over 1,000 C without "
  "air until the volatiles are driven off, leaving a hard, porous, "
  "almost-pure-carbon fuel. It is the established fuel of ironmaking: a "
  "blast furnace eats roughly 350 to 500 kilograms of coke per tonne of "
  "hot metal. Coke does three jobs at once - it is the fuel that heats "
  "the furnace, the chemical reductant that strips oxygen from iron ore "
  "(C + Fe2O3 chemistry), and the permeable bed that lets hot gases rise "
  "through the charge. About 70 to 75 percent of the coal's mass survives "
  "as coke; the driven-off gases become coke-oven gas, a valuable fuel in "
  "its own right. Coke delivers about 28 to 30 megajoules per kilogram "
  "and must be strong enough to hold up the crushing weight of the "
  "furnace burden without crumbling."),
 "how_it_works": ("Coking happens in slot ovens: selected coking coals "
  "(low ash, low sulfur, the right plasticity) are charged into narrow "
  "chambers and heated from the walls for 15 to 25 hours. The coal softens, "
  "swells, re-solidifies, and shrinks away from the wall as coke. The "
  "record traces the blast-furnace chemistry: coke burns to CO at the "
  "tuyeres, CO reduces iron ore to iron higher up, and limestone flux "
  "carries off impurities as slag. Strength is measured by tumbler tests "
  "(coke must survive handling and the furnace without making fines that "
  "choke gas flow), and reactivity is controlled - too reactive and the "
  "coke burns away before doing its chemical work. Petroleum coke "
  "(petcoke), the refinery cousin, is noted as a separate established "
  "fuel for cement kilns and power."),
 "key_points": [
  "Coke is coal baked above 1,000 C without air: hard, porous, nearly pure carbon.",
  "A blast furnace uses roughly 350-500 kg of coke per tonne of hot metal.",
  "Coke is fuel, chemical reductant, and permeable furnace bed in one material.",
  "Coking yield is about 70-75 percent of coal mass; off-gases become coke-oven gas fuel.",
  "Coke must be mechanically strong: fines choke furnace gas flow."],
 "requirements": [
  "Learner must name the three jobs coke does in a blast furnace.",
  "Learner must compute coke-oven mass yield from a stated coal charge.",
  "Learner must explain why coke strength matters to furnace operation.",
  "Learner must distinguish metallurgical coke from petroleum coke."],
 "standards": [
  "Coke sampling and analysis: ASTM D2013 / D3172 applied to coke.",
  "Coke strength: tumbler and shatter test methods.",
  "Blast-furnace coke quality specifications (industry practice)."],
 "citations": [
  "Speight JG. The Chemistry and Technology of Coal. 3rd ed. CRC Press; 2013 (carbonization and coke).",
  "Ghosh A, Chatterjee A. Ironmaking and Steelmaking: Theory and Practice. PHI Learning; 2008 (coke in the blast furnace).",
  "ASTM D2013/D3172 series (coal and coke sampling and proximate analysis)."],
 "sig_lens": ("Signature reframing: the Signature Triple-Duty model teaches "
  "coke as the only fuel that is simultaneously fuel, chemistry, and "
  "structure - the Signature lens for spotting materials that do three "
  "jobs at once. The Signature coke specification (strength first, "
  "reactivity second, ash and sulfur third) is presented as a buying "
  "checklist, and the Signature yield ledger tracks every tonne of coking "
  "coal into coke, gas, and tar so nothing of value leaves uncounted."),
},
{
 "key": "peat",
 "name": "Peat: young coal from the bog",
 "group": "coal-family",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "description": ("Peat is the first step on the coal ladder: partially "
  "decayed plant matter dug from bogs, the fuel Ireland, Finland, and "
  "parts of Russia still burn at meaningful scale. Fresh peat is up to 90 "
  "percent water; air-dried peat bricks settle near 30 to 40 percent "
  "moisture and deliver about 12 to 15 megajoules per kilogram dry. It "
  "burns with a long, lazy flame and a distinctive sweet smell, and "
  "historically it heated homes, fired brick kilns, and even ran "
  "peat-fired power stations. Peat's modern complication is climate: bogs "
  "are enormous carbon stores, and draining and burning them releases "
  "carbon accumulated over millennia - several jurisdictions now restrict "
  "or phase out peat extraction for fuel."),
 "how_it_works": ("Peat forms where dead plants accumulate faster than "
  "they decay - cold, waterlogged, acidic bogs. Cut by hand or milled by "
  "machine, it is dried in the field (traditional sods) or industrially "
  "(milled peat for power stations). The record works the drying "
  "arithmetic that dominates peat economics: removing water is the whole "
  "game, and every point of moisture above 40 percent is energy spent "
  "boiling the fuel's own water. It also covers the carbon-store issue "
  "honestly: a peat bog holds far more carbon per hectare than a forest, "
  "so the fuel decision is inseparable from the land-use decision. "
  "Small-scale use - the Irish turf fire - and industrial use - milled "
  "peat power stations with fluidized-bed boilers - are presented as two "
  "different engineering answers to the same wet fuel."),
 "key_points": [
  "Peat is the first coalification step: partially decayed bog plants, 12-15 MJ/kg dry.",
  "Fresh peat is up to 90 percent water; drying dominates its economics.",
  "It burns with a long lazy flame and a distinctive sweet smell.",
  "Bogs are huge carbon stores; draining them has climate consequences beyond the smoke.",
  "Still an established fuel in Ireland, Finland, and parts of Russia."],
 "requirements": [
  "Learner must place peat on the coalification sequence.",
  "Learner must compute the energy penalty of peat at a stated moisture.",
  "Learner must explain why bogs matter beyond the fuel they hold.",
  "Learner must name two regions where peat remains an established fuel."],
 "standards": [
  "Peat classification and sampling: industry and national standards.",
  "Moisture conventions for peat fuel (wet basis).",
  "Carbon-stock accounting for peatlands (IPCC wetland guidance)."],
 "citations": [
  "IPCC. 2013 Supplement to the 2006 Guidelines: Wetlands (peatland carbon stocks).",
  "Speight JG. The Chemistry and Technology of Coal. 3rd ed. CRC Press; 2013 (peat as coal precursor).",
  "Smil V. Energy and Civilization: A History. MIT Press; 2017 (peat in European energy history)."],
 "sig_lens": ("Signature reframing: the Signature Bog Ledger counts peat "
  "twice - once as fuel megajoules, once as carbon-store megajoules left "
  "in the ground - so the true cost of a turf fire is visible. The "
  "Signature drying protocol (cut, turn, stack, test at 40 percent) is "
  "taught as a field discipline, and the Signature land rule is absolute: "
  "fuel peat only where the bog's carbon accounts have been settled."),
},
{
 "key": "kerosene",
 "name": "Kerosene: the lamp fuel that lit the world",
 "group": "petroleum-distillates",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "description": ("Kerosene is the middle distillate of crude oil - "
  "hydrocarbon chains roughly 10 to 16 carbons long - that replaced whale "
  "oil in lamps in the 1860s and lit the world before electricity. It "
  "delivers about 35 megajoules per liter (about 43 MJ/kg) at a density "
  "near 0.81 kg/L, and its defining safety trait is a flash point above "
  "38 C: it does not give off ignitable vapor at room temperature the way "
  "gasoline does. That single property made it the safe household fuel of "
  "the 19th century and keeps it the safe middle fuel today: jet fuel is "
  "essentially highly specified kerosene, and kerosene heaters, stoves, "
  "and lamps remain established across the developing world. Standard "
  "grades are 1-K (low sulfur, for unvented heaters) and 2-K."),
 "how_it_works": ("Kerosene is cut from crude oil in the atmospheric "
  "distillation column between the gasoline/naphtha cut and the diesel "
  "cut, boiling roughly between 150 and 275 C. In a lamp or wick burner, "
  "capillary action draws it up the wick where heat vaporizes it and the "
  "vapor burns with a bright, steady flame; in a jet engine the same "
  "molecules are sprayed as a fine mist and burn continuously. The record "
  "explains the flash-point logic that governs handling: above 38 C means "
  "ordinary room-temperature storage will not produce an ignitable "
  "atmosphere, which is why kerosene ships and stores under far simpler "
  "rules than gasoline. It also covers the 1-K vs 2-K distinction (sulfur "
  "content and its effect on indoor air) and the straight run from "
  "kerosene to Jet A: the jet fuel specification is kerosene plus "
  "stringent freeze-point, thermal-stability, and cleanliness limits."),
 "key_points": [
  "Kerosene is a middle distillate (C10-C16), about 35 MJ/L at 0.81 kg/L.",
  "Flash point above 38 C: no ignitable vapor at room temperature.",
  "It replaced whale oil in the 1860s and lit the world before electricity.",
  "Jet fuel is essentially highly specified kerosene.",
  "Grades 1-K (low sulfur, unvented heaters) and 2-K."],
 "requirements": [
  "Learner must explain what flash point means using kerosene vs gasoline.",
  "Learner must state kerosene's energy density per liter and per kilogram.",
  "Learner must describe how a wick burner vaporizes and burns kerosene.",
  "Learner must explain the 1-K vs 2-K distinction."],
 "standards": [
  "ASTM D3699: standard specification for kerosine.",
  "Flash point: minimum 38 C (ASTM D56/D93).",
  "Sulfur limits distinguishing 1-K from 2-K grades."],
 "citations": [
  "ASTM D3699-19. Standard Specification for Kerosine.",
  "Gary JH, Handwerk GE, Kaiser MJ. Petroleum Refining: Technology and Economics. 5th ed. CRC Press; 2007 (distillate cuts).",
  "Smil V. Energy and Civilization: A History. MIT Press; 2017 (kerosene and the lamp era)."],
 "sig_lens": ("Signature reframing: the Signature Flash-Point Rule is "
  "taught as the one number that sets handling for every liquid fuel - "
  "kerosene is the teaching example because its 38 C line is the legal "
  "boundary between ordinary and hazardous handling. The Signature "
  "Kerosene Ladder shows the molecule's journey from lamp to jet engine "
  "as proof that a fuel's grade is a specification, not a substance: same "
  "cut, stricter tests, higher duty."),
},
{
 "key": "heating-oil",
 "name": "Heating oil No. 2: the home heat standard",
 "group": "petroleum-distillates",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "description": ("Heating oil No. 2 is the standard home-heating fuel of "
  "the northeastern United States and much of northern Europe: essentially "
  "the same middle distillate as diesel, dyed and taxed for heating use. "
  "One gallon delivers about 138,500 BTU (about 146 MJ), and a typical "
  "older home in a cold climate burns 600 to 900 gallons per winter. The "
  "oil sits in a basement or outdoor tank, a burner atomizes it into a "
  "fine spray, and it ignites in the combustion chamber - a system so "
  "established that millions of installations have run for half a century. "
  "Modern condensing oil boilers reach 90 percent-plus efficiency, and the "
  "industry's Bioheat program blends biodiesel into heating oil (B5 to "
  "B20) to cut carbon without changing equipment."),
 "how_it_works": ("The heating-oil system is fuel plus appliance: storage "
  "tank, fuel line with filter, burner with pump pressurizing oil to "
  "about 100 psi through a nozzle that atomizes it, electrodes that spark "
  "it, and a heat exchanger that passes the heat to water or air. The "
  "record works the homeowner's arithmetic: annual gallons times price "
  "per gallon is the heating bill; dividing by boiler efficiency gives "
  "delivered heat; and each gallon burned releases about 10.2 kilograms "
  "of CO2 (EIA factor), so an 800-gallon winter commits about 8.2 tonnes "
  "of CO2. It covers tank care (water in the tank grows sludge and "
  "corrosion; indoor tanks outlast outdoor ones), the dyed-fuel tax rule "
  "(heating oil is dyed red and untaxed for road use - burning it in a "
  "truck is tax evasion), and the Bioheat blending path that is "
  "decarbonizing the installed base without replacing it."),
 "key_points": [
  "No. 2 heating oil: about 138,500 BTU per gallon, dyed red, taxed for heating not roads.",
  "A cold-climate home typically burns 600-900 gallons per winter.",
  "System: tank, filter, pressurized burner nozzle, spark ignition, heat exchanger.",
  "Each gallon releases about 10.2 kg of CO2 (EIA factor).",
  "Bioheat blends (B5-B20) cut carbon in existing equipment."],
 "requirements": [
  "Learner must compute a winter heating bill and CO2 from stated gallons and price.",
  "Learner must describe the burner nozzle atomization step.",
  "Learner must explain why heating oil is dyed and what the dye signifies.",
  "Learner must state the BTU content of a gallon from memory."],
 "standards": [
  "ASTM D396: standard specification for fuel oils (No. 2 included).",
  "Dyed-fuel tax marking rules (IRS / national equivalents).",
  "Boiler efficiency ratings: AFUE method."],
 "citations": [
  "ASTM D396-21. Standard Specification for Fuel Oils.",
  "U.S. DOE Energy Information Administration. Heating oil explained: heat content and CO2 factors.",
  "Gary JH, Handwerk GE, Kaiser MJ. Petroleum Refining: Technology and Economics. 5th ed. CRC Press; 2007 (distillate production)."],
 "sig_lens": ("Signature reframing: the Signature Home-Heat Ledger turns "
  "the oil tank into a visible energy account - gallons on the gauge, "
  "BTUs in the bank, dollars per delivered BTU after efficiency. The "
  "Signature winter protocol (summer fill when prices dip, filter change "
  "each fall, water check each spring) is presented as a deterministic "
  "maintenance loop, and the Signature Bioheat path is framed as the "
  "upgrade that needs no new boiler: same tank, same burner, cleaner "
  "ledger."),
},
{
 "key": "fuel-oil-grades",
 "name": "Fuel oil grades: No. 1 through No. 6",
 "group": "petroleum-distillates",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "description": ("Fuel oils are graded No. 1 through No. 6 in a single "
  "ladder from light to heavy, and the grade number tells you almost "
  "everything about handling. No. 1 is a light distillate close to "
  "kerosene, used where it gets very cold. No. 2 is the standard heating "
  "oil and diesel cousin. No. 4 is a light residual for commercial "
  "boilers. No. 5 and No. 6 are heavy residuals - thick, tar-like, nearly "
  "solid at room temperature - burned in power plants, large ships, and "
  "industry. Energy density climbs with grade: No. 2 holds about 38.6 "
  "MJ/L while No. 6 holds about 40 to 42 MJ/L at a density near 0.99 "
  "kg/L. The price of that density is handling: No. 6 must be heated to "
  "flow and atomize, stored in heated tanks, and burned with preheated "
  "combustion air."),
 "how_it_works": ("The grades separate in the refinery by boiling range: "
  "distillates (No. 1, No. 2) come off the atmospheric column, residuals "
  "(No. 5, No. 6) are what is left after the vacuum column - the bottom "
  "of the barrel. Viscosity is the master variable: it rises roughly a "
  "hundredfold from No. 2 to No. 6, so each step up the grade ladder "
  "demands more heat just to move the fuel. The record presents the grade "
  "table as one continuum - density, viscosity, pour point, sulfur, and "
  "energy per liter all marching together - and explains the economic "
  "logic: residuals are cheap because few burners can handle them, so the "
  "fuel discount pays for the heated handling system. Sulfur is the "
  "regulatory shadow over the heavy grades: high-sulfur residual is "
  "increasingly restricted, which is why low-sulfur grades and scrubbers "
  "dominate new installations."),
 "key_points": [
  "Grades No. 1 to No. 6 form one ladder from light distillate to heavy residual.",
  "No. 2 is standard heating oil; No. 6 is tar-like residual near 0.99 kg/L.",
  "Energy per liter climbs with grade: about 38.6 MJ/L (No. 2) to 40-42 MJ/L (No. 6).",
  "Viscosity rises roughly a hundredfold from No. 2 to No. 6; heavy grades need heated handling.",
  "Residuals are cheap because few burners can handle them; sulfur rules are tightening."],
 "requirements": [
  "Learner must place any grade on the distillate-to-residual continuum.",
  "Learner must explain why No. 6 needs heated tanks and lines.",
  "Learner must state the energy-density trend across grades.",
  "Learner must explain the economic logic of cheap residual fuel."],
 "standards": [
  "ASTM D396: the grade definitions (No. 1 through No. 6).",
  "Viscosity measurement: ASTM D445 kinematic viscosity.",
  "Sulfur limits by grade and jurisdiction."],
 "citations": [
  "ASTM D396-21. Standard Specification for Fuel Oils (the grade system).",
  "Gary JH, Handwerk GE, Kaiser MJ. Petroleum Refining: Technology and Economics. 5th ed. CRC Press; 2007 (residual production).",
  "Speight JG. Handbook of Petroleum Product Analysis. 2nd ed. Wiley; 2015 (fuel oil properties)."],
 "sig_lens": ("Signature reframing: the Signature Grade Slider presents "
  "No. 1 through No. 6 as a single handling-vs-density tradeoff curve - "
  "every step up buys megajoules per liter and pays in heat, pumps, and "
  "sulfur paperwork. The Signature residual rule is blunt: never buy a "
  "heavy grade without pricing the heated system it demands. The "
  "Signature viscosity table (one page, all six grades) replaces a shelf "
  "of data sheets for the buying decision."),
},
{
 "key": "natural-gas",
 "name": "Natural gas: methane, the pipeline fuel",
 "group": "gaseous-fuels",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "description": ("Natural gas is mostly methane (CH4), the simplest "
  "hydrocarbon, and the established gaseous fuel of homes, power plants, "
  "and industry worldwide. Pipeline gas is typically 85 to 95 percent "
  "methane with small amounts of ethane, propane, and inerts; an "
  "odorant (mercaptan) is added so leaks smell. Methane holds about 55.5 "
  "megajoules per kilogram (higher heating value) - the highest mass "
  "energy density of any common chemical fuel - but as a gas at room "
  "conditions it is feather-light (about 0.72 kg per cubic meter), so "
  "volume is the problem and pipelines, compression, and liquefaction "
  "are the answers. It burns cleaner than coal or oil: about 53 kilograms "
  "of CO2 per gigajoule, the lowest of the fossil fuels, with essentially "
  "no sulfur or ash."),
 "how_it_works": ("Natural gas moves as a continuous river: wells feed "
  "gathering lines, processing plants strip out water, sulfur, and "
  "natural-gas liquids, and high-pressure transmission pipelines (up to "
  "about 100 bar) carry it to cities where distribution lines at low "
  "pressure bring it to the meter. Billing is by energy, not volume - the "
  "therm (100,000 BTU, about 105.5 MJ) or the cubic meter corrected for "
  "heating value. The record explains combustion (CH4 + 2O2 -> CO2 + 2H2O), "
  "the blue flame of a well-tuned burner versus the yellow flame of "
  "incomplete combustion making carbon monoxide, and the methane-leak "
  "caveat: methane is a potent greenhouse gas, so the climate advantage "
  "over coal depends on keeping leaks small - typically a few percent "
  "erases much of the benefit."),
 "key_points": [
  "Natural gas is 85-95 percent methane; about 55.5 MJ/kg, the highest mass density of common chemical fuels.",
  "As a gas it is feather-light (0.72 kg/m3), so pipelines, compression, and liquefaction solve the volume problem.",
  "Lowest CO2 of fossil fuels: about 53 kg CO2 per gigajoule; no sulfur, no ash.",
  "Odorant is added because methane itself is odorless.",
  "Methane leaks undercut the climate advantage; leak control is part of the fuel system."],
 "requirements": [
  "Learner must write the methane combustion equation and compute CO2 per gigajoule.",
  "Learner must explain why gas is billed by energy (therms) not volume.",
  "Learner must describe the well-to-meter chain in order.",
  "Learner must explain the methane-leak caveat quantitatively."],
 "standards": [
  "Pipeline gas quality: heating value, Wobbe index, and interchangeability limits.",
  "ASTM D3588: calculating heat value of gaseous fuels.",
  "Odorization requirements for distribution gas."],
 "citations": [
  "ASTM D3588-98(2017). Standard Practice for Calculating Heat Value, Compressibility Factor, and Relative Density of Gaseous Fuels.",
  "U.S. DOE Energy Information Administration. Natural gas explained (composition, heat content).",
  "IPCC. Emission factor for natural gas: 56.1 kg CO2/GJ (guidelines for national inventories)."],
 "sig_lens": ("Signature reframing: the Signature Gas Chain maps the "
  "well-to-burner path as one continuous energy river with meters at "
  "every lock - heating value measured, leaks hunted, therms billed. The "
  "Signature blue-flame test (flame color as a combustion diagnostic any "
  "homeowner can read) and the Signature leak-first rule (methane "
  "accounting before combustion accounting) are presented as the two "
  "disciplines that keep gas the cleanest fossil fuel in practice, not "
  "just on paper."),
},
{
 "key": "propane",
 "name": "Propane: bottled gas energy",
 "group": "gaseous-fuels",
 "ladder_rank": 12, "ladder_tier": "foundations",
 "description": ("Propane (C3H8) is the established fuel that goes where "
  "pipelines do not: rural homes, grills, forklifts, farms, and RVs. It "
  "is a byproduct of natural-gas processing and oil refining, and its "
  "trick is easy liquefaction - modest pressure (about 10 bar at room "
  "temperature) turns it liquid, so a steel bottle holds roughly 270 "
  "times more energy than the same volume of propane gas. Liquid propane "
  "delivers about 25.3 megajoules per liter (about 46.4 MJ/kg) at 0.51 "
  "kg/L; one gallon holds about 91,500 BTU. Tanks are never filled past "
  "80 percent so the liquid has room to expand with heat - the single "
  "most important propane safety rule. It burns clean (about 63 kg CO2 "
  "per gigajoule) with no sulfur."),
 "how_it_works": ("A propane system is a pressure vessel plus a regulator: "
  "the tank holds liquid under its own vapor pressure, the regulator "
  "drops it to inches of water column for the appliance, and the liquid "
  "boils to replace what is drawn - which is why a hard-working tank "
  "frosts over in winter (vaporization chills the tank, slowing "
  "vaporization). The record works the 80-percent rule: liquid expands "
  "about 1.5 percent per 10 F, so the vapor space is the expansion "
  "allowance that keeps the relief valve shut. It covers leak behavior "
  "(propane vapor is heavier than air and pools in low spots - the "
  "basement-floor hazard), the rotten-egg odorant, and the standard "
  "appliance set: furnaces, water heaters, ranges, grills, and the "
  "forklift fleets that run on propane indoors because it burns so "
  "cleanly."),
 "key_points": [
  "Propane liquefies under modest pressure, so bottles hold about 270x the energy of the same volume of gas.",
  "Liquid propane: about 25.3 MJ/L; one gallon about 91,500 BTU.",
  "Tanks are filled to 80 percent maximum: the vapor space is the expansion allowance.",
  "Propane vapor is heavier than air and pools low - the key leak hazard.",
  "Clean burn (about 63 kg CO2/GJ); the fuel where pipelines do not reach."],
 "requirements": [
  "Learner must compute usable gallons in a tank under the 80-percent rule.",
  "Learner must explain why a hard-working tank frosts in winter.",
  "Learner must describe propane leak behavior and the low-spot hazard.",
  "Learner must state propane's BTU per gallon from memory."],
 "standards": [
  "ASTM D1835: standard specification for liquefied petroleum gases.",
  "NFPA 58: liquefied petroleum gas code (storage and handling).",
  "The 80-percent filling rule (fixed maximum liquid level)."],
 "citations": [
  "ASTM D1835-22. Standard Specification for Liquefied Petroleum (LP) Gases.",
  "NFPA 58. Liquefied Petroleum Gas Code (filling limits and leak behavior).",
  "U.S. DOE Energy Information Administration. Propane explained: heat content 91,500 BTU per gallon."],
 "sig_lens": ("Signature reframing: the Signature Bottle Ledger treats "
  "every propane tank as a pressure-rated energy account - gallons in, "
  "BTUs banked, 80 percent never exceeded. The Signature frost reading "
  "(frost line as a fuel gauge and a vaporization diagnostic) and the "
  "Signature low-spot rule (detectors near the floor, never near the "
  "ceiling) are presented as the two field disciplines of bottled gas. "
  "The Signature off-pipeline map shows where propane beats extending "
  "the gas main."),
},
]
ENTRIES += [
{
 "key": "gasoline",
 "name": "Gasoline and the octane number",
 "group": "liquid-transport-fuels",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "description": ("Gasoline is the established spark-ignition engine fuel: "
  "a blend of 150-plus hydrocarbons in the C4-C12 range, tuned so it "
  "vaporizes easily, resists knocking, and burns cleanly in millions of "
  "engines. It delivers about 34.2 megajoules per liter (about 46.4 MJ/kg) "
  "at roughly 0.74 kg/L. The octane number is its defining quality "
  "measure: it rates resistance to knock (premature detonation), with US "
  "pumps showing the anti-knock index AKI = (RON + MON) / 2 - regular 87, "
  "midgrade 89, premium 91-93. Higher octane is not more energy; it is "
  "more knock resistance, which lets high-compression engines extract "
  "more work from the same energy. Gasoline's safety signature is its "
  "flash point near minus 43 C: it makes ignitable vapor at any normal "
  "temperature, which is why gasoline handling rules are the strictest of "
  "any common fuel."),
 "how_it_works": ("Refineries build gasoline by blending streams - "
  "reformate, alkylate, isomerate, FCC gasoline - each chosen for octane "
  "and volatility, then add the detergent and deposit-control additive "
  "package required in most markets. In the engine, the injector sprays "
  "it, the spark ignites it, and the flame front should sweep smoothly; "
  "knock is the end gas detonating before the flame arrives, hammering "
  "pistons. The record explains the octane test engines (the CFR engine "
  "comparing fuel against iso-octane/n-heptane reference blends), the "
  "linear blending arithmetic used at the rack (blend octane is volume-"
  "weighted to first order), ethanol's role as the modern octane booster "
  "(ethanol's blending octane is about 112-113), and the volatility "
  "classes that keep summer gasoline from vapor-locking and winter "
  "gasoline starting in the cold. Each gallon burned releases about 8.9 "
  "kg of CO2."),
 "key_points": [
  "Gasoline: C4-C12 blend, about 34.2 MJ/L; octane measures knock resistance, not energy.",
  "US pumps show AKI = (RON + MON) / 2: regular 87, premium 91-93.",
  "Flash point near -43 C: ignitable vapor at any normal temperature, strictest handling rules.",
  "Refineries blend streams (reformate, alkylate, isomerate) plus additive packages.",
  "One gallon releases about 8.9 kg of CO2; ethanol is the modern octane booster."],
 "requirements": [
  "Learner must compute AKI from stated RON and MON.",
  "Learner must explain knock in terms of flame front vs end-gas detonation.",
  "Learner must compute a two-stream blend octane by volume weighting.",
  "Learner must explain why premium fuel does not help an engine designed for regular."],
 "standards": [
  "ASTM D4814: standard specification for automotive spark-ignition engine fuel.",
  "Octane measurement: ASTM D2699 (RON) / D2700 (MON).",
  "Volatility classes and vapor-pressure limits by season and region."],
 "citations": [
  "ASTM D4814-21c. Standard Specification for Automotive Spark-Ignition Engine Fuel.",
  "Heywood JB. Internal Combustion Engine Fundamentals. McGraw-Hill; 1988 (knock and octane).",
  "Gary JH, Handwerk GE, Kaiser MJ. Petroleum Refining: Technology and Economics. 5th ed. CRC Press; 2007 (gasoline blending)."],
 "sig_lens": ("Signature reframing: the Signature Octane Ledger treats "
  "knock resistance as a purchased commodity - every octane point has a "
  "price, and the Signature rule is to buy exactly the octane the engine "
  "was designed for, never more. The Signature blend board (streams as "
  "sliders, octane and volatility as targets) turns refinery blending "
  "into a visible optimization puzzle, and the Signature flash-point "
  "doctrine makes gasoline the reference hazard: handle everything else "
  "by comparison to it."),
},
{
 "key": "diesel",
 "name": "Diesel fuel and the cetane number",
 "group": "liquid-transport-fuels",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "description": ("Diesel is the established compression-ignition fuel: "
  "heavier than gasoline (C10-C20 range), oilier, and made to ignite from "
  "heat and pressure rather than a spark. It delivers about 38.6 "
  "megajoules per liter (about 45.5 MJ/kg) at roughly 0.85 kg/L - about "
  "13 percent more energy per liter than gasoline, which is half the "
  "diesel economy advantage (the rest is the engine's higher compression "
  "ratio). The cetane number is diesel's quality measure and the mirror "
  "of octane: it rates ignition readiness, with US diesel at 40 minimum "
  "and European EN 590 at 51 minimum - higher cetane means shorter "
  "ignition delay, quieter cold starts, and cleaner combustion. Diesel's "
  "safety signature is a flash point above 52 C: far safer to store and "
  "handle than gasoline, which is why diesel powers trucks, ships, "
  "trains, tractors, and generators worldwide."),
 "how_it_works": ("In a diesel engine there is no spark: the piston "
  "compresses air until it is hotter than about 500 C, fuel is injected "
  "as a fine spray, and it ignites almost on contact. Cetane measures how "
  "quickly that happens - low cetane means long ignition delay, diesel "
  "knock, white smoke, and hard cold starts. The record explains the "
  "cetane test (ASTM D613, ignition delay in a test engine), the "
  "lubricity problem created by ultra-low-sulfur diesel (sulfur removal "
  "stripped natural lubricity, so additives restore it per ASTM D975), "
  "the cold-flow problem (wax crystals gel the fuel - cloud point and "
  "CFPP set winter grades), and the emissions chain (high combustion "
  "temperatures make NOx; modern trucks answer with selective catalytic "
  "reduction using diesel exhaust fluid). Each liter burned releases "
  "about 2.68 kg of CO2."),
 "key_points": [
  "Diesel: C10-C20, about 38.6 MJ/L; ignites by compression heat, no spark.",
  "Cetane rates ignition readiness (mirror of octane): US 40 min, EU 51 min.",
  "Flash point above 52 C: far safer handling than gasoline.",
  "Ultra-low-sulfur diesel needs lubricity additives; winter needs cold-flow grades.",
  "One liter releases about 2.68 kg of CO2; NOx handled by SCR systems."],
 "requirements": [
  "Learner must explain cetane as the mirror of octane with the ignition-delay mechanism.",
  "Learner must compute the per-liter energy advantage of diesel over gasoline.",
  "Learner must explain the lubricity and cold-flow problems and their fixes.",
  "Learner must state diesel's flash point and CO2 per liter."],
 "standards": [
  "ASTM D975: standard specification for diesel fuel.",
  "Cetane measurement: ASTM D613; lubricity: ASTM D6079 (HFRR).",
  "EN 590 (Europe): 51 cetane minimum; cold-flow grades by climate."],
 "citations": [
  "ASTM D975-21. Standard Specification for Diesel Fuel Oil.",
  "Heywood JB. Internal Combustion Engine Fundamentals. McGraw-Hill; 1988 (compression ignition and cetane).",
  "Knothe G, Krahl J, Van Gerpen J. The Biodiesel Handbook. 2nd ed. AOCS Press; 2010 (diesel fuel properties and lubricity)."],
 "sig_lens": ("Signature reframing: the Signature Cetane Clock visualizes "
  "ignition delay as a stopwatch - every cetane point buys microseconds "
  "of readiness, and the Signature cold-start rule converts winter "
  "complaints into a CFPP number before buying fuel. The Signature diesel "
  "ledger (energy per liter, CO2 per liter, cents per megajoule) is the "
  "fleet buyer's one-page truth, and the Signature lubricity check makes "
  "the additive package a line item, never an assumption."),
},
{
 "key": "ethanol-blends",
 "name": "Ethanol and E10/E15: gasoline stretched with grain",
 "group": "biofuels",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "description": ("Fuel ethanol is ethyl alcohol (C2H5OH) made by "
  "fermenting sugars - corn in the US, sugarcane in Brazil - then "
  "distilled and denatured so it cannot be drunk. Neat ethanol delivers "
  "about 23.4 megajoules per liter (about 26.8 MJ/kg) at 0.79 kg/L, "
  "roughly two-thirds the energy per liter of gasoline, but its blending "
  "octane of about 112-113 makes it the refinery's favorite octane "
  "booster. E10 (10 percent ethanol) is the standard gasoline of the "
  "United States; E15 is approved for cars built since 2001. The energy "
  "math is honest: E10 holds about 3 percent less energy per gallon than "
  "pure gasoline, so fuel economy drops about 3 percent - the driver "
  "pays in volume what the blend gains in octane and renewable content."),
 "how_it_works": ("Ethanol is made by fermentation (yeast turns sugar "
  "into alcohol and CO2), distillation to near-azeotrope (95 percent), "
  "and molecular-sieve drying to fuel grade (99+ percent), then "
  "denatured with a few percent gasoline. At the terminal it is splash-"
  "blended into gasoline - never in the refinery, because ethanol picks "
  "up water in pipelines. The record explains the water affinity that "
  "drives the logistics (ethanol is hygroscopic; phase separation in a "
  "tank ruins the fuel), the octane economics (a refinery can make a "
  "lower-octane base gasoline and let ethanol carry it to 87 AKI), and "
  "the carbon debate in one honest paragraph: corn ethanol cuts "
  "lifecycle greenhouse gases modestly versus gasoline (estimates vary "
  "with land-use assumptions), sugarcane ethanol cuts them substantially "
  "more. Flash point is about 13 C - handle like gasoline."),
 "key_points": [
  "Fuel ethanol: fermented, distilled, dried, denatured; about 23.4 MJ/L.",
  "Blending octane about 112-113: the refinery's octane booster.",
  "E10 is standard US gasoline; E10 carries about 3 percent less energy per gallon.",
  "Ethanol is hygroscopic: splash-blended at the terminal, never pipelined.",
  "Corn ethanol cuts lifecycle CO2 modestly; sugarcane ethanol cuts it substantially more."],
 "requirements": [
  "Learner must compute E10 energy per gallon from the component values.",
  "Learner must explain why ethanol is blended at the terminal, not the refinery.",
  "Learner must explain the octane economics of ethanol blending.",
  "Learner must state ethanol's flash point and handling class."],
 "standards": [
  "ASTM D4806: denatured fuel ethanol for blending.",
  "ASTM D4814: finished E10/E15 gasoline requirements.",
  "Denaturant and water-content limits."],
 "citations": [
  "ASTM D4806-21a. Standard Specification for Denatured Fuel Ethanol for Blending with Gasolines.",
  "Demirbas A. Biofuels: Securing the Planet's Future Energy Needs. Springer; 2009 (ethanol production and properties).",
  "U.S. DOE Alternative Fuels Data Center. Ethanol fuel basics (blends, energy content)."],
 "sig_lens": ("Signature reframing: the Signature Blend Ledger shows "
  "every ethanol blend as three numbers - octane bought, energy lost, "
  "renewable share gained - so the tradeoff is never hidden. The "
  "Signature water rule (ethanol never sees a pipeline, tanks get water "
  "checks) is taught as logistics law, and the Signature feedstock "
  "comparison (corn vs cane on the same lifecycle ledger) lets the "
  "carbon claim be audited instead of believed."),
},
{
 "key": "e85",
 "name": "E85: the flex-fuel blend",
 "group": "biofuels",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "description": ("E85 is the high-ethanol blend - 51 to 83 percent "
  "ethanol, the rest gasoline, with the exact ratio shifting by season "
  "(more gasoline in winter for cold starts). It is the established fuel "
  "of flex-fuel vehicles (FFVs), which carry a sensor that reads the "
  "actual ethanol fraction and adjusts injection and timing on the fly. "
  "E85 delivers about 25 megajoules per liter - roughly 26 percent less "
  "energy per gallon than gasoline - so an FFV's range drops by about a "
  "quarter on E85; the honest comparison is cost per mile, not price per "
  "gallon. The payoff is octane: E85's effective octane near 100-105 "
  "lets tuned engines run high boost, which is why it is a darling of "
  "the performance world as well as the renewable-fuels world."),
 "how_it_works": ("The flex-fuel sensor (measuring dielectric properties) "
  "tells the engine computer the ethanol fraction several times per "
  "second; the computer stretches injector pulse width (more fuel per "
  "combustion event, since ethanol carries less energy) and advances "
  "timing to exploit the octane. Cold starting is the engineering "
  "constraint: ethanol vaporizes poorly below about 15 C, so winter E85 "
  "is really E51-E60 with extra gasoline for volatility. The record "
  "works the driver's arithmetic - the break-even rule: E85 must be "
  "priced at least 25-30 percent below gasoline per gallon to match cost "
  "per mile - and the materials story: FFVs use ethanol-compatible fuel "
  "lines, pumps, and seals because ethanol attacks some rubbers and "
  "absorbs water that corrodes steel. Brazil's decades of high-ethanol "
  "operation are presented as the long-term proof case."),
 "key_points": [
  "E85: 51-83 percent ethanol by season; only for flex-fuel vehicles.",
  "About 25 MJ/L: roughly 26 percent less energy per gallon than gasoline.",
  "The honest comparison is cost per mile, with a 25-30 percent per-gallon discount break-even.",
  "Effective octane near 100-105: high boost and performance applications.",
  "Winter E85 drops to E51-E60 for cold-start volatility."],
 "requirements": [
  "Learner must compute the break-even E85 price from a stated gasoline price.",
  "Learner must explain how the flex-fuel sensor and computer adapt to the blend.",
  "Learner must explain why winter E85 carries less ethanol.",
  "Learner must state E85's energy penalty per gallon."],
 "standards": [
  "ASTM D5798: standard specification for ethanol fuel blends for FFVs.",
  "Seasonal volatility classes for E85.",
  "FFV materials compatibility requirements."],
 "citations": [
  "ASTM D5798-21. Standard Specification for Ethanol Fuel Blends for Flexible-Fuel Automotive Spark-Ignition Engines.",
  "U.S. DOE Alternative Fuels Data Center. Flexible fuel vehicles and E85 (energy content, break-even).",
  "Demirbas A. Biofuels: Securing the Planet's Future Energy Needs. Springer; 2009 (high-ethanol blends)."],
 "sig_lens": ("Signature reframing: the Signature Mile Ledger replaces "
  "price-per-gallon with cost-per-mile as the only honest E85 number, "
  "with the break-even discount computed live at the pump. The Signature "
  "season dial (blend vs temperature vs startability) teaches winter "
  "fuel as a designed compromise, and the Signature octane dividend "
  "shows tuners exactly what E85's 100-plus octane buys in boost - the "
  "performance case stated in numbers, not slogans."),
},
{
 "key": "biodiesel",
 "name": "Biodiesel B100: diesel from vegetable oil",
 "group": "biofuels",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "description": ("Biodiesel is diesel fuel made from vegetable oils or "
  "animal fats by transesterification: oil plus methanol becomes "
  "fatty-acid methyl esters (FAME) plus glycerol. B100 (pure biodiesel) "
  "delivers about 33.3 megajoules per liter (about 37.8 MJ/kg) at 0.88 "
  "kg/L - roughly 8 percent less energy per gallon than petroleum diesel "
  "- with a naturally high cetane number of 50-60 and superb lubricity "
  "that refiners envy. It is biodegradable, essentially sulfur-free, and "
  "cuts lifecycle CO2 substantially versus petroleum diesel because the "
  "plants absorbed CO2 as they grew. Its weaknesses are cold flow (it "
  "gels sooner than diesel), oxidative stability (it ages faster), and "
  "feedstock limits: there is not enough waste oil and cropland to "
  "replace more than a fraction of diesel demand."),
 "how_it_works": ("Transesterification is the core chemistry: a "
  "triglyceride plus three methanols, with a catalyst (usually sodium or "
  "potassium hydroxide), yields three methyl esters plus glycerol. The "
  "record walks the plant: feedstock pretreatment (free fatty acids "
  "neutralized), reaction, glycerol separation, washing and drying, and "
  "quality testing to ASTM D6751 - the specification that separates fuel "
  "from fryer oil. It explains why B100's high cetane and lubricity come "
  "free with the molecule (oxygen in the ester, long straight chains), "
  "why cold flow is the Achilles heel (saturated esters crystallize - "
  "palm biodiesel gels near room temperature), and the honest scale "
  "math: US waste-oil and soybean capacity covers single-digit percents "
  "of diesel demand, which is why biodiesel is a blend component, not a "
  "replacement."),
 "key_points": [
  "Biodiesel: vegetable oil plus methanol becomes FAME plus glycerol (transesterification).",
  "B100: about 33.3 MJ/L; cetane 50-60; superb natural lubricity; sulfur-free.",
  "Cuts lifecycle CO2 substantially vs petroleum diesel; biodegradable.",
  "Weaknesses: cold flow (gels early), oxidation stability, limited feedstock scale.",
  "ASTM D6751 is the specification separating fuel from fryer oil."],
 "requirements": [
  "Learner must write the transesterification equation in words and products.",
  "Learner must compute the energy penalty of B100 vs petroleum diesel per gallon.",
  "Learner must explain the cold-flow mechanism (saturated ester crystallization).",
  "Learner must state the feedstock-scale limit honestly."],
 "standards": [
  "ASTM D6751: biodiesel fuel blend stock (B100).",
  "EN 14214 (Europe): FAME specification.",
  "Oxidation stability and cold-flow test methods."],
 "citations": [
  "ASTM D6751-20a. Standard Specification for Biodiesel Fuel Blend Stock (B100) for Middle Distillate Fuels.",
  "Knothe G, Krahl J, Van Gerpen J. The Biodiesel Handbook. 2nd ed. AOCS Press; 2010 (chemistry, properties, standards).",
  "Demirbas A. Biodiesel: A Realistic Fuel Alternative for Diesel Engines. Springer; 2008 (production and scale)."],
 "sig_lens": ("Signature reframing: the Signature Ester Ledger tracks "
  "every batch from feedstock to tank - oil in, methanol in, glycerol "
  "out, esters banked - with the ASTM D6751 test panel as the gate that "
  "no batch skips. The Signature cold-flow map (feedstock vs gel point) "
  "tells blenders which oil works in which winter, and the Signature "
  "scale honesty rule states the fraction of diesel demand biodiesel can "
  "cover before anyone plans a fleet on it."),
},
{
 "key": "biodiesel-blends",
 "name": "Biodiesel blends: B5 and B20",
 "group": "biofuels",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "description": ("Biodiesel is mostly burned blended: B5 (5 percent "
  "biodiesel) runs in any diesel with no changes and is the quiet "
  "default across much of Europe; B20 (20 percent) is the established "
  "US fleet blend, approved by most engine makers with minor material "
  "and maintenance notes. B20 delivers about 37.4 megajoules per liter - "
  "only about 3 percent less energy than straight diesel - while adding "
  "biodiesel's lubricity, cutting lifecycle CO2 roughly 15 percent, and "
  "keeping cold-flow and stability behavior close to diesel. Blends above "
  "B20 exist but demand real attention to seals, filters (biodiesel "
  "cleans old deposits loose), and storage time. The blend ladder is the "
  "practical compromise between petroleum diesel's scale and biodiesel's "
  "benefits."),
 "how_it_works": ("Blending is linear to first order: B20's energy, "
  "cetane, and density sit 20 percent of the way from diesel to B100, "
  "and the record's demo verifies it. The engineering notes that matter: "
  "biodiesel is a mild solvent, so the first tanks of B20 scrub years of "
  "petroleum deposits off tank walls and plug filters - a one-time "
  "purge, planned for. Elastomer compatibility: pre-1994 natural-rubber "
  "seals can swell; modern Viton handles B20 fine. Storage: biodiesel "
  "oxidizes faster than diesel, so B20 gets a six-month turnover rule "
  "where diesel tolerates a year. The record also covers the Bioheat "
  "crossover - the same B5-B20 logic heating homes - and the quality "
  "chain: B100 must meet ASTM D6751 before blending, and the finished "
  "B20 must meet ASTM D7467."),
 "key_points": [
  "B5 runs in any diesel unchanged; B20 is the established US fleet blend.",
  "B20: about 37.4 MJ/L, only ~3 percent less energy than diesel; ~15 percent lifecycle CO2 cut.",
  "Biodiesel's solvent effect purges old deposits: plan the first filter changes.",
  "Storage turnover: about six months for B20 vs a year for diesel.",
  "Quality chain: D6751 for the B100, D7467 for the finished B20."],
 "requirements": [
  "Learner must compute B20 energy content by linear blending.",
  "Learner must explain the first-fill filter-plugging phenomenon.",
  "Learner must state the storage-turnover rule and its cause.",
  "Learner must name the two ASTM specifications in the quality chain."],
 "standards": [
  "ASTM D7467: diesel fuel oil, biodiesel blend (B6-B20).",
  "ASTM D6751: the B100 blend stock entering the blend.",
  "Engine-maker approvals for B20 (OEM position statements)."],
 "citations": [
  "ASTM D7467-20a. Standard Specification for Diesel Fuel Oil, Biodiesel Blend (B6 to B20).",
  "Knothe G, Krahl J, Van Gerpen J. The Biodiesel Handbook. 2nd ed. AOCS Press; 2010 (blend properties and materials).",
  "U.S. DOE Alternative Fuels Data Center. Biodiesel blends (B20 handling and approvals)."],
 "sig_lens": ("Signature reframing: the Signature Blend Slider shows "
  "B0 to B100 as one continuum - energy, CO2, cold flow, and maintenance "
  "all moving together - so a fleet manager picks the blend point with "
  "eyes open. The Signature first-fill protocol (filters on hand, tanks "
  "inspected, turnover clock started) turns biodiesel's solvent effect "
  "from a surprise into a scheduled purge, and the Signature quality "
  "chain makes D6751-then-D7467 a non-negotiable sequence."),
},
{
 "key": "methanol",
 "name": "Methanol: the simplest alcohol fuel",
 "group": "alternative-fuels",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "description": ("Methanol (CH3OH) is the simplest alcohol: a "
  "single-carbon fuel made at scale from natural gas (steam reforming "
  "to syngas, then catalytic synthesis) and burnable in engines, "
  "turbines, and direct-methanol fuel cells. It delivers about 15.8 "
  "megajoules per liter (about 19.9 MJ/kg) - roughly half the energy per "
  "liter of gasoline - so a methanol vehicle needs about twice the tank "
  "volume for the same range. Its virtues are high octane (about 109), "
  "clean combustion, and easy synthesis from many feedstocks including "
  "biomass and captured CO2. Its shadow is toxicity: swallowing even "
  "tens of milliliters can cause blindness or death, and its flame is "
  "nearly invisible in daylight - the two facts that dominate every "
  "methanol safety program. Established uses include racing fuel, "
  "chemical feedstock, marine fuel trials, and China's M15/M85 vehicle "
  "fleets."),
 "how_it_works": ("Methanol synthesis is mature industrial chemistry: "
  "natural gas is reformed to carbon monoxide plus hydrogen, then "
  "converted over a copper-zinc catalyst at 50-100 bar and 200-300 C. "
  "In an engine, methanol's high latent heat of vaporization cools the "
  "charge (a power bonus) and its octane tolerates high compression; in "
  "a direct-methanol fuel cell it oxidizes electrochemically without "
  "reforming. The record covers the toxicity mechanism honestly "
  "(methanol metabolizes to formaldehyde and formic acid - the antidote "
  "is ethanol or fomepizole, which block the metabolic pathway), the "
  "invisible-flame hazard and its countermeasures (colored additives, "
  "thermal imaging at race tracks), and the energy arithmetic that sets "
  "tank sizing: about 2.2 liters of methanol per liter of gasoline for "
  "equal energy."),
 "key_points": [
  "Methanol: CH3OH, about 15.8 MJ/L - roughly half gasoline's energy per liter.",
  "Made from natural gas via syngas; burnable in engines, turbines, DMFC fuel cells.",
  "High octane (~109) and charge-cooling: performance virtues.",
  "Toxic: tens of milliliters can blind or kill; flame nearly invisible in daylight.",
  "Established in racing, chemicals, marine trials, and Chinese M-fleets."],
 "requirements": [
  "Learner must compute the tank-volume ratio of methanol to gasoline for equal energy.",
  "Learner must explain the toxicity mechanism and the antidote logic.",
  "Learner must describe the invisible-flame hazard and countermeasures.",
  "Learner must outline the synthesis route from natural gas."],
 "standards": [
  "IMPCA methanol reference specifications (fuel-grade).",
  "Methanol handling: toxicity exposure limits and labeling.",
  "Marine methanol fuel: developing class-society rules noted as evolving."],
 "citations": [
  "Olah GA, Goeppert A, Prakash GKS. Beyond Oil and Gas: The Methanol Economy. 2nd ed. Wiley-VCH; 2009 (synthesis, fuel use, safety).",
  "IMPCA. Methanol Reference Specifications (fuel-grade quality).",
  "U.S. DOE Alternative Fuels Data Center. Methanol fuel basics (properties, toxicity)."],
 "sig_lens": ("Signature reframing: the Signature Methanol Ledger states "
  "the fuel's whole truth on one page - half the energy per liter, "
  "double the tank, plus-109 octane, minus-toxicity - so no decision "
  "ignores the shadow. The Signature toxicity protocol (sealed systems, "
  "labeled lines, antidote knowledge posted) is taught as the price of "
  "admission, and the Signature synthesis map shows every feedstock road "
  "to the same molecule: gas today, biomass and captured CO2 tomorrow."),
},
{
 "key": "avgas",
 "name": "Aviation gasoline: 100LL for piston aircraft",
 "group": "aviation-fuels",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "description": ("Aviation gasoline (avgas) is the established fuel of "
  "piston-engine aircraft: high-octane gasoline refined to far tighter "
  "limits than road fuel. The world standard is 100LL (low lead), dyed "
  "blue, with a lean-mixture octane rating of 100 and no more than 0.56 "
  "grams of lead per liter - the last leaded fuel in widespread use, "
  "kept because aircraft engines were certified around lead's octane "
  "and valve protection. It delivers about 33-34 megajoules per liter. "
  "Avgas must not vapor-lock at altitude, must start a cold engine on a "
  "winter ramp, and must keep for months in a wing tank - so its "
  "volatility, stability, and cleanliness specifications exceed anything "
  "on the road. The industry's transition to unleaded replacements "
  "(G100UL and Swift's 100R) is the fuel's defining current story."),
 "how_it_works": ("Avgas is blended from high-octane refinery streams "
  "(alkylate especially) plus tetraethyl lead at a fraction of historic "
  "levels, with strict limits on aromatics, olefins, and gum. The record "
  "explains the lead dilemma honestly: lead boosts octane cheaply and "
  "protects exhaust valve seats in old engine designs, but it is a "
  "neurotoxin - the entire avgas system (dedicated trucks, sumps, fuel "
  "farm segregation) exists to keep leaded fuel out of the unleaded "
  "world. Preflight discipline is part of the fuel system: pilots sump "
  "the tanks to check for water (avgas and water do not mix; water "
  "sinks) and verify the blue color. The demo computes lead mass per "
  "fill-up and the energy on board a typical four-seat aircraft, and the "
  "record closes with the unleaded transition: drop-in replacements now "
  "certified, fleet turnover measured in decades."),
 "key_points": [
  "100LL: blue-dyed, 100 lean octane, max 0.56 g lead/L - the last leaded fuel in wide use.",
  "About 33-34 MJ/L; tighter volatility, stability, and cleanliness limits than road gasoline.",
  "Lead protects old valve designs but is a neurotoxin: segregated handling throughout.",
  "Pilots sump tanks preflight: water sinks, color must be blue.",
  "Unleaded replacements (G100UL, 100R) are certified; transition will take decades."],
 "requirements": [
  "Learner must compute lead mass in a stated fuel load at the 0.56 g/L limit.",
  "Learner must explain the lead dilemma (valve protection vs neurotoxicity).",
  "Learner must describe the preflight sump check and what it detects.",
  "Learner must explain why avgas volatility limits are tighter than road gasoline."],
 "standards": [
  "ASTM D910: standard specification for leaded aviation gasolines.",
  "ASTM D7547: unleaded aviation gasoline test fuel (transition path).",
  "FAA certification of unleaded replacements (G100UL STC)."],
 "citations": [
  "ASTM D910-21. Standard Specification for Leaded Aviation Gasolines.",
  "FAA. Unleaded aviation gasoline transition program documentation.",
  "Heywood JB. Internal Combustion Engine Fundamentals. McGraw-Hill; 1988 (octane and knock in aircraft engines)."],
 "sig_lens": ("Signature reframing: the Signature Lead Ledger counts "
  "every gram of lead from refinery to exhaust - the Signature method "
  "for managing a hazardous legacy fuel honestly while it remains "
  "necessary. The Signature preflight protocol (sump, color, quantity, "
  "three checks before every flight) is taught as fuel discipline, and "
  "the Signature transition map tracks the unleaded replacements "
  "airport by airport, so the end of leaded avgas is managed, not "
  "wished for."),
},
{
 "key": "jet-fuel",
 "name": "Jet fuel: Jet A and Jet A-1",
 "group": "aviation-fuels",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "description": ("Jet fuel is highly specified kerosene: the established "
  "fuel of turbine aviation, burned in every airliner flying. Jet A "
  "(US) and Jet A-1 (international) deliver about 35.3 megajoules per "
  "liter (about 43.2 MJ/kg) and differ mainly in freeze point: minus 40 "
  "C for Jet A, minus 47 C for Jet A-1, because fuel in a wing tank at "
  "cruise altitude gets brutally cold. The specification (ASTM D1655) "
  "controls what passengers never think about: thermal stability (no "
  "deposits in hot fuel lines), existent gum, water separation, "
  "lubricity, smoke point, and microbial growth. A wide-body airliner "
  "can carry over 100 tonnes of it; fuel is typically 20-30 percent of "
  "an airline's operating cost, which is why the industry measures "
  "everything in kilograms per flight."),
 "how_it_works": ("In a turbine, jet fuel is sprayed into the combustor "
  "as a fine mist and burns continuously - no pistons, no spark after "
  "start, just a controlled blowtorch driving the turbine. The record "
  "explains the cold-soak problem (fuel must still flow and ignite after "
  "hours at minus 40 C - the freeze-point specification is a flight-"
  "safety item), the water problem (dissolved water plus cold equals ice "
  "crystals that can block filters - fuel-system icing inhibitor is the "
  "answer where approved), and the quality chain from refinery to wing: "
  "batch testing, dedicated pipelines and trucks, filter-separators, and "
  "the daily sump checks at the airport farm. It also covers sustainable "
  "aviation fuel (SAF): certified drop-in blends up to 50 percent that "
  "meet the same D1655-derived specification, the industry's "
  "decarbonization path that changes nothing about the engine."),
 "key_points": [
  "Jet A / Jet A-1: specified kerosene, about 35.3 MJ/L; freeze points -40 C / -47 C.",
  "ASTM D1655 controls thermal stability, gum, water separation, smoke point, microbes.",
  "Turbines burn it continuously as a fine mist; fuel is 20-30 percent of airline operating cost.",
  "Cold-soak and water-ice are the two flight-safety fuel problems.",
  "SAF: certified drop-in blends to 50 percent, same specification, lower lifecycle carbon."],
 "requirements": [
  "Learner must explain why freeze point is a flight-safety specification.",
  "Learner must describe the water-ice mechanism and its countermeasure.",
  "Learner must outline the refinery-to-wing quality chain.",
  "Learner must explain what makes SAF 'drop-in'."],
 "standards": [
  "ASTM D1655: aviation turbine fuel (Jet A / Jet A-1).",
  "Defence Standard 91-091 (UK MoD turbine fuel).",
  "ASTM D7566: sustainable aviation fuel blend components."],
 "citations": [
  "ASTM D1655-22. Standard Specification for Aviation Turbine Fuels.",
  "ASTM D7566-22. Standard Specification for Aviation Turbine Fuel Containing Synthesized Hydrocarbons.",
  "Gary JH, Handwerk GE, Kaiser MJ. Petroleum Refining: Technology and Economics. 5th ed. CRC Press; 2007 (jet fuel production)."],
 "sig_lens": ("Signature reframing: the Signature Cold-Soak Ledger "
  "treats freeze point as the master number of jet fuel - every colder "
  "route, every longer cruise, checked against minus 40 or minus 47 "
  "before dispatch. The Signature quality chain (batch test, dedicated "
  "transport, filter-separator, daily sump) is taught as a chain of "
  "custody for energy, and the Signature SAF ledger counts lifecycle "
  "carbon per flight so the drop-in claim is audited in megajoules and "
  "tonnes, not adjectives."),
},
{
 "key": "lng",
 "name": "LNG: natural gas made liquid",
 "group": "gaseous-fuels",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "description": ("Liquefied natural gas (LNG) is methane cooled to minus "
  "162 C until it becomes a clear liquid occupying about 1/600th the "
  "volume of the gas - the technology that lets natural gas cross oceans "
  "without pipelines. LNG delivers about 22.2 megajoules per liter at "
  "0.45 kg/L: less per liter than diesel, but the established fuel of "
  "gas carriers, peak-shaving plants, and increasingly of ships and "
  "heavy trucks. The chain is liquefaction plant, insulated carrier "
  "ship, regasification terminal, pipeline - each link handling "
  "cryogenic liquid. LNG boils constantly (heat leaks in no matter how "
  "good the insulation), so tanks vent boil-off gas at roughly 0.1 "
  "percent per day, which ships burn as fuel - the cargo powers the "
  "voyage."),
 "how_it_works": ("Liquefaction is refrigeration at heroic scale: "
  "pretreated gas (water, CO2, and sulfur removed - they would freeze "
  "solid) is cooled in stages to minus 162 C. Storage uses double-walled "
  "insulated tanks; transport uses membrane or spherical Moss tanks on "
  "carriers that are among the largest ships afloat. The record explains "
  "the boil-off economy (0.1 percent per day sounds small; over a "
  "20-day voyage it is 2 percent of cargo - burned in the ship's engines "
  "as the cheapest fuel aboard), the regasification step (seawater or "
  "burners warm it back to gas for the pipeline), and the safety logic: "
  "LNG itself cannot explode as a liquid; the hazard is the cold (brittle "
  "steel, frostbite) and the vapor cloud if it spills and warms. As a "
  "vehicle fuel, LNG suits long-haul trucks and ships that can use a "
  "full tank before boil-off matters."),
 "key_points": [
  "LNG: methane at -162 C, 1/600th the gas volume; about 22.2 MJ/L.",
  "Chain: liquefaction, carrier ship, regasification terminal, pipeline.",
  "Boil-off about 0.1 percent/day; ships burn it as voyage fuel.",
  "Gas must be pretreated (water, CO2, sulfur removed) before liquefaction.",
  "Hazards are cryogenic cold and vapor clouds, not liquid explosion."],
 "requirements": [
  "Learner must compute the volume reduction and the energy in a stated LNG volume.",
  "Learner must compute boil-off loss over a stated voyage length.",
  "Learner must explain why pretreatment precedes liquefaction.",
  "Learner must describe the LNG safety logic (cold and vapor, not liquid explosion)."],
 "standards": [
  "LNG composition and interchangeability: national gas-quality specs.",
  "Carrier and terminal design: SIGTTO / industry guidelines.",
  "Cryogenic materials and insulation standards."],
 "citations": [
  "Society of International Gas Tanker and Terminal Operators (SIGTTO). LNG industry guidelines.",
  "U.S. DOE Energy Information Administration. Liquefied natural gas explained (liquefaction chain).",
  "Gary JH, Handwerk GE, Kaiser MJ. Petroleum Refining: Technology and Economics. 5th ed. CRC Press; 2007 (gas processing)."],
 "sig_lens": ("Signature reframing: the Signature Cold Chain Ledger "
  "follows every LNG molecule from wellhead to burner - liquefaction "
  "energy spent, boil-off burned, regas heat applied - so the delivered "
  "megajoule is fully costed. The Signature 1:600 rule is taught as the "
  "master ratio of gas logistics, and the Signature boil-off discipline "
  "(cargo as its own fuel, voyage planned around it) turns a loss into "
  "a designed feature of the system."),
},
{
 "key": "cng",
 "name": "CNG: natural gas under pressure",
 "group": "gaseous-fuels",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "description": ("Compressed natural gas (CNG) is pipeline gas squeezed "
  "to about 200-250 bar (3,000-3,600 psi) and stored in strong cylinders "
  "- the established vehicle fuel of city buses, refuse trucks, taxis, "
  "and fleet vans across much of the world. A gasoline-gallon-equivalent "
  "(GGE) of CNG is 5.66 pounds (about 2.57 kg) of gas, delivering the "
  "same energy as a gallon of gasoline; CNG's mass energy density is "
  "methane's 55.5 MJ/kg, but the heavy cylinders cut into the vehicle's "
  "effective efficiency. The fuel's virtues are price (often well below "
  "gasoline per GGE), clean combustion (about 53 kg CO2 per gigajoule, "
  "very low particulates), and domestic supply where gas is produced. "
  "The constraint is range: even at 250 bar, a practical tank holds the "
  "energy of a few gallons of gasoline."),
 "how_it_works": ("A CNG station is a compressor plus storage cascade: "
  "pipeline gas is dried, compressed in stages, and stored in high-"
  "pressure bottles; vehicles fill in minutes through a standardized "
  "nozzle. On board, a regulator drops pressure in two stages to feed "
  "the engine, which may be a converted gasoline engine (spark-ignited, "
  "slight power loss from the gaseous fuel displacing air) or a "
  "dedicated high-compression CNG engine. The record explains cylinder "
  "types (Type 1 all-steel through Type 4 plastic-lined composite - "
  "lighter and pricier as the number rises), the inspection regime "
  "(cylinders have a defined service life and periodic requalification), "
  "and the leak-safety logic: methane rises and disperses outdoors, so "
  "CNG is safer than gasoline in open air and demands ventilation "
  "indoors. Home refueling appliances (compressing overnight from the "
  "house gas line) are covered as the established niche solution."),
 "key_points": [
  "CNG: pipeline gas at 200-250 bar; 1 GGE = 5.66 lb of gas.",
  "Established fleet fuel: buses, refuse trucks, taxis, vans.",
  "Cylinders Type 1-4 (steel to composite); defined service life and requalification.",
  "Methane rises and disperses: safer than gasoline outdoors, ventilate indoors.",
  "Constraint is range: practical tanks hold a few GGE."],
 "requirements": [
  "Learner must convert a stated CNG mass to gasoline-gallon-equivalents.",
  "Learner must explain the cylinder type ladder and the weight tradeoff.",
  "Learner must describe the station cascade and the fill process.",
  "Learner must explain CNG leak behavior vs gasoline."],
 "standards": [
  "CNG fuel quality: SAE J1616 / national specs.",
  "Cylinder standards: NGV2 / ISO 11439; requalification intervals.",
  "Station and vehicle installation codes (NFPA 52)."],
 "citations": [
  "NFPA 52. Vehicular Natural Gas Fuel Systems Code.",
  "ISO 11439:2013. Gas cylinders - High pressure cylinders for the on-board storage of natural gas.",
  "U.S. DOE Alternative Fuels Data Center. Natural gas vehicles: CNG basics (GGE, stations)."],
 "sig_lens": ("Signature reframing: the Signature Pressure Ledger "
  "converts every CNG decision to GGE - price per GGE, range per GGE, "
  "cylinder weight per GGE - so gas competes with gasoline on one "
  "scale. The Signature cylinder ladder (type vs weight vs cost vs "
  "life) is the buying tool, and the Signature fleet rule is quantitative: "
  "CNG wins where daily mileage fits the tank and the station is on the "
  "route - the ledger proves it before the first cylinder is bought."),
},
{
 "key": "hydrogen-production",
 "name": "Hydrogen production: steam methane reforming",
 "group": "hydrogen",
 "ladder_rank": 24, "ladder_tier": "compounded",
 "description": ("Almost all the world's hydrogen today - tens of "
  "millions of tonnes per year - is made by steam methane reforming "
  "(SMR): natural gas plus high-temperature steam becomes hydrogen plus "
  "carbon dioxide. This is the established production method, feeding "
  "refineries (desulfurization, hydrocracking) and ammonia/fertilizer "
  "plants. The chemistry is CH4 + 2H2O -> CO2 + 4H2: in theory 2 "
  "kilograms of methane yield 1 kilogram of hydrogen; in practice, with "
  "heat and efficiency losses, about 3 to 4 kilograms of gas make a "
  "kilogram of hydrogen, releasing roughly 9 to 10 kilograms of CO2 per "
  "kilogram of H2 - the 'grey hydrogen' footprint. Adding carbon capture "
  "makes 'blue' hydrogen; electrolyzing water with clean electricity "
  "makes 'green' hydrogen - the colors are industry shorthand for "
  "production carbon intensity, and this record keeps them distinct."),
 "how_it_works": ("An SMR plant runs in three stages: reforming (methane "
  "and steam over a nickel catalyst at 700-900 C and 15-30 bar make "
  "syngas), shift conversion (carbon monoxide plus more steam becomes "
  "more hydrogen plus CO2), and purification (pressure-swing adsorption "
  "delivers 99.9 percent-plus hydrogen). The record works the mass and "
  "carbon balance end to end: per kilogram of hydrogen, about 5.5 kg of "
  "CO2 is stoichiometric and 9-10 kg is real-world including fuel burned "
  "for heat. It explains why refineries are the anchor customers "
  "(hydrogen strips sulfur from diesel and cracks heavy oil - hydrogen "
  "is already a fuel-industry feedstock), what carbon capture changes "
  "(capturing 60-90 percent of the CO2 at an energy cost), and why "
  "electrolysis, though simple (water plus electricity), remains the "
  "minority route on cost - about 50-55 kWh of electricity per kilogram "
  "of hydrogen at typical electrolyzer efficiency."),
 "key_points": [
  "SMR (CH4 + 2H2O -> CO2 + 4H2) makes nearly all the world's hydrogen today.",
  "Real-world: ~3-4 kg methane and ~9-10 kg CO2 per kg of grey hydrogen.",
  "Anchor customers are refineries (desulfurization, hydrocracking) and ammonia plants.",
  "Blue = SMR plus carbon capture; green = water electrolysis with clean power.",
  "Electrolysis needs about 50-55 kWh per kg H2 at typical efficiency."],
 "requirements": [
  "Learner must balance the SMR equation and compute the theoretical methane and CO2 per kg H2.",
  "Learner must explain the three SMR stages in order.",
  "Learner must distinguish grey, blue, and green hydrogen precisely.",
  "Learner must compute electrolysis electricity for a stated hydrogen mass."],
 "standards": [
  "Hydrogen purity: ISO 14687 (fuel-cell grade).",
  "SMR plant safety: hydrogen production codes and pressure-vessel rules.",
  "Carbon-intensity accounting: emerging clean-hydrogen standards."],
 "citations": [
  "Rosen MA, Koohi-Fayegh S. The prospects for hydrogen as an energy carrier: an overview of hydrogen energy and hydrogen energy systems. Energy. 2016;98:5-20.",
  "U.S. DOE. Hydrogen Production: Natural Gas Reforming (SMR process description and efficiencies).",
  "Thomas CE. Fuel Cell and Battery Electric Vehicles Compared. DOE; 2009 (hydrogen production routes)."],
 "sig_lens": ("Signature reframing: the Signature Hydrogen Ledger "
  "prices every kilogram of hydrogen three ways - dollars, megajoules "
  "in, and kilograms of CO2 out - so grey, blue, and green are compared "
  "on one page instead of by color marketing. The Signature SMR balance "
  "(mass in, mass out, carbon accounted) is taught as the template for "
  "auditing any fuel plant, and the Signature color decoder strips the "
  "shorthand back to measured carbon intensity before any buying "
  "decision."),
},
]

ENTRIES += [
{
 "key": "hydrogen-use",
 "name": "Hydrogen use: storage, handling, and fuel cells",
 "group": "hydrogen",
 "ladder_rank": 25, "ladder_tier": "compounded",
 "description": ("Using hydrogen as a fuel means solving its storage "
  "problem: at 120 megajoules per kilogram (lower heating value) it is "
  "the most energy-dense fuel by mass ever used, but at room conditions "
  "a kilogram occupies 11 cubic meters - so every application is a "
  "packaging technology. Established practice compresses it to 350 or "
  "700 bar for vehicles (about 5.6 MJ/L at 700 bar), liquefies it at "
  "minus 253 C for rockets and bulk transport (about 8.5 MJ/L), or binds "
  "it in metal hydrides and liquid carriers for niche uses. Handling "
  "rules are strict because hydrogen's flammability range is enormous "
  "(4 to 75 percent in air), its ignition energy tiny, and its flame "
  "nearly invisible. The established end uses are refining, ammonia, "
  "methanol, fuel-cell vehicles and forklifts, backup power, and above "
  "all rocketry - liquid hydrogen plus liquid oxygen remains the "
  "highest-performing chemical rocket propellant combination."),
 "how_it_works": ("A proton-exchange-membrane fuel cell turns hydrogen "
  "into electricity without burning: hydrogen splits into protons and "
  "electrons at the anode, protons cross the membrane, electrons drive "
  "the external circuit, and they recombine with oxygen to make water - "
  "about 50-60 percent efficient, roughly double a combustion engine. "
  "The record explains the storage ladder (compressed gas: simple, "
  "heavy tanks; liquid: dense, boils off about 1-3 percent per day; "
  "hydrides and LOHC carriers: dense and safe, heavy and costly), the "
  "compression energy tax (compressing to 700 bar costs roughly 10-15 "
  "percent of the hydrogen's energy), and the safety engineering that "
  "makes it workable: ventilation (hydrogen rises fast), no ignition "
  "sources, leak detection, and materials chosen against embrittlement "
  "(hydrogen cracks many steels). Forklift fleets are presented as the "
  "quiet established success - indoor, fast refueling, zero local "
  "emissions."),
 "key_points": [
  "Hydrogen: 120 MJ/kg by mass, but 11 cubic meters per kg at room conditions - storage is the technology.",
  "700-bar compressed: ~5.6 MJ/L; liquid at -253 C: ~8.5 MJ/L.",
  "Flammability 4-75 percent in air; tiny ignition energy; nearly invisible flame.",
  "PEM fuel cells: ~50-60 percent efficient, water as the only exhaust.",
  "Established uses: refining, ammonia, forklifts, backup power, rockets."],
 "requirements": [
  "Learner must rank hydrogen storage methods by volumetric density with numbers.",
  "Learner must explain the compression energy tax quantitatively.",
  "Learner must describe the fuel-cell reaction in words (anode, membrane, cathode).",
  "Learner must state the three key hydrogen hazards and their countermeasures."],
 "standards": [
  "Hydrogen fuel quality: ISO 14687.",
  "Fueling: SAE J2601; storage vessels: ISO 19881.",
  "Hydrogen safety: ISO/TR 15916; ventilation and detection practice."],
 "citations": [
  "Rosen MA, Koohi-Fayegh S. The prospects for hydrogen as an energy carrier. Energy. 2016;98:5-20.",
  "Thomas CE. Fuel Cell and Battery Electric Vehicles Compared. DOE; 2009 (fuel-cell efficiency and storage).",
  "ISO/TR 15916:2015. Basic considerations for the safety of hydrogen systems."],
 "sig_lens": ("Signature reframing: the Signature Storage Ladder ranks "
  "every hydrogen packaging method on one scale - MJ/L, energy tax, "
  "boil-off or weight penalty, and hazard class - so the application "
  "picks the package, not the fashion. The Signature hydrogen safety "
  "protocol (ventilate up, detect early, embrittlement-proof materials) "
  "is taught as non-negotiable engineering, and the Signature "
  "forklift-first rule advises proving hydrogen indoors at small scale "
  "before betting a fleet on it."),
},
{
 "key": "uranium-natural",
 "name": "Natural uranium: the nuclear fuel starting point",
 "group": "nuclear-fuels",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "description": ("Natural uranium is the mined starting point of the "
  "nuclear fuel chain: a dense grey metal (19.1 g/cm3, denser than lead) "
  "whose atoms are 99.27 percent uranium-238 and 0.71 percent "
  "uranium-235 - and only the U-235 splits easily in a thermal reactor. "
  "A kilogram of natural uranium therefore holds about 7.1 grams of the "
  "fissile isotope, yet that tiny fraction is the seed of enormous "
  "energy: fully fissioned, a kilogram of U-235 releases about 82 "
  "terajoules (about 24 million kWh of heat). Uranium is mined in "
  "Kazakhstan, Canada, Australia, and Namibia above all, milled to "
  "yellowcake (U3O8), and converted to uranium hexafluoride (UF6) for "
  "enrichment. It is an established fuel in the strictest sense: "
  "hundreds of reactors in more than 30 countries run on its refined "
  "descendants, supplying about a tenth of world electricity."),
 "how_it_works": ("Mining takes two main forms: open-pit/underground "
  "mining of ore, and in-situ leaching (pumping chemistry through the "
  "orebody and recovering dissolved uranium - now the dominant method). "
  "Milling crushes and leaches the ore to yellowcake; conversion turns "
  "it into UF6 gas, the only uranium compound volatile enough for the "
  "enrichment step. The record explains the isotope physics plainly: "
  "U-235 fissions when struck by a slow neutron, releasing 2-3 more "
  "neutrons plus about 200 MeV - the chain reaction is neutron "
  "bookkeeping, and natural uranium's 0.71 percent is too dilute to "
  "sustain it in ordinary water-moderated reactors, which is why "
  "enrichment (or heavy-water designs like CANDU) is required. "
  "Radiation basics are covered honestly: uranium is primarily an alpha "
  "emitter and a heavy-metal chemical hazard; the radiation fear "
  "surrounding the un-enriched material is disproportionate to the "
  "measured dose."),
 "key_points": [
  "Natural uranium: 99.27 percent U-238, 0.71 percent U-235; only U-235 fissions easily.",
  "1 kg U-235 fissioned releases about 82 TJ (about 24 million kWh of heat).",
  "Chain: mining -> milling (yellowcake) -> conversion (UF6) -> enrichment.",
  "In-situ leaching is now the dominant mining method.",
  "Uranium metal: 19.1 g/cm3; mainly an alpha emitter and heavy-metal hazard."],
 "requirements": [
  "Learner must compute the U-235 mass in a stated mass of natural uranium.",
  "Learner must explain why 0.71 percent cannot sustain a chain reaction in light water.",
  "Learner must order the front-end fuel-cycle steps.",
  "Learner must state the energy of 1 kg fissioned U-235 in TJ and kWh."],
 "standards": [
  "Uranium concentrate specifications: ASTM C967.",
  "Conversion and UF6 handling: ASTM C996.",
  "Mining and milling radiation protection: IAEA safety standards."],
 "citations": [
  "Glasstone S, Sesonske A. Nuclear Reactor Engineering. 4th ed. Springer; 1994 (isotope physics, chain reaction).",
  "OECD Nuclear Energy Agency / IAEA. Uranium: Resources, Production and Demand (mining and milling).",
  "ASTM C967-13. Standard Specification for Uranium Ore Concentrate."],
 "sig_lens": ("Signature reframing: the Signature Isotope Ledger starts "
  "every nuclear calculation at 0.71 percent - the Signature habit of "
  "beginning at the ore, not the reactor, so enrichment is understood "
  "as concentration, not magic. The Signature 82-terajoule anchor (one "
  "kilogram of U-235) is the energy reference against which every "
  "chemical fuel is measured and found wanting by a factor of millions. "
  "The Signature dose-honesty rule states measured radiation facts "
  "before addressing fears."),
},
{
 "key": "uranium-enriched",
 "name": "Enriched uranium: pellets and fuel assemblies",
 "group": "nuclear-fuels",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "description": ("Enriched uranium is natural uranium concentrated from "
  "0.71 percent U-235 to the 3-5 percent used in power reactors - still "
  "overwhelmingly U-238, but now rich enough to sustain a chain reaction "
  "in ordinary water. The finished fuel is unglamorous and precise: "
  "uranium dioxide (UO2) powder pressed into ceramic pellets about the "
  "size of a fingertip, stacked in zirconium-alloy tubes, bundled into "
  "assemblies of 200-plus rods that stand about four meters tall. A "
  "single pellet holds roughly the energy of a tonne of coal; a reactor "
  "core holds tens of thousands of them. At typical burnup (about 50 "
  "gigawatt-days per tonne), a kilogram of enriched uranium yields "
  "roughly 1,200 megawatt-hours of heat - about 400 MWh of electricity - "
  "before it is discharged as spent fuel."),
 "how_it_works": ("Enrichment exploits the tiny mass difference between "
  "U-235 and U-238: modern plants spin UF6 gas in centrifuge cascades, "
  "thousands of stages, each nudging the U-235 fraction upward while the "
  "depleted remainder ('tails', about 0.25 percent U-235) is stockpiled. "
  "The record works the feed arithmetic: making 1 kg of 4-percent "
  "enriched uranium takes about 8 kg of natural-uranium feed. Fabrication "
  "is powder metallurgy - UO2 powder pressed, sintered at 1,700 C into "
  "ceramic, ground to tolerance, loaded into cladding tubes backfilled "
  "with helium, sealed, and assembled. In the reactor, each fission "
  "releases about 200 MeV; the pellets run at centerline temperatures "
  "above 1,000 C while water coolant keeps the cladding near 300 C - "
  "that temperature drop across millimeters of ceramic is the thermal "
  "engineering of nuclear fuel."),
 "key_points": [
  "Power-reactor enrichment: 3-5 percent U-235 (up from 0.71 percent natural).",
  "Fuel form: UO2 ceramic pellets in zirconium tubes, bundled into assemblies.",
  "One pellet holds roughly the energy of a tonne of coal.",
  "About 8 kg of natural feed per kg of 4-percent enriched uranium.",
  "1 kg enriched U at 50 GWd/t yields about 1,200 MWh of heat."],
 "requirements": [
  "Learner must compute the feed-to-product ratio for a stated enrichment.",
  "Learner must describe the pellet-to-assembly fabrication chain.",
  "Learner must compute the electricity from a stated mass of enriched uranium at stated burnup.",
  "Learner must explain the centrifuge enrichment principle."],
 "standards": [
  "Fuel pellet specifications: ASTM C776 (UO2 pellets).",
  "Cladding: zirconium alloy specifications (ASTM B811).",
  "Enrichment plant safeguards: IAEA safeguards agreements."],
 "citations": [
  "Glasstone S, Sesonske A. Nuclear Reactor Engineering. 4th ed. Springer; 1994 (enrichment, fuel design, burnup).",
  "ASTM C776-17. Standard Specification for Sintered Uranium Dioxide Pellets.",
  "OECD Nuclear Energy Agency. Nuclear Fuel Cycle data (feed factors, burnup)."],
 "sig_lens": ("Signature reframing: the Signature Pellet Standard - one "
  "pellet, one tonne of coal - is the most concentrated energy fact in "
  "this database, taught as the anchor for all energy-density thinking. "
  "The Signature feed ledger (8 kg in, 1 kg out, tails accounted) makes "
  "enrichment a visible mass balance, and the Signature fabrication "
  "chain (powder to pellet to rod to assembly) is presented as the "
  "precision-manufacturing counterpart to the refinery's bulk chemistry."),
},
{
 "key": "nuclear-fuel-cycle",
 "name": "The nuclear fuel cycle: mine to reactor to storage",
 "group": "nuclear-fuels",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "description": ("The nuclear fuel cycle is the full industrial system "
  "behind nuclear fuel: mining, milling, conversion, enrichment, "
  "fabrication, reactor irradiation, then spent-fuel storage and either "
  "direct disposal or reprocessing. The 'front end' (mine to fresh fuel) "
  "is established chemistry and manufacturing; the 'back end' (spent "
  "fuel) is the system's defining challenge. A typical 1-gigawatt "
  "reactor discharges about 20-25 tonnes of spent fuel per year - "
  "intensely radioactive when fresh, cooling in pools for years, then "
  "moving to dry-cask storage: massive steel-and-concrete casks that "
  "cool passively for decades. Spent fuel is about 95 percent unused "
  "uranium plus about 1 percent plutonium and 3-4 percent fission "
  "products; reprocessing (established in France, the UK, Russia, and "
  "Japan) recovers the uranium and plutonium as new fuel, shrinking the "
  "high-level waste volume dramatically."),
 "how_it_works": ("In the reactor, U-235 fissions while U-238 partly "
  "converts to plutonium-239 (which also fissions - about a third of a "
  "reactor's energy comes from bred plutonium). After 3-5 years the "
  "assembly is 'spent': fission products poison the chain reaction even "
  "though most uranium remains. The record follows the back end step by "
  "step - pool cooling (water shields radiation and carries decay heat), "
  "dry-cask loading (typically after 5-10 years), and the two national "
  "strategies: the once-through cycle (US, Sweden - spent fuel as waste "
  "to a geological repository) versus the closed cycle (France, Japan - "
  "reprocess, recycle, vitrify the remainder). It states the waste "
  "honesty plainly: high-level waste stays hazardous for thousands of "
  "years, but its total volume is tiny - all the spent fuel from decades "
  "of US nuclear power would fit on a single football field stacked "
  "meters deep - and geological repositories (Finland's Onkalo, "
  "operating) are the engineered answer."),
 "key_points": [
  "Front end: mine, mill, convert, enrich, fabricate. Back end: cool, store, dispose or reprocess.",
  "A 1-GW reactor discharges about 20-25 tonnes of spent fuel per year.",
  "Spent fuel: ~95 percent unused uranium, ~1 percent plutonium, fission products.",
  "About a third of reactor energy comes from bred plutonium-239.",
  "Back-end strategies: once-through (US) vs closed cycle with reprocessing (France, Japan)."],
 "requirements": [
  "Learner must order the full fuel-cycle steps front end to back end.",
  "Learner must explain where the reactor's plutonium comes from and its energy share.",
  "Learner must compare once-through and closed-cycle strategies.",
  "Learner must state the spent-fuel volume fact and the repository answer."],
 "standards": [
  "Spent-fuel storage: 10 CFR Part 72 (US dry-cask licensing).",
  "Transport: 10 CFR Part 71 / IAEA SSR-6.",
  "Geological disposal: national repository licensing (e.g., Finland STUK)."],
 "citations": [
  "Glasstone S, Sesonske A. Nuclear Reactor Engineering. 4th ed. Springer; 1994 (fuel cycle, burnup, reprocessing).",
  "IAEA. Nuclear Fuel Cycle Information System (front-end and back-end data).",
  "U.S. NRC. 10 CFR Part 72: Licensing Requirements for Dry Storage of Spent Nuclear Fuel."],
 "sig_lens": ("Signature reframing: the Signature Cycle Map draws the "
  "whole fuel system as one loop - mine to reactor to cask to "
  "repository or recycle - with mass and radioactivity accounted at "
  "every gate, the Signature discipline of never losing track of "
  "material. The Signature waste-volume truth (football field, meters "
  "deep, decades of US power) replaces vague dread with a measured "
  "engineering problem, and the Signature strategy ledger compares "
  "once-through and closed-cycle nations on cost, waste, and "
  "proliferation controls side by side."),
},
{
 "key": "naphtha",
 "name": "Naphtha and refinery streams",
 "group": "refining-systems",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "description": ("Naphtha is the refinery's versatile middle child: the "
  "light distillate cut boiling roughly between 30 and 180 C, too light "
  "for diesel and too heavy for gases, and the feedstock for half the "
  "modern world. Light naphtha goes to isomerization and gasoline "
  "blending; heavy naphtha goes to the catalytic reformer, which "
  "rearranges its molecules into high-octane reformate and - crucially - "
  "releases hydrogen as a byproduct, making the refinery partly "
  "self-sufficient in hydrogen. Naphtha is also the primary feedstock "
  "for ethylene crackers: the plastics, fibers, and chemicals of modern "
  "life begin as naphtha. It delivers about 31-32 megajoules per liter. "
  "As a fuel itself it is a solvent and a blending component; its "
  "importance is as the system's hinge between fuels and chemicals."),
 "how_it_works": ("The atmospheric column cuts naphtha as the fraction "
  "boiling just above gases and just below kerosene. The record follows "
  "the three great naphtha roads: (1) the reformer - heavy naphtha over "
  "platinum catalyst at 500 C becomes aromatics-rich reformate (octane "
  "90-100) plus hydrogen; (2) the cracker - naphtha steam-cracked at "
  "800 C shatters into ethylene, propylene, and butadiene for "
  "petrochemicals; (3) the gasoline pool - light naphtha isomerized from "
  "straight chains to branched (octane jump) and blended. The hydrogen "
  "link is the elegant part: the reformer makes hydrogen the refinery's "
  "desulfurizers and hydrocrackers consume - one unit's byproduct is "
  "another's feedstock, the refinery as an integrated system in "
  "miniature. The demo works a typical crude assay: about 15-25 percent "
  "of a barrel arrives as naphtha-range material, and the record shows "
  "where every liter goes."),
 "key_points": [
  "Naphtha: the 30-180 C cut; about 31-32 MJ/L; the refinery's hinge between fuels and chemicals.",
  "Heavy naphtha to the reformer: high-octane reformate plus byproduct hydrogen.",
  "Naphtha to the steam cracker: ethylene, propylene - the start of plastics.",
  "Light naphtha: isomerized and blended into gasoline.",
  "Refinery hydrogen integration: reformer byproduct feeds desulfurizers."],
 "requirements": [
  "Learner must name the three great naphtha roads and their products.",
  "Learner must explain the reformer hydrogen link to desulfurization.",
  "Learner must compute naphtha volume from a stated crude assay.",
  "Learner must explain isomerization's octane effect."],
 "standards": [
  "Naphtha cut definitions: refinery assay practice (TBP curves).",
  "Reformer feed specifications (industry practice).",
  "Steam-cracker feed quality requirements."],
 "citations": [
  "Gary JH, Handwerk GE, Kaiser MJ. Petroleum Refining: Technology and Economics. 5th ed. CRC Press; 2007 (naphtha processing, reforming, cracking).",
  "Speight JG. Handbook of Petroleum Product Analysis. 2nd ed. Wiley; 2015 (naphtha characterization).",
  "ASTM D86: distillation of petroleum products (cut definitions)."],
 "sig_lens": ("Signature reframing: the Signature Hinge Model teaches "
  "naphtha as the molecule that chose both careers - fuel and chemical "
  "- with the refinery routing each barrel to the highest value. The "
  "Signature hydrogen loop (reformer makes it, hydrotreater spends it) "
  "is presented as the template for industrial symbiosis: design units "
  "whose wastes feed each other. The Signature assay ledger converts "
  "every crude offer into naphtha, distillate, and residual fractions "
  "before price is discussed."),
},
{
 "key": "refinery",
 "name": "The refinery: crude oil distilled into fuels",
 "group": "refining-systems",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "description": ("The refinery is the largest fuel-manufacturing system "
  "on Earth: crude oil in, gasoline, diesel, jet fuel, heating oil, "
  "asphalt, and petrochemical feedstocks out - hundreds of thousands of "
  "barrels per day through a single plant. The master step is "
  "atmospheric distillation: crude heated to about 400 C enters a tower "
  "50-plus meters tall, and fractions condense at trays by boiling "
  "point - gases off the top, naphtha, kerosene, diesel down the sides, "
  "residual out the bottom. But distillation alone yields too much heavy "
  "fuel and too little gasoline for the market, so conversion units "
  "rebuild the molecules: fluid catalytic cracking shatters heavy gas "
  "oil into gasoline, hydrocracking adds hydrogen to make diesel and "
  "jet, coking turns the bottom of the barrel into lighter products "
  "plus solid coke. A modern refinery is less a distillery than a "
  "molecule-rebuilding factory tuned daily to the market's fuel slate."),
 "how_it_works": ("The record walks a barrel through the plant in order: "
  "desalting, atmospheric distillation (the primary cut), vacuum "
  "distillation of the residual (recovering more distillate under "
  "reduced pressure), then the conversion train - FCC, hydrocracker, "
  "reformer, alkylation, isomerization - then treating (hydrodesulfur-"
  "ization strips sulfur to meet clean-fuel rules) and finally blending "
  "to specification. The key insight is the yield shift: simple "
  "distillation of typical crude gives maybe 20 percent gasoline, but "
  "a complex refinery delivers 45-50 percent gasoline plus diesel and "
  "jet by cracking the heavies. The demo runs the mass balance - cuts "
  "summing to 100 percent of the barrel - and the economics in one line: "
  "the crack spread (product value minus crude cost) is the refinery's "
  "pulse, and complexity (Nelson index) is its fitness for heavy, sour "
  "crudes."),
 "key_points": [
  "Master step: atmospheric distillation near 400 C in a 50-meter tower, fractions by boiling point.",
  "Distillation alone mismatches the market; conversion units (FCC, hydrocracker, coker) rebuild molecules.",
  "Complex refineries shift yield to 45-50 percent gasoline from ~20 percent natural.",
  "Hydrodesulfurization strips sulfur to meet clean-fuel specifications.",
  "The crack spread (products minus crude) is the refinery's economic pulse."],
 "requirements": [
  "Learner must order the barrel's path through the refinery's major units.",
  "Learner must explain why conversion units exist (yield vs market mismatch).",
  "Learner must run the cut mass balance summing to 100 percent.",
  "Learner must explain the crack spread in one sentence."],
 "standards": [
  "Distillation cut definitions: ASTM D86 / D1160.",
  "Clean-fuel sulfur limits: e.g., 10-15 ppm diesel/gasoline specs by jurisdiction.",
  "Refinery complexity: Nelson Complexity Index (industry measure)."],
 "citations": [
  "Gary JH, Handwerk GE, Kaiser MJ. Petroleum Refining: Technology and Economics. 5th ed. CRC Press; 2007 (full refinery flow).",
  "Speight JG. The Refinery of the Future. 2nd ed. Elsevier; 2020 (conversion units).",
  "ASTM D86-20b. Standard Test Method for Distillation of Petroleum Products at Atmospheric Pressure."],
 "sig_lens": ("Signature reframing: the Signature Barrel Ledger follows "
  "one barrel from dock to pump - every cut weighed, every conversion "
  "unit's yield shift priced, the crack spread computed daily. The "
  "Signature molecule-rebuilding principle (distillation separates what "
  "is there; conversion makes what the market wants) is taught as the "
  "master distinction of fuel manufacturing, and the Signature "
  "complexity rule states it plainly: complexity is the refinery's "
  "fitness for cheap, heavy, sour crude."),
},
{
 "key": "blending",
 "name": "Fuel blending and additives: the finished-fuel system",
 "group": "refining-systems",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "description": ("No refinery stream is a finished fuel: gasoline, diesel, "
  "and jet fuel are all assembled by blending - the final manufacturing "
  "system that turns refinery streams into specification products. "
  "Gasoline blending mixes reformate, alkylate, isomerate, FCC gasoline, "
  "and butane to hit octane, volatility, and distillation targets "
  "simultaneously; the blender solves it as a constrained optimization, "
  "often by linear programming, because every stream has a price and "
  "every specification is a constraint. Then comes the additive package: "
  "detergents and deposit-control additives (required in US gasoline), "
  "antioxidants, corrosion inhibitors, lubricity improvers for diesel, "
  "static dissipators and icing inhibitors for jet fuel, cold-flow "
  "improvers for winter diesel - each dosed in parts per million, each "
  "doing a job no bulk stream can do. Blending is where the refinery's "
  "chemistry becomes the driver's fuel."),
 "how_it_works": ("The record teaches blending as math first: to first "
  "order, blend properties are volume-weighted averages, so hitting 87 "
  "AKI from 93-octane reformate and 83-octane naphtha is a two-equation "
  "solve - the demo does exactly this. Real blenders add the "
  "nonlinearities (octane blending is not perfectly linear; the "
  "blender's model corrects it) and the giveaway concept: every barrel "
  "blended above specification is quality given away for free, so the "
  "optimizer rides the specification limits. The additive tour covers "
  "each package's job: detergents keep intake valves clean, lubricity "
  "additives protect diesel pumps after sulfur removal, jet-fuel icing "
  "inhibitor keeps filters ice-free at altitude, and marker dyes enforce "
  "tax law (red for off-road diesel and heating oil). Ethanol and "
  "biodiesel enter at the terminal rack - splash-blended into the "
  "finished fuel on the way to the truck."),
 "key_points": [
  "Finished fuels are assembled by blending streams to specification targets.",
  "Blending is constrained optimization: stream prices vs specification limits; excess quality is giveaway.",
  "Additive packages (ppm doses): detergents, lubricity, antioxidants, icing inhibitors, dyes.",
  "Octane blending is volume-weighted to first order; real blenders correct the nonlinearities.",
  "Biofuels enter at the terminal rack, splash-blended into finished fuel."],
 "requirements": [
  "Learner must solve a two-stream octane blend for the volume ratio.",
  "Learner must explain the giveaway concept in blending economics.",
  "Learner must name four additive types and the job each does.",
  "Learner must explain why biofuels blend at the terminal, not the refinery."],
 "standards": [
  "Finished-fuel specifications: ASTM D4814 (gasoline), D975 (diesel), D1655 (jet).",
  "Additive certification: e.g., Top Tier detergent standards (industry).",
  "Dye and marker regulations for tax-distinguished fuels."],
 "citations": [
  "Gary JH, Handwerk GE, Kaiser MJ. Petroleum Refining: Technology and Economics. 5th ed. CRC Press; 2007 (blending and optimization).",
  "ASTM D4814-21c / D975-21 / D1655-22 (finished-fuel specifications).",
  "Heywood JB. Internal Combustion Engine Fundamentals. McGraw-Hill; 1988 (deposit and detergent effects)."],
 "sig_lens": ("Signature reframing: the Signature Blend Optimizer is "
  "taught as the purest applied math in the fuel business - prices, "
  "constraints, and one objective function, solved daily. The Signature "
  "giveaway rule (ride the spec, never donate quality) is the blender's "
  "profit discipline, and the Signature additive ledger lists every "
  "ppm-dose package as a line item with its job stated - no mystery "
  "ingredients, only specified chemistry at specified doses."),
},
{
 "key": "bunker",
 "name": "Bunker fuel: residual oil for ships",
 "group": "fuel-systems",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "description": ("Bunker fuel is the heavy residual oil that powers most "
  "of the world's merchant ships: the bottom of the refinery barrel, "
  "burned in giant two-stroke marine diesels that are the most efficient "
  "combustion engines ever built (over 50 percent thermal efficiency). "
  "The standard grades are IFO 180 and IFO 380 (intermediate fuel oils, "
  "viscosity 180/380 cSt at 50 C) and the heavier RMG/RMK residual grades "
  "under ISO 8217, delivering about 40-42 megajoules per liter at "
  "densities near 0.99 kg/L. A large container ship can burn 150-250 "
  "tonnes per day - fuel is the voyage's dominant cost. Handling is "
  "industrial: heated storage, centrifugal purifiers to strip water and "
  "sludge, and heated injection. The regulatory story is sulfur: the IMO "
  "2020 rule cut the global sulfur cap from 3.5 percent to 0.5 percent, "
  "forcing the fleet to low-sulfur fuel, scrubbers, or LNG."),
 "how_it_works": ("The record follows the fuel from bunker barge to "
  "propeller: heated settling tanks, purifiers spinning out water and "
  "catalytic fines (aluminum-silicon particles from the refinery's "
  "cat cracker that will destroy an engine if not removed - the fuel's "
  "most notorious contaminant), heated injection at the right viscosity "
  "(about 12-15 cSt at the injector, which for 380-cSt fuel means "
  "heating toward 140 C), and combustion in slow-speed two-strokes "
  "running at 60-100 RPM directly coupled to the propeller shaft. The "
  "demo works the voyage economics: tonnes per day times days times "
  "price per tonne is the bunker bill, and the slow-steaming arithmetic "
  "(fuel burn rises roughly with the cube of speed - cutting speed 10 "
  "percent saves nearly 30 percent of fuel) that reshaped shipping "
  "economics. The IMO 2020 compliance trilemma - low-sulfur fuel vs "
  "scrubber vs LNG - is presented as a capital-vs-operating-cost "
  "decision with the numbers attached."),
 "key_points": [
  "Bunker fuel: residual oil (IFO 180/380, ISO 8217 RMG/RMK), about 40-42 MJ/L.",
  "Burned in slow-speed two-stroke marine diesels: 50%+ thermal efficiency.",
  "Handling: heated storage, centrifugal purifiers, heated injection (~140 C for 380 cSt).",
  "Catalytic fines are the notorious contaminant: purifiers must remove them.",
  "IMO 2020: sulfur cap 3.5% -> 0.5%; compliance is low-sulfur fuel, scrubbers, or LNG."],
 "requirements": [
  "Learner must compute a voyage bunker bill from burn rate, days, and price.",
  "Learner must explain the cube law of slow steaming with the 10-percent example.",
  "Learner must describe the purifier's job and the catalytic-fines hazard.",
  "Learner must state the IMO 2020 sulfur change and the three compliance paths."],
 "standards": [
  "ISO 8217: petroleum products - fuels (class F) for marine use.",
  "IMO MARPOL Annex VI: sulfur caps (0.50% global, 0.10% ECAs).",
  "Bunker quantity and quality: sampling and dispute practice."],
 "citations": [
  "ISO 8217:2017. Petroleum products - Fuels (class F) - Specifications of marine fuels.",
  "IMO. MARPOL Annex VI: Prevention of Air Pollution from Ships (2020 sulfur cap).",
  "Woodyard D. Pounder's Marine Diesel Engines and Gas Turbines. 9th ed. Butterworth-Heinemann; 2009 (marine fuel systems)."],
 "sig_lens": ("Signature reframing: the Signature Voyage Ledger makes "
  "the bunker bill the center of shipping economics - tonnes per day, "
  "dollars per tonne, speed cubed - with slow steaming presented as the "
  "highest-leverage fuel decision in transport. The Signature purifier "
  "protocol (heat, spin, verify - catalytic fines treated as guilty "
  "until proven innocent) is the machinery-protection discipline, and "
  "the Signature sulfur trilemma turns IMO 2020 into a capital-decision "
  "worksheet: fuel premium vs scrubber vs LNG conversion, all in "
  "dollars per tonne-mile."),
},
{
 "key": "storage-safety",
 "name": "Fuel storage, transport, and safety systems",
 "group": "fuel-systems",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "description": ("Every fuel is also a hazard system: storage, transport, "
  "and safety engineering are what let civilization keep millions of "
  "tonnes of flammable energy sitting quietly in tanks. The master "
  "variables are flash point (which fuels make ignitable vapor at "
  "ambient temperature), vapor density (whether leaked vapor rises or "
  "pools), and containment: double-walled tanks, secondary containment "
  "dikes sized to 110 percent of the largest tank, floating roofs on "
  "gasoline tanks to kill the vapor space, and pressure relief sized for "
  "fire exposure. Transport follows the same logic scaled up - pipeline, "
  "tanker truck (MC306/DOT406), rail tank car, and marine tanker, each "
  "with its placards, segregation rules, and emergency-response "
  "playbooks. The safety record of the system rests on one discipline "
  "above all: bonding and grounding to kill static sparks during "
  "transfer, because a flowing fuel is a Van de Graaff generator."),
 "how_it_works": ("The record builds the hazard assessment as a "
  "procedure: (1) classify the fuel (flash point, boiling range, vapor "
  "density, toxicity); (2) size the containment (dike at 110 percent, "
  "separation distances by code); (3) engineer the transfer (bonding "
  "cables first, then hoses; flow-rate limits to control static "
  "generation; bottom loading for gasoline to cut splash and vapor); "
  "(4) plan the emergency (foam for liquid-fuel fires - water spreads "
  "burning gasoline; containment booms for spills; evacuation distances "
  "from the Emergency Response Guidebook). It covers the classic "
  "accident mechanisms honestly - static discharge during tank-truck "
  "loading, vapor-cloud migration into ignition sources, overfill from "
  "failed level gauges (Buncefield, 2005, is the case study) - and the "
  "engineered answers: independent high-level alarms, automatic shutoff, "
  "and the management systems (process safety management) that keep "
  "procedures alive after the engineers go home."),
 "key_points": [
  "Master variables: flash point, vapor density, containment integrity.",
  "Secondary containment: dikes at 110 percent of the largest tank.",
  "Static electricity during transfer is the leading ignition source: bond and ground first.",
  "Foam for liquid-fuel fires; water spreads burning gasoline.",
  "Buncefield (2005) is the overfill case study: independent alarms and auto-shutoff are the answers."],
 "requirements": [
  "Learner must size a containment dike for a stated largest tank.",
  "Learner must order the safe transfer procedure (bond, hose, flow limits).",
  "Learner must explain why water is wrong for a gasoline fire.",
  "Learner must describe the Buncefield mechanism and its engineered fixes."],
 "standards": [
  "Flammable liquid storage: NFPA 30 / API 650 (tank design).",
  "Static control: API RP 2003 (protection against ignitions from static).",
  "Emergency response: DOT Emergency Response Guidebook."],
 "citations": [
  "NFPA 30. Flammable and Combustible Liquids Code (storage and containment).",
  "API RP 2003. Protection Against Ignitions Arising Out of Static, Lightning, and Stray Currents.",
  "UK Health and Safety Executive. The Buncefield Incident investigation reports (overfill mechanism)."],
 "sig_lens": ("Signature reframing: the Signature Hazard Ledger scores "
  "every fuel on flash point, vapor behavior, and toxicity before a "
  "single tank is sited - the hazard assessment as a one-page gate. The "
  "Signature transfer protocol (bond first, bottom-load, flow-limited, "
  "alarmed) is taught as a ritual that never gets skipped, and the "
  "Signature Buncefield rule is absolute: no tank fills without an "
  "independent high-level alarm and automatic shutoff, because gauges "
  "fail and gravity does not forgive."),
},
{
 "key": "energy-density",
 "name": "Energy density: comparing every fuel on one scale",
 "group": "fuel-systems",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "description": ("This record is the database's capstone: every "
  "established fuel ranked on the two scales that govern all fuel "
  "decisions - megajoules per kilogram and megajoules per liter. By "
  "mass, the ranking runs hydrogen (120 MJ/kg), methane (55.5), propane "
  "and gasoline (about 46), diesel and jet fuel (43-45), ethanol (26.8), "
  "methanol (19.9), dry wood (18-19), coal (24-33 by rank), and "
  "uranium-235 (82,000,000 MJ/kg - in a league of its own). By volume, "
  "the order scrambles: residual fuel oil and diesel (about 40-42 "
  "MJ/L) top the chemical fuels, gasoline and jet fuel follow (34-35), "
  "LNG (22), liquid hydrogen (8.5), and gaseous fuels at ambient "
  "pressure trail far behind. The framework's lesson is the selection "
  "rule: mass density picks aircraft and rocket fuels, volume density "
  "picks vehicle and ship fuels, and cost per megajoule - not price per "
  "gallon, tonne, or cubic meter - picks the winner in every honest "
  "comparison."),
 "how_it_works": ("The record builds the comparison as a repeatable "
  "method: (1) convert every fuel price to dollars per gigajoule "
  "delivered (price per unit divided by energy per unit, divided by the "
  "appliance efficiency); (2) rank by the density that the application "
  "constrains (a rocket is mass-limited, a car is volume-limited, a "
  "power station is cost-limited); (3) overlay the non-energy "
  "constraints - flash point, toxicity, sulfur, carbon intensity - that "
  "disqualify or tax each candidate. Worked examples carry the method: "
  "home heating (heating oil vs natural gas vs propane per delivered "
  "gigajoule), trucking (diesel vs CNG vs LNG per mile), and the "
  "gasoline-equivalent liter that lets any fuel quote its range in "
  "familiar units. The demo computes the full ranking table from the "
  "database's own numbers and verifies the capstone claims - diesel "
  "tops gasoline per liter, hydrogen tops everything per kilogram, "
  "uranium tops everything by millions - so the framework is "
  "machine-checked, not asserted."),
 "key_points": [
  "Two scales govern fuel choice: MJ/kg (mass-limited applications) and MJ/L (volume-limited).",
  "By mass: hydrogen 120 MJ/kg leads chemical fuels; U-235 at 82 TJ/kg leads absolutely.",
  "By volume: residual oil and diesel (~40-42 MJ/L) lead; gaseous fuels trail far behind.",
  "Honest comparison is cost per delivered gigajoule, not price per gallon or tonne.",
  "The framework adds non-energy constraints: flash point, toxicity, sulfur, carbon intensity."],
 "requirements": [
  "Learner must reproduce the mass-density ranking of the major fuels from memory.",
  "Learner must reproduce the volume-density ranking and explain the scramble.",
  "Learner must convert any fuel price to dollars per delivered gigajoule.",
  "Learner must select a fuel for a stated application using the framework's three steps."],
 "standards": [
  "Energy units: SI joules; heating values HHV/LHV distinguished.",
  "Gasoline-equivalent conversions: energy-basis comparisons.",
  "Lifecycle carbon intensity: gCO2e/MJ conventions."],
 "citations": [
  "U.S. DOE Energy Information Administration. Energy units and fuel heat contents (comparison data).",
  "Smil V. Energy and Civilization: A History. MIT Press; 2017 (energy density through history).",
  "Heywood JB. Internal Combustion Engine Fundamentals. McGraw-Hill; 1988 (fuel property comparisons)."],
 "sig_lens": ("Signature reframing: the Signature Fuel Selection "
  "Framework is the database's master tool - every fuel, two densities, "
  "one cost-per-gigajoule ledger, and the constraint overlay that "
  "disqualifies the unfit. The Signature rule is carved plainly: "
  "mass density flies, volume density drives, and dollars per "
  "gigajoule decide - everything else is commentary. The Signature "
  "capstone drill asks the learner to spec the fuel for a new "
  "application from a blank page using only this record."),
},
]
