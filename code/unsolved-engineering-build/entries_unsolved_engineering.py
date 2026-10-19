#!/usr/bin/env python3
"""Entries for the Unsolved Engineering databases (Manon 2026-10-17 16:15
orders, Unsolved Problems Solved series batch 1).

Verified 2026-10-17: whole-system dedupe sweep over the full manifest
(2,442 databases) plus the shared exact-title gate: 67 of 68 candidate
titles FREE; the single refusal, "Space-Based Solar Power" (already in the
futurology database as JAH-FUT-0000061), was renamed to the gate-verified
free title "Orbital Solar Power Stations". All 68 final titles (34 public +
34 " (Signature Edition)") are gate-clean.

Two NEW databases, 34 ladder-ordered records each:

  unsolved-engineering            - The Unsolved Engineering Database
                                    (public-harvest: real, fact-checked
                                    famous unsolved engineering problems -
                                    energy, materials, transport,
                                    environment, and space - every record
                                    carrying the problem statement, its
                                    history, why it matters, and a short
                                    pointer to the Signature proposed
                                    solution; civilian problems only)
  unsolved-engineering-signature  - The Unsolved Engineering Signature
                                    Database
                                    (his original Signature Engineering
                                    Method applied to the same 34 problems:
                                    every record carries the full
                                    Signature-generated proposed solution,
                                    opening with the exact honesty label,
                                    laying out assumptions, reasoning path,
                                    proposed mechanism, confirm/kill
                                    evidence, and what it does NOT claim;
                                    src signature, titles suffixed
                                    " (Signature Edition)", never presented
                                    as established science or authentic
                                    public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-34,
ladder_tier approachable/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-USEN- (public) and JAH-USENS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits).

Standing exclusion honored: nothing on neutralizing or defeating military
or defense-grade systems - every problem here is civilian (energy,
materials, transport, environment, space). No religious talk. Nothing
hate-adjacent, profane, or inappropriate.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_unsolved_engineering.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), walks
the Signature solution approach as a solution-explorer, and ends with the
OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature original - his original Signature Engineering Method "
            "applied to famous unsolved engineering problems: proposed "
            "solution approaches with stated assumptions, a reasoning path, "
            "a proposed mechanism, what evidence would confirm or kill the "
            "approach, and what it does not claim. Clearly labeled "
            "Signature-made, never presented as established science or "
            "authentic public record.")

CIT_IEA = ("International Energy Agency. Net Zero by 2050: A Roadmap for the "
           "Global Energy Sector. IEA; 2021, updated 2023.")
CIT_DOE_SHOT = ("U.S. Department of Energy. Energy Earthshots Initiative: "
                "Long Duration Storage Shot (90 percent cost reduction by "
                "2030), Hydrogen Shot, Carbon Negative Shot.")
CIT_IPCC = ("IPCC. Climate Change 2023: Synthesis Report. Contribution of "
            "Working Groups I, II and III to the Sixth Assessment Report.")
CIT_NACE = ("NACE International. International Measures of Prevention, "
            "Application, and Economics of Corrosion Technologies Study "
            "(IMPACT); 2016. Global cost of corrosion estimated at "
            "2.5 trillion US dollars, about 3.4 percent of global GDP.")
CIT_ESA_DEBRIS = ("European Space Agency. ESA Space Environment Report; "
                  "2024. About 36,500 tracked objects larger than 10 cm in "
                  "Earth orbit.")
CIT_NASA = ("National Aeronautics and Space Administration. Technology "
            "Roadmaps and Mars Design Reference Architecture 5.0.")
CIT_NIF = ("Lawrence Livermore National Laboratory. National Ignition "
           "Facility ignition announcement; December 2022. First laboratory "
           "fusion ignition: 3.15 MJ fusion output from 2.05 MJ laser input.")
CIT_ITER = ("ITER Organization. ITER Technical Basis and staged assembly "
            "schedule; Saint-Paul-lez-Durance.")
CIT_SUPERCON = ("Schilling A et al. Superconductivity above 130 K in the "
                "Hg-Ba-Ca-Cu-O system. Nature 363, 56-58; 1993. Drozdov AP "
                "et al. Superconductivity at 250 K in lanthanum hydride under "
                "high pressures. Nature 569, 528-531; 2019.")
CIT_DESAL = ("International Desalination Association. Desalination Yearbook "
             "and energy surveys: modern seawater reverse osmosis plants "
             "operate near 3 to 4 kWh per cubic meter.")
CIT_H2 = ("International Energy Agency. Global Hydrogen Review 2024: "
          "electrolytic hydrogen costs and efficiency ranges.")
CIT_SAF = ("International Air Transport Association. Sustainable Aviation "
           "Fuel fact sheets: SAF costs roughly two to four times fossil jet "
           "fuel; EU ReFuelEU Aviation mandate from 2025.")
CIT_GPGP = ("Lebreton L et al. Evidence that the Great Pacific Garbage Patch "
            "is rapidly accumulating plastic. Scientific Reports 8, 4666; "
            "2018. Estimated 80,000 tonnes over about 1.6 million square km.")
CIT_GEO = ("U.S. Department of Energy. GeoVision: Harnessing the Heat "
           "Beneath Our Feet; 2019. Enhanced geothermal systems and drilling "
           "cost analysis.")
CIT_BATTERY = ("BloombergNEF. Battery Price Survey 2024: lithium-ion pack "
               "prices near 115 to 150 US dollars per kWh at utility scale.")
CIT_AV = ("Kalra N, Paddock SM. Driving to Safety: How Many Miles of Driving "
          "Would It Take to Demonstrate Autonomous Vehicle Reliability? "
          "RAND Corporation; 2016.")
CIT_STARSHOT = ("Breakthrough Starshot initiative. System concept: gram-scale "
               "sail accelerated by ground-based laser array toward 0.2 c.")
CIT_SPS = ("Mankins JC. SPS-ALPHA: The First Practical Solar Power Satellite "
           "via Arbitrarily Large Phased Array. NASA Innovative Advanced "
           "Concepts final report; 2012.")

ENTRIES = [
    {
        "key": "grid_storage",
        "name": "Grid-Scale Long-Duration Energy Storage",
        "group": "Energy",
        "ladder_rank": 1,
        "ladder_tier": "approachable",
        "problem": (
            "How to store electricity cheaply enough, and for long enough, "
            "to run a power grid on mostly wind and solar. Short bursts of "
            "storage exist - lithium-ion batteries cover hours - but the grid "
            "needs days and weeks of backup for wind lulls and cloudy "
            "stretches, at a cost far below what batteries cost today."
        ),
        "background": (
            "Pumped hydro has stored grid energy since the 1890s and still "
            "provides most of the world storage capacity, but it needs the "
            "right mountains and valleys, and the good sites are taken. "
            "Lithium-ion prices fell roughly 90 percent from 2010 to 2024, "
            "which made 2-to-4-hour storage economic in many markets. "
            "Beyond about 8 to 10 hours, batteries get too expensive: you "
            "pay for energy capacity you rarely use. Dozens of alternatives "
            "are in development - flow batteries, compressed air, iron-air "
            "batteries, gravity storage, thermal storage in molten salt or "
            "hot rocks, green hydrogen - but none has yet delivered "
            "100-hour storage at the target cost in commercial operation. "
            "The U.S. Department of Energy Long Duration Storage Shot calls "
            "for a 90 percent cost reduction by 2030, which shows how far "
            "the field believes it still has to go. Utility-scale "
            "lithium-ion installations are commonly reported near 150 "
            "dollars per kWh of energy capacity, so a 72-hour wind lull "
            "on a 1 GW city load - 72 GWh of missing energy - prices out "
            "near 10.8 billion dollars in batteries at today costs."
        ),
        "why_it_matters": (
            "Wind and solar are now the cheapest new electricity in most of "
            "the world, but their variability is the ceiling on how far "
            "they can go. Cheap long-duration storage would let grids run "
            "80 to 100 percent on renewables without keeping fossil plants "
            "on standby. It is widely described as the single biggest "
            "engineering bottleneck between today electricity mix and a "
            "fully clean one."
        ),
        "sig_pointer": (
            "The Signature approach treats the storage problem as a time "
            "problem, not a chemistry problem: it pairs ultra-cheap "
            "abundant materials for the bulk of the energy with a small "
            "fast layer for the peaks, and sizes the system against real "
            "weather records instead of average days."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the binding constraint is "
            "cost per stored kilowatt-hour for durations over 24 hours, not "
            "round-trip efficiency, because curtailed renewable electricity "
            "is nearly free at the moments storage would charge. Step two, "
            "the reasoning path: separate the power machinery from the "
            "energy medium completely - the medium should be dirt, water, "
            "air, or iron, materials whose raw cost is measured in dollars "
            "per ton, not dollars per kilogram. Step three, the proposed "
            "mechanism: a hybrid yard with three layers - a shallow "
            "lithium-ion layer for seconds-to-hours smoothing, a bulk "
            "iron-air or thermal layer for the 10-to-100-hour band where "
            "the economics actually break today, and a seasonal layer of "
            "underground hydrogen or compressed air sized from thirty years "
            "of local weather data rather than from averages. Step four, "
            "what would confirm it: a pilot that rides through a real "
            "multi-day wind lull with metered cost below 20 dollars per "
            "kWh of installed energy capacity. Step five, what would kill "
            "it: if the bulk layer materials degrade faster than modeled, "
            "or if the balance-of-plant costs refuse to fall with scale. "
            "What this does not claim: it does not claim any new chemistry, "
            "any efficiency breakthrough, or that one technology wins - the "
            "claim is only that the architecture, matched to real weather, "
            "changes which costs matter."
        ),
        "citations": [CIT_DOE_SHOT, CIT_BATTERY, CIT_IEA],
    },
    {
        "key": "direct_air_capture",
        "name": "Direct Air Capture at Climate Scale",
        "group": "Environment",
        "ladder_rank": 2,
        "ladder_tier": "approachable",
        "problem": (
            "How to pull carbon dioxide straight out of ambient air at a "
            "price and scale that matters for the climate. The chemistry "
            "works - pilot plants do it today - but it costs hundreds of "
            "dollars per ton, while the atmosphere needs billions of tons "
            "removed per year to offset hard-to-abate emissions."
        ),
        "background": (
            "Carbon capture on smokestacks dates to the 1970s, but catching "
            "CO2 from air is far harder: air holds about 420 parts per "
            "million of CO2, roughly 300 times more dilute than flue gas. "
            "The first commercial direct air capture plants - Climeworks in "
            "Iceland, Carbon Engineering designs in Texas - proved the "
            "process end to end: fans, sorbent filters, heat to release the "
            "CO2, then mineralization in basalt or underground storage. "
            "Reported costs sit near 600 to 1000 dollars per ton, against "
            "a commonly cited target of 100 dollars per ton for "
            "climate relevance. The IPCC pathways that limit warming "
            "assume large-scale carbon removal in the second half of the "
            "century, yet the installed base today captures only thousands "
            "of tons per year against a need measured in gigatons."
        ),
        "why_it_matters": (
            "Some emissions - from aviation, shipping, cement, farming - "
            "have no clean substitute on the horizon, and past emissions "
            "stay in the sky for centuries. If removal stays expensive, "
            "those tons stay. If removal gets cheap, humanity gains a "
            "thermostat knob for the atmosphere instead of only an "
            "emissions brake."
        ),
        "sig_pointer": (
            "The Signature approach attacks the energy bill, not the "
            "sorbent: it co-locates capture with stranded renewable power "
            "that would otherwise be curtailed, and treats the captured "
            "CO2 as a feedstock for materials rather than a waste to bury."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the dominant cost is energy "
            "and heat, not the capture hardware, and the cheapest energy "
            "on any grid is the curtailed surplus that renewables throw "
            "away on windy sunny days. Step two, the reasoning path: a "
            "capture plant that only runs on surplus power can be built "
            "from cheaper, less efficient components, because its fuel is "
            "free - the optimization flips from efficiency to capital "
            "cost. Step three, the proposed mechanism: modular capture "
            "units sited at curtailed wind and solar farms, running "
            "intermittently on surplus, feeding CO2 into on-site "
            "mineralization using local basalt or industrial waste "
            "alkalinity, with the whole unit containerized so it ships "
            "like freight. Step four, what would confirm it: a "
            "full-year metered run showing capture cost tracking the "
            "local curtailment price curve downward, with third-party "
            "audit of every ton. Step five, what would kill it: if "
            "sorbent degradation under intermittent cycling erases the "
            "energy savings, or if mineralization kinetics at ambient "
            "temperature prove too slow outside volcanic regions. What "
            "this does not claim: it does not claim 100 dollars per ton "
            "today, and it does not claim capture substitutes for cutting "
            "emissions - it is framed strictly as the cleanup crew for "
            "the tons nothing else can reach."
        ),
        "citations": [CIT_IPCC, CIT_DOE_SHOT],
    },
    {
        "key": "desalination_energy",
        "name": "The Energy Cost of Desalination",
        "group": "Environment",
        "ladder_rank": 3,
        "ladder_tier": "approachable",
        "problem": (
            "How to turn seawater into fresh water without spending so much "
            "energy that only rich coastal regions can afford it. Modern "
            "reverse osmosis needs about 3 to 4 kilowatt-hours per cubic "
            "meter - near the thermodynamic limit for the separation "
            "itself - yet the full system cost keeps desalination out of "
            "reach for the places facing the worst water stress."
        ),
        "background": (
            "Thermal desalination - boiling seawater, as in multi-stage "
            "flash plants - dominated the Gulf states for decades at 10 to "
            "15 kWh per cubic meter or more. Reverse osmosis, pushing water "
            "through membranes at high pressure, cut that to a third and "
            "now supplies cities from Carlsbad to Tel Aviv to Perth. "
            "Membrane and energy-recovery advances have pushed large plants "
            "to about 3 kWh per cubic meter, and the theoretical minimum "
            "for seawater at 50 percent recovery is near 1 kWh per cubic "
            "meter, so the separation step has little headroom left. The "
            "remaining costs sit in intake, pretreatment, brine disposal, "
            "and the energy to run it all. Meanwhile aquifers keep falling "
            "from India to California, and brine concentrate - twice as "
            "salty as the sea - is an ecological problem with no settled "
            "answer."
        ),
        "why_it_matters": (
            "About two billion people live in water-stressed regions, and "
            "the oceans are effectively infinite. Cracking the cost of "
            "desalination would decouple civilization growth from rainfall "
            "luck - but only if the energy comes clean and the brine does "
            "not poison the coasts it is meant to serve."
        ),
        "sig_pointer": (
            "The Signature approach stops chasing the membrane limit and "
            "attacks the system around it: free waste heat for pretreatment, "
            "brine mining to turn the waste stream into revenue, and "
            "co-location with power plants so the energy is surplus, not "
            "purchased."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the membrane is already good "
            "enough, and the next halving of cost must come from everything "
            "around the membrane - energy sourcing, pretreatment, and "
            "brine. Step two, the reasoning path: treat the plant as a "
            "materials refinery that happens to make water, because brine "
            "contains magnesium, lithium traces, and salt worth money, "
            "which converts a disposal cost into a revenue line. Step "
            "three, the proposed mechanism: co-locate reverse osmosis with "
            "a thermal power or data-center site to harvest waste heat "
            "for feed preheating, run high-pressure pumps on dedicated "
            "off-peak renewables, and add a brine-mining stage that "
            "extracts magnesium hydroxide and table salt before the "
            "remainder is diffused offshore. Step four, what would confirm "
            "it: a plant-level audit showing water cost falling as brine "
            "revenues rise, with marine monitoring showing no brine "
            "damage zone. Step five, what would kill it: if brine mineral "
            "markets saturate at the first few plants, or if biofouling "
            "under waste-heat preheating wipes out the membrane gains. "
            "What this does not claim: it does not claim to beat the "
            "thermodynamic limit, and it does not claim desalination can "
            "replace watershed stewardship - it is framed as a drought "
            "backstop, not a license to drain aquifers."
        ),
        "citations": [CIT_DESAL, CIT_IPCC],
    },
    {
        "key": "green_steel",
        "name": "Green Steel at Cost Parity",
        "group": "Materials",
        "ladder_rank": 4,
        "ladder_tier": "approachable",
        "problem": (
            "How to make steel without coal at a price builders will "
            "actually pay. Steelmaking causes roughly 7 to 8 percent of "
            "global CO2, mostly from blast furnaces that use coke both as "
            "fuel and as the chemical reducing agent. Hydrogen-based "
            "routes work in pilots, but the hydrogen bill keeps the steel "
            "too expensive."
        ),
        "background": (
            "A blast furnace reduces iron ore with carbon monoxide from "
            "coke, emitting about 1.8 to 2 tons of CO2 per ton of steel. "
            "The leading clean route is hydrogen direct reduction: hydrogen "
            "gas strips the oxygen from ore to make sponge iron, which an "
            "electric arc furnace then melts - emitting water instead of "
            "CO2 if the hydrogen and electricity are clean. Pilot plants in "
            "Sweden and Germany have made real steel this way. The catch "
            "is arithmetic: about 50 to 60 kilograms of hydrogen per ton "
            "of steel, and at 50 kWh per kilogram of hydrogen from "
            "electrolysis, that is roughly 2,500 to 3,000 kWh of "
            "electricity per ton - before the arc furnace. Green premiums "
            "of 20 to 40 percent are reported, which construction markets "
            "have so far refused to pay at scale."
        ),
        "why_it_matters": (
            "Steel is the skeleton of civilization - buildings, bridges, "
            "cars, wind turbines - and demand keeps rising. There is no "
            "civilization-scale substitute. Either steel gets clean or the "
            "climate math does not close, which makes its cost the "
            "decisive variable."
        ),
        "sig_pointer": (
            "The Signature approach refuses to buy hydrogen on the open "
            "market: it pairs the steel plant with captive curtailed "
            "renewables and sizes hydrogen storage to the ore schedule, "
            "turning the intermittency of cheap power into the plant "
            "economic advantage."
        ),
        "signature_solution": (
            "Step one, state the assumptions: hydrogen cost dominates green "
            "steel cost, and the cheapest hydrogen comes from electricity "
            "that would otherwise be curtailed, not from grid power at "
            "retail rates. Step two, the reasoning path: a steel plant is "
            "one of the few loads flexible enough to chase surplus power - "
            "ore reduction can pause and resume - so the plant should be "
            "designed as a giant controllable load first and a steelmaker "
            "second. Step three, the proposed mechanism: co-site the direct "
            "reduction plant with overbuilt wind and solar, add enough "
            "hydrogen buffer storage to ride through calm weeks, run the "
            "electrolyzers only on surplus, and sell grid services with the "
            "controllable load to stack a second revenue line. Step four, "
            "what would confirm it: audited cost per ton at or below the "
            "blast-furnace route in a full production year, with the power "
            "purchase records to prove the surplus thesis. Step five, what "
            "would kill it: if hydrogen buffer storage at the required "
            "scale costs more than modeled, or if ore grades available to "
            "the plant need pelletizing energy that erases the margin. "
            "What this does not claim: it does not claim hydrogen steel "
            "is cheap today, and it does not claim every region has the "
            "surplus renewables to host such a plant - siting is part of "
            "the design."
        ),
        "citations": [CIT_IEA, CIT_H2],
    },
    {
        "key": "zero_carbon_cement",
        "name": "Zero-Carbon Cement",
        "group": "Materials",
        "ladder_rank": 5,
        "ladder_tier": "approachable",
        "problem": (
            "How to make cement - the glue of concrete, the most consumed "
            "material on Earth after water - without the CO2 baked into "
            "its chemistry. About 60 percent of cement emissions come not "
            "from fuel but from the limestone itself splitting into lime "
            "and CO2, which no fuel switch can fix."
        ),
        "background": (
            "Portland cement is made by heating limestone and clay to about "
            "1,450 degrees C. The heat needs fuel, but the deeper problem "
            "is calcination: calcium carbonate becomes calcium oxide plus "
            "CO2 by stoichiometry, roughly half a ton of CO2 per ton of "
            "clinker, unavoidable as long as limestone is the feedstock. "
            "Cement causes about 7 to 8 percent of global CO2. The industry "
            "has three live strategies: substitute part of the clinker "
            "with slag or fly ash, capture the CO2 from the kiln, or "
            "reinvent the chemistry - magnesium silicate cements, "
            "electrochemical cement that splits limestone without heat, "
            "and limestone-free binders. Each works in a lab or pilot; none "
            "has displaced Portland cement at commodity scale and price."
        ),
        "why_it_matters": (
            "Concrete builds the modern world and there are four billion "
            "tons of cement made every year. Because the emissions are "
            "chemical, not just thermal, this is the purest test of whether "
            "industry can decarbonize by invention rather than by "
            "efficiency alone."
        ),
        "sig_pointer": (
            "The Signature approach treats the kiln as a CO2 concentrator "
            "doing useful work for free: pure-process CO2 is the easiest "
            "stream on Earth to capture, so the plant is redesigned to "
            "capture first and sell the CO2 into materials, flipping the "
            "chemistry problem into a feedstock business."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the calcination CO2 cannot "
            "be prevented, but it emerges from the kiln as a concentrated "
            "stream, which is the cheapest possible capture starting "
            "point. Step two, the reasoning path: stop trying to avoid "
            "the CO2 and instead make the kiln the front end of a "
            "carbon-utilization plant - the emissions become inventory. "
            "Step three, the proposed mechanism: oxy-fuel or electric "
            "kilns that yield a pure CO2 off-gas, piped directly into "
            "adjacent mineralization making construction aggregate and "
            "into concrete curing chambers where CO2 mineralizes inside "
            "the product itself, with clinker substitution (calcined clay, "
            "slag) cutting the per-ton process emissions in parallel. "
            "Step four, what would confirm it: a plant gate-to-gate "
            "audit showing net-zero or net-negative cement at commodity "
            "price, with the CO2 mass balance independently verified. "
            "Step five, what would kill it: if mineralization markets "
            "saturate, or if alternative binders fail decades-long "
            "durability testing that Portland cement passed a century "
            "ago. What this does not claim: it does not claim the "
            "chemistry is repealed - the claim is only that a "
            "concentrated unavoidable stream is an asset, not a "
            "liability, when the plant is designed around it."
        ),
        "citations": [CIT_IEA, CIT_IPCC],
    },
    {
        "key": "solid_state_batteries",
        "name": "Solid-State Batteries at Scale",
        "group": "Energy",
        "ladder_rank": 6,
        "ladder_tier": "approachable",
        "problem": (
            "How to replace the flammable liquid electrolyte in lithium "
            "batteries with a solid ceramic or sulfide layer - unlocking "
            "higher energy density and removing fire risk - and then "
            "manufacture the result by the billions at a competitive price. "
            "Lab cells impress; factory lines do not yet exist at scale."
        ),
        "background": (
            "Liquid electrolytes make lithium-ion work but also make it "
            "burn: thermal runaway fires in phones, cars, and grid "
            "installations are the technology tax. A solid electrolyte "
            "could enable lithium-metal anodes, pushing energy density "
            "from today 250 to 300 Wh per kg toward 400 to 500, while "
            "removing the flammable component. Toyota, Samsung, QuantumScape "
            "and others have run multi-layer prototypes for years. The "
            "barriers are manufacturing, not chemistry alone: ceramic "
            "layers crack, sulfide layers react with moisture, interfaces "
            "between solid layers develop resistance, and the dry-room, "
            "high-pressure processes imagined so far look expensive next "
            "to the roll-to-roll coating lines that make conventional "
            "cells cheap."
        ),
        "why_it_matters": (
            "Batteries are the hinge of both electric transport and "
            "renewable grids. A safe, denser, cheaper cell would extend EV "
            "range, shrink packs, and cut the cost of every storage "
            "project on the planet - while ending the era of battery "
            "fires."
        ),
        "sig_pointer": (
            "The Signature approach treats the interface as the product: "
            "instead of perfecting one miracle ceramic, it grades the "
            "electrolyte layer by layer and accepts a hybrid cell, trading "
            "a fraction of the theoretical density for a process that "
            "runs on adapted existing coating lines."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the factory is the problem, "
            "not the cell - any solid-state design that needs a brand-new "
            "factory type will lose to incremental lithium-ion on cost. "
            "Step two, the reasoning path: design backward from existing "
            "roll-to-roll lines, accepting hybrid solid-liquid interfaces "
            "where they buy manufacturability, and reserve the pure "
            "ceramic only for the separator function where it matters "
            "most. Step three, the proposed mechanism: a graded composite "
            "electrolyte - polymer-rich at the electrodes for contact, "
            "ceramic-dense in the middle for dendrite blocking - laid down "
            "by slot-die coating with in-line sintering, plus pressure "
            "management built into the module casing rather than the cell. "
            "Step four, what would confirm it: 1,000-cycle life at 80 "
            "percent capacity on a pilot line running at real line "
            "speeds, with costed bill of materials. Step five, what would "
            "kill it: if interfacial resistance grows with cycling faster "
            "than modeled, or if moisture sensitivity forces dry-room "
            "costs that erase the line-speed advantage. What this does not "
            "claim: it does not claim the full 500 Wh per kg theoretical "
            "limit - it explicitly trades peak density for a cell that "
            "can actually be built."
        ),
        "citations": [CIT_BATTERY, CIT_DOE_SHOT],
    },
    {
        "key": "green_hydrogen_economics",
        "name": "Green Hydrogen Economics",
        "group": "Energy",
        "ladder_rank": 7,
        "ladder_tier": "approachable",
        "problem": (
            "How to make hydrogen from water and clean electricity cheap "
            "enough to displace the fossil hydrogen the world already uses "
            "90 million tons of per year. Green hydrogen costs roughly 4 "
            "to 6 dollars per kilogram against about 1.50 for grey hydrogen "
            "from natural gas, and physics sets a floor under the "
            "electricity bill."
        ),
        "background": (
            "Nearly all hydrogen today is grey - steam reformed from "
            "methane, emitting about 10 tons of CO2 per ton of hydrogen - "
            "and it goes to refineries and fertilizer. Green hydrogen "
            "splits water with renewable electricity: at about 50 kWh per "
            "kilogram against hydrogen lower heating value of 33.3 kWh "
            "per kilogram, the electrolyzer runs near 60 to 70 percent "
            "efficiency. The U.S. Hydrogen Shot targets 1 dollar per "
            "kilogram within a decade. The obstacles stack up: electrolyzer "
            "capital cost, the price of the electricity, capacity factor "
            "(cheap curtailed power is intermittent), plus storage and "
            "transport - hydrogen leaks, embrittles steel, and carries "
            "little energy per volume, so moving it is its own engineering "
            "problem."
        ),
        "why_it_matters": (
            "Hydrogen is the leading candidate to clean up steel, "
            "fertilizer, shipping, and long-duration energy storage - the "
            "sectors batteries cannot easily reach. Every one of those "
            "decarbonization plans quietly assumes cheap green hydrogen "
            "arrives on schedule."
        ),
        "sig_pointer": (
            "The Signature approach stops shipping hydrogen and starts "
            "shipping its products: make the hydrogen where the surplus "
            "power is, convert it immediately to ammonia or sponge iron "
            "on site, and let the molecule travel as something dense and "
            "easy to handle."
        ),
        "signature_solution": (
            "Step one, state the assumptions: transporting hydrogen is "
            "harder than making it, so the economic plant never sells "
            "hydrogen gas - it sells what hydrogen becomes. Step two, the "
            "reasoning path: co-locate electrolysis with the end process "
            "(ammonia synthesis, direct reduced iron, methanol) at the "
            "renewable site, so the only thing that travels is a dense, "
            "stable commodity the world already ships. Step three, the "
            "proposed mechanism: overbuilt renewables plus modular "
            "electrolyzers running on surplus, feeding a flexible ammonia "
            "or DRI unit designed for variable hydrogen flow, with "
            "underground salt-cavern buffer where geology allows. Step "
            "four, what would confirm it: delivered green ammonia or "
            "green iron at cost parity with the grey route in a full "
            "operating year, audited end to end. Step five, what would "
            "kill it: if variable-flow chemical synthesis proves "
            "uncontrollable at scale, or if electrolyzer degradation "
            "under intermittent duty destroys the maintenance budget. "
            "What this does not claim: it does not claim a hydrogen "
            "pipeline economy - it claims the opposite, that hydrogen "
            "wins by never traveling as hydrogen."
        ),
        "citations": [CIT_H2, CIT_DOE_SHOT, CIT_IEA],
    },
    {
        "key": "sustainable_aviation_fuel",
        "name": "Sustainable Aviation Fuel at Scale",
        "group": "Transport",
        "ladder_rank": 8,
        "ladder_tier": "approachable",
        "problem": (
            "How to fuel airliners without fossil oil. Batteries are far "
            "too heavy for long flights - jet fuel carries about 43 MJ per "
            "kilogram, fifty times a lithium battery - so aviation needs "
            "liquid fuel. Sustainable aviation fuel exists and flies in "
            "regular engines, but it costs two to four times fossil jet "
            "fuel and supplies a fraction of one percent of demand."
        ),
        "background": (
            "SAF is a drop-in replacement: refined from used cooking oil, "
            "animal fats, municipal waste, or synthesized from CO2 and "
            "hydrogen, it burns in existing turbines and is certified for "
            "blends up to 50 percent. The EU ReFuelEU mandate phases in "
            "rising SAF shares from 2025. The feedstock wall is the "
            "problem: waste oils are limited, energy crops compete with "
            "food and forests, and power-to-liquid e-fuels need enormous "
            "clean electricity. A long-haul widebody burns on the order "
            "of 100 tons of fuel per flight; scaling SAF to even 10 "
            "percent of global jet demand means building a whole new "
            "fuels industry from scratch, at prices airlines - operating "
            "on thin margins - resist."
        ),
        "why_it_matters": (
            "Aviation is about 2 to 3 percent of global CO2 and growing, "
            "with no battery-electric path for long haul in sight. SAF is "
            "the only decarbonization lever the industry has that does not "
            "require replacing the world fleet - which makes its cost "
            "the industry climate plan."
        ),
        "sig_pointer": (
            "The Signature approach treats SAF as a refinery scheduling "
            "problem: standardize a small set of certified pathways, run "
            "them on agricultural and municipal waste streams that are "
            "already aggregated, and let e-fuels handle only the peak "
            "mandate volumes."
        ),
        "signature_solution": (
            "Step one, state the assumptions: feedstock, not chemistry, "
            "is the binding constraint, and waste streams that are already "
            "collected (used oils, municipal solid waste, forestry "
            "residues) are the only feedstocks that scale without land "
            "conflict. Step two, the reasoning path: the industry fails "
            "when every producer invents its own pathway; it wins when a "
            "handful of certified pathways run at refinery scale with "
            "shared logistics. Step three, the proposed mechanism: "
            "regional SAF hubs co-located with existing refineries and "
            "waste aggregation points, running two standardized pathways "
            "(waste-oil hydroprocessing and gasification plus Fischer-"
            "Tropsch), with e-fuel modules added only to cover mandate "
            "volumes the waste streams cannot, sited on curtailed "
            "renewables. Step four, what would confirm it: hub-gate fuel "
            "cost within 1.5 times fossil jet with lifecycle audit, at "
            "volumes measured in millions of tons. Step five, what would "
            "kill it: if waste feedstock competition with other sectors "
            "bids prices past the break-even, or if certification of new "
            "pathways stays a multi-year bottleneck. What this does not "
            "claim: it does not claim SAF reaches fossil price parity, "
            "and it does not claim aviation demand can grow unchecked - "
            "the claim is only that a standardized waste-first system "
            "closes most of the gap."
        ),
        "citations": [CIT_SAF, CIT_IEA],
    },
    {
        "key": "battery_recycling",
        "name": "Closed-Loop Lithium Battery Recycling",
        "group": "Materials",
        "ladder_rank": 9,
        "ladder_tier": "approachable",
        "problem": (
            "How to take back the millions of tons of lithium-ion batteries "
            "that will retire from cars and grids, and recover their "
            "lithium, nickel, cobalt, and copper cleanly enough to build "
            "new batteries - instead of mining it all again. Collection, "
            "dismantling, and economics all lag the coming wave."
        ),
        "background": (
            "A typical EV pack holds on the order of 8 kilograms of "
            "lithium, plus nickel, cobalt, manganese, copper, aluminum, "
            "and graphite. Two recycling routes dominate: pyrometallurgy "
            "(smelting, which loses lithium and aluminum to slag) and "
            "hydrometallurgy (acid leaching, which recovers over 95 "
            "percent of cobalt and nickel and around 90 percent of "
            "lithium). Direct recycling - healing cathode crystals without "
            "fully breaking them down - works in labs. The industry "
            "problem is logistics: packs are heavy, varied, glued shut, "
            "and sometimes damaged, making automated disassembly hard; "
            "collection networks are thin; and recycled material must "
            "compete with mined material on price in a volatile commodity "
            "market. The first great wave of EV retirements arrives in "
            "the late 2020s and early 2030s."
        ),
        "why_it_matters": (
            "Mining for battery metals is slow, geopolitically fraught, "
            "and environmentally costly. A true closed loop would turn the "
            "world vehicle fleet into a mine that never depletes - "
            "urban mining at civilization scale - and cut the footprint "
            "of every future battery."
        ),
        "sig_pointer": (
            "The Signature approach designs the loop backward from the "
            "cathode: standardize pack disassembly interfaces now, run "
            "hydrometallurgy tuned per chemistry, and contract recycled "
            "content back to the same automakers so the loop is closed "
            "by contract, not by hope."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the binding constraints are "
            "disassembly labor and feedstock aggregation, not the "
            "chemistry of recovery - the leaching works. Step two, the "
            "reasoning path: a recycler that must reverse-engineer every "
            "pack design loses; the loop only closes if packs arrive in "
            "known, machine-readable formats with standardized fasteners "
            "and module sizes. Step three, the proposed mechanism: an "
            "industry disassembly standard (module dimensions, connector "
            "positions, chemistry labeling readable by machine vision), "
            "regional hydrometallurgy hubs running chemistry-specific "
            "lines, and take-back contracts that route retired packs from "
            "named automakers straight back into their cathode supply. "
            "Step four, what would confirm it: audited recovery above 90 "
            "percent for lithium and above 95 percent for nickel and "
            "cobalt at a cost below mined equivalents across a full "
            "year of operation. Step five, what would kill it: if pack "
            "designs keep fragmenting faster than standards converge, or "
            "if commodity price crashes make even efficient recycling "
            "uneconomic without policy support. What this does not claim: "
            "it does not claim recycling eliminates mining - the fleet "
            "keeps growing, so mining continues - it claims only that "
            "retired batteries stop being waste."
        ),
        "citations": [CIT_BATTERY, CIT_IEA],
    },
    {
        "key": "pfas_destruction",
        "name": "PFAS Destruction at Scale",
        "group": "Environment",
        "ladder_rank": 10,
        "ladder_tier": "approachable",
        "problem": (
            "How to actually destroy PFAS - the forever chemicals - rather "
            "than just filtering them out and moving them somewhere else. "
            "The carbon-fluorine bond is among the strongest in chemistry, "
            "so these molecules survive water treatment, survive landfills, "
            "and accumulate in blood and the environment."
        ),
        "background": (
            "Per- and polyfluoroalkyl substances coat pans, repel water on "
            "jackets, and put out fuel fires; they are now found in "
            "rainwater, Arctic ice, and most human blood samples. The C-F "
            "bond stores about 485 kJ per mol, stronger than C-C at 347 "
            "or C-H at 413, which is why nothing in nature breaks them "
            "down on human timescales. Treatment today mostly means "
            "granular activated carbon or ion exchange: the PFAS is "
            "captured, and then the spent media must be landfilled or "
            "incinerated - which risks incomplete destruction and "
            "re-release. True destruction methods exist in labs: "
            "supercritical water oxidation, electrochemical oxidation, "
            "UV plus sulfite hydrated-electron chemistry, and mechanochemical "
            "milling. None yet runs at municipal water-plant scale and "
            "cost."
        ),
        "why_it_matters": (
            "Regulators are setting drinking-water limits in parts per "
            "trillion, and the contamination is already everywhere. "
            "Without a destruction technology, every cleanup just "
            "relocates the problem to the next landfill - forever "
            "chemicals demand an ending, not a transfer."
        ),
        "sig_pointer": (
            "The Signature approach pairs concentration with destruction: "
            "cheap sorbents gather the PFAS from huge water volumes into "
            "a small stream, and only that small stream meets the "
            "expensive destruction step - hydrated-electron chemistry "
            "driven by surplus electricity."
        ),
        "signature_solution": (
            "Step one, state the assumptions: destruction energy per "
            "molecule is affordable, but destruction energy per million "
            "gallons of dilute water is not - so the process must "
            "concentrate first and destroy second. Step two, the reasoning "
            "path: separate the mass-transfer problem (getting PFAS out "
            "of water) from the bond-breaking problem (killing the "
            "molecule), and optimize each with different equipment. Step "
            "three, the proposed mechanism: low-cost regenerable sorbent "
            "beds or foam fractionation to concentrate PFAS by factors of "
            "thousands, then a compact destruction reactor - UV-sulfite "
            "hydrated-electron or electrochemical oxidation - treating "
            "only the concentrate, powered by off-peak electricity, with "
            "fluoride ion monitoring as the proof-of-destruction signal. "
            "Step four, what would confirm it: continuous operation on "
            "real contaminated groundwater showing non-detect PFAS in "
            "effluent and stoichiometric fluoride release matching the "
            "influent fluorine mass. Step five, what would kill it: if "
            "concentrate matrices (co-contaminants, salts) poison the "
            "destruction chemistry, or if sorbent regeneration itself "
            "becomes the cost center. What this does not claim: it does "
            "not claim to clean the oceans or the rain - the claim is "
            "limited to point sources and drinking-water plants, the "
            "places where concentration is feasible."
        ),
        "citations": [CIT_IPCC],
    },
    {
        "key": "ocean_plastic",
        "name": "Ocean Plastic Removal at Scale",
        "group": "Environment",
        "ladder_rank": 11,
        "ladder_tier": "approachable",
        "problem": (
            "How to get plastic out of the ocean faster than rivers and "
            "wind put it in. The Great Pacific Garbage Patch holds on the "
            "order of 80,000 tons across 1.6 million square kilometers, and "
            "cleanup systems harvest a tiny fraction of the inflow - while "
            "sunlight keeps shredding surface plastic into microplastics "
            "that no net can catch."
        ),
        "background": (
            "An estimated 8 to 12 million tons of plastic enter the ocean "
            "each year, mostly from rivers in Asia and Africa. Surface "
            "currents gather floating debris into five great gyres. The "
            "Ocean Cleanup project has shown that passive drifting barriers "
            "can concentrate and extract surface plastic, removing thousands "
            "of tons. But the physics fights back: most ocean plastic is "
            "not floating in patches - it is suspended, beached, sunk, or "
            "fragmented below net mesh size. Microplastics now appear in "
            "seafood, sea salt, and human tissue. Interceptor-style river "
            "barriers attack the inflow, which modelers say is the higher-"
            "leverage point, yet thousands of rivers remain unguarded and "
            "waste collection upstream is the true root."
        ),
        "why_it_matters": (
            "The ocean is the planet life-support system and the plastic "
            "layer is still thickening. Removal buys time, but the deeper "
            "prize is proving that humanity can run cleanup infrastructure "
            "at planetary scale - a capability the century will need again "
            "and again."
        ),
        "sig_pointer": (
            "The Signature approach ranks the problem by leverage: rivers "
            "first, gyres second, microplastics by prevention - a layered "
            "interception system where each layer is sized to the flux it "
            "faces, funded by the recycled plastic it harvests."
        ),
        "signature_solution": (
            "Step one, state the assumptions: you cannot filter the ocean, "
            "so removal must happen where plastic is concentrated - river "
            "mouths before dispersal, gyre cores after concentration - and "
            "prevention upstream beats every downstream technology. Step "
            "two, the reasoning path: sort the plastic flux by capture "
            "cost per ton and attack in that order, letting each layer "
            "fund the next through sale of recovered material. Step three, "
            "the proposed mechanism: solar-powered river interceptors on "
            "the highest-flux rivers with automated sorting and local "
            "recycling markets; gyre harvesters scheduled by drift models "
            "to work the densest windrows; and upstream, deposit-return "
            "packaging systems in the top emitting watersheds to choke the "
            "inflow at its source. Step four, what would confirm it: "
            "measured year-on-year decline in river plastic flux at "
            "instrumented mouths, plus gyre mass-balance surveys showing "
            "removal exceeding new accumulation. Step five, what would "
            "kill it: if recovered-plastic markets collapse under "
            "contamination, or if storm events redistribute gyre plastic "
            "faster than harvesters can track. What this does not claim: "
            "it does not claim to remove microplastics from the water "
            "column - that is stated as currently infeasible - the claim "
            "covers macroplastic fluxes only."
        ),
        "citations": [CIT_GPGP, CIT_IPCC],
    },
    {
        "key": "corrosion",
        "name": "Ending Structural Corrosion",
        "group": "Materials",
        "ladder_rank": 12,
        "ladder_tier": "approachable",
        "problem": (
            "How to stop rust and corrosion from eating civilization. "
            "Corrosion costs about 2.5 trillion dollars a year - roughly "
            "3.4 percent of global GDP - in bridges, pipelines, ships, "
            "cars, and reinforced concrete. We manage it with paint and "
            "replacement; we have never solved it."
        ),
        "background": (
            "Iron wants to be iron oxide - rust is the metal returning to "
            "its natural ore state, and thermodynamics is on rust side. "
            "The NACE IMPACT study put the global bill at 2.5 trillion "
            "dollars annually, and estimated 15 to 35 percent of it "
            "avoidable with existing best practice that simply is not "
            "applied. Current defenses: coatings, galvanizing, cathodic "
            "protection (sacrificial anodes or impressed current), "
            "corrosion inhibitors, and stainless alloys that armor "
            "themselves with chromium oxide films. The failures are "
            "legendary and deadly - bridge collapses, pipeline ruptures, "
            "the reinforced-concrete cancer that cracks structures from "
            "inside as rebar rusts and expands. Research directions "
            "include self-healing coatings with microencapsulated agents, "
            "graphene barriers, and alloys designed atom by atom, but "
            "nothing has changed the global cost curve."
        ),
        "why_it_matters": (
            "Corrosion is a hidden tax on everything built - several "
            "percent of the world economy, paid in maintenance, "
            "replacement, and occasional catastrophe. Solving it would "
            "free capital on the scale of a major industry and extend "
            "the life of every structure standing."
        ),
        "sig_pointer": (
            "The Signature approach treats corrosion as an information "
            "problem first and a materials problem second: instrument "
            "structures with cheap corrosion sensing, intervene at the "
            "first electrochemical whisper, and reserve the exotic "
            "materials for the joints and interfaces where failures "
            "start."
        ),
        "signature_solution": (
            "Step one, state the assumptions: most corrosion damage comes "
            "not from unknown chemistry but from undetected early-stage "
            "attack at interfaces - rebar in concrete, welds, crevices - "
            "where inspection never reaches. Step two, the reasoning path: "
            "a structure that reports its own corrosion can be maintained "
            "at the pit stage for pennies instead of the collapse stage "
            "for billions, so sensing buys more than any coating. Step "
            "three, the proposed mechanism: embed printed electrochemical "
            "sensor grids at known-vulnerable interfaces during "
            "construction, networked to report corrosion current density; "
            "pair with targeted impressed-current zones that activate only "
            "where sensors report attack; and specify self-healing "
            "coatings only at joints and welds, the failure origins. Step "
            "four, what would confirm it: instrumented structures showing "
            "a decade of near-zero section loss with maintenance cost an "
            "order of magnitude below uninstrumented twins. Step five, "
            "what would kill it: if sensor drift in real concrete and "
            "soil environments produces false confidence, or if the "
            "electronics themselves become the maintenance burden. What "
            "this does not claim: it does not claim to repeal the "
            "thermodynamics of rust - the claim is only that measured, "
            "targeted protection beats blind, uniform protection by an "
            "order of magnitude."
        ),
        "citations": [CIT_NACE],
    },
    {
        "key": "refree_magnets",
        "name": "Rare-Earth-Free High-Performance Magnets",
        "group": "Materials",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "problem": (
            "How to build a permanent magnet as strong as neodymium-iron-"
            "boron without rare earths. NdFeB magnets top out near 400 kJ "
            "per cubic meter in commercial grades against a theoretical "
            "512, while the best rare-earth-free ferrites stall near 38. "
            "EV motors and wind turbines depend on that strength, and the "
            "supply chain depends on a handful of mines."
        ),
        "background": (
            "Neodymium magnets, commercialized in the 1980s, made modern "
            "EV traction motors and direct-drive wind turbines possible: "
            "their energy product - the figure of merit for how much "
            "magnetic work a volume can do - dwarfs alnico and ferrite. "
            "China refines the great majority of rare earths, which has "
            "made the supply chain a strategic anxiety in Washington, "
            "Brussels, and Tokyo. Alternatives each fall short somewhere: "
            "ferrites are cheap but weak, samarium-cobalt is strong but "
            "still rare-earth and brittle, manganese-bismuth and "
            "iron-nitride compounds show promise in labs but resist "
            "scale-up, and motor designers work around the problem with "
            "wound-rotor or ferrite-assisted designs that trade size and "
            "weight. The prize is a magnet above roughly 200 kJ per cubic "
            "meter made from abundant elements."
        ),
        "why_it_matters": (
            "Every electric vehicle and every direct-drive offshore "
            "turbine carries kilograms of rare earths. A strong "
            "rare-earth-free magnet would de-risk the entire clean-energy "
            "supply chain, cut motor costs, and remove one of the "
            "dirtiest mining operations from the energy transition."
        ),
        "sig_pointer": (
            "The Signature approach hunts in the neglected middle: "
            "nanocomposite exchange-spring magnets that couple a hard "
            "magnetic phase to a soft high-magnetization phase at the "
            "nanoscale, designed computationally and screened by robot "
            "labs rather than by decades of trial and error."
        ),
        "signature_solution": (
            "Step one, state the assumptions: no single abundant compound "
            "will match NdFeB alone, so the answer must be a composite "
            "whose properties emerge from nanoscale architecture, not "
            "from chemistry alone. Step two, the reasoning path: "
            "exchange-spring theory says a hard phase (high coercivity) "
            "coupled to a soft phase (high saturation) at grain sizes "
            "below about 10 nanometers can exceed either phase alone - "
            "the magnet becomes a designed metamaterial. Step three, the "
            "proposed mechanism: computational screening of "
            "manganese-, iron-, and cobalt-based hard phases paired with "
            "iron-cobalt soft phases, synthesized as core-shell "
            "nanoparticles, consolidated by field-assisted sintering "
            "that preserves the nanostructure, with robot-run "
            "composition spreads mapping the design space thousands of "
            "times faster than graduate-student labor. Step four, what "
            "would confirm it: bulk pellets above 200 kJ per cubic meter "
            "with coercivity surviving 150 C operating temperature, "
            "reproduced across three independent batches. Step five, "
            "what would kill it: if grain growth during consolidation "
            "provably cannot be suppressed at industrial throughput, or "
            "if the best pairs need cobalt at levels that recreate the "
            "supply problem. What this does not claim: it does not claim "
            "to beat NdFeB - the stated target is half its strength at a "
            "tenth its supply risk, which is enough to change motor "
            "design."
        ),
        "citations": [CIT_IEA],
    },
    {
        "key": "inert_anode_aluminum",
        "name": "Inert-Anode Aluminum Smelting",
        "group": "Materials",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "problem": (
            "How to smelt aluminum without burning carbon anodes. The "
            "Hall-Heroult process consumes about 0.4 tons of carbon anode "
            "per ton of aluminum, releasing roughly 1.5 tons of CO2 per "
            "ton of metal directly - plus PFC gases during anode effects. "
            "An inert anode that survives the cryolite bath would emit "
            "oxygen instead."
        ),
        "background": (
            "Aluminum has been smelted the same way since 1886: alumina "
            "dissolved in cryolite at about 960 C, electric current "
            "splitting it, carbon anodes consumed in the reaction. The "
            "industry makes about 70 million tons a year and consumes "
            "roughly 3 percent of world electricity doing it. Inert "
            "anodes - typically cermets of nickel ferrite and copper, or "
            "related ceramics - have been the holy grail for decades: "
            "they would eliminate the direct CO2 and the perfluorocarbon "
            "bursts, and cut the labor of constantly replacing anodes. "
            "The Elysis joint venture has run pilot cells and announced "
            "commercial timelines, but no inert-anode cell has yet run "
            "for years at full industrial current density without the "
            "anode corroding, contaminating the metal, or simply "
            "dissolving into the bath."
        ),
        "why_it_matters": (
            "Aluminum is the lightweight metal of the energy transition - "
            "cars, planes, power lines, solar frames. Smelting already "
            "uses clean hydroelectricity in many regions; the carbon "
            "anode is the remaining direct emission. Solving it takes a "
            "full percent-scale bite out of global CO2 with no change to "
            "the downstream product."
        ),
        "sig_pointer": (
            "The Signature approach treats anode survival as a dynamic "
            "equilibrium problem: a thin self-repairing oxide skin fed "
            "by the bath chemistry itself, monitored electrically in real "
            "time, rather than a search for one immortal material."
        ),
        "signature_solution": (
            "Step one, state the assumptions: no static material survives "
            "cryolite at 960 C indefinitely, so the anode must be a "
            "steady-state system - dissolving and rebuilding at equal "
            "rates - rather than an inert object. Step two, the reasoning "
            "path: the bath already contains the elements of protective "
            "oxide skins; the design task is to tune bath chemistry so "
            "the skin rebuilds faster than it erodes, the way stainless "
            "steel re-passivates in air. Step three, the proposed "
            "mechanism: a nickel-ferrite cermet anode with engineered "
            "porosity, run in a bath doped to favor skin reformation, "
            "with cell voltage harmonics monitored continuously as an "
            "early-warning signal of skin breakdown, and current "
            "density modulated to let the skin recover during "
            "micro-cycles. Step four, what would confirm it: a pilot "
            "cell running 12 months at industrial current density with "
            "anode wear below the economic threshold and metal purity "
            "meeting P1020 spec. Step five, what would kill it: if the "
            "dissolved anode metals contaminate aluminum beyond "
            "refining tolerance, or if the micro-cycling cuts current "
            "efficiency below the carbon-anode baseline. What this does "
            "not claim: it does not claim a maintenance-free anode - "
            "the claim is a managed steady state with scheduled renewal "
            "far less frequent than carbon anode changes."
        ),
        "citations": [CIT_IEA],
    },
    {
        "key": "fusion_power",
        "name": "Practical Fusion Power",
        "group": "Energy",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "problem": (
            "How to get usable electricity from fusing atomic nuclei - the "
            "reaction that powers the sun - at a price anyone would pay. "
            "In December 2022 the National Ignition Facility achieved "
            "laboratory ignition, releasing 3.15 MJ of fusion energy from "
            "2.05 MJ of laser input. A power plant needs that to happen "
            "repeatedly, cheaply, and converted to electricity."
        ),
        "background": (
            "Fusion has been twenty years away for about sixty years. Two "
            "main roads: magnetic confinement (tokamaks like ITER, "
            "stellarators like Wendelstein 7-X, and a pack of private "
            "startups chasing compact high-field designs) and inertial "
            "confinement (NIF laser implosions). The physics milestone is "
            "the Lawson criterion - temperature, density, and confinement "
            "time multiplied past ignition. NIF proved ignition is "
            "possible; the engineering milestones are all still ahead: "
            "materials that survive years of neutron bombardment, "
            "breeding tritium fuel from lithium blankets faster than it "
            "is burned, rep-rated drivers firing many times per second, "
            "and capital costs that do not exceed fission, let alone "
            "solar. Dozens of private companies have raised billions on "
            "faster timelines than public programs."
        ),
        "why_it_matters": (
            "Fusion fuel is seawater and lithium - effectively limitless, "
            "with no long-lived waste and no meltdown physics. A working "
            "plant would be dispatchable clean power independent of "
            "weather, geography, and fuel markets: the end of energy "
            "scarcity as a constraint on civilization."
        ),
        "sig_pointer": (
            "The Signature approach treats fusion as a manufacturing and "
            "materials problem wearing a physics costume: it bets the "
            "winning design is the one whose neutron-facing components "
            "can be swapped like printer cartridges, making the plant a "
            "serviceable machine instead of a cathedral."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the physics of ignition is "
            "now demonstrated, so the binding constraints are neutron "
            "damage, tritium breeding, and capital cost - all engineering "
            "and manufacturing problems. Step two, the reasoning path: "
            "every fusion concept dies the same death, a blanket or "
            "first wall that cannot be maintained; therefore the "
            "maintainable machine beats the optimal plasma. Step three, "
            "the proposed mechanism: design the reactor around "
            "cartridge-style blanket modules replaced by robots during "
            "scheduled outages, liquid-metal or molten-salt blankets "
            "that breed tritium and carry heat in one loop, and "
            "high-temperature superconducting magnets wound from "
            "factory-made segments - with the whole plant instrumented "
            "to sell its operating data back into the design loop. Step "
            "four, what would confirm it: a module surviving a full "
            "neutron fluence cycle with measured tritium breeding ratio "
            "above 1.0 and a maintenance outage measured in weeks, not "
            "years. Step five, what would kill it: if neutron damage "
            "to superconductors or structural steels proves "
            "fundamentally faster than any serviceable replacement "
            "schedule, or if tritium breeding cannot close the fuel "
            "cycle at any blanket design. What this does not claim: it "
            "does not claim a date for grid power, and it does not claim "
            "any particular confinement concept wins - the claim is "
            "only about where the decisive engineering battle is fought."
        ),
        "citations": [CIT_NIF, CIT_ITER, CIT_DOE_SHOT],
    },
    {
        "key": "room_temp_superconductor",
        "name": "Room-Temperature Superconductors",
        "group": "Materials",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "problem": (
            "How to make a material that conducts electricity with zero "
            "resistance at room temperature and ordinary pressure. The "
            "ambient-pressure record still belongs to mercury-based "
            "cuprates at 133 K, set in 1993; hydrides reach 250 K but "
            "only under about 170 gigapascals - nearly two million "
            "atmospheres. A 2023 claim of room-temperature "
            "superconductivity in LK-99 did not reproduce."
        ),
        "background": (
            "Superconductivity was found in 1911 and explained by BCS "
            "theory in 1957; the 1986 cuprate discovery shattered the "
            "temperature ceiling and won a Nobel within a year. Each "
            "record since has come with a catch: cuprates are brittle "
            "ceramics, iron pnictides need careful doping, and the "
            "hydride records require diamond-anvil pressures no wire "
            "will ever see. The applications waiting are enormous: "
            "lossless grids, compact fusion magnets, maglev without "
            "cryogenics, MRI machines without liquid helium. The field "
            "has been burned before - most famously by retracted claims "
            "in the 2020s - so extraordinary evidence is now demanded "
            "as a matter of professional survival."
        ),
        "why_it_matters": (
            "About 5 to 8 percent of generated electricity is lost as "
            "heat in transmission and distribution. A room-temperature "
            "superconductor would erase those losses, shrink every "
            "electromagnet on Earth, and unlock technologies - from "
            "compact fusion to grid-scale magnetic storage - that are "
            "cryogenically impractical today."
        ),
        "sig_pointer": (
            "The Signature approach stops hunting single miracle "
            "compounds and engineers the electron pairing environment "
            "instead: hydride-like hydrogen cages stabilized at ambient "
            "pressure by chemical pre-compression inside rigid "
            "frameworks, screened computationally before anyone grows "
            "a crystal."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the hydride results prove "
            "that dense hydrogen environments pair electrons at high "
            "temperature, so the problem is purely one of stabilizing "
            "that environment without the diamond anvil. Step two, the "
            "reasoning path: chemical pressure - crowding hydrogen with "
            "large atoms inside rigid clathrate-like frameworks - can "
            "mimic hundreds of gigapascals permanently, the way some "
            "minerals hold high-pressure phases at the surface for "
            "geologic time. Step three, the proposed mechanism: "
            "computational screening for ternary hydride frameworks "
            "with the highest predicted critical temperature at zero "
            "external pressure, synthesized by high-pressure "
            "pre-loading then quenched into metastability, with "
            "resistivity, Meissner, and specific-heat measurements "
            "required together before any claim is announced. Step four, "
            "what would confirm it: zero resistance plus full magnetic "
            "expulsion plus a heat-capacity jump at the same "
            "temperature, at ambient pressure, reproduced by an "
            "independent lab from the published recipe. Step five, what "
            "would kill it: if every ambient-stabilized hydride "
            "predicted by theory decomposes on quenching, or if the "
            "electron-phonon coupling needed proves incompatible with "
            "ambient-pressure lattice stability as a matter of "
            "principle. What this does not claim: it does not claim any "
            "existing material works, and it pointedly does not endorse "
            "any past unreproduced claim - the bar is set at triple "
            "measurement plus independent replication."
        ),
        "citations": [CIT_SUPERCON],
    },
    {
        "key": "geothermal_anywhere",
        "name": "Geothermal Energy Anywhere",
        "group": "Energy",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "problem": (
            "How to tap Earth heat anywhere, not just in volcanic zones. "
            "The temperature rises about 25 to 30 C per kilometer of "
            "depth, so useful 150 to 200 C rock sits 5 to 7 kilometers "
            "down almost everywhere - but drilling that deep costs "
            "exponentially more, and hot dry rock does not flow like a "
            "natural hydrothermal reservoir."
        ),
        "background": (
            "Geothermal power works beautifully where nature cooperates - "
            "Iceland, Kenya, the Geysers in California - delivering "
            "baseload clean power from natural steam. Enhanced geothermal "
            "systems try to engineer the reservoir: drill two deep wells, "
            "fracture the hot rock between them, circulate water. The "
            "DOE GeoVision study mapped the prize: tens of gigawatts in "
            "the US alone if EGS works. Startups are attacking the two "
            "hard parts with oil-industry technology: faster cheaper "
            "deep drilling (one company literally vaporizes rock with "
            "millimeter-wave beams) and closed-loop well designs that "
            "avoid fracturing altogether. The record so far is pilots "
            "measured in megawatts against a need measured in "
            "terawatts."
        ),
        "why_it_matters": (
            "Geothermal is the only clean baseload source available on "
            "every continent regardless of weather - always-on power "
            "from a planet that will stay hot for billions of years. "
            "Making it work anywhere turns the clean-energy transition "
            "from a weather-management problem into a drilling problem."
        ),
        "sig_pointer": (
            "The Signature approach treats the well as a manufactured "
            "product: standardized closed-loop well pairs drilled by "
            "automated rigs, with the heat harvested by a working fluid "
            "that never touches the rock - no fracturing politics, no "
            "reservoir uncertainty, just depth times temperature."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the reservoir is the "
            "risk - fracturing hot rock is unpredictable and politically "
            "fraught - so the design eliminates the reservoir entirely. "
            "Step two, the reasoning path: a closed-loop well is just a "
            "very deep heat exchanger; its output is boringly predictable "
            "from depth and gradient, which is exactly what project "
            "finance wants to hear. Step three, the proposed mechanism: "
            "standardized U-shaped well pairs drilled to 5 to 7 km by "
            "automated rigs running 24 hours, vacuum-insulated upper "
            "sections, a sealed working-fluid loop, and modular "
            "binary-cycle power units at the surface sized to the "
            "measured thermal output of each pair. Step four, what would "
            "confirm it: a 10-pair field delivering its modeled output "
            "for two years with drilling cost per pair falling along a "
            "documented learning curve. Step five, what would kill it: "
            "if deep drilling costs refuse to fall with repetition, or "
            "if thermal drawdown around the wellbore chokes output "
            "faster than conduction replenishes it. What this does not "
            "claim: it does not claim to match the cost of the best "
            "volcanic sites - the claim is baseload power at a "
            "financeable price anywhere, which is a different and "
            "larger prize."
        ),
        "citations": [CIT_GEO, CIT_DOE_SHOT],
    },
    {
        "key": "artificial_photosynthesis",
        "name": "Artificial Photosynthesis at Industrial Scale",
        "group": "Energy",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "problem": (
            "How to do what leaves do - turn sunlight, water, and CO2 "
            "into fuel - at industrial efficiency and scale. Natural "
            "photosynthesis runs near 1 percent efficiency; the best "
            "lab photoelectrochemical cells reach toward 10 percent "
            "solar-to-fuel, while solar panels plus electrolyzers "
            "already exceed 20 percent. The direct route has never "
            "scaled."
        ),
        "background": (
            "The dream is an artificial leaf: dip it in water, shine "
            "light, collect fuel. Research splits into photoelectrochemical "
            "cells (semiconductors wired to catalysts in one device), "
            "photocatalytic powders (dust that makes hydrogen in "
            "sunlight), and molecular systems mimicking the "
            "photosystem II water-splitting complex. Decades of work "
            "have produced hero efficiencies on square-centimeter "
            "devices that degrade in hours or use iridium and platinum "
            "no industry could afford. Meanwhile the indirect route - "
            "cheap solar panels feeding electrolyzers - keeps getting "
            "cheaper and sets the bar the artificial leaf must beat. "
            "The remaining argument for the direct route is simplicity: "
            "no wires, no power electronics, just surfaces in the sun."
        ),
        "why_it_matters": (
            "A scalable artificial leaf would turn every sunlit surface "
            "into a fuel factory with no moving parts - the simplest "
            "imaginable solar fuel, deployable where grids and "
            "factories cannot go. It is also the long-term answer to "
            "recycling atmospheric CO2 back into the fuels we still "
            "need."
        ),
        "sig_pointer": (
            "The Signature approach concedes the efficiency race to "
            "panels-plus-electrolyzers and competes on simplicity "
            "instead: ultra-cheap photocatalytic sheets, replaced like "
            "roofing felt, where the economic metric is fuel per dollar "
            "of installed sheet, not efficiency per photon."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the artificial leaf will "
            "never beat PV-plus-electrolysis on efficiency, so it must "
            "win on installed cost per unit of fuel - a manufacturing "
            "contest, not a physics contest. Step two, the reasoning "
            "path: if the active material is printable like newspaper "
            "from earth-abundant elements, even 5 percent efficiency "
            "wins where land is cheap and maintenance must be zero. "
            "Step three, the proposed mechanism: roll-to-roll printed "
            "photocatalyst sheets (doped carbon nitrides or oxynitrides, "
            "no precious metals) floated on shallow water basins, "
            "evolving hydrogen collected under a membrane cover, with "
            "sheets swapped on a roofing-like replacement cycle and "
            "spent sheets recycled into new ones. Step four, what would "
            "confirm it: a one-hectare basin running a full year with "
            "metered hydrogen output and a costed sheet-replacement "
            "log showing fuel cost trending toward the PV-electrolysis "
            "benchmark. Step five, what would kill it: if photocorrosion "
            "destroys the sheets faster than the replacement economics "
            "allow, or if gas separation at basin scale proves "
            "impractical outside the lab. What this does not claim: it "
            "does not claim high efficiency or precious-metal-free "
            "heroics in a single device - the claim is explicitly that "
            "cheap and replaceable beats efficient and delicate."
        ),
        "citations": [CIT_DOE_SHOT, CIT_IEA],
    },
    {
        "key": "orbital_solar",
        "name": "Orbital Solar Power Stations",
        "group": "Energy",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "problem": (
            "How to collect solar power in orbit - where the sun never "
            "sets and no atmosphere dims it - and beam it to Earth. A "
            "geostationary station sees roughly 99 percent capacity "
            "factor against 15 to 25 percent for ground solar, but "
            "launching thousands of tons and beaming gigawatts through "
            "the atmosphere are unsolved at scale."
        ),
        "background": (
            "Peter Glaser patented the solar power satellite in 1968; "
            "NASA and DOE studied it seriously in the 1970s and priced "
            "it out of reach at Shuttle-era launch costs. Two things "
            "changed: reusable rockets cut launch cost toward 1,500 "
            "dollars per kilogram and falling, and phased-array and "
            "photovoltaic efficiency made the station lighter. Concepts "
            "like SPS-ALPHA propose modular, robot-assembled stations "
            "beaming microwaves to rectenna farms. The open problems: "
            "assembly of kilometer-scale structures in orbit, beam "
            "safety and pointing at gigawatt scale, end-to-end "
            "efficiency (sunlight to grid through two conversions and "
            "the atmosphere), and a business case against ground solar "
            "plus batteries that keeps getting cheaper."
        ),
        "why_it_matters": (
            "Orbital solar is baseload solar - clean power through the "
            "night, through winter, through clouds, deliverable to any "
            "rectenna on Earth. If the economics ever close, it "
            "decouples clean electricity from both weather and land "
            "use, the two great constraints of the terrestrial "
            "transition."
        ),
        "sig_pointer": (
            "The Signature approach refuses the cathedral station: it "
            "builds the power plant as a swarm of identical small "
            "satellites, each beaming a modest wattage, so capacity "
            "grows incrementally and no single launch or assembly "
            "mission can fail the program."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the killer risks are "
            "assembly complexity and all-or-nothing capital exposure, "
            "not the physics of beaming - so the architecture must be "
            "incremental and failure-tolerant. Step two, the reasoning "
            "path: a thousand identical 10-megawatt beaming satellites "
            "in formation can be launched on existing rockets, tested "
            "one at a time, and scaled like a solar farm rather than "
            "bet like a moonshot. Step three, the proposed mechanism: "
            "standardized power-beaming cubesats with deployable PV "
            "wings and phased-array transmitters, flying in a "
            "coordinated cluster whose beams combine coherently at the "
            "rectenna, with the first revenue from premium "
            "always-on power to remote sites before any grid-scale "
            "ambition. Step four, what would confirm it: a 10-unit "
            "cluster delivering metered power to a rectenna for a year "
            "with beam intensity outside the site below safety limits "
            "at all times. Step five, what would kill it: if coherent "
            "beam combination at the required precision proves "
            "unmaintainable in a real orbital environment, or if "
            "end-to-end efficiency cannot clear the bar set by "
            "terrestrial solar plus storage. What this does not claim: "
            "it does not claim to beat ground solar on price in "
            "sunny regions - the claim is baseload delivery where "
            "baseload commands a premium."
        ),
        "citations": [CIT_SPS, CIT_NASA],
    },
    {
        "key": "hypersonic_flight",
        "name": "Sustained Hypersonic Flight",
        "group": "Transport",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "problem": (
            "How to fly an air-breathing vehicle at Mach 5 and above for "
            "useful distances - say, two hours across an ocean in under "
            "an hour of flight time for civil transport. The X-43A hit "
            "Mach 9.6 in 2004, but only for seconds; sustained cruise "
            "means managing heat loads that scale brutally with speed "
            "and an engine that must work from runway to hypersonic."
        ),
        "background": (
            "Above Mach 5, air stops behaving politely: shock heating "
            "scales roughly with the cube of velocity, stagnation "
            "temperatures exceed the melting point of most alloys, and "
            "the scramjet engine - which burns fuel in supersonic "
            "airflow - has no moving parts but only works once already "
            "moving fast. Research programs have flown scramjet "
            "demonstrators for tens to hundreds of seconds. A civil "
            "hypersonic transport would need combined-cycle engines "
            "(turbine to ramjet to scramjet handoff), actively cooled "
            "structures circulating fuel as coolant, and materials "
            "surviving repeated thermal cycles - plus a sonic-boom and "
            "emissions story regulators can accept. Every attempt so "
            "far has been an experiment, not a vehicle."
        ),
        "why_it_matters": (
            "Civil hypersonic flight would compress the planet: any two "
            "cities within about ninety minutes. Beyond speed, the "
            "materials, cooling, and propulsion advances spill into "
            "space launch, power generation, and high-temperature "
            "industry - it is a forcing function for extreme-"
            "environment engineering."
        ),
        "sig_pointer": (
            "The Signature approach treats the vehicle as a flying heat "
            "exchanger: the fuel is the coolant, the structure is the "
            "radiator, and the flight profile is designed around thermal "
            "budgets first and aerodynamics second."
        ),
        "signature_solution": (
            "Step one, state the assumptions: heat, not thrust, is the "
            "binding constraint - any sustained hypersonic design that "
            "does not budget every watt of heat rejection will melt, "
            "regardless of its engine. Step two, the reasoning path: "
            "design the thermal system first, with cryogenic or "
            "endothermic fuel absorbing heat through the structure "
            "before it burns, making the cooling loop and the fuel "
            "system the same hardware. Step three, the proposed "
            "mechanism: a waverider airframe with fuel-cooled leading "
            "edges, a turbine-based combined-cycle engine for the climb "
            "to scramjet takeover, endothermic cracking fuel that "
            "absorbs extra heat chemically, and a trajectory shaped to "
            "hold dynamic pressure inside the structural-thermal "
            "envelope rather than chasing maximum speed. Step four, "
            "what would confirm it: a subscale demonstrator completing "
            "a 30-minute sustained cruise with post-flight inspection "
            "showing thermal margins intact. Step five, what would kill "
            "it: if combined-cycle handoff proves uncontrollable at "
            "full scale, or if maintenance of the cooled structures "
            "between flights costs more than the speed is worth to "
            "passengers. What this does not claim: it does not claim "
            "affordable tickets or regulatory approval - those are "
            "separate mountains. The claim is strictly the sustained "
            "thermal-mechanical feasibility of the vehicle."
        ),
        "citations": [CIT_NASA],
    },
    {
        "key": "supersonic_economics",
        "name": "Supersonic Civil Flight Economics",
        "group": "Transport",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "problem": (
            "How to fly passengers faster than sound without repeating "
            "the Concorde story: a beautiful aircraft retired in 2003 "
            "because its fuel burn per seat-mile cost several times a "
            "subsonic jet and its sonic boom banned it from flying "
            "supersonic over land - cutting off most routes."
        ),
        "background": (
            "Concorde cruised at Mach 2 with afterburners, burning "
            "roughly three times the fuel per passenger-mile of a 747 "
            "while carrying 100 seats. The 1973 US overland supersonic "
            "ban, driven by boom complaints, confined it to "
            "transatlantic routes. New startups promise Mach 1.4 to 1.7 "
            "airliners with modern engines - no afterburner, better "
            "aerodynamics - and NASA low-boom demonstrators aim to "
            "prove a shaped boom quiet enough to revisit the overland "
            "rule. The economics remain unforgiving: supersonic drag "
            "is physics, fuel is most of an airline cost, and business "
            "travelers - the target market - now have video calls. "
            "Several well-funded attempts have already folded."
        ),
        "why_it_matters": (
            "Speed is the one dimension of air travel that has gone "
            "backward since the 1970s. Cracking the economics would "
            "reopen it - and the low-boom, efficient-engine technology "
            "transfers directly to quieter subsonic aircraft and better "
            "propulsion generally."
        ),
        "sig_pointer": (
            "The Signature approach sizes the aircraft to the boom "
            "rule, not to nostalgia: a small low-boom design whose "
            "economics work on premium transoceanic routes first, "
            "earning the overland case with measured data instead of "
            "promises."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the business closes only "
            "if the aircraft is allowed over land, and regulators move "
            "only on measured boom data - so the first product is a "
            "flying boom-measurement campaign with seats attached. Step "
            "two, the reasoning path: build the smallest viable "
            "low-boom airliner (dozens of seats, not hundreds), prove "
            "the boom signature block by block with instrumented "
            "flyovers, and let the data argue the regulation. Step "
            "three, the proposed mechanism: a shaped-fuselage Mach 1.4 "
            "design with modern medium-bypass engines, composite "
            "structure, and SAF compatibility from day one; initial "
            "service on transoceanic premium routes to build the "
            "operating record; then a petition for overland corridors "
            "backed by years of community noise measurements. Step "
            "four, what would confirm it: certified boom levels at or "
            "below the demonstrated annoyance threshold with load "
            "factors and fares covering operating cost on real routes. "
            "Step five, what would kill it: if the low-boom shaping "
            "costs more drag than modeled, or if regulators decline "
            "regardless of data. What this does not claim: it does not "
            "claim mass-market supersonic travel - the claim is a "
            "sustainable premium niche that funds the technology "
            "forward."
        ),
        "citations": [CIT_NASA],
    },
    {
        "key": "hyperloop",
        "name": "Vacuum-Tube High-Speed Transport",
        "group": "Transport",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "problem": (
            "How to run passenger pods through near-vacuum tubes at "
            "near-supersonic speed - the hyperloop concept - safely, "
            "comfortably, and cheaper than high-speed rail. The physics "
            "is attractive (no air drag, no weather), but the systems "
            "engineering of hundreds of kilometers of vacuum tube with "
            "people inside is unproven."
        ),
        "background": (
            "The 2013 white paper proposed pods at 700-plus mph in "
            "tubes held near 100 pascals - about a thousandth of "
            "atmospheric pressure - levitated magnetically or on air "
            "bearings, driven by linear motors. Test tracks have run "
            "pods at hundreds of km/h; no full-scale passenger system "
            "exists. The hard problems: the Kantrowitz limit (a pod "
            "in a tube chokes airflow like a piston unless bypassed), "
            "maintaining vacuum across a continental tube with "
            "thermal expansion joints, emergency egress from a sealed "
            "tube, switching pods between tubes at speed, and "
            "throughput - a pod every few seconds must match a train "
            "every few minutes to justify the civil cost. High-speed "
            "rail, the incumbent, already runs 300 km/h with a century "
            "of operating knowledge."
        ),
        "why_it_matters": (
            "Short-haul flights are the most carbon-intensive travel "
            "per mile and the most annoying. A working hyperloop would "
            "erase the time advantage of flying under 1,500 km while "
            "running on electricity - and prove that vacuum "
            "infrastructure can be built at civil scale."
        ),
        "sig_pointer": (
            "The Signature approach de-risks by de-speeding: a "
            "medium-vacuum, moderate-speed freight-first system that "
            "pays for the tube with cargo, proving vacuum operations "
            "and economics before any passenger ever boards."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the vacuum, the "
            "switching, and the emergency systems are the risks, not "
            "the top speed - so the first system should optimize for "
            "learning per dollar, not miles per hour. Step two, the "
            "reasoning path: freight does not care about comfort, "
            "egress, or windows, and containerized cargo pays real "
            "money for 500 km/h overnight delivery - let cargo fund "
            "the tube. Step three, the proposed mechanism: a "
            "medium-vacuum (not ultra-vacuum) tube at moderate speed "
            "with compressor-bypass pods, built first as a "
            "port-to-inland freight corridor, operating for years to "
            "prove vacuum maintenance, switching, and safety systems "
            "at revenue service before a passenger variant is even "
            "designed. Step four, what would confirm it: three years "
            "of freight operation at 99 percent dispatch reliability "
            "with audited cost per ton-km below trucking on the "
            "corridor. Step five, what would kill it: if tube "
            "maintenance and vacuum pumping energy exceed the model "
            "at real scale, or if throughput per tube cannot pay the "
            "civil debt. What this does not claim: it does not claim "
            "passenger hyperloop is near - it claims the freight-first "
            "path is the only honest way to find out."
        ),
        "citations": [CIT_IEA],
    },
    {
        "key": "megawatt_charging",
        "name": "Megawatt Charging for Heavy Trucks",
        "group": "Transport",
        "ladder_rank": 23,
        "ladder_tier": "compounded",
        "problem": (
            "How to recharge a long-haul electric truck in a driver "
            "rest break. A 500 kWh truck battery filled in 30 minutes "
            "needs a full megawatt of power - the draw of a small "
            "neighborhood - and a truck stop serving dozens of rigs "
            "would need a substation, not a service panel."
        ),
        "background": (
            "Passenger EVs charge at up to 350 kW today; the Megawatt "
            "Charging System standard targets up to 3.75 MW for heavy "
            "trucks. Battery-electric trucks work for regional routes "
            "with depot charging, but long-haul needs public "
            "megawatt charging along freight corridors. The barriers "
            "stack: grid interconnection queues measured in years, "
            "demand charges that punish spiky megawatt loads, cable "
            "and connector cooling at those currents, battery "
            "degradation from routine ultra-fast charging, and the "
            "chicken-and-egg of building chargers before the trucks "
            "arrive. Diesel, meanwhile, refuels in 15 minutes from "
            "infrastructure amortized decades ago."
        ),
        "why_it_matters": (
            "Trucking is a large share of transport emissions and one "
            "of the hardest to abate - hydrogen and e-fuels compete "
            "here too. If megawatt charging works economically, the "
            "cheapest zero-emission truck is battery-electric, and the "
            "freight system electrifies on economics alone."
        ),
        "sig_pointer": (
            "The Signature approach treats the truck stop as a grid "
            "asset: buffer batteries shave the megawatt spikes, the "
            "site sells grid services between trucks, and charging "
            "schedules sync with mandatory driver rest periods so the "
            "power profile is planned, not random."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the grid connection, not "
            "the charger, is the binding constraint - demand charges "
            "and interconnection delays kill more projects than any "
            "connector standard. Step two, the reasoning path: a "
            "stationary buffer battery turns spiky truck demand into a "
            "flat grid draw, and that same battery earns money from "
            "the grid when no truck is plugged in. Step three, the "
            "proposed mechanism: corridor charging plazas with "
            "multi-megawatt-hour buffers, chargers dispatched against "
            "truck telematics (the plaza knows each rig state of "
            "charge and arrival time an hour out), charging windows "
            "aligned to regulated driver rest breaks, and grid-service "
            "contracts covering the buffer economics. Step four, what "
            "would confirm it: a plaza running a year with truck "
            "throughput matching diesel-stop dwell times and audited "
            "energy cost per mile below diesel. Step five, what would "
            "kill it: if battery degradation under daily deep cycling "
            "of the buffer destroys the business case, or if fleets "
            "refuse schedule coordination. What this does not claim: "
            "it does not claim to beat diesel on every route today - "
            "the claim is corridor-by-corridor parity starting with "
            "the densest freight lanes."
        ),
        "citations": [CIT_IEA, CIT_BATTERY],
    },
    {
        "key": "autonomous_vehicle_safety",
        "name": "Autonomous Vehicle Safety at Scale",
        "group": "Transport",
        "ladder_rank": 24,
        "ladder_tier": "compounded",
        "problem": (
            "How to prove a self-driving car is safer than a human "
            "driver - and then deploy millions of them. RAND calculated "
            "that demonstrating even 20 percent better than human safety "
            "at 95 percent confidence needs hundreds of millions to "
            "billions of test miles, because fatal crashes are rare. "
            "After a decade of investment, no company operates a "
            "truly general self-driving car service at scale."
        ),
        "background": (
            "The field splits into robotaxi services in geofenced "
            "cities (operating today in limited areas), driver-assist "
            "systems on highways, and the long-promised general "
            "autonomy. US road deaths run about 1.1 per 100 million "
            "vehicle miles, and the RAND study estimated that proving "
            "a 20 percent improvement at 95 percent confidence needs "
            "on the order of 275 million test miles at the low end. "
            "The technical stack - lidar, radar, cameras, "
            "HD maps, prediction and planning software - handles the "
            "common cases well; the failures cluster in the long tail "
            "of rare events: emergency vehicles, construction zones, "
            "sensor-blinding weather. Regulation is fragmented across "
            "jurisdictions, liability law is unsettled, and public "
            "trust swings with each high-profile crash. The economic "
            "prize - removing the driver, the largest cost in "
            "ride-hailing and trucking - keeps the investment flowing "
            "despite the timeline slips."
        ),
        "why_it_matters": (
            "About 1.2 million people die on roads each year, the vast "
            "majority from human error. Proven-safer autonomy would be "
            "one of the great public-health advances of the century - "
            "plus mobility for the elderly and blind, and a "
            "restructuring of cities built around parking."
        ),
        "sig_pointer": (
            "The Signature approach stops counting miles and starts "
            "counting scenarios: a public, adversarial scenario "
            "library covering the long tail, with vehicles certified "
            "against scenarios rather than against odometers - plus "
            "freight-corridor deployment first, where the environment "
            "is simplest and the economics strongest."
        ),
        "signature_solution": (
            "Step one, state the assumptions: miles are the wrong "
            "metric because crashes are rare and miles are mostly "
            "empty repetition - safety evidence must come from "
            "scenario coverage, not odometer readings. Step two, the "
            "reasoning path: aviation certifies aircraft against "
            "enumerated failure scenarios, not billions of flight "
            "hours; autonomy needs the same shift from statistics to "
            "structured assurance. Step three, the proposed mechanism: "
            "an open, continuously extended scenario library (cut-ins, "
            "sensor failures, emergency vehicles, construction, "
            "adversarial pedestrians) with every scenario reproducible "
            "in simulation and on closed courses; vehicles earn "
            "operational domains scenario by scenario; deployment "
            "begins on hub-to-hub freight corridors - the simplest "
            "driving environment with the clearest economics. Step "
            "four, what would confirm it: a certified vehicle "
            "operating a corridor for a year with incident rates "
            "below the human baseline on the same corridor, with all "
            "disengagements published. Step five, what would kill it: "
            "if the scenario space proves effectively infinite - new "
            "failure modes appearing faster than the library grows - "
            "or if simulation-to-reality gaps stay uncloseable. What "
            "this does not claim: it does not claim general autonomy "
            "is near, and it does not claim scenarios replace real-"
            "world monitoring - the claim is only that certification "
            "must be scenario-shaped to ever terminate."
        ),
        "citations": [CIT_AV],
    },
    {
        "key": "drone_delivery",
        "name": "Urban Drone Delivery at Scale",
        "group": "Transport",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "problem": (
            "How to deliver millions of small packages by drone in a "
            "city without the noise, safety risk, and air-traffic chaos "
            "making it politically impossible. Demonstrations deliver "
            "thousands of packages; a city needs millions per day with "
            "airline-grade safety over people heads."
        ),
        "background": (
            "Delivery drones work technically: multirotor and fixed-wing "
            "hybrids carry a few kilograms for tens of kilometers, and "
            "operators run medical and suburban delivery in several "
            "countries. The scaling walls are well known. Noise: "
            "high-frequency rotor buzz annoys far out of proportion to "
            "its decibels, and thousands of daily overflights would be "
            "a political event. Safety: a 25 kg aircraft failing over a "
            "crowd must demonstrate failure rates near one in a million "
            "flight hours. Air traffic: beyond-visual-line-of-sight "
            "operations need unmanned traffic management that barely "
            "exists. Energy: a drone uses roughly 0.1 kWh per delivery, "
            "efficient per package but trivial against a van carrying "
            "150. The unit economics only work at high utilization, "
            "which is exactly when the noise and traffic problems peak."
        ),
        "why_it_matters": (
            "Last-mile delivery is the most expensive and polluting leg "
            "of e-commerce, and cities keep growing denser. A working "
            "drone layer would cut delivery vans, speed medical "
            "logistics, and prove that low-altitude airspace can be a "
            "managed public utility rather than a free-for-all."
        ),
        "sig_pointer": (
            "The Signature approach designs the airspace before the "
            "aircraft: fixed sky-lane corridors over railways and "
            "rivers, rooftop ports as the only takeoff and landing "
            "points, and a noise budget per corridor enforced like "
            "pollution permits - the drones then become interchangeable "
            "commodities inside a managed system."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the vehicle is not the "
            "problem - managed airspace is - so the design starts with "
            "the corridors, the ports, and the noise budget, and the "
            "drone is specified last. Step two, the reasoning path: "
            "cities already manage scarce shared resources (road lanes, "
            "radio spectrum, water) with corridors and permits; "
            "low-altitude airspace needs the same treatment before "
            "scale, not after. Step three, the proposed mechanism: "
            "designated sky lanes following existing linear "
            "infrastructure, rooftop vertiports on commercial buildings "
            "as the only legal endpoints, per-corridor daily noise and "
            "flight budgets auctioned like spectrum, and standardized "
            "detect-and-avoid plus parachute recovery as the price of "
            "admission for any operator. Step four, what would confirm "
            "it: a pilot district running a year with published noise "
            "complaints, incident rates, and cost per delivery all "
            "within the permitted budgets. Step five, what would kill "
            "it: if residents reject even corridor-confined operations, "
            "or if the port infrastructure cost per delivery never "
            "clears the van alternative. What this does not claim: it "
            "does not claim drones replace vans wholesale - the claim "
            "is a managed aerial layer for the time-critical fraction "
            "of deliveries."
        ),
        "citations": [CIT_NASA, CIT_IEA],
    },
    {
        "key": "cheap_tunneling",
        "name": "Ten-Times-Cheaper Tunneling",
        "group": "Transport",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "problem": (
            "How to bore tunnels at a tenth of today cost. A mile of "
            "urban subway can exceed a billion dollars in the US, which "
            "is why so little gets built. Tunnel boring machines are "
            "mature technology, yet costs keep rising - the problem is "
            "systems and process, not the cutter head."
        ),
        "background": (
            "Modern TBMs are marvels: 15-meter-diameter machines that "
            "grind through rock and install concrete lining as they go. "
            "Yet megaproject costs are dominated by everything around "
            "the machine - stations, utility relocation, labor rules, "
            "permitting, risk contingencies, and bespoke designs for "
            "every project. Madrid built subway cheaply in the 2000s "
            "with standardized stations and 24-hour work; most cities "
            "did not copy the recipe. New entrants propose smaller "
            "diameter tunnels, continuous boring without stopping to "
            "build the lining, automated muck handling, and "
            "electric machines with no diesel logistics underground. "
            "The prize: if tunneling cost like trenching, cities could "
            "bury traffic, freight, and utilities as a matter of "
            "routine."
        ),
        "why_it_matters": (
            "Surface space in cities is the binding constraint on "
            "housing, transit, and quality of life. Cheap tunneling "
            "unlocks the third dimension: underground transit, freight, "
            "and utilities that do not compete with streets and parks - "
            "a civilizational capacity multiplier."
        ),
        "sig_pointer": (
            "The Signature approach standardizes the hole: one small "
            "diameter, one lining system, one machine design repeated "
            "hundreds of times - treating tunneling as manufactured "
            "product with a learning curve instead of a bespoke "
            "megaproject."
        ),
        "signature_solution": (
            "Step one, state the assumptions: cost lives in "
            "bespoke-ness - every tunnel a unique megaproject cannot "
            "learn, so the fix is repetition of an identical system. "
            "Step two, the reasoning path: manufacturing beats "
            "construction on cost whenever the product repeats; the "
            "tunnel must become a product with version numbers, not a "
            "project with a name. Step three, the proposed mechanism: "
            "a single standardized small-diameter system (one TBM "
            "design, one precast lining, one station kit), continuous "
            "boring with simultaneous lining, electric everything, "
            "and a standing crew that moves from tunnel to tunnel "
            "accumulating the learning curve instead of disbanding. "
            "Step four, what would confirm it: cost per kilometer "
            "falling on a documented curve across the first ten "
            "deployments toward the order-of-magnitude target. Step "
            "five, what would kill it: if geology variability defeats "
            "standardization - every city ground proving truly unique "
            "- or if station and utility costs, not the bore itself, "
            "dominate regardless. What this does not claim: it does "
            "not claim geology can be ignored - the claim is that "
            "process standardization captures most of the prize even "
            "with geological adaptation at the margins."
        ),
        "citations": [CIT_IEA],
    },
    {
        "key": "self_healing_concrete",
        "name": "Self-Healing Concrete at Scale",
        "group": "Materials",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "problem": (
            "How to make concrete repair its own cracks before water "
            "reaches the steel inside. Cracks up to about half a "
            "millimeter can be healed by bacteria that precipitate "
            "limestone - demonstrated in labs and pilots - but no "
            "formulation has yet survived the cost, scale, and "
            "decades-long proof that the construction industry demands."
        ),
        "background": (
            "Concrete cracks; water enters; rebar rusts, expands, and "
            "spalls the concrete from inside - the number-one "
            "durability failure of infrastructure. In 2015 researchers "
            "demonstrated bioconcrete: limestone-producing bacteria "
            "(Sporosarcina pasteurii and relatives) plus their food "
            "encapsulated in the mix, germinating when cracks let "
            "water in and sealing them with calcium carbonate. Parallel "
            "routes use encapsulated polymers or mineral admixtures. "
            "The gaps to scale: the bacteria and capsules add cost to "
            "the cheapest structural material on Earth, healing is "
            "limited to narrow cracks, long-term field data spans "
            "years not decades, and building codes have no category "
            "for living materials."
        ),
        "why_it_matters": (
            "Concrete infrastructure represents the largest capital "
            "stock humanity owns, and much of it is aging past design "
            "life simultaneously. Self-healing concrete would extend "
            "service life by decades, cut the maintenance bill, and "
            "avoid the enormous carbon cost of demolishing and "
            "rebuilding."
        ),
        "sig_pointer": (
            "The Signature approach does not ask all concrete to heal: "
            "it targets the failure points - joints, water-retaining "
            "structures, and marine exposure - with a two-part system "
            "where cheap mineral healing handles hairlines and "
            "bacterial capsules handle the wider cracks, each used "
            "only where its economics close."
        ),
        "signature_solution": (
            "Step one, state the assumptions: universal self-healing "
            "concrete cannot beat plain concrete on price, so the "
            "product must be targeted at the structures where "
            "cracking costs the most. Step two, the reasoning path: "
            "a two-tier system matches the crack distribution - "
            "mineral admixtures autogenously heal the finest cracks "
            "for nearly free, while encapsulated bacteria are "
            "reserved for the wider cracks that actually threaten "
            "rebar. Step three, the proposed mechanism: a standard "
            "mineral-healing base mix for all structural concrete, "
            "plus bacterial capsule dosing specified only for "
            "high-exposure elements (marine, water-retaining, joints), "
            "with healing verified by embedded crack monitors on "
            "flagship structures building the decades-long dataset "
            "codes require. Step four, what would confirm it: "
            "instrumented structures showing sealed cracks and zero "
            "rebar corrosion initiation at ten years against "
            "control sections. Step five, what would kill it: if "
            "capsule survival through mixing and decades of dormancy "
            "proves unreliable in real batching plants, or if healed "
            "zones fail under cyclic loading. What this does not "
            "claim: it does not claim concrete becomes maintenance-"
            "free - the claim is a targeted, code-accepted extension "
            "of service life where it pays."
        ),
        "citations": [CIT_NACE],
    },
    {
        "key": "waste_transmutation",
        "name": "Nuclear Waste Transmutation",
        "group": "Energy",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "problem": (
            "How to shrink the million-year problem of nuclear waste "
            "to a centuries problem. Spent fuel minor actinides stay "
            "dangerous for hundreds of thousands of years; bombarding "
            "them with fast neutrons can fission them into "
            "shorter-lived products - demonstrated in principle, never "
            "deployed as a system."
        ),
        "background": (
            "A ton of spent fuel contains uranium and plutonium that "
            "can be recycled, plus a few kilograms of minor actinides "
            "(neptunium, americium, curium) that dominate the "
            "long-term radiotoxicity. Americium-241, a representative "
            "minor actinide, has a 432-year half-life, against about 30 "
            "years for the cesium-137 fission product that dominates "
            "shorter-term heat. Fast-neutron reactors can burn "
            "actinides as fuel, and accelerator-driven subcritical "
            "systems (like Belgium MYRRHA project) aim to do it "
            "without a critical reactor. The obstacles: separating "
            "actinides from spent fuel needs advanced reprocessing "
            "with its own proliferation sensitivities, the "
            "transmutation systems are first-of-a-kind nuclear builds "
            "with first-of-a-kind costs, and several countries have "
            "simply chosen deep geological burial instead - Finland "
            "Onkalo repository is under construction. Transmutation "
            "does not eliminate the need for a repository; it shrinks "
            "what goes in it and for how long."
        ),
        "why_it_matters": (
            "The waste timescale is the deepest public objection to "
            "nuclear power - asking geology to guarantee a million "
            "years strains credibility. Cutting the hazard to "
            "centuries changes the moral and political calculus of "
            "the largest clean baseload source available."
        ),
        "sig_pointer": (
            "The Signature approach treats transmutation as fuel-cycle "
            "plumbing, not a moonshot reactor: standardize actinide "
            "separation once, burn the product in a fleet of identical "
            "fast burner modules, and let the repository shrink as the "
            "burners accumulate operating history."
        ),
        "signature_solution": (
            "Step one, state the assumptions: no single machine solves "
            "this - the system is separation plus burning plus "
            "disposal, and it fails if any leg is bespoke. Step two, "
            "the reasoning path: make the burner boring - a small, "
            "identical, factory-built fast module whose only job is "
            "eating actinides - and put the innovation budget into "
            "the separation chemistry that feeds it. Step three, the "
            "proposed mechanism: one standardized aqueous separation "
            "flowsheet deployed at existing reprocessing sites, "
            "actinide fuel fabricated into burner assemblies, and a "
            "fleet of identical subcritical or fast burner modules "
            "co-located with the separation plants to avoid transport, "
            "with the residual waste form qualified for the same "
            "repository at far lower heat load. Step four, what would "
            "confirm it: a burner module destroying actinides at a "
            "measured rate matching the separation plant output, with "
            "the repository heat-load model independently validated. "
            "Step five, what would kill it: if separation losses keep "
            "the un-transmuted fraction above the level that changes "
            "the repository case, or if burner economics never clear "
            "the cost of simply building the bigger repository. What "
            "this does not claim: it does not claim waste disappears, "
            "and it does not take a position on reprocessing politics "
            "- the claim is strictly the engineering feasibility of "
            "shrinking the hazard timescale."
        ),
        "citations": [CIT_ITER, CIT_NASA],
    },
    {
        "key": "smr_cost_parity",
        "name": "Small Modular Reactors at Cost Parity",
        "group": "Energy",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "problem": (
            "How to build nuclear reactors small enough to factory-"
            "manufacture - typically under 300 MW - at a cost per "
            "kilowatt-hour that competes with gas and renewables. The "
            "first Western SMR projects have seen costs balloon like "
            "their giant predecessors, and none has yet demonstrated "
            "the factory learning curve the concept promises."
        ),
        "background": (
            "Large nuclear plants failed economically largely because "
            "each was a bespoke megaproject built once. SMRs invert "
            "the logic: small enough to ship, identical units from a "
            "factory, passive safety systems needing no operator "
            "action or external power. Dozens of designs exist - light "
            "water, high-temperature gas, molten salt, sodium-cooled. "
            "But the first movers stumbled: the cancelled Utah "
            "NuScale project saw its cost estimates roughly double, "
            "reminding everyone that first-of-a-kind nuclear is "
            "expensive regardless of size, with overnight costs "
            "estimated in the high single thousands of dollars per "
            "kilowatt. The open question is "
            "whether factory repetition actually delivers the "
            "learning curve, or whether nuclear regulation and "
            "financing impose a cost floor no design can duck."
        ),
        "why_it_matters": (
            "If SMRs hit cost parity, clean baseload power becomes a "
            "manufactured product deployable anywhere - for grids, "
            "industrial heat, desalination, and hydrogen. If they do "
            "not, nuclear stays a bespoke luxury and the transition "
            "leans entirely on renewables plus storage."
        ),
        "sig_pointer": (
            "The Signature approach treats the factory as the reactor "
            "design: freeze one design, build the production line "
            "before the tenth unit is ordered, and sell the first "
            "units to buyers who value the heat and the reliability "
            "premium - not to merchant power markets that punish "
            "first-of-a-kind costs."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the product is not the "
            "reactor, it is the reactor factory - unit one will be "
            "expensive no matter what, so the business plan must "
            "survive unit one. Step two, the reasoning path: sell the "
            "first units where the value of firm clean heat exceeds "
            "the power price - industrial sites, remote mines, "
            "desalination plants - and let merchant-grid parity arrive "
            "with the learning curve instead of being demanded of "
            "unit one. Step three, the proposed mechanism: a single "
            "frozen light-water-based design (licensing familiarity "
            "beats thermodynamic elegance for unit one), factory "
            "tooling sized for dozens of units per year from the "
            "start, and anchor customers contracted for heat-plus-"
            "power before the factory breaks ground. Step four, what "
            "would confirm it: audited overnight cost per kilowatt "
            "falling across the first ten units on a published curve, "
            "with construction schedules measured in months. Step "
            "five, what would kill it: if regulatory ratcheting "
            "re-customizes every unit, or if financing costs for "
            "first-of-a-kind nuclear swamp the factory savings. What "
            "this does not claim: it does not claim SMRs are cheap "
            "today, and it does not claim any particular coolant wins "
            "- the claim is only that the factory-learning path is "
            "the one that can be tested honestly."
        ),
        "citations": [CIT_IEA, CIT_DOE_SHOT],
    },
    {
        "key": "asteroid_mining",
        "name": "Asteroid Mining Economics",
        "group": "Space",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "problem": (
            "How to make mining asteroids pay. A single metallic "
            "asteroid can hold more platinum-group metals than ever "
            "mined on Earth, and water-rich asteroids could refuel "
            "spacecraft - but prospecting, extraction, and return all "
            "remain PowerPoint-deep, and two well-funded startups "
            "already failed trying."
        ),
        "background": (
            "Near-Earth asteroids fall into useful classes: C-type "
            "(water and organics), S-type (silicates and some metal), "
            "M-type (nickel-iron, sometimes enriched in platinum-group "
            "metals). The economic dreams: return platinum worth tens "
            "of thousands of dollars per kilogram, or mine water for "
            "propellant depots so deep-space missions never haul fuel "
            "up from Earth. Planetary Resources and Deep Space "
            "Industries both folded without mining anything. The "
            "problems: we have visited only a handful of asteroids "
            "(Hayabusa2 and OSIRIS-REx returned grams), ore grades are "
            "inferred from meteorites and spectra, microgravity mining "
            "has no demonstrated method, and flooding Earth with space "
            "platinum would crash the price that justified the mission. "
            "The arithmetic is stark: launch costs near 1,500 dollars "
            "per kilogram against platinum-group metals near 30,000 "
            "dollars per kilogram."
        ),
        "why_it_matters": (
            "Earth mines are finite and increasingly destructive; space "
            "industry needs materials that never come down the gravity "
            "well. Whoever cracks asteroid mining first owns the "
            "feedstock of the space economy - and a demonstration that "
            "resources are not a zero-sum planetary inheritance."
        ),
        "sig_pointer": (
            "The Signature approach mines water first and metals "
            "never - at least not for Earth: water becomes propellant "
            "sold in orbit where launch cost makes it precious, while "
            "metal extraction waits for an in-space manufacturing "
            "customer that actually needs the metal up there."
        ),
        "signature_solution": (
            "Step one, state the assumptions: returning material to "
            "Earth gravity well fights physics and economics at once, "
            "so the first viable mine sells to customers already in "
            "space. Step two, the reasoning path: a kilogram of water "
            "delivered to high orbit is worth the launch cost avoided "
            "- thousands of dollars - which makes even a crude water "
            "mine economic long before any platinum scheme closes. "
            "Step three, the proposed mechanism: prospect carbonaceous "
            "near-Earth asteroids spectroscopically, land a solar-"
            "thermal extraction package that bakes water from regolith "
            "and electrolyzes part of it to propellant, and sell to "
            "satellite servicing and lunar missions from an orbital "
            "depot - with metals stockpiled on site as a byproduct "
            "awaiting future in-space manufacturing demand. Step four, "
            "what would confirm it: a demonstration mission returning "
            "a measured water-extraction rate and energy budget from a "
            "real asteroid surface, plus signed depot customers. Step "
            "five, what would kill it: if water turns out bound too "
            "tightly in the accessible regolith, or if launch costs "
            "fall so far that Earth water undercuts the space mine. "
            "What this does not claim: it does not claim platinum "
            "riches or Earth-return economics - those are explicitly "
            "deferred to a later era with in-space customers."
        ),
        "citations": [CIT_NASA, CIT_STARSHOT],
    },
    {
        "key": "space_debris",
        "name": "Space Debris Removal at Scale",
        "group": "Space",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "problem": (
            "How to clean up Earth orbit before collisions cascade. "
            "About 36,500 objects larger than 10 cm are tracked, plus "
            "perhaps a million lethal-but-untracked fragments between 1 "
            "and 10 cm. Each collision breeds more debris - the "
            "Kessler syndrome - and demonstrations have removed single "
            "objects at high cost, not the thousands needed."
        ),
        "background": (
            "The 2009 Iridium-Cosmos collision and the 2007 Chinese "
            "anti-satellite test each added thousands of tracked "
            "fragments. Mega-constellations now add thousands of "
            "satellites per year, each a future debris source. Removal "
            "concepts demonstrated or proposed: nets, harpoons, robotic "
            "arms, tethers, and just nudging dead satellites into "
            "disposal orbits; the European ClearSpace-1 mission aims to "
            "grab a single 100 kg upper stage. The economics are "
            "brutal: rendezvous with an uncooperative tumbling object "
            "costs tens of millions per removal, nobody is clearly "
            "liable to pay, and removing the roughly 50 highest-risk "
            "objects - the ones models say would stabilize the "
            "environment - has no funded customer."
        ),
        "why_it_matters": (
            "Orbit is infrastructure now - weather, GPS, communications, "
            "science - and a cascade could render the most useful "
            "altitudes unusable for generations. Cleanup is the "
            "prerequisite for everything else humanity wants to do in "
            "space."
        ),
        "sig_pointer": (
            "The Signature approach industrializes the rendezvous: one "
            "standardized servicer design, refueled in orbit, working "
            "down a ranked risk list - and funded by making debris "
            "removal a license condition for new constellations, so "
            "the polluters pay per launch."
        ),
        "signature_solution": (
            "Step one, state the assumptions: technology demonstrations "
            "are done - the missing pieces are unit cost and a paying "
            "customer, both of which are institutional, not technical. "
            "Step two, the reasoning path: models agree that removing "
            "a few dozen of the most massive derelicts in crowded "
            "sun-synchronous orbits disproportionately cuts future "
            "collisions, so the job is finite and rankable. Step three, "
            "the proposed mechanism: a standardized robotic servicer "
            "with refuelable propulsion, built in a small production "
            "run, working the ranked list orbit by orbit; funding from "
            "a per-launch orbital-use fee hypothecated to removal, so "
            "constellation operators pay in proportion to their "
            "contribution to the problem. Step four, what would confirm "
            "it: a servicer removing five ranked objects in one "
            "mission lifetime at a published cost per removal trending "
            "down, plus a measurable flattening of the tracked-object "
            "growth curve. Step five, what would kill it: if "
            "rendezvous with tumbling derelicts proves un-automatable "
            "at the assumed cost, or if international liability "
            "disputes block touching other nations hardware "
            "indefinitely. What this does not claim: it does not claim "
            "to remove the million small fragments - that is stated as "
            "currently infeasible - the claim covers the large, "
            "ranked, removable objects that drive the cascade."
        ),
        "citations": [CIT_ESA_DEBRIS, CIT_NASA],
    },
    {
        "key": "space_elevator",
        "name": "The Space Elevator",
        "group": "Space",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "problem": (
            "How to build a ribbon from Earth surface to beyond "
            "geostationary orbit that climbers ascend like elevators - "
            "cutting launch cost to electricity prices. The ribbon "
            "needs a specific strength near 50 megayuri (gigapascals "
            "per gram per cubic centimeter); the best bulk carbon "
            "nanotube fibers manage a small fraction of that, and no "
            "one has made a continuous defect-free ribbon at any "
            "length."
        ),
        "background": (
            "Tsiolkovsky imagined the tower in 1895; Arthur C. Clarke "
            "popularized the elevator in 1979. The physics is settled: "
            "a counterweight past geostationary orbit holds the ribbon "
            "taut by centrifugal force, climbers crawl up on laser or "
            "solar power, and payload cost falls toward the energy "
            "price. The material is the wall: steel snaps under its "
            "own weight at a fraction of the needed length, and only "
            "carbon nanotubes or graphene in theory clear the bar. "
            "Lab nanotubes are phenomenally strong individually; spun "
            "into macroscopic fibers they lose an order of magnitude "
            "to defects and slip. Competitions for climber prototypes "
            "and ribbon materials ran for years with incremental "
            "results. Skeptics note that even with the ribbon, "
            "micrometeorites, space weather, and terrorism make a "
            "single-point-of-failure space artery a daunting system."
        ),
        "why_it_matters": (
            "Chemical rockets will always cost roughly their propellant "
            "and hardware; an elevator breaks the rocket equation "
            "entirely. It is the difference between visiting space and "
            "commuting to it - the infrastructure that makes everything "
            "else in this database space entries affordable."
        ),
        "sig_pointer": (
            "The Signature approach stops waiting for the perfect "
            "fiber and builds the elevator in generations: first a "
            "lunar elevator from proven materials, then an orbital "
            "ring with short tethers, letting each generation fund and "
            "teach the next while fiber manufacturing matures."
        ),
        "signature_solution": (
            "Step one, state the assumptions: the Earth elevator "
            "ribbon does not exist as a manufacturable material, so a "
            "program staked entirely on it cannot start - the path "
            "must generate value with today materials. Step two, the "
            "reasoning path: the Moon needs only about a sixth of the "
            "strength (low gravity, no atmosphere), and existing fibers "
            "like Zylon or Dyneema clear that bar - a lunar elevator is "
            "buildable now and teaches every discipline the Earth "
            "version needs. Step three, the proposed mechanism: phase "
            "one, a lunar surface-to-libration-point tether moving "
            "regolith and supplies; phase two, momentum-exchange "
            "tethers in Earth orbit catching payloads from suborbital "
            "launchers; phase three, the full Earth ribbon, attempted "
            "only when continuous fiber production demonstrably holds "
            "the required specific strength over kilometer lengths. "
            "Step four, what would confirm it: an operating lunar "
            "tether moving cargo for a year, plus fiber production "
            "hitting the strength-length milestone in independent "
            "testing. Step five, what would kill it: if defect-free "
            "fiber scaling hits a fundamental length limit, or if the "
            "lunar tether economics never close without the Earth "
            "ribbon they were meant to precede. What this does not "
            "claim: it does not claim the Earth elevator is near - it "
            "claims the generational path is the only program that can "
            "honestly begin."
        ),
        "citations": [CIT_NASA],
    },
    {
        "key": "interstellar_propulsion",
        "name": "Interstellar Propulsion",
        "group": "Space",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "problem": (
            "How to send anything to another star within a human "
            "lifetime. Chemical rockets would take tens of thousands of "
            "years to Proxima Centauri; even the fastest spacecraft "
            "flown would take millennia. Breakthrough Starshot proposes "
            "gram-scale sails pushed by lasers to 20 percent of light "
            "speed - a 20-year crossing - but the laser array, sail "
            "materials, and interstellar dust survival are all unsolved."
        ),
        "background": (
            "Interstellar concepts span the spectrum: Project Daedalus "
            "(1970s fusion-pulse starship), antimatter catalysis, "
            "Bussard ramjets (likely unworkable - drag exceeds thrust), "
            "and beamed propulsion. Starshot reframed the problem: do "
            "not send people or tons, send grams at relativistic "
            "speed. A gram at 0.2 c carries about 1.8 terajoules of "
            "kinetic energy - the launch energy of a small power "
            "station delivered in minutes by a 100-gigawatt phased "
            "laser array. The unsolved list: a sail that reflects "
            "99.999 percent of that laser without vaporizing, "
            "stability of the sail on the beam, surviving dust-grain "
            "impacts at 0.2 c (each grain hits like an artillery "
            "shell), and returning any data across four light-years "
            "with a gram-scale transmitter."
        ),
        "why_it_matters": (
            "Every star is currently unreachable, which makes humanity "
            "a single-point-of-failure species. Interstellar "
            "propulsion is the technology that converts the galaxy "
            "from scenery into destination - and the physics it "
            "forces (beamed energy, ultralight materials) pays off "
            "across the whole space program."
        ),
        "sig_pointer": (
            "The Signature approach treats Starshot as a technology "
            "program wearing a starship costume: build the laser array "
            "for solar-system propulsion first - pushing cargo sails "
            "around the inner system for profit - and let the "
            "interstellar shot be the graduation exercise of a mature "
            "beamed-energy infrastructure."
        ),
        "signature_solution": (
            "Step one, state the assumptions: a 100-gigawatt laser "
            "array cannot be justified for a single shot, so the "
            "array must pay for itself doing nearer-term work. Step "
            "two, the reasoning path: the same beamed-energy "
            "infrastructure that pushes gram sails to stars can push "
            "ton-scale cargo sails around the solar system fast and "
            "cheap - that is a business, and the business builds the "
            "array. Step three, the proposed mechanism: phase one, "
            "megawatt-class beamed propulsion for rapid inner-system "
            "cargo; phase two, gigawatt array pushing instrumented "
            "kilogram-scale sails to the outer planets in months; "
            "phase three, the full array and gram-scale interstellar "
            "probe, with sail materials and dust shielding proven on "
            "the nearer missions. Step four, what would confirm it: "
            "a laser-pushed sail demonstrating stable beam-riding and "
            "measured acceleration matching the beam model, at any "
            "scale, in space. Step five, what would kill it: if "
            "atmospheric beam distortion caps ground-based power "
            "delivery below the needed flux, or if dust-erosion "
            "models show no sail survives 0.2 c regardless of "
            "material. What this does not claim: it does not claim "
            "human interstellar travel - the claim is strictly "
            "instrumented gram-to-kilogram probes, with everything "
            "beyond that explicitly out of scope."
        ),
        "citations": [CIT_STARSHOT, CIT_NASA],
    },
    {
        "key": "mars_life_support",
        "name": "Closed-Loop Life Support for Mars",
        "group": "Space",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "problem": (
            "How to keep a crew alive on Mars without resupply from "
            "Earth. A crew of four needs about 0.84 kg of oxygen per "
            "person per day plus water and food; the ISS recycles about "
            "98 percent of water but only about half its oxygen (via "
            "the Sabatier reaction), and Mars adds dust, radiation, and "
            "a two-year resupply delay to every failure."
        ),
        "background": (
            "Biosphere 2 showed in the 1990s how hard closed ecology "
            "is - oxygen mysteriously declined and the crew struggled. "
            "The ISS took the physicochemical route: the Water Recovery "
            "System distills urine and humidity, the Oxygen Generation "
            "Assembly electrolyzes water, and Sabatier reactors combine "
            "exhaled CO2 with hydrogen to recover half the oxygen. For "
            "Mars, in-situ resource utilization changes the equation: "
            "MOXIE demonstrated making oxygen from Martian CO2 air in "
            "2021-2023, and water ice is confirmed at the poles and in "
            "mid-latitude glaciers. The unsolved part is the integrated "
            "system: full oxygen loop closure, food production (crops "
            "need light, water, and radiation shielding), dust "
            "mitigation (perchlorate-laden fines that destroy equipment "
            "and lungs), and reliability measured in years with no "
            "spare-parts truck coming."
        ),
        "why_it_matters": (
            "Mars is the nearest plausible second home, and every Mars "
            "architecture collapses without life support that closes "
            "the loop - shipping air and water across interplanetary "
            "space at thousands of dollars per kilogram cannot sustain "
            "a settlement. This is the problem whose solution turns "
            "expeditions into habitation."
        ),
        "sig_pointer": (
            "The Signature approach closes the loop in the order of "
            "mass payback: oxygen from the air first (MOXIE scaled), "
            "water from ice second, food last - with each loop proven "
            "on the Moon, where rescue is three days away instead of "
            "two years, before Mars commits lives to it."
        ),
        "signature_solution": (
            "Step one, state the assumptions: loop closure must be "
            "earned in mass-payback order - the heaviest consumable "
            "first - and no loop flies crew until it has run uncrewed "
            "for longer than the mission it supports. Step two, the "
            "reasoning path: oxygen from Martian air is the highest "
            "leverage (MOXIE already proved the chemistry), water "
            "recycling is flight-proven on ISS, and food is last "
            "because crops are the least mature loop - sequence the "
            "program by this ranking, not by romance. Step three, the "
            "proposed mechanism: scaled solid-oxide electrolysis for "
            "oxygen from atmospheric CO2, closed water loops adapted "
            "from ISS with Martian-ice feedstock, and a crop module "
            "using LED-lit stacked growth with perchlorate-washed "
            "regolith as substrate - the entire stack first operated "
            "for two full years at a lunar proving ground under "
            "real dust and radiation. Step four, what would confirm "
            "it: the lunar system supporting its rated crew-load of "
            "consumables for 24 continuous months with measured "
            "closure fractions (oxygen above 95 percent, water above "
            "98 percent) and zero unplanned resupply. Step five, what "
            "would kill it: if perchlorate chemistry poisons the "
            "water loop irreversibly, or if crop productivity under "
            "real space radiation falls below the caloric breakeven. "
            "What this does not claim: it does not claim a "
            "self-sufficient Mars colony - the claim is a "
            "resupply-independent surface mission, the necessary "
            "first step."
        ),
        "citations": [CIT_NASA],
    },
]
