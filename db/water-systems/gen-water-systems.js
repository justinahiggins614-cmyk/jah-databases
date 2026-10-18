/* JAH Water Systems Database generator — jahdb-water-systems-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: seed -> full water entry. 1,000,000 address space (seed % 1M).
   Records are either sourced (real, verifiable water knowledge) or Signature-generated
   (homegrown system designs/plans), labeled in `origin`. Never fabricates real-world facts. */
(function () {
'use strict';
function prng(seed) { var a = (seed >>> 0) || 1; return function () { a |= 0; a = (a + 0x6D2B79F5) | 0; var t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
function pick(a, r) { return a[(r() * a.length) | 0]; }
function ri(r, a, b) { return a + ((r() * (b - a + 1)) | 0); }
function shuffle(a, r) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = (r() * (i + 1)) | 0; var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
function interleave(lists) { var out = [], i = 0, more = true; while (more) { more = false; for (var k = 0; k < lists.length; k++) { if (i < lists[k].length) { out.push(lists[k][i]); more = true; } } i++; } return out; }

var SLUG = 'water-systems';
var PREFIX = 'JAH-WTR-';
var VERSION = 'jahdb-water-systems-1.0';
var RECORD_KIND = 'water entry';
var CATS = ['water-cycle', 'treatment', 'infrastructure', 'conservation', 'wastewater'];

/* ================= REAL (sourced) data: [title, key_points, body] ================= */
var REAL_CYCLE = [
['Evaporation', 'Liquid water becomes vapor, powered by solar energy; the largest source is the ocean surface', 'Evaporation lifts water from oceans, lakes, and soil into the atmosphere as vapor. Warmer air holds more vapor, which is why evaporation intensifies with heat. Transpiration from plants adds a second great flow, together called evapotranspiration.'],
['Condensation', 'Water vapor cools into liquid droplets, forming clouds and dew', 'Rising vapor cools with altitude until it condenses on tiny particles, forming cloud droplets. When droplets grow heavy enough, they fall as precipitation. Dew is condensation forming directly on cool surfaces overnight.'],
['Precipitation', 'Rain, snow, sleet, and hail return water to the surface', 'Precipitation takes many forms \u2014 rain, snow, sleet, hail, drizzle \u2014 depending on temperature through the air column. Mountains wring moisture from air masses, creating wet windward slopes and dry rain shadows.'],
['Infiltration and groundwater', 'Water soaks into soil and rock, recharging aquifers that store most liquid freshwater', 'Infiltrating water percolates downward until it reaches saturated rock \u2014 an aquifer. Groundwater moves slowly, sometimes over centuries, and feeds springs and wells. About 97% of Earth\u2019s water is salty ocean water; most of the remainder is locked in ice, leaving a small fraction as accessible freshwater.'],
['Runoff and watersheds', 'Surface water flows downhill into streams and rivers; a watershed is all land draining to one outlet', 'Runoff gathers into rills, streams, and rivers that carry water \u2014 and sediment \u2014 to lakes and seas. Every point on land belongs to a watershed; what happens upstream shapes everything downstream.'],
['The water cycle as a whole', 'A continuous loop driven by the sun: evaporation, condensation, precipitation, collection', 'Water is never created or destroyed in the cycle, only moved and transformed. Human withdrawals, dams, and climate shifts reroute the loop, which is why watershed-scale management matters.'],
['The ocean\u2019s role', 'Oceans hold about 97% of Earth\u2019s water and drive weather through evaporation and currents', 'Ocean evaporation feeds most rainfall; currents redistribute heat worldwide. The ocean is also the climate\u2019s great buffer, absorbing heat and carbon dioxide.'],
['Glaciers and ice caps', 'Most freshwater is locked in ice; meltwater feeds rivers billions depend on', 'Ice sheets and mountain glaciers store the bulk of freshwater. Their seasonal melt sustains rivers through dry months \u2014 a supply threatened as glaciers retreat.'],
['The Amazon\u2019s flying rivers', 'The Amazon rainforest recycles moisture inland, watering distant farmland', 'Trees transpire vast volumes of vapor that ride air currents \u2014 \u201cflying rivers\u201d \u2014 carrying rain deep into the continent. Deforestation weakens this pump.'],
['The Nile: a river civilization', 'One of the world\u2019s longest rivers, sustaining agriculture for millennia', 'The Nile\u2019s annual flood deposited fertile silt that built ancient Egyptian agriculture. The Aswan High Dam now regulates its flow, trading flood fertility for controlled irrigation and hydropower.']
];
var REAL_TREATMENT = [
['Coagulation and flocculation', 'Chemicals make fine particles clump into floc that can settle out', 'Coagulants neutralize the charges keeping tiny particles suspended; gentle mixing then builds them into fluffy floc. This first step removes the particles that make water cloudy.'],
['Sedimentation', 'Floc settles by gravity in quiet basins', 'Treated water rests in sedimentation basins while floc sinks to the bottom as sludge. Clear water flows off the top to filtration. Patience does the work \u2014 no energy required.'],
['Filtration', 'Water passes through sand, gravel, or membranes to trap remaining particles', 'Filters of sand and gravel \u2014 or modern membranes \u2014 catch what settling missed. Backwashing periodically cleans the media. Filtration is the barrier that makes disinfection reliable.'],
['Disinfection: chlorination', 'Chlorine kills pathogens; a residual protects water through the pipes', 'Chlorine or chloramine destroys bacteria and viruses. A small residual travels with the water, guarding against contamination in the distribution system. Dosing is carefully controlled to balance safety and taste.'],
['Disinfection: ultraviolet light', 'UV light inactivates pathogens without chemicals', 'UV reactors damage pathogen DNA so organisms cannot reproduce. No chemicals are added and no residual remains, so UV usually pairs with a secondary disinfectant for distribution.'],
['Reverse osmosis desalination', 'Pressure forces seawater through membranes that block salt', 'High-pressure pumps push seawater against semipermeable membranes; water passes, salt stays. Energy is the main cost, and brine disposal must be managed. It now supplies major cities in arid regions.'],
['Wastewater: primary treatment', 'Screens and settling remove solids from sewage', 'Bar screens catch debris, grit chambers settle sand, and primary clarifiers settle suspended solids. About half the suspended load is removed mechanically.'],
['Wastewater: secondary treatment', 'Microorganisms digest dissolved pollutants', 'Aeration basins feed oxygen to bacteria that consume organic waste \u2014 the activated-sludge process. Secondary clarifiers settle the biomass. This biological step does the heavy lifting of sewage treatment.'],
['Wastewater: tertiary treatment', 'Filtration and disinfection polish effluent for discharge or reuse', 'Tertiary steps \u2014 filtration, nutrient removal, disinfection \u2014 produce water clean enough for sensitive waterways or reuse. Advanced plants now produce near-drinking-quality water.'],
['Biosolids management', 'Treated sewage sludge becomes fertilizer or energy feedstock', 'Digesters stabilize sludge, killing pathogens and capturing biogas for energy. The resulting biosolids fertilize farmland under strict standards.']
];
var REAL_INFRA = [
['Dams', 'Barriers that store water, control floods, and generate hydropower', 'Dams impound rivers into reservoirs, smoothing seasonal flow into year-round supply. They generate hydropower and blunt floods, but trap sediment and block fish migration \u2014 trade-offs managed with fish ladders and environmental flows.'],
['The Hoover Dam', 'Completed 1936 on the Colorado River; an icon of water engineering', 'Hoover Dam\u2019s reservoir, Lake Mead, stores Colorado River water for cities and farms across the Southwest. Its hydropower plant was among the world\u2019s largest at completion.'],
['Aqueducts', 'Channels carrying water across distance by gravity', 'Roman aqueducts used precise gradients to move water for miles; modern aqueducts like California\u2019s State Water Project lift and carry water hundreds of miles to cities and farms.'],
['Reservoirs', 'Stored water buffering supply against dry seasons', 'Reservoirs bank wet-season flows for dry months. Operators balance supply, flood control, hydropower, and ecology \u2014 a constant negotiation.'],
['Water towers', 'Elevated tanks that pressurize distribution by gravity', 'A water tower\u2019s height creates pressure: every 2.3 feet of elevation adds about 1 psi. Towers also buffer demand spikes without oversizing pumps.'],
['Distribution mains', 'Pressurized pipe networks delivering treated water to taps', 'Mains, valves, and hydrants form the grid beneath streets. Utilities hunt leaks \u2014 some systems lose a fifth of their water underground \u2014 and replace aging pipe on decades-long cycles.'],
['Wells and groundwater pumping', 'Wells tap aquifers; overpumping lowers water tables', 'Wells from hand-dug to deep turbine supply farms and towns worldwide. Sustainable pumping stays within recharge; overdraft drops water tables and can collapse aquifer storage.'],
['Storm drains and sewers', 'Separate or combined systems carrying stormwater and sewage', 'Separate systems keep stormwater and sewage apart; combined sewers carry both and can overflow in heavy rain. Green infrastructure \u2014 rain gardens, permeable pavement \u2014 is easing the load.'],
['Levees and floodwalls', 'Embankments holding rivers within their channels', 'Levees protect floodplains but can raise flood heights downstream and fail catastrophically if overtopped. Modern practice pairs levees with floodplain restoration.'],
['Canals', 'Artificial waterways for navigation and irrigation', 'Canals like Panama and Suez reshape world trade; irrigation canals green deserts. Locks lift vessels over elevation changes.'],
['Irrigation: drip vs flood', 'Drip delivers water to roots efficiently; flood is cheap but wasteful', 'Drip irrigation cuts water use dramatically by wetting only the root zone. Flood irrigation is simple and cheap but loses much to evaporation. The choice shapes regional water budgets.'],
['Desalination plants', 'Seawater-to-drinking-water factories for arid coasts', 'Reverse-osmosis plants now anchor supply for cities from the Middle East to California. Energy cost and brine management are the defining challenges.']
];
var REAL_CONSERV = [
['Fixing household leaks', 'A dripping faucet can waste thousands of gallons a year; most leaks are cheap to fix', 'Check: read the meter, wait two hours without using water, read again. Fix: replace worn washers, flappers, and seals \u2014 usually a few dollars in parts. A running toilet alone can waste hundreds of gallons daily.'],
['Low-flow fixtures', 'Modern showerheads, faucets, and toilets use a fraction of old models\u2019 water', 'Swap: WaterSense-labeled fixtures cut use without hurting performance. Toilets: old models used 3.5+ gallons per flush; modern ones use 1.28. Payback: lower water and water-heating bills repay the cost.'],
['Xeriscaping', 'Landscaping with native, drought-tolerant plants slashes outdoor watering', 'Plan: group plants by water need (hydrozoning). Mulch: deep mulch holds soil moisture. Irrigate smart: drip lines on timers, watering at dawn. Lawns are the thirstiest choice in dry climates.'],
['Rainwater harvesting', 'Roofs catch rain into barrels or cisterns for irrigation and more', 'Catch: gutters feed first-flush diverters that skip the dirty first runoff. Store: sealed barrels or cisterns keep water clean and mosquito-free. Use: irrigation first; potable use needs treatment and local code compliance.'],
['Greywater reuse', 'Gentle reuse of shower and laundry water for irrigation', 'Source: showers, bathroom sinks, and laundry \u2014 never toilets or kitchen sinks. Filter: simple mulch basins handle laundry water. Plant-safe: use biodegradable, low-salt soaps. Check codes: rules vary widely by jurisdiction.'],
['Watershed protection', 'Protecting the land that feeds reservoirs is cheaper than treating dirty water', 'Forests and wetlands filter runoff naturally. New York City\u2019s watershed protection famously avoided a multi-billion-dollar filtration plant. Conservation easements keep headwaters intact.'],
['Aquifer recharge', 'Spreading basins and injection wells bank surplus water underground', 'During wet years, flood spreading grounds and recharge wells push water into aquifers. Banked groundwater is drought insurance \u2014 if pumping stays within the account.'],
['Agricultural water efficiency', 'Most freshwater goes to farming; efficiency gains free huge volumes', 'Schedule: irrigate by soil moisture, not the calendar. Technology: drip and microsprinklers beat flood. Crops: match crops to climate \u2014 and price water to reflect scarcity.'],
['Industrial water recycling', 'Factories can reuse process water in closed loops', 'Audit: map every water use in the plant. Loop: treat and return process water instead of discharging. Cool: recirculating cooling beats once-through. Zero-liquid-discharge is the frontier.'],
['Detecting hidden leaks with data', 'Smart meters and acoustic sensors find leaks before they surface', 'Meter analytics flag continuous flow as probable leaks. Acoustic sensors hear leaks in mains. Pressure management cuts both leakage and pipe bursts.']
];

/* ================= Signature-generation pools ================= */
var DESIGN_TOPICS = [
['Neighborhood rain garden network','conservation','A block-scale chain of rain gardens that drinks the street\u2019s stormwater.','Survey: map where water ponds after rain and where downspouts discharge. Size: each garden holds the first inch of its drainage area. Dig: shallow basins with amended soil and native plants. Maintain: mulch yearly, weed seasonally, and watch the street flood less.'],
['Household greywater laundry-to-landscape','conservation','Laundry water irrigates the yard through a simple branched drain.','Check codes: confirm local rules allow laundry greywater. Plumb: divert the washer discharge to a branched-drain mulch basin field. Plant: use the water on ornamentals and fruit trees, not root vegetables. Soap: switch to biodegradable, low-sodium detergent.'],
['Community wellhead protection plan','infrastructure','A volunteer plan keeping the town\u2019s well field clean.','Delineate: map the recharge zone feeding the wells. Inventory: list every potential contaminant source inside it. Protect: work with owners on best practices and spill readiness. Monitor: test the wells on schedule and publish results.'],
['School rainwater harvesting system','infrastructure','A school roof becomes a teaching tool and an irrigation source.','Measure: calculate roof area times local rainfall. Size: tanks to bridge the dry season for the garden. Plumb: first-flush diverters and screened inlets. Teach: students log rainfall, storage, and use.'],
['Apartment leak-detection program','conservation','Smart submeters find the leaks hiding in a hundred units.','Meter: install submeters on each unit\u2019s supply. Baseline: learn each unit\u2019s normal pattern. Alert: flag continuous flow automatically. Fix: maintenance responds within 48 hours.'],
['Small-town water audit','infrastructure','A volunteer audit mapping every gallon the town produces and loses.','Meter the sources: measure production at each well and intake. Zone the town: district meters reveal where losses hide. Walk the lines: acoustic survey the worst zones. Plan: turn findings into a ten-year pipe replacement program.'],
['Farm drip conversion plan','conservation','Converting flood irrigation to drip, field by field, without losing a season.','Pilot: convert one field and meter both. Design: laterals, emitters, and filtration sized to the crop. Finance: stack grants and water-savings payments. Expand: roll the savings into the next field.'],
['Green-street retrofit','infrastructure','A street rebuilt to drink its own stormwater.','Design: curb cuts feed bioswales between parking bays. Build: permeable pavement where loads allow. Plant: street trees in structural soil. Maintain: vacuum sweeping and inlet cleaning on schedule.'],
['Emergency water plan for a neighborhood','conservation','Seventy-two hours of drinking water, staged before the disaster.','Store: one gallon per person per day for three days, rotated twice yearly. Share: map vulnerable neighbors and assign check-ins. Treat: keep filters and bleach dosing instructions with the stash. Drill: practice distribution once a year.'],
['Cooling-tower water recycling','treatment','A building\u2019s cooling tower stops drinking potable water.','Audit: measure makeup and blowdown flows. Treat: side-stream filtration and smart blowdown control. Reuse: route blowdown to irrigation or toilet flushing. Monitor: track cycles of concentration and savings.'],
['Constructed wetland for a village','treatment','A planted wetland treats a village\u2019s wastewater naturally.','Size: area per person based on climate and loading. Build: lined cells with graded gravel and wetland plants. Plant: native reeds and rushes. Tend: harvest biomass yearly and monitor effluent.'],
['Fog-harvesting pilot','infrastructure','Mesh nets wring drinking water from coastal fog.','Site: ridgelines where fog is frequent and persistent. Erect: large mesh collectors facing the wind. Collect: gutter the drip to storage. Measure: log yield per square meter to size the full array.']
];
var CYCLE_TOPICS = [
['The urban water cycle','water-cycle','Cities reroute the natural cycle through pipes, pavement, and treatment plants.','Follow a raindrop: roof to gutter to storm drain to river \u2014 or to a treatment plant and back to taps. Notice the shortcuts: pavement skips infiltration; pipes skip streams. Restore the loops: green roofs, permeable pavement, and rain gardens reinsert nature into the circuit.'],
['The deep water cycle','water-cycle','Some water dives into the mantle and returns through volcanoes over geologic time.','Subduct: ocean plates carry hydrated minerals deep. Store: the mantle may hold oceans\u2019 worth of water. Return: volcanoes exhale it back over millions of years. Perspective: the surface cycle is the fast lane of a far slower loop.'],
['A watershed\u2019s year','water-cycle','One watershed through four seasons of rain, snowmelt, and low flow.','Winter: snowpack banks the water. Spring: melt swells the streams. Summer: baseflow \u2014 groundwater\u2019s gift \u2014 keeps rivers alive. Fall: first rains recharge the soils. Manage for the year, not the moment.'],
['How aquifers breathe','water-cycle','Aquifers fill in wet years and drain in dry ones \u2014 if we let them.','Recharge: rain and rivers refill the pore space. Discharge: springs and wells draw it out. Balance: pumping beyond recharge is mining. Stewardship: wet-year recharge projects bank water for droughts.'],
['The atmospheric river','water-cycle','Narrow sky-rivers deliver a season\u2019s rain in days.','Form: tropical moisture streams ride the jet. Landfall: mountains squeeze out the water. Consequence: floods and reservoir-filling bounty in one event. Forecast: tracking these rivers is now central to water operations.'],
['Evapotranspiration on the farm','water-cycle','Crops drink and breathe water back to the sky.','Measure: weather stations estimate daily crop water use. Schedule: irrigate to replace exactly what left. Save: mulch and drip cut the skyward loss. Account: every drop transpired is a drop pumped.']
];
var REAL = interleave([
  REAL_CYCLE.map(function (e) { return { k: 'c', e: e }; }),
  REAL_TREATMENT.map(function (e) { return { k: 't', e: e }; }),
  REAL_INFRA.map(function (e) { return { k: 'i', e: e }; }),
  REAL_CONSERV.map(function (e) { return { k: 'v', e: e }; })
]);
/* ================= Wastewater/sanitation engineering (expansion 2026-10-17):
   sourced knowledge [title, key_points, body] + Signature designs
   [title, summary, implementation]. ================= */
var REAL_WW = [
['Sanitary sewer collection networks', 'Gravity sewers carry wastewater downhill through pipes, manholes, and lift stations to treatment', 'Sanitary sewers are sized for peak flow with minimum slopes that keep solids moving — typically 2 feet per second at design flow. Manholes at every junction and direction change allow inspection and cleaning. Where gravity cannot reach, lift stations pump sewage uphill into the next gravity reach.'],
['Combined versus separate sewers', 'Separate systems keep stormwater and sewage apart; combined systems carry both and can overflow in storms', 'Older cities built combined sewers that carry sewage and stormwater in one pipe; heavy rain overwhelms them and combined sewer overflows discharge diluted sewage to waterways. Modern practice builds separate sanitary and storm systems, and many cities are separating old combined networks or adding storage tunnels.'],
['Wastewater pumping and lift stations', 'Wet wells collect sewage and pumps lift it where gravity flow is impossible', 'A lift station\u2019s wet well fills by gravity; level controls start pumps that push sewage through a force main to higher ground. Duplex pumps alternate for even wear, with a lag pump for peaks. Backup power is mandatory — a station without power becomes an overflow within hours.'],
['Sewer inspection and cleaning', 'CCTV crawlers find defects; jetting and root cutters restore capacity', 'Crews send camera crawlers through sewers to grade cracks, roots, grease, and sags. High-pressure jetting scours deposits; mechanical cutters clear roots. Inspection on a 5-to-10-year cycle catches failures while repairs are still cheap.'],
['Infiltration and inflow control', 'Groundwater leaking in (infiltration) and stormwater pouring in (inflow) overload sewers and plants', 'Cracked pipes and bad joints admit groundwater — infiltration — while roof drains and manhole covers admit stormwater — inflow. Together they can multiply dry-weather flow several times over. Smoke testing finds inflow sources; lining and joint sealing cut infiltration.'],
['Wastewater reuse for irrigation', 'Treated effluent irrigates crops, golf courses, and landscapes under quality standards', 'Reclaimed water extends supply where freshwater is scarce. Treatment level matches the use: unrestricted irrigation needs filtration plus disinfection. Purple pipe marks reclaimed distribution so it is never confused with potable lines.'],
['Industrial pretreatment programs', 'Industries must treat or limit discharges before sending waste to the public sewer', 'Pretreatment permits cap what factories may discharge — metals, oils, pH, flammables — protecting sewers, treatment biology, and workers. Grease traps on restaurants are the most common pretreatment device. Violations bring fines and surcharges.'],
['Onsite sanitation: septic systems', 'Septic tanks settle solids; drainfields let soil finish treatment', 'A septic tank holds wastewater long enough for solids to settle and scum to float; the clarified liquid flows to a drainfield where soil microbes treat it. Tanks need pumping every 3 to 5 years. Failed systems surface sewage and contaminate wells — the classic rural sanitation failure.'],
['Sludge handling and disposal', 'Treatment concentrates pollutants into sludge that must be thickened, stabilized, and put to use or landfilled', 'Primary and secondary sludge are thickened, then digested — anaerobically, capturing biogas — or stabilized aerobically. Dewatering by belt press or centrifuge cuts volume for hauling. Land application as biosolids returns nutrients to soil under strict pathogen and metals limits.'],
['Nutrient removal: nitrogen and phosphorus', 'Excess nutrients cause algal blooms; biological processes now strip them from effluent', 'Nitrifying bacteria convert ammonia to nitrate; anoxic zones then denitrify it to nitrogen gas. Phosphorus is removed biologically by specialized organisms or chemically with metal salts. Nutrient limits protect lakes and estuaries from eutrophication.'],
['Disinfection of wastewater effluent', 'Chlorine or UV kills pathogens before effluent reaches waterways', 'Chlorination is cheap and leaves a residual, but forms disinfection byproducts; dechlorination protects aquatic life. UV inactivates pathogens without chemicals and is now standard for sensitive receiving waters. Disinfection is the final public-health barrier.'],
['Sewer odor and corrosion control', 'Hydrogen sulfide from septic sewage smells and eats concrete; control starts with keeping sewage fresh', 'Stagnant sewage goes septic, generating hydrogen sulfide — the rotten-egg smell that corrodes concrete crowns and sickens workers. Ventilation, chemical dosing, and keeping velocities up prevent the worst. Crown corrosion has collapsed sewers that looked fine from the street.']
];
var DESIGN_WW = [
['Neighborhood decentralized treatment cluster', 'wastewater', 'A cluster of homes shares one compact treatment plant instead of each running a septic tank.', 'Form the district: group 20 to 50 homes with failing or aging septics. Size: a package extended-aeration plant matched to total flow. Collect: small-diameter gravity or pressure sewers to the plant. Operate: contract a licensed operator — shared cost beats 40 individual pump-outs.'],
['Sewer-mining pilot for a business district', 'wastewater', 'Pull water out of the sewer, treat it locally, and reuse it — the sewer becomes a resource.', 'Tap: a side-stream intake on the trunk sewer. Treat: membrane bioreactor plus disinfection in a compact skid. Reuse: toilet flushing and cooling towers in the district. Return: residuals go back to the sewer. Measure: meter every gallon reused and publish the offset.'],
['FOG compliance program for restaurants', 'wastewater', 'Fats, oils, and grease clog sewers; a permit-and-inspect program keeps them out.', 'Permit: every food-service site holds a FOG permit. Size: grease interceptors matched to fixture units. Inspect: quarterly checks with a pass/fail dipstick test. Enforce: fines escalate; chronic violators get monitored. Educate: staff training in three languages.'],
['Rain-garden overflow relief for combined sewers', 'wastewater', 'Green infrastructure trims the storm peak that triggers combined sewer overflows.', 'Map: model which sub-catchments drive overflows. Build: curb-cut rain gardens and permeable alleys upstream. Meter: flow monitors prove the peak shaved. Maintain: vacuum sweeping and inlet cleaning on schedule. Report: overflow events before and after, published yearly.'],
['Community latrine upgrade program', 'wastewater', 'Replace open pits with lined, ventilated latrines across a village cluster.', 'Survey: count households and map water points. Design: lined pits with slabs and vent pipes, sited 30 meters from wells. Build: train local masons; households dig, program supplies slabs. Maintain: pit-emptying service on rotation. Verify: open-defecation-free certification by transect walk.'],
['Septage receiving station for a rural county', 'wastewater', 'Give pumpers a legal place to dump instead of the ditch behind the plant.', 'Site: at the treatment plant with truck access. Build: receiving manhole, screening, and equalization. Charge: per-gallon tipping fees that cover operation. Track: manifest every load by hauler and source. Enforce: illegal dumping fines fund the station.'],
['Effluent reuse loop for a sports complex', 'wastewater', 'The complex irrigates its fields with its own treated wastewater.', 'Treat: package plant sized to the complex\u2019s flow with filtration and UV. Store: a lined pond buffers irrigation demand. Distribute: purple-pipe zones with backflow prevention. Monitor: weekly effluent testing posted at the gate. Sign: public education boards explain the loop.'],
['Sewer acoustic monitoring network', 'wastewater', 'Listening sensors find blockages forming before the backup call comes in.', 'Deploy: acoustic sensors at key manholes on chronic-blockage lines. Baseline: learn each reach\u2019s normal sound profile. Alert: deviations page the cleaning crew automatically. Clean: jet the flagged reach and confirm the profile returns. Track: blockage calls per mile, before and after.'],
['Decentralized MBR package plant for a campus', 'wastewater', 'A membrane bioreactor in a box treats a campus to reuse quality.', 'Size: design flow plus 25 percent for growth. Install: skid-mounted MBR with fine screening upstream. Operate: remote monitoring with weekly site visits. Reuse: cooling towers and irrigation take the effluent. Plan: membrane replacement budgeted on a 7-year cycle.'],
['Biosolids composting cooperative', 'wastewater', 'Neighboring towns compost biosolids together instead of landfilling alone.', 'Form: interlocal agreement sharing costs by tonnage. Build: aerated static piles under cover with biofilters. Test: every batch for pathogens and metals before release. Sell: bagged compost funds the operation. Audit: annual third-party review of records.'],
['Sewer lateral replacement program', 'wastewater', 'The private pipes from house to main cause half the problems; fix them systematically.', 'Inventory: camera every lateral during main replacement. Share cost: city funds the public half, low-interest loans cover the private half. Replace: trenchless lining where possible, open cut where not. Verify: post-repair camera and air test. Track: backup complaints by block, published yearly.'],
['Constructed wetland polishing for a lagoon town', 'wastewater', 'A planted wetland polishes lagoon effluent to meet tightening nutrient limits.', 'Size: wetland area from design loading rates for the climate. Build: lined cells with graded media and native plants. Plant: reeds and rushes in zones. Tend: harvest biomass yearly to export nutrients. Monitor: influent and effluent sampling against the permit.']
];
function realWWRecord(e, id, seed) {
  var secs = [
    { heading: 'Key points', body: e[0] + '. ' + e[1] + '.' },
    { heading: 'In depth', body: e[2] }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: e[0], category: 'wastewater', record_kind: RECORD_KIND, origin: 'sourced', summary: e[1] + '.', details: { key_points: e[1].split('; ') }, sections: secs, record_text: text, source_note: 'Sourced: standard wastewater and sanitation engineering knowledge.', related: [], _seed: seed };
}
function sigWWDesign(r, id, seed, topic) {
  var t = topic || pick(DESIGN_WW, r);
  var secs = [{ heading: 'The design', body: t[0] + ' (' + t[1] + '). ' + t[2] }, { heading: 'Implementation', body: t[3] }];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: t[0] + ' \u2014 Signature design', category: 'wastewater', record_kind: RECORD_KIND, origin: 'signature-generated', summary: t[2], details: { area: 'wastewater', key_points: t[2].split('. ') }, sections: secs, record_text: text, source_note: 'Signature-generated: a homegrown wastewater-system design; verify against local codes and engineering review.', related: [], _seed: seed };
}
function realRecord(e, id, seed, cat) {
  var secs = [
    { heading: 'Key points', body: e[0] + '. ' + e[1] + '.' },
    { heading: 'In depth', body: e[2] }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: e[0], category: cat, record_kind: RECORD_KIND, origin: 'sourced', summary: e[1] + '.', details: { key_points: e[1].split('; ') }, sections: secs, record_text: text, source_note: 'Sourced: standard hydrology and water-engineering knowledge.', related: [], _seed: seed };
}
function sigDesign(r, id, seed, topic) {
  var t = topic || pick(DESIGN_TOPICS, r);
  var secs = [{ heading: 'The design', body: t[0] + ' (' + t[1] + '). ' + t[2] }, { heading: 'Implementation', body: t[3] }];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: t[0] + ' \u2014 Signature design', category: t[1], record_kind: RECORD_KIND, origin: 'signature-generated', summary: t[2], details: { area: t[1], key_points: t[2].split('. ') }, sections: secs, record_text: text, source_note: 'Signature-generated: a homegrown water-system design; verify against local codes and engineering review.', related: [], _seed: seed };
}
function sigCycle(r, id, seed) {
  var t = pick(CYCLE_TOPICS, r);
  var secs = [{ heading: 'The concept', body: t[0] + '. ' + t[1] }, { heading: 'In depth', body: t[2] }, { heading: 'Why it matters', body: 'Understanding this part of the water cycle helps communities plan supply, predict floods, and protect the sources their taps depend on. Water literacy turns an invisible system into decisions people can make: where to build, what to plant, and how much to store.' }];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: t[0] + ' \u2014 Signature explainer', category: 'water-cycle', record_kind: RECORD_KIND, origin: 'signature-generated', summary: t[1], details: { area: 'water-cycle' }, sections: secs, record_text: text, source_note: 'Signature-generated: a homegrown explainer of water-cycle science.', related: [], _seed: seed };
}
var CATMAP = { c: 'water-cycle', t: 'treatment', i: 'infrastructure', v: 'conservation' };
function generate(seed, opts, rnd) {
  opts = opts || {}; rnd = rnd || prng(seed);
  var idx = ((seed % 1000000) + 1000000) % 1000000;
  var id = PREFIX + String(idx + 1).padStart(7, '0');
  if (idx < REAL.length) {
    var re = REAL[idx];
    if (!opts.category || CATMAP[re.k] === opts.category) return realRecord(re.e, id, seed, CATMAP[re.k]);
  }
  var cat = opts.category || pick(CATS, rnd);
  if (cat === 'wastewater') {
    var wix = (((seed - 10002) % 24) + 24) % 24;
    if (wix < REAL_WW.length) return realWWRecord(REAL_WW[wix], id, seed);
    return sigWWDesign(rnd, id, seed, DESIGN_WW[(wix - REAL_WW.length) % DESIGN_WW.length]);
  }
  if (cat === 'water-cycle' && rnd() < 0.5) return sigCycle(rnd, id, seed);
  var pool = DESIGN_TOPICS.filter(function (x) { return !opts.category || x[1] === cat; });
  return sigDesign(rnd, id, seed, pick(pool.length ? pool : DESIGN_TOPICS, rnd));
}
var REQUIRED = ['id', 'title', 'category', 'record_kind', 'origin', 'summary', 'details', 'sections', 'record_text', 'source_note'];
function validate(rec) {
  var errors = [];
  if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
  REQUIRED.forEach(function (k) { if (rec[k] === undefined || rec[k] === null || rec[k] === '') errors.push('missing ' + k); });
  if (rec.id && !/^JAH-WTR-\d{7}$/.test(rec.id)) errors.push('bad id format');
  if (rec.category && CATS.indexOf(rec.category) < 0) errors.push('bad category');
  if (rec.origin && ['sourced', 'signature-generated'].indexOf(rec.origin) < 0) errors.push('bad origin');
  if (rec.sections && (!Array.isArray(rec.sections) || !rec.sections.length)) errors.push('sections empty');
  if (rec.record_text && rec.record_text.length < 120) errors.push('record_text too short');
  return { ok: errors.length === 0, errors: errors };
}
function driftCheck(rec, sample) {
  var errors = [];
  for (var i = 0; i < sample.length; i++) {
    if (sample[i] && sample[i].t === rec.title && sample[i].id !== rec.id) { errors.push('duplicate title in archive sample'); break; }
  }
  return { ok: errors.length === 0, errors: errors };
}
var GEN = { version: VERSION, generate: generate, validate: validate, driftCheck: driftCheck, slug: SLUG, prefix: PREFIX, categories: CATS, record_kind: RECORD_KIND, realCount: REAL.length };
if (typeof JAHDB !== 'undefined' && JAHDB.registerGenerator) JAHDB.registerGenerator(SLUG, GEN);
if (typeof module !== 'undefined' && module.exports) module.exports = GEN;
})();
