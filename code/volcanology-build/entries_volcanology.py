#!/usr/bin/env python3
"""Seed entries for the Volcanology field build (field #11, taxonomy order).

Verified 2026-10-17: NO database covers volcanology as a science. The broad
'geology' database is a specimen-style catalog with no magma-system science,
no eruption styles, no VEI, no monitoring, no hazards, no historic-eruption
analysis. 'geology-public' carries only generic volcano overviews. The
'volcanoes' database (28 topics) is stub-grade: one-line topic briefs with
content_completeness 'stub' - it does not cover volcanology as a science.
'volcano-energy' covers only geothermal energy use. So this build creates
two NEW databases:

  volcanology              — The Volcanology Database (public-harvest: real,
                             fact-checked volcanology - what volcanology is;
                             magma formation; lava; plate tectonics and
                             volcanic settings; the Ring of Fire; shield
                             volcanoes; stratovolcanoes; cinder cones;
                             craters and calderas; magma chambers and
                             plumbing; viscosity and gas control; the
                             basalt-to-rhyolite composition scale; Hawaiian
                             and Strombolian eruption styles; Vulcanian and
                             Plinian styles; pyroclastic flows; lahars;
                             tephra and ashfall; volcanic gases and climate;
                             the VEI scale; pahoehoe, aa, and lava tubes;
                             seismic monitoring; ground deformation;
                             gas monitoring; eruption forecasting and alert
                             levels; supervolcanoes; magma chamber dynamics;
                             crystal fractionation; volcanic hazard maps;
                             pyroclastic-flow modeling; volcano tsunamis;
                             geothermal energy; magma mixing; Vesuvius 79 AD;
                             Tambora and Krakatau; St. Helens and Pinatubo;
                             frontiers of volcanology)
  volcanology-signature    — The Volcanology Signature Database (his original
                             Signature interpretation; src signature, titles
                             suffixed " (Signature Edition)", never presented
                             as authentic public record)

36 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

# Shared citation constants (standard volcanology literature)
CIT_SIGURDSSON = ("Sigurdsson, H. et al. (2015). 'The Encyclopedia of "
                  "Volcanoes', 2nd ed. Academic Press.")
CIT_FRANCIS = ("Francis, P. & Oppenheimer, C. (2004). 'Volcanoes', 2nd ed. "
               "Oxford University Press.")
CIT_SCHMINCKE = ("Schmincke, H.-U. (2004). 'Volcanism'. Springer.")
CIT_CAS = ("Cas, R. A. F. & Wright, J. V. (1987). 'Volcanic Successions: "
           "Modern and Ancient'. Allen & Unwin.")
CIT_NEWHALL = ("Newhall, C. G. & Self, S. (1982). 'The Volcanic Explosivity "
               "Index (VEI): An estimate of explosive magnitude for historical "
               "volcanism.' Journal of Geophysical Research 87: 1231-1238.")
CIT_SPARKS = ("Sparks, R. S. J. (1976). 'Grain size variations in "
              "ignimbrites and implications for the transport of pyroclastic "
              "flows.' Sedimentology 23: 147-188.")
CIT_MOGI = ("Mogi, K. (1958). 'Relations between the eruptions of various "
            "volcanoes and the deformations of the ground surfaces around "
            "them.' Bulletin of the Earthquake Research Institute 36: "
            "99-134.")
CIT_ROBOCK = ("Robock, A. (2000). 'Volcanic eruptions and climate.' Reviews "
              "of Geophysics 38: 191-219.")
CIT_MILLER = ("Miller, C. F. & Wark, D. A. (2008). 'Supervolcanoes and "
              "their explosive super-eruptions.' Elements 4: 11-16.")
CIT_GVP = ("Global Volcanism Program, Smithsonian Institution. 'Volcanoes "
           "of the World' database (public record).")
CIT_USGS = ("U.S. Geological Survey Volcano Hazards Program fact sheets "
            "(public record).")
CIT_PLINY = ("Pliny the Younger, Letters 6.16 and 6.20 (79 AD account of "
             "the Vesuvius eruption; public historical record).")
CIT_LIPMAN = ("Lipman, P. W. & Mullineaux, D. R. (1981). 'The 1980 "
              "eruptions of Mount St. Helens, Washington.' USGS Professional "
              "Paper 1250.")
CIT_PINATUBO = ("Newhall, C. G. & Punongbayan, R. S., eds. (1996). 'Fire and "
                "Mud: Eruptions and Lahars of Mount Pinatubo, Philippines.' "
                "PHIVOLCS / University of Washington Press.")
CIT_TAMBORA = ("Self, S. et al. (1984). 'The great Tambora eruption in 1815 "
               "and its aftermath.' Science 224: 1191-1198.")
CIT_KRAKATAU = ("Simkin, T. & Fiske, R. S. (1983). 'Krakatau 1883: The "
                "Volcanic Eruption and Its Effects.' Smithsonian Institution "
                "Press.")
CIT_TILLING = ("Tilling, R. I., ed. (1989). 'Volcanic Hazards: A Sourcebook "
               "on the Effects of Eruptions.' Academic Press.")
CIT_FISHER = ("Fisher, R. V. & Schmincke, H.-U. (2009). 'Pyroclastic "
              "Rocks'. Springer.")
CIT_STD = ("Standard volcanology literature (peer-reviewed textbooks and "
           "journals).")

ENTRIES = [
{
 "key": "what-is-volcanology",
 "name": "What Volcanology Is",
 "group": "Foundations",
 "ladder_rank": 1,
 "ladder_tier": "foundations",
 "description": (
  "Volcanology is the science of volcanoes and volcanic phenomena: where "
  "magma forms, how it rises and erupts, what the eruptions produce, and "
  "what they do to the land, the atmosphere, and people. It draws on "
  "geology, geophysics, geochemistry, and atmospheric science. Its branches "
  "include physical volcanology (eruption processes and deposits), volcanic "
  "petrology (the chemistry of lavas), volcano monitoring and hazard "
  "assessment, and volcanology's sister record - tephrochronology, which "
  "uses ash layers to date the past. Modern volcanology is an operational "
  "science: observatories watch restless volcanoes around the clock and "
  "issue the forecasts that save lives."),
 "how_it_works": (
  "Volcanology works by combining field deposits with live measurement. "
  "Physical volcanologists map lava flows, ash layers, and pyroclastic "
  "deposits to reconstruct what an eruption did; petrologists read the "
  "chemistry and crystals of the rocks to reconstruct what the magma was "
  "doing before it erupted. Monitoring volcanologists deploy seismometers "
  "(magma cracking rock as it moves), GPS and tiltmeters (the ground "
  "swelling as a chamber inflates), gas sensors (sulfur dioxide flux "
  "rising), and satellite thermal and radar data. The branches meet at "
  "the forecast: deposits tell what the volcano is capable of, monitoring "
  "tells what it is doing now, and eruption models turn both into "
  "warnings."),
 "key_points": [
  "Volcanology studies magma formation, transport, eruption, deposits, and effects on land, air, and people.",
  "Its branches: physical volcanology, volcanic petrology, monitoring/hazards, tephrochronology, and climate effects.",
  "It is an operational science - observatories issue real-time forecasts and alert levels.",
  "Deposits record the past; monitoring reads the present; models bridge them into forecasts.",
  "Volcanology borrows from seismology, geodesy, geochemistry, and atmospheric science."],
 "requirements": [
  "Field access to volcanic deposits and a working knowledge of igneous rock identification.",
  "Monitoring instrumentation (seismic, geodetic, gas) for any live-volcano study.",
  "An eruption chronology for the volcano in question, ideally from the Global Volcanism Program catalog."],
 "standards": [
  "Field observations follow standard stratigraphic logging of volcanic deposits.",
  "Hazard statements follow the observatory alert-level framework (e.g., USGS Normal/Advisory/Watch/Warning)."],
 "citations": [CIT_SIGURDSSON, CIT_FRANCIS],
 "sig_lens": (
  "Signature edition: volcanology reframed as his original planetary "
  "pressure science - the Earth venting its stored heat and strain through "
  "his Signature vent inventory, every eruption a solved release of "
  "planetary pressure."),
 "demo_kind": "volcano_branches",
},
{
 "key": "magma-how-melts-form",
 "name": "How Magma Forms",
 "group": "Foundations",
 "ladder_rank": 1,
 "ladder_tier": "foundations",
 "description": (
  "Magma is molten rock beneath the surface, and it forms in only three "
  "tectonic ways. Decompression melting happens where plates pull apart "
  "(mid-ocean ridges, rifts): rising mantle crosses its solidus and melts "
  "without any added heat. Flux melting happens at subduction zones: water "
  "carried down on the sinking slab lowers the melting point of the mantle "
  "above it, generating the magmas of volcanic arcs. Heat-transfer melting "
  "happens above mantle plumes (hotspots like Hawaii and Iceland), where "
  "extra-hot rock rises and melts. In every case the melt is partial - "
  "typically a few percent to a few tens of percent of the source rock - "
  "and the first melts are always richer in silica and incompatible "
  "elements than the source."),
 "how_it_works": (
  "Melting starts when rock crosses its solidus, the temperature where the "
  "first melt appears. Raise the temperature (plumes), lower the pressure "
  "(decompression under ridges), or add volatiles (water at arcs), and the "
  "solidus drops or the geotherm rises until they meet. The melt fraction "
  "grows roughly linearly between the solidus and the liquidus. Because "
  "silica and incompatible elements prefer the melt, small melt fractions "
  "make basaltic magma from peridotite mantle; larger fractions or re-"
  "melting of crustal rock make more silicic magmas. Buoyancy then drives "
  "the melt upward through cracks and porous channels toward chambers and "
  "the surface."),
 "key_points": [
  "Three melting mechanisms: decompression (ridges/rifts), flux melting (arcs), heat transfer (hotspots).",
  "Melting is partial - a few to tens of percent; first melts are silica-rich relative to source.",
  "The solidus-liquidus window controls how much melt forms at a given temperature.",
  "Water carried down at subduction zones is the flux that melts arc mantle.",
  "Melt buoyancy drives upward transport through dikes toward magma chambers."],
 "requirements": [
  "A phase diagram (solidus/liquidus) for peridotite at the relevant pressure.",
  "Knowledge of the tectonic setting to identify which melting mechanism applies.",
  "Geochemical data (major elements, water content) to confirm the melt source."],
 "standards": [
  "Melt fractions are reported with the pressure and assumed source composition stated.",
  "Arc magma studies report volatile contents from melt inclusions where available."],
 "citations": [CIT_SCHMINCKE, CIT_SIGURDSSON],
 "sig_lens": (
  "Signature edition: magma genesis reframed as his original planetary "
  "furnace model - three Signature melt engines (stretch, flux, plume) "
  "that forge every volcano's starting material."),
 "demo_kind": "partial_melting",
},
{
 "key": "lava-magma-on-surface",
 "name": "Lava: Magma on the Surface",
 "group": "Foundations",
 "ladder_rank": 1,
 "ladder_tier": "foundations",
 "description": (
  "Lava is magma that has reached the surface and begun to lose its "
  "dissolved gases. Basaltic lava erupts at about 1100-1200 degrees "
  "Celsius, flows easily, and builds broad shield volcanoes and lava "
  "plains; andesitic lava is cooler and stiffer; rhyolitic lava erupts "
  "near 700-850 degrees, barely flows, and piles into domes. As lava "
  "cools it radiates heat, crystallizes, and its viscosity climbs "
  "exponentially - the same flow can start fluid and end frozen. Lava "
  "morphology records this history: smooth ropy pahoehoe where it stayed "
  "hot and fluid, jagged clinkery aa where it cooled and tore, and blocky "
  "flows for the stiffest lavas."),
 "how_it_works": (
  "Lava cools by radiation from its surface and conduction into the "
  "ground, forming a crust that insulates the still-molten interior - "
  "this is why lava tubes can carry fluid lava kilometers from the vent. "
  "Cooling drives crystallization, which raises viscosity; when viscosity "
  "passes a threshold the smooth pahoehoe surface tears into aa. Gas "
  "bubbles trapped during flow become vesicles in the solid rock; "
  "abundant tiny bubbles make pumice, rapid quenching without crystals "
  "makes obsidian glass. Flow advance stops when the yield strength of "
  "the cooling crust exceeds the driving pressure, freezing the flow's "
  "final shape in place."),
 "key_points": [
  "Lava is degassed magma; its temperature and composition set how far it flows.",
  "Basaltic lava (1100-1200 C) flows far; rhyolitic lava (700-850 C) piles into domes.",
  "Surface crusts insulate interiors, letting lava tubes transport lava for kilometers.",
  "Pahoehoe vs aa records the cooling history of the flow surface.",
  "Quenched textures (obsidian, pumice, vesicles) record gas content and cooling rate."],
 "requirements": [
  "Eruption temperature estimates (thermal cameras, thermocouples, or petrologic thermometers).",
  "Flow morphology mapping to read the cooling and viscosity history.",
  "Sample collection of quenched margins for glass and vesicle analysis."],
 "standards": [
  "Lava temperatures are reported with the measurement method and its uncertainty.",
  "Flow type classifications use the standard pahoehoe/aa/blocky terminology."],
 "citations": [CIT_FRANCIS, CIT_CAS],
 "sig_lens": (
  "Signature edition: lava reframed as his original surface-forge ledger - "
  "every flow a Signature cooling curve, temperature and texture read as "
  "one continuous record of the planet's heat leaving."),
 "demo_kind": "lava_temperature",
},
{
 "key": "plate-tectonics-and-volcanoes",
 "name": "Plate Tectonics and Volcanic Settings",
 "group": "Foundations",
 "ladder_rank": 1,
 "ladder_tier": "foundations",
 "description": (
  "Nearly every volcano on Earth sits in one of three tectonic settings. "
  "Divergent boundaries (mid-ocean ridges, continental rifts like the East "
  "African Rift) produce basaltic volcanism by decompression melting as "
  "plates pull apart. Convergent boundaries (subduction zones) produce "
  "explosive arc volcanoes by flux melting - the Andes, Cascades, Japan, "
  "Indonesia. Hotspots (Hawaii, Iceland, Yellowstone) produce volcanism "
  "far from plate boundaries, fed by deep mantle plumes. This is why the "
  "map of volcanoes is the map of plate boundaries plus a scattering of "
  "plume dots: tectonic setting predicts magma chemistry, eruption style, "
  "and hazard."),
 "how_it_works": (
  "At divergent boundaries, upwelling mantle melts by decompression and "
  "erupts as fluid basalt - the process that builds oceanic crust. At "
  "subduction zones, the sinking slab releases water into the overlying "
  "mantle wedge, lowering its solidus; the resulting hydrous magmas rise, "
  "differentiate in crustal chambers, and erupt as gas-rich, explosive "
  "andesite to rhyolite. At hotspots, a hot plume rises from deep mantle, "
  "melting extensively to produce large volumes of basalt (oceanic "
  "hotspots) or, where the plume sits under thick continent, melted crust "
  "that erupts catastrophically (Yellowstone). Each setting leaves a "
  "geochemical fingerprint in trace elements and isotopes."),
 "key_points": [
  "Three settings: divergent (ridges/rifts), convergent (arcs), hotspots (plumes).",
  "Setting predicts chemistry: basaltic at ridges, explosive andesitic-rhyolitic at arcs.",
  "Decompression, flux, and plume melting map one-to-one onto the three settings.",
  "Geochemical fingerprints (trace elements, isotopes) confirm the setting.",
  "The volcano map is the plate-boundary map plus plume dots."],
 "requirements": [
  "A plate-boundary map to place the volcano in its tectonic context.",
  "Whole-rock geochemistry to confirm the setting's chemical fingerprint.",
  "Age dating to link volcanism to the tectonic history."],
 "standards": [
  "Tectonic classifications follow the standard divergent/convergent/hotspot scheme.",
  "Arc magma studies report slab-fluid tracers (e.g., boron, water) where available."],
 "citations": [CIT_SCHMINCKE, CIT_SIGURDSSON],
 "sig_lens": (
  "Signature edition: tectonic settings reframed as his original three-"
  "engine planetary forge - stretch, squeeze, and plume circuits mapped in "
  "his Signature setting atlas."),
 "demo_kind": "volcano_settings",
},
{
 "key": "ring-of-fire",
 "name": "The Ring of Fire",
 "group": "Foundations",
 "ladder_rank": 2,
 "ladder_tier": "foundations",
 "description": (
  "The Ring of Fire is the 40,000-kilometer belt of subduction zones "
  "circling the Pacific Ocean, hosting roughly 450 of the world's active "
  "volcanoes and the great majority of its largest earthquakes. It runs "
  "from the Andes up through Central America, the Cascades and Alaska, "
  "down through Kamchatka, Japan, the Philippines, and Indonesia to New "
  "Zealand. The ring exists because the Pacific Plate and its neighbors "
  "are subducting on nearly every side at once. Its volcanoes are the "
  "classic explosive arc type - Fuji, Pinatubo, Krakatau - and its "
  "megathrust faults have produced the largest recorded earthquakes, "
  "including the 1960 Chile magnitude 9.5 event."),
 "how_it_works": (
  "Oceanic plates dive beneath continental or other oceanic plates all "
  "around the Pacific rim. As each slab descends past about 100 "
  "kilometers depth, water squeezed from its minerals fluxes the mantle "
  "wedge above, generating magma that rises to build a volcanic arc "
  "parallel to the trench. Meanwhile the plate interface itself locks "
  "and accumulates strain for centuries, then ruptures in megathrust "
  "earthquakes. The ring's continuity is no coincidence: the Pacific is "
  "a shrinking ocean basin, subducting on almost all margins "
  "simultaneously, so arcs and trenches ring it nearly unbroken."),
 "key_points": [
  "A 40,000 km belt of subduction zones around the Pacific, ~450 active volcanoes.",
  "Hosts most of Earth's largest earthquakes, including the 1960 Chile M9.5.",
  "Arc volcanoes form parallel to trenches, ~100 km above the sinking slab.",
  "Classic explosive arc volcanoes: Fuji, Pinatubo, Krakatau, St. Helens (Cascadia).",
  "The Pacific is shrinking; subduction on all sides sustains the ring."],
 "requirements": [
  "Trench and arc positions from bathymetry and seismicity catalogs.",
  "Slab depth contours (Benioff zone) to locate the magma-generation zone.",
  "Eruption histories from the Global Volcanism Program for ring volcanoes."],
 "standards": [
  "Volcano counts reference the Global Volcanism Program Holocene list.",
  "Megathrust magnitudes use moment magnitude (Mw) from seismic catalogs."],
 "citations": [CIT_GVP, CIT_SIGURDSSON],
 "sig_lens": (
  "Signature edition: the Ring of Fire reframed as his original planetary "
  "discharge circuit - the main Signature pressure-relief loop of the "
  "Pacific basin, every arc a vent on the circuit."),
 "demo_kind": "ring_stats",
},
{
 "key": "shield-volcanoes",
 "name": "Shield Volcanoes",
 "group": "Foundations",
 "ladder_rank": 2,
 "ladder_tier": "foundations",
 "description": (
  "Shield volcanoes are the broad, gently sloping giants built by fluid "
  "basaltic lava - slopes of only 4 to 10 degrees, profiles like a "
  "warrior's shield lying on the ground. Mauna Loa in Hawaii is the "
  "largest volcano on Earth by volume, about 75,000 cubic kilometers, "
  "rising 9 kilometers from the seafloor. Shield eruptions are typically "
  "effusive: lava fountains, rivers of pahoehoe and aa, and lava tubes "
  "that extend flows for tens of kilometers. Because the lava is fluid "
  "and gas escapes easily, shields erupt often but usually without "
  "catastrophic explosions - though their sheer volume and flank "
  "instability (giant landslides, tsunamis) are hazards of their own."),
 "how_it_works": (
  "Low-viscosity basalt (10^2-10^3 Pa s) spreads far before freezing, so "
  "thousands of thin flows stack into a broad low dome. Eruptions feed "
  "from a summit magma chamber through rift zones - lateral crack systems "
  "where dikes intrude sideways. Lava tubes insulate the flow, letting it "
  "travel 10-50 km from the vent. The edifice grows until its own weight "
  "causes flank spreading and giant sector collapses; the amphitheater-"
  "headed valleys of Hawaii are the scars. Caldera collapse at the summit "
  "follows large drainages of the shallow chamber."),
 "key_points": [
  "Broad low shields (4-10 degree slopes) built from fluid basaltic flows.",
  "Mauna Loa: ~75,000 km^3, the largest volcano on Earth by volume.",
  "Eruptions are effusive: fountains, lava rivers, tubes extending flows tens of km.",
  "Rift zones feed lateral eruptions; summit calderas collapse when chambers drain.",
  "Main hazards: lava inundation, vog (volcanic smog), and giant flank landslides."],
 "requirements": [
  "Topographic profiles to measure edifice slopes and volumes.",
  "Flow mapping and dating to reconstruct growth history.",
  "Rift-zone and flank-stability assessment for landslide hazard."],
 "standards": [
  "Edifice volumes are reported with the base level (seafloor vs. sea level) stated.",
  "Shield vs. stratovolcano classification uses slope, composition, and eruptive style."],
 "citations": [CIT_FRANCIS, CIT_SCHMINCKE],
 "sig_lens": (
  "Signature edition: shield volcanoes reframed as his original "
  "slow-forge giants - Signature low-and-wide construction, every thin "
  "flow a layer in his planetary shielding record."),
 "demo_kind": "shield_slope",
},
{
 "key": "stratovolcanoes",
 "name": "Stratovolcanoes",
 "group": "Foundations",
 "ladder_rank": 2,
 "ladder_tier": "foundations",
 "description": (
  "Stratovolcanoes (composite volcanoes) are the steep, conical icons - "
  "Fuji, Mayon, Rainier - built of alternating layers of lava flows, ash, "
  "and pyroclastic deposits, hence 'strato'. Their intermediate magmas "
  "(andesite to dacite) are viscous and gas-rich, so eruptions alternate "
  "between lava flows, dome growth, and violent explosions. Slopes reach "
  "30 degrees near the summit. These are the volcanoes that destroy "
  "cities: their eruptions produce pyroclastic flows, lahars, and ash "
  "columns, and their steep, hydrothermally weakened flanks collapse into "
  "sector failures. Most of history's deadliest eruptions came from "
  "stratovolcanoes."),
 "how_it_works": (
  "Viscous andesitic magma rises slowly, degassing as it goes; the "
  "escalating viscosity traps the remaining gas until fragmentation "
  "blasts the magma apart. Between explosions, lava flows and domes add "
  "competent layers; pyroclastic deposits add loose ones. The cone "
  "steepens until it approaches the angle of repose, and the layered "
  "structure - strong lavas alternating with weak ash - becomes "
  "prone to sector collapse, especially where hot acidic fluids have "
  "rotted the interior rock. Crater glaciers on peaks like Rainier "
  "guarantee lahars when eruptions melt the ice."),
 "key_points": [
  "Steep cones of alternating lava and fragmental layers - Fuji, Mayon, Rainier.",
  "Intermediate, gas-rich magmas give mixed effusive and explosive behavior.",
  "Produce the classic killer hazards: pyroclastic flows, lahars, ash columns.",
  "Layered structure plus hydrothermal weakening invites sector collapse.",
  "Most historically deadly eruptions came from stratovolcanoes."],
 "requirements": [
  "Stratigraphic section through the cone to read its eruptive history.",
  "Hydrothermal alteration mapping to find weakened sectors.",
  "Glacier/snowpack inventory where ice-capped (lahar source assessment)."],
 "standards": [
  "Layer descriptions follow standard volcanic stratigraphic nomenclature.",
  "Sector-collapse hazard zones use runout models calibrated on past events."],
 "citations": [CIT_CAS, CIT_SIGURDSSON],
 "sig_lens": (
  "Signature edition: stratovolcanoes reframed as his original layered "
  "fortresses - Signature alternating armor of lava and ash, every "
  "stratum a dated entry in his eruption ledger."),
 "demo_kind": "strat_layers",
},
{
 "key": "cinder-cones",
 "name": "Cinder Cones",
 "group": "Foundations",
 "ladder_rank": 2,
 "ladder_tier": "foundations",
 "description": (
  "Cinder cones (scoria cones) are the smallest volcanoes - steep piles "
  "of loose cinders and bombs around a single vent, usually under 300 "
  "meters tall with slopes at the angle of repose, about 30-33 degrees. "
  "They form in single eruptive episodes: gas-rich basaltic magma "
  "fountains and throws out fragments that weld loosely as they land. "
  "Paricutin in Mexico famously grew from a cornfield in 1943, reaching "
  "150 meters in a year, and Sunset Crater in Arizona is a pristine "
  "example. Most cinder cones erupt once and die, though their feeder "
  "dikes can birth new cones nearby, building cinder-cone fields of "
  "hundreds of vents."),
 "how_it_works": (
  "Strombolian-style bursting throws molten clots (bombs) and cinders "
  "ballistically around the vent. Fragments land hot, stack at the "
  "angle of repose, and the cone grows symmetrically unless wind or a "
  "breached side biases it. Larger bombs may weld into agglutinate near "
  "the vent. When the eruption ends, the loose pile compacts and erodes "
  "quickly by geological standards - a cinder cone's sharp profile is a "
  "sign of youth. The underlying dike often continues to feed flank "
  "vents, which is why cones cluster in monogenetic volcanic fields."),
 "key_points": [
  "Smallest volcanoes: <300 m tall, single-vent, slopes at ~30-33 degrees.",
  "Built by Strombolian bursting of gas-rich basalt in one eruptive episode.",
  "Paricutin (1943) grew 150 m in a year from flat farmland - watched from birth.",
  "Loose piles erode fast; sharp profiles mean young cones.",
  "Cluster in monogenetic fields where one dike system feeds many vents."],
 "requirements": [
  "Cone morphometry (height, basal diameter, crater size) to estimate volume and age.",
  "Bomb and cinder sampling to confirm basaltic, Strombolian origin.",
  "Vent alignment mapping to find the feeder dike trend in cone fields."],
 "standards": [
  "Morphometric parameters follow the standard cone-measurement protocol.",
  "Monogenetic vs. polygenetic classification is stated explicitly."],
 "citations": [CIT_SCHMINCKE, CIT_GVP],
 "sig_lens": (
  "Signature edition: cinder cones reframed as his original single-shot "
  "vents - Signature one-eruption builders, each cone a completed "
  "Signature work order."),
 "demo_kind": "cone_angle",
},
{
 "key": "craters-and-calderas",
 "name": "Craters and Calderas",
 "group": "Foundations",
 "ladder_rank": 3,
 "ladder_tier": "foundations",
 "description": (
  "A crater is the bowl at a volcano's summit, usually under a kilometer "
  "across, excavated by explosions or built by accumulation around the "
  "vent. A caldera is something far bigger: a collapse structure "
  "kilometers across, formed when a shallow magma chamber empties in a "
  "huge eruption and the roof founders into the void. Crater Lake, Oregon "
  "fills the 10-kilometer caldera left when Mount Mazama collapsed about "
  "7,700 years ago. Calderas mark the largest eruptions on Earth - the "
  "ones that eject hundreds to thousands of cubic kilometers and can "
  "alter global climate."),
 "how_it_works": (
  "Craters form at the surface: explosions dig them, spatter rims them. "
  "Calderas form at depth: when an eruption withdraws a large fraction "
  "of a shallow chamber, the unsupported roof subsides along ring faults, "
  "sometimes piston-like, sometimes piecemeal. The collapse itself can "
  "squeeze more magma out, prolonging the eruption. Afterward, the "
  "caldera fills with tuff, lava, and lakes; resurgent domes may rise as "
  "deep magma recharges. The diameter of a caldera scales with the "
  "erupted volume - 10-km calderas mean hundreds of cubic kilometers of "
  "magma left the chamber."),
 "key_points": [
  "Craters (<1 km) are surface features; calderas (km to tens of km) are chamber-collapse structures.",
  "Calderas form when a drained magma chamber's roof founders along ring faults.",
  "Crater Lake: 10 km caldera from Mazama's collapse ~7,700 years ago.",
  "Caldera size scales with erupted volume - the signature of giant eruptions.",
  "Post-collapse: tuff fill, lakes, resurgent domes, renewed volcanism."],
 "requirements": [
  "Caldera rim and ring-fault mapping from topography and geology.",
  "Volume estimate of the caldera-forming deposit (ignimbrite sheet).",
  "Geophysical imaging of the underlying magma system."],
 "standards": [
  "Caldera dimensions are reported as rim-to-rim with the measurement basis stated.",
  "Collapse style (piston, piecemeal, trapdoor) is classified per standard schemes."],
 "citations": [CIT_SIGURDSSON, CIT_SCHMINCKE],
 "sig_lens": (
  "Signature edition: calderas reframed as his original chamber-collapse "
  "records - Signature roof-foundering events, every ring fault a "
  "structural receipt for magma withdrawn."),
 "demo_kind": "caldera_area",
},
{
 "key": "magma-chambers-and-plumbing",
 "name": "Magma Chambers and Plumbing Systems",
 "group": "Foundations",
 "ladder_rank": 3,
 "ladder_tier": "foundations",
 "description": (
  "A volcano's plumbing system is the network that moves magma from "
  "source to surface: a deep source region, one or more storage zones "
  "(magma chambers or mush zones), and the conduits - dikes (vertical "
  "cracks), sills (horizontal sheets), and the central vent. Modern "
  "imaging shows chambers are rarely big vats of liquid; they are "
  "'mush zones' of mostly crystalline rock with interstitial melt, "
  "recharged by hotter injections from below. Kilauea's summit reservoir "
  "sits about 3 kilometers down; many arc volcanoes store magma at 5-15 "
  "kilometers. The geometry of this plumbing - where magma stalls, mixes, "
  "and degasses - decides what erupts and how violently."),
 "how_it_works": (
  "Buoyant melt rises until it reaches neutral buoyancy or a structural "
  "trap, then spreads as sills and accumulates in mush zones. Heat from "
  "repeated recharge keeps parts molten; cooling crystallizes the "
  "margins. Pressure builds as new magma arrives and volatiles exsolve; "
  "when pressure exceeds the strength of the roof rock, a dike propagates "
  "upward - sometimes to the surface (eruption), sometimes stalling "
  "(intrusion). Seismicity maps the dike's path in real time; ground "
  "deformation tracks chamber inflation and drainage. Eruption style is "
  "largely set here: shallow degassed storage gives effusive lava, deep "
  "gas-rich recharge gives explosions."),
 "key_points": [
  "Plumbing: source, mush-zone storage, dikes, sills, central vent.",
  "Chambers are crystal mush with melt, not vats of liquid.",
  "Recharge + volatile exsolution build the pressure that drives eruptions.",
  "Dike propagation is tracked live by earthquake swarms and deformation.",
  "Storage depth and degassing history set the eruption style."],
 "requirements": [
  "Seismic tomography or receiver-function imaging of the storage zone.",
  "Deformation data (GPS/InSAR) to locate inflation sources.",
  "Petrologic barometry from mineral chemistry to pin storage depths."],
 "standards": [
  "Storage depths are reported with the barometer or geophysical method stated.",
  "Mush vs. melt-dominated interpretations distinguish data from model."],
 "citations": [CIT_SIGURDSSON, CIT_MOGI],
 "sig_lens": (
  "Signature edition: plumbing systems reframed as his original magma "
  "logistics network - Signature routing from source to vent, every dike "
  "a delivery line in his subsurface supply chain."),
 "demo_kind": "chamber_volume",
},
{
 "key": "viscosity-gas-eruption-control",
 "name": "Viscosity, Gas, and Eruption Control",
 "group": "Foundations",
 "ladder_rank": 3,
 "ladder_tier": "foundations",
 "description": (
  "Two properties decide whether an eruption is a lava fountain or a "
  "cataclysm: magma viscosity and dissolved gas. Viscosity spans eight "
  "orders of magnitude - fluid basalt around 10^2-10^3 pascal-seconds, "
  "sticky rhyolite up to 10^8-10^10. Dissolved water and carbon dioxide "
  "exsolve as magma rises and pressure drops, forming bubbles; in fluid "
  "magma the bubbles escape and lava flows out, but in viscous magma "
  "they are trapped, foam the magma, and finally fragment it into an "
  "explosive eruption. Silica content drives viscosity (more silica, more "
  "polymerized melt), temperature opposes it, and crystals multiply it."),
 "how_it_works": (
  "As magma ascends, falling pressure lets volatiles exsolve - the same "
  "physics as opening a shaken soda. Bubbles grow and the mixture "
  "accelerates upward; if the gas volume fraction passes about 70-80 "
  "percent, the foam fragments into ash and pumice: the "
  "effusive-to-explosive transition. Viscosity controls the race: in "
  "low-viscosity basalt, bubbles rise and escape faster than the magma "
  "ascends, so eruptions stay effusive; in high-viscosity rhyolite, "
  "bubbles are locked in, pressure builds, and fragmentation is "
  "inevitable. Crystal content raises viscosity further, which is why "
  "cool, crystal-rich magmas erupt most violently."),
 "key_points": [
  "Viscosity range: basalt 10^2-10^3 Pa s to rhyolite 10^8-10^10 Pa s.",
  "Dissolved gas exsolves on ascent; trapped bubbles drive explosivity.",
  "Fragmentation near 70-80% gas fraction marks the explosive transition.",
  "Silica raises viscosity; temperature lowers it; crystals multiply it.",
  "The viscosity-gas race decides fountain versus cataclysm."],
 "requirements": [
  "Melt viscosity estimates from composition and temperature models.",
  "Dissolved volatile contents from melt-inclusion analysis.",
  "Vesicle textures in erupted products to reconstruct fragmentation depth."],
 "standards": [
  "Viscosities are reported with temperature, composition, and crystal content.",
  "Fragmentation criteria reference the standard vesicularity thresholds."],
 "citations": [CIT_SCHMINCKE, CIT_CAS],
 "sig_lens": (
  "Signature edition: viscosity and gas reframed as his original "
  "eruption-control dials - Signature twin knobs, stickiness and fizz, "
  "that he tunes to predict every eruption's character."),
 "demo_kind": "viscosity_scale",
},
{
 "key": "basalt-to-rhyolite",
 "name": "The Basalt-to-Rhyolite Composition Scale",
 "group": "Foundations",
 "ladder_rank": 3,
 "ladder_tier": "foundations",
 "description": (
  "Volcanic rocks are classified by silica content, and the scale runs "
  "from fluid to explosive. Basalt (under 52% SiO2) is dark, "
  "magnesium-rich, and fluid - the lava of ocean islands and ridges. "
  "Andesite (52-63%) is the intermediate gray lava of arcs. Dacite "
  "(63-69%) is paler and stiffer. Rhyolite (over 69%) is the "
  "light-colored, gas-rich extreme that builds domes and drives the "
  "largest explosions. The same volcano can erupt across this spectrum "
  "as its magma differentiates: Kilauea erupts basalt, Mount St. Helens "
  "erupts dacite, and Yellowstone's caldera eruptions were rhyolite. "
  "Color, mineralogy, and behavior all follow silica."),
 "how_it_works": (
  "Silica polymerizes the melt - SiO4 tetrahedra link into chains and "
  "networks, and longer chains mean higher viscosity. Mafic minerals "
  "(olivine, pyroxene) crystallize first from basaltic melt, removing "
  "magnesium and iron and leaving the remaining liquid richer in silica: "
  "this fractional crystallization walks magma up the scale from basalt "
  "toward rhyolite. Assimilation of silica-rich crust pushes the same "
  "direction. Because viscosity rises exponentially with silica, each "
  "step up the scale is a step toward more explosive behavior - the "
  "composition scale is effectively an explosivity scale."),
 "key_points": [
  "Basalt <52%, andesite 52-63%, dacite 63-69%, rhyolite >69% SiO2.",
  "Silica polymerizes melt: more silica means exponentially higher viscosity.",
  "Fractional crystallization walks magma from basalt toward rhyolite.",
  "The scale doubles as an explosivity scale - rhyolite erupts most violently.",
  "One volcano can span the spectrum as its system differentiates."],
 "requirements": [
  "Whole-rock major-element analysis (XRF or equivalent) for SiO2.",
  "Mineral assemblage identification to confirm the classification.",
  "Stratigraphic context - which units are which composition."],
 "standards": [
  "Classification follows the IUGS total-alkali-silica (TAS) scheme.",
  "Analyses are reported normalized volatile-free with the method stated."],
 "citations": [CIT_SCHMINCKE, CIT_SIGURDSSON],
 "sig_lens": (
  "Signature edition: the composition scale reframed as his original "
  "magma grading system - Signature silica grades from fluid basalt to "
  "explosive rhyolite, every rock stamped with its grade."),
 "demo_kind": "silica_classify",
},
]

ENTRIES += [
{
 "key": "eruption-styles-hawaiian-strombolian",
 "name": "Eruption Styles: Hawaiian and Strombolian",
 "group": "Compounded",
 "ladder_rank": 4,
 "ladder_tier": "compounded",
 "description": (
  "Hawaiian and Strombolian are the gentle end of the eruption spectrum, "
  "both driven by low-viscosity basaltic magma. Hawaiian eruptions "
  "produce sustained lava fountains - Kilauea Iki's 1959 fountain reached "
  "about 580 meters - feeding lava flows and building shields. Strombolian "
  "eruptions are rhythmic cannon-like bursts every few minutes as large "
  "gas slugs burst through the magma column, throwing incandescent bombs "
  "and cinders that build cinder cones; Stromboli in Italy has done this "
  "for centuries. Both styles are effusive at heart: gas escapes freely "
  "through fluid magma, so pressure never builds to fragmentation."),
 "how_it_works": (
  "In Hawaiian fountaining, rapid magma ascent keeps gas coupled to the "
  "melt until near the surface, where it expands and tears the lava into "
  "a continuous jet - fountain height scales with exit velocity "
  "ballistically. In Strombolian activity, gas coalesces into large slugs "
  "during slow ascent; each slug bursts at the vent like a bubble in "
  "syrup, ejecting a discrete burst of bombs. The difference is ascent "
  "rate and gas flux: fast and steady gives fountains, slow and sluggy "
  "gives bursts. When gas flux rises too high even basalt can shift "
  "toward sustained explosive fountaining - the styles are a continuum, "
  "not boxes."),
 "key_points": [
  "Hawaiian: sustained lava fountains (Kilauea Iki 1959: ~580 m) feeding flows.",
  "Strombolian: rhythmic bursts every few minutes from bursting gas slugs.",
  "Both need fluid basalt where gas escapes freely - no pressure buildup.",
  "Fountain height follows ballistic scaling with magma exit velocity.",
  "Styles form a continuum controlled by ascent rate and gas flux."],
 "requirements": [
  "Vent observations (fountain height, burst frequency) during the eruption.",
  "Magma ascent-rate estimates from deformation or petrology.",
  "Gas flux measurements to place the eruption on the continuum."],
 "standards": [
  "Style names follow the classic (Hawaiian/Strombolian) descriptive scheme.",
  "Fountain heights are reported with the measurement method and time."],
 "citations": [CIT_FRANCIS, CIT_GVP],
 "sig_lens": (
  "Signature edition: gentle eruption styles reframed as his original "
  "low-pressure venting modes - Signature open-valve eruptions, fountains "
  "and bursts logged as controlled releases."),
 "demo_kind": "fountain_height",
},
{
 "key": "eruption-styles-vulcanian-plinian",
 "name": "Eruption Styles: Vulcanian and Plinian",
 "group": "Compounded",
 "ladder_rank": 4,
 "ladder_tier": "compounded",
 "description": (
  "Vulcanian and Plinian are the explosive end of the spectrum, driven by "
  "viscous, gas-rich magma. Vulcanian eruptions are discrete cannon-blast "
  "explosions - a solidified plug caps the vent, pressure builds beneath "
  "it, and the plug shatters into ballistic blocks and ash; Vulcano in "
  "Italy gave the style its name. Plinian eruptions are sustained "
  "gas-thrust columns rising 20 to 45 kilometers into the stratosphere, "
  "named for Pliny the Younger's 79 AD description of Vesuvius's "
  "'pine-tree' cloud. Plinian columns rain ash over continents and "
  "generate the pyroclastic flows that bury landscapes - the style of "
  "Pinatubo 1991 and Tambora 1815."),
 "how_it_works": (
  "Vulcanian explosions happen when a viscous plug seals the conduit: "
  "exsolved gas accumulates below until overpressure fractures the plug, "
  "venting in seconds. The eruption is the seal failing. Plinian columns "
  "are sustained: fragmented magma and gas jet upward, entrain and heat "
  "air, and buoyant rise takes over - column height scales with mass "
  "eruption rate (roughly H proportional to MER^1/4), so taller columns "
  "mean vastly larger eruptions. If the column becomes too dense to stay "
  "buoyant, it collapses into pyroclastic flows. The same eruption can "
  "oscillate between stable columns and collapse as vent conditions "
  "change."),
 "key_points": [
  "Vulcanian: plug-sealed vent, discrete cannon-blast explosions.",
  "Plinian: sustained 20-45 km columns, the largest explosive style.",
  "Column height scales with mass eruption rate - taller means vastly bigger.",
  "Column collapse generates pyroclastic flows; eruptions oscillate between the two.",
  "Pinatubo 1991 and Tambora 1815 are the archetypal Plinian events."],
 "requirements": [
  "Column-height measurements (satellite, radar, or ground observation).",
  "Mass eruption rate estimates from deposit volumes and durations.",
  "Vent imagery to identify plug formation in Vulcanian events."],
 "standards": [
  "Column heights are reported above the vent with the observation method.",
  "Plinian classification requires sustained column behavior, not single blasts."],
 "citations": [CIT_CAS, CIT_PLINY],
 "sig_lens": (
  "Signature edition: explosive styles reframed as his original "
  "high-pressure discharge modes - Signature sealed-valve blasts and "
  "sustained column events, each rated by his column-height scale."),
 "demo_kind": "plinian_column",
},
{
 "key": "pyroclastic-flows",
 "name": "Pyroclastic Flows and Surges",
 "group": "Compounded",
 "ladder_rank": 4,
 "ladder_tier": "compounded",
 "description": (
  "Pyroclastic flows (pyroclastic density currents) are the deadliest "
  "volcanic phenomenon: avalanches of hot gas, ash, and rock racing "
  "downhill at 100 to 700 kilometers per hour at temperatures up to 700 "
  "degrees Celsius. They form when an eruption column collapses, when a "
  "lava dome crumbles, or in directed blasts. The 1902 Mont Pelee flow "
  "destroyed St. Pierre and killed about 30,000 people in minutes; the "
  "79 AD Vesuvius surges killed the remaining population of Pompeii. "
  "Surges are the dilute, turbulent cousins that can detach from the "
  "main flow and overtop ridges. Nothing in the path survives - "
  "structures are flattened, organic matter carbonized."),
 "how_it_works": (
  "A collapsing column or crumbling dome feeds a ground-hugging current "
  "denser than air. The dense basal part carries blocks and bombs; the "
  "overriding dilute ash cloud billows kilometers high. The flow rides "
  "on a cushion of trapped, heated air and fluidized ash, which is why "
  "it moves so fast and far - runout follows energy-line (energy cone) "
  "scaling, descending at roughly 0.2 of the drop height per unit "
  "distance. Friction at the base and sedimentation bleed energy; the "
  "flow stops where its energy is spent, depositing unsorted ignimbrite. "
  "Surges detach where the flow accelerates over breaks in slope, "
  "decoupling the dilute cloud from the dense base."),
 "key_points": [
  "Fastest, hottest, deadliest: 100-700 km/h, up to ~700 C.",
  "Generated by column collapse, dome collapse, or directed blasts.",
  "Mont Pelee 1902 (~30,000 dead) and Pompeii's surges are the archetypes.",
  "Runout follows energy-cone scaling; flows stop where energy is spent.",
  "Surges are dilute turbulent clouds that can overtop topographic barriers."],
 "requirements": [
  "Ignimbrite deposit mapping (thickness, extent, grain size) to reconstruct flow paths.",
  "Column or dome behavior observations to identify the generation mechanism.",
  "Runout modeling (energy cone or numerical) for hazard zoning."],
 "standards": [
  "Pyroclastic-flow vs. surge deposits are distinguished by standard sedimentological criteria.",
  "Hazard zones use calibrated runout models, not arbitrary buffers."],
 "citations": [CIT_FISHER, CIT_SPARKS],
 "sig_lens": (
  "Signature edition: pyroclastic flows reframed as his original "
  "gravity-driven incineration currents - Signature hot avalanches, "
  "every runout a solved energy-budget entry."),
 "demo_kind": "pdc_runout",
},
{
 "key": "lahars",
 "name": "Lahars: Volcanic Mudflows",
 "group": "Compounded",
 "ladder_rank": 5,
 "ladder_tier": "compounded",
 "description": (
  "Lahars are volcanic mudflows - slurries of water, mud, and rock "
  "debris mobilized on volcano flanks - and they are among the longest-"
  "reaching volcanic killers, traveling tens of kilometers down river "
  "valleys at up to 100 kilometers per hour. They form when eruptions "
  "melt snow and ice, when crater lakes breach, when heavy rain "
  "remobilizes fresh ash, or when sector collapses dam and release "
  "rivers. The 1985 Nevado del Ruiz lahar killed about 23,000 people in "
  "Armero, Colombia, 74 kilometers from the volcano, from an eruption "
  "rated only VEI 3. Pinatubo's 1991 deposits generated devastating "
  "lahars for more than a decade after the eruption ended."),
 "how_it_works": (
  "Water mixes with loose volcanic debris to make a slurry denser than "
  "water alone - up to twice the density - so lahars carry boulders "
  "meters across and exert enormous impact forces. They bulk up as they "
  "descend, eroding channel banks and entraining more sediment, which is "
  "why small initial flows become valley-filling torrents. Flow velocity "
  "depends on slope, channel confinement, and sediment concentration; "
  "confinement in valleys keeps them fast and deep far from the volcano. "
  "Acoustic flow monitors on Pinatubo and Rainier detect the ground "
  "vibration of approaching lahars, giving downstream towns tens of "
  "minutes of warning."),
 "key_points": [
  "Volcanic mudflows: water + debris slurries reaching tens of km at up to ~100 km/h.",
  "Nevado del Ruiz 1985: ~23,000 dead 74 km from a VEI 3 eruption.",
  "Triggered by ice melt, crater-lake breach, rain on fresh ash, or collapse.",
  "Bulk up by erosion downstream - small starts become valley-filling torrents.",
  "Acoustic flow monitors give downstream warning; hazard maps follow valleys."],
 "requirements": [
  "Drainage and valley mapping to trace lahar pathways from the edifice.",
  "Water-source inventory (glaciers, crater lakes, rainfall climatology).",
  "Acoustic or seismic flow sensors on key drainages for warning."],
 "standards": [
  "Lahar hazard zones follow mapped drainages with modeled inundation, not circles.",
  "Warning systems use calibrated acoustic-flow-monitor thresholds."],
 "citations": [CIT_TILLING, CIT_PINATUBO],
 "sig_lens": (
  "Signature edition: lahars reframed as his original slurry-weapon "
  "hydrology - Signature debris torrents, every valley a mapped "
  "delivery channel in his hazard ledger."),
 "demo_kind": "lahar_velocity",
},
{
 "key": "tephra-and-ashfall",
 "name": "Tephra and Ashfall",
 "group": "Compounded",
 "ladder_rank": 5,
 "ladder_tier": "compounded",
 "description": (
  "Tephra is the collective term for everything blasted out of a "
  "volcano: bombs and blocks (over 64 mm), lapilli (2-64 mm), and ash "
  "(under 2 mm). Ashfall is the most far-reaching volcanic hazard - "
  "Pinatubo 1991 dusted the region in centimeters of ash, and "
  "Eyjafjallajokull's 2010 ash closed European airspace for a week. "
  "Ash is pulverized rock and glass: it collapses roofs, shorts "
  "electrical systems, contaminates water, destroys jet engines, and "
  "damages lungs. Because fine ash rides stratospheric winds, even "
  "moderate eruptions can disrupt continents - and because ash layers "
  "are instant time markers, tephrochronologists use them to date "
  "archaeological and geological events worldwide."),
 "how_it_works": (
  "Fragmented magma leaves the vent as a mixture spanning microns to "
  "meters. The eruption column sorts it by size: coarse bombs fall near "
  "the vent ballistically, while fine ash is carried by the umbrella "
  "cloud and winds, settling by gravity and aggregation. Deposit "
  "thickness thins exponentially with distance (isopach maps), and the "
  "thinning rate encodes column height and wind - the basis for "
  "reconstructing past eruptions from their deposits. Ash aggregation "
  "(fine particles clumping in the moist plume) makes ash fall out "
  "closer than simple settling predicts. In the stratosphere, the "
  "finest ash and sulfate aerosols circle the globe for years."),
 "key_points": [
  "Tephra sizes: bombs/blocks >64 mm, lapilli 2-64 mm, ash <2 mm.",
  "Ashfall is the farthest-reaching hazard - roofs, power, water, aviation, health.",
  "Eyjafjallajokull 2010 ash closed European airspace for a week.",
  "Isopach thinning with distance encodes column height and wind.",
  "Ash layers are global time markers - the basis of tephrochronology."],
 "requirements": [
  "Isopach and isopleth mapping of the fall deposit.",
  "Grain-size analysis to reconstruct column and wind conditions.",
  "Aviation ash-dispersion modeling during the eruption."],
 "standards": [
  "Tephra size classes follow the standard >64 / 2-64 / <2 mm scheme.",
  "Ashfall hazard maps use dispersion models calibrated on the eruption."],
 "citations": [CIT_CAS, CIT_FISHER],
 "sig_lens": (
  "Signature edition: tephra reframed as his original airborne fragment "
  "ledger - Signature sorted fallout, every isopach a contour of his "
  "dispersal accounting."),
 "demo_kind": "tephra_fallout",
},
{
 "key": "volcanic-gases-and-climate",
 "name": "Volcanic Gases and Climate",
 "group": "Compounded",
 "ladder_rank": 5,
 "ladder_tier": "compounded",
 "description": (
  "Volcanoes exhale water vapor, carbon dioxide, and sulfur dioxide, "
  "and the sulfur is what changes the climate. SO2 injected into the "
  "stratosphere converts to sulfate aerosols that reflect sunlight and "
  "cool the planet: Pinatubo's 1991 injection of about 20 megatons of "
  "SO2 cooled the globe roughly 0.5 degrees Celsius for two to three "
  "years, and Tambora's 1815 eruption caused 1816's 'Year Without a "
  "Summer' with crop failures across the Northern Hemisphere. Volcanic "
  "CO2, by contrast, is a small fraction of human emissions - about 1 "
  "percent - and does not drive modern warming. Halogen gases can chew "
  "at the ozone layer. The climate fingerprint of a big eruption is "
  "unmistakable in ice cores and tree rings."),
 "how_it_works": (
  "Eruption columns that breach the tropopause inject SO2 directly into "
  "the stratosphere, where it oxidizes to sulfuric acid droplets over "
  "weeks. The aerosols persist for 1-3 years, scattering incoming solar "
  "radiation back to space; the surface cools while the stratosphere "
  "warms from absorbed radiation. Cooling scales roughly with the "
  "stratospheric sulfur load and the latitude of injection - tropical "
  "eruptions spread aerosols to both hemispheres. Ice cores preserve the "
  "sulfate spikes, letting scientists match climate anomalies to "
  "eruptions thousands of years old, and satellite sensors now track "
  "SO2 clouds in near real time."),
 "key_points": [
  "Stratospheric SO2 becomes sulfate aerosols that reflect sunlight and cool Earth.",
  "Pinatubo 1991 (~20 Mt SO2): ~0.5 C global cooling for 2-3 years.",
  "Tambora 1815 caused 1816's 'Year Without a Summer'.",
  "Volcanic CO2 is ~1% of human emissions - not the driver of modern warming.",
  "Ice-core sulfate spikes fingerprint ancient eruptions and their climate hits."],
 "requirements": [
  "SO2 emission estimates (satellite or ground-based) for the eruption.",
  "Stratospheric injection height - tropospheric sulfur rains out quickly.",
  "Ice-core or instrumental climate records to measure the response."],
 "standards": [
  "Climate forcing is reported as aerosol optical depth with the estimation method.",
  "Volcanic vs. anthropogenic CO2 comparisons use published global budgets."],
 "citations": [CIT_ROBOCK, CIT_TAMBORA],
 "sig_lens": (
  "Signature edition: volcanic climate effects reframed as his original "
  "planetary thermostat - Signature sulfur injections, every cooling "
  "event a metered adjustment in his climate ledger."),
 "demo_kind": "aerosol_cooling",
},
{
 "key": "vei-scale",
 "name": "The Volcanic Explosivity Index (VEI)",
 "group": "Compounded",
 "ladder_rank": 6,
 "ladder_tier": "compounded",
 "description": (
  "The Volcanic Explosivity Index, published by Newhall and Self in "
  "1982, rates explosive eruptions from 0 to 8 on the volume of ejected "
  "material - each step is roughly ten times the volume of the last. "
  "VEI 0 is a gentle Hawaiian lava flow; VEI 5 (St. Helens 1980, ~1 "
  "km^3) is very large; VEI 6 (Pinatubo 1991, Krakatau 1883, ~10 km^3) "
  "is colossal; VEI 7 (Tambora 1815, ~150 km^3) is super-colossal; VEI 8 "
  "(over 1,000 km^3 - Yellowstone's Huckleberry Ridge, Toba) is "
  "mega-colossal, the supervolcano class. The scale also folds in "
  "column height and qualitative descriptions, but volume is its "
  "backbone - and because it is logarithmic, the jump from VEI 6 to 8 "
  "is a hundredfold leap in erupted mass."),
 "how_it_works": (
  "VEI is assigned from the dense-rock-equivalent volume of erupted "
  "tephra: field teams map isopachs, integrate thickness over area, and "
  "correct for deposit density to get DRE volume, then read the VEI "
  "from the logarithmic bins (0.00001 km^3 at VEI 0 up to >1000 km^3 "
  "at VEI 8). Column height and eruption descriptors corroborate the "
  "assignment for historical events. The index is descriptive, not "
  "predictive - it rates what happened, and it saturates for the "
  "largest events - but it lets scientists compare eruptions across "
  "centuries: Tambora's VEI 7 was about ten times Pinatubo's VEI 6, "
  "which was about ten times St. Helens' VEI 5."),
 "key_points": [
  "VEI 0-8, logarithmic: each step ~10x the ejecta volume (Newhall & Self 1982).",
  "VEI 5: St. Helens 1980 (~1 km^3); VEI 6: Pinatubo 1991 (~10 km^3).",
  "VEI 7: Tambora 1815 (~150 km^3); VEI 8: >1,000 km^3 - the supervolcanoes.",
  "Assigned from dense-rock-equivalent deposit volume plus column height.",
  "Descriptive, not predictive - it rates eruptions after they happen."],
 "requirements": [
  "Isopach-mapped deposit volume converted to dense-rock equivalent.",
  "Column-height observations where available for corroboration.",
  "Historical accounts calibrated against deposit evidence."],
 "standards": [
  "VEI assignments cite the volume estimate and its method.",
  "DRE conversions state the assumed deposit density."],
 "citations": [CIT_NEWHALL, CIT_GVP],
 "sig_lens": (
  "Signature edition: the VEI reframed as his original eruption-rating "
  "ladder - Signature magnitude classes, every eruption scored on his "
  "tenfold volume scale."),
 "demo_kind": "vei_table",
},
{
 "key": "lava-flows-pahoehoe-aa-tubes",
 "name": "Lava Flows: Pahoehoe, Aa, and Lava Tubes",
 "group": "Compounded",
 "ladder_rank": 6,
 "ladder_tier": "compounded",
 "description": (
  "Pahoehoe and aa are the two great textures of basaltic lava flows. "
  "Pahoehoe is smooth, ropy, billowy - the skin of a flow that stayed "
  "hot and fluid, wrinkling as it advanced. Aa (pronounced 'ah-ah') is "
  "a jagged field of sharp clinkers - the same lava after its surface "
  "cooled, stiffened, and tore apart as the fluid interior kept moving. "
  "A single flow can start as pahoehoe and transform into aa downstream "
  "as it cools and crystallizes. Where pahoehoe's roof solidifies over "
  "a still-flowing stream, lava tubes form - insulated pipelines that "
  "carry lava tens of kilometers with little heat loss, the reason "
  "shield volcanoes can flood such vast areas from one vent."),
 "how_it_works": (
  "The pahoehoe-to-aa transition is a race between cooling and shear: "
  "as crystals grow, viscosity climbs; when the applied shear rate "
  "exceeds what the stiffening crust can accommodate smoothly, the "
  "surface ruptures into clinkers. Faster flow, steeper slopes, and "
  "higher eruption rates favor aa; slow, insulated advance favors "
  "pahoehoe. Tubes form when the surface crusts over - levees join, or "
  "a pahoehoe lobe inflates and roofs itself - and the insulated "
  "interior stays near eruption temperature for weeks. Tube-fed flows "
  "advance by breakouts at the front, building broad sheet flows "
  "almost invisibly from the surface."),
 "key_points": [
  "Pahoehoe: smooth and ropy (hot, fluid); aa: jagged clinker (cooled, torn).",
  "One flow can evolve pahoehoe to aa downstream as it cools and crystallizes.",
  "The transition is controlled by cooling rate vs. shear rate.",
  "Lava tubes are crusted-over streams - insulated pipelines tens of km long.",
  "Tube-fed breakouts build the broad sheet flows of shield volcanoes."],
 "requirements": [
  "Flow-surface mapping to classify pahoehoe/aa/blocky facies.",
  "Eruption-rate and slope data to explain the observed transition point.",
  "Tube surveys (or skylight mapping) for the feeder system."],
 "standards": [
  "Flow textures use the standard pahoehoe/aa/blocky terminology.",
  "Tube dimensions are reported from survey, not estimated from skylights alone."],
 "citations": [CIT_CAS, CIT_FRANCIS],
 "sig_lens": (
  "Signature edition: flow textures reframed as his original cooling-"
  "race record - Signature pahoehoe-to-aa transitions, every clinker a "
  "timestamp of the heat leaving the flow."),
 "demo_kind": "lava_morphology",
},
{
 "key": "volcano-monitoring-seismic",
 "name": "Seismic Monitoring of Volcanoes",
 "group": "Compounded",
 "ladder_rank": 6,
 "ladder_tier": "compounded",
 "description": (
  "Seismometers are a volcano observatory's first eyes: magma on the "
  "move cracks rock, and each crack is an earthquake. Volcano-tectonic "
  "(VT) quakes are brittle-failure events as magma forces its way "
  "upward; swarms of VTs migrating toward the surface track an "
  "intrusion in real time. Long-period events and volcanic tremor are "
  "the resonance of fluids - magma and gas sloshing through conduits - "
  "and sustained tremor often means eruption is underway or imminent. "
  "RSAM (real-time seismic amplitude) plots give watchstanders a single "
  "heartbeat line for the volcano. Nearly every successful eruption "
  "forecast in history - Pinatubo 1991, St. Helens 1980, Eyjafjallajokull "
  "2010 - began with seismic unrest."),
 "how_it_works": (
  "A network of seismometers around the edifice locates quakes in three "
  "dimensions; the migration of hypocenters maps the dike or conduit as "
  "it propagates - upward migration over hours to days is the classic "
  "pre-eruption signal. Frequency content distinguishes types: VT "
  "events are high-frequency like tectonic quakes; long-period events "
  "are low-frequency fluid resonance; tremor is continuous low-frequency "
  "chatter. RSAM compresses all of it into amplitude-vs-time, and "
  "alarm thresholds on RSAM trigger observatory response. Seismic data "
  "alone rarely gives the eruption time, but combined with deformation "
  "and gas it forms the core of every forecast."),
 "key_points": [
  "VT swarms track magma forcing upward; migrating hypocenters map intrusions live.",
  "Long-period events and tremor are fluid resonance - magma and gas moving.",
  "RSAM gives a single heartbeat line; thresholds trigger observatory alarms.",
  "Nearly every successful eruption forecast began with seismic unrest.",
  "Seismic + deformation + gas together make the forecast; seismic is the first eye."],
 "requirements": [
  "A seismic network (ideally 4+ stations) around the edifice.",
  "Event classification (VT, long-period, tremor, hybrid) in near real time.",
  "RSAM or equivalent amplitude monitoring with set alarm thresholds."],
 "standards": [
  "Event types follow standard volcano-seismic classification.",
  "Locations are reported with the velocity model and uncertainty stated."],
 "citations": [CIT_TILLING, CIT_USGS],
 "sig_lens": (
  "Signature edition: volcano seismology reframed as his original "
  "subsurface listening array - Signature magma-tracking ears, every "
  "swarm a footstep of rising melt in his ledger."),
 "demo_kind": "rsam_alarm",
},
{
 "key": "ground-deformation",
 "name": "Ground Deformation: GPS, Tilt, and InSAR",
 "group": "Compounded",
 "ladder_rank": 7,
 "ladder_tier": "compounded",
 "description": (
  "When magma accumulates underground, the ground surface swells - and "
  "measuring that swelling locates the magma. GPS stations track "
  "millimeter-scale displacements continuously; tiltmeters sense "
  "microradian tilts of the edifice; satellite InSAR (interferometric "
  "synthetic aperture radar) maps deformation over whole volcanoes at "
  "centimeter precision from orbit. The classic Mogi model treats the "
  "inflation as a pressurized sphere, relating surface uplift to the "
  "chamber's depth and volume change. Kilauea's summit inflates and "
  "deflates like a breathing lung with magma supply; the 1980 St. "
  "Helens bulge grew 5 feet per day before the flank failed - "
  "deformation was the warning."),
 "how_it_works": (
  "A pressurizing magma chamber pushes the surface up and outward in a "
  "characteristic radial pattern; inverting the pattern gives the "
  "source depth and volume change (Mogi 1958 for a sphere, Okada "
  "solutions for dikes and sills). GPS gives point time series, "
  "tiltmeters give ultra-sensitive local slope, and InSAR gives spatial "
  "maps - differencing two radar images reveals fringes, each fringe a "
  "half-wavelength (about 2.8 cm for C-band) of line-of-sight motion. "
  "Rapid inflation means magma arriving; rapid deflation during "
  "eruption measures the withdrawn volume. Sustained inflation without "
  "eruption is watched closely - it is stored potential."),
 "key_points": [
  "Inflation locates magma: GPS (mm), tilt (microradians), InSAR (cm from orbit).",
  "Mogi model: surface uplift pattern gives chamber depth and volume change.",
  "Kilauea breathes with magma supply; St. Helens' bulge warned of 1980.",
  "Deflation during eruption measures the withdrawn magma volume.",
  "Inflation without eruption is stored potential - watched, not ignored."],
 "requirements": [
  "Continuous GPS or tilt stations on the edifice flanks and summit.",
  "Repeat InSAR acquisitions for spatial deformation maps.",
  "An elastic half-space model (Mogi/Okada) for source inversion."],
 "standards": [
  "Deformation is reported with the reference frame and time window stated.",
  "Source inversions state the model geometry and its non-uniqueness."],
 "citations": [CIT_MOGI, CIT_USGS],
 "sig_lens": (
  "Signature edition: ground deformation reframed as his original "
  "planetary breathing monitor - Signature inflation gauges, every "
  "millimeter of uplift a pressure reading in his ledger."),
 "demo_kind": "mogi_uplift",
},
{
 "key": "gas-monitoring",
 "name": "Volcanic Gas Monitoring",
 "group": "Compounded",
 "ladder_rank": 7,
 "ladder_tier": "compounded",
 "description": (
  "Rising magma exsolves gas, so gas is the most direct chemical signal "
  "of what magma is doing. Sulfur dioxide (SO2) flux is the workhorse: "
  "a climbing SO2 flux means fresh, gas-rich magma is ascending, and "
  "many eruptions are preceded by SO2 increases - measured by "
  "ultraviolet spectrometers (COSPEC, DOAS, and now the TROPOMI "
  "satellite) scanning the plume. CO2, which exsolves deeper, can "
  "signal deep recharge before SO2 moves; diffuse CO2 killed trees at "
  "Mammoth Mountain and people at Lake Nyos. Plume chemistry ratios "
  "(CO2/SO2, H2S/SO2) track magma depth: deep gas is CO2-rich, shallow "
  "degassing is SO2-rich."),
 "how_it_works": (
  "UV spectrometers measure how much sunlight the plume absorbs at SO2 "
  "wavelengths; multiplying the path concentration by wind speed and "
  "plume width gives flux in tons per day. MultiGAS stations on crater "
  "rims sample the plume directly for CO2, SO2, H2S, and water ratios. "
  "Because CO2 exsolves at greater depth than SO2, a rising CO2/SO2 "
  "ratio means magma is coming up from depth - one of the earliest "
  "deep-recharge signals available. Satellite SO2 tracking now catches "
  "unrest at remote volcanoes with no ground instruments at all."),
 "key_points": [
  "SO2 flux is the workhorse precursor - rising flux means ascending gas-rich magma.",
  "UV spectrometers and satellites (TROPOMI) measure plumes remotely.",
  "CO2 exsolves deeper than SO2: rising CO2/SO2 signals deep recharge.",
  "Diffuse CO2 is itself lethal (Mammoth Mountain, Lake Nyos).",
  "Gas ratios track magma depth - chemistry as a depth sounder."],
 "requirements": [
  "UV spectrometer traverses or scanning stations with wind data for flux.",
  "MultiGAS or direct sampling for gas ratios.",
  "Baseline flux measurements - anomalies only mean something against a baseline."],
 "standards": [
  "Fluxes are reported in tons/day with wind source and uncertainty.",
  "Gas ratios state the sampling method (plume, fumarole, soil)."],
 "citations": [CIT_FRANCIS, CIT_USGS],
 "sig_lens": (
  "Signature edition: gas monitoring reframed as his original magma "
  "breathalyzer - Signature plume chemistry, every ton of SO2 a "
  "metered exhalation in his ledger."),
 "demo_kind": "so2_flux",
},
{
 "key": "eruption-forecasting-alerts",
 "name": "Eruption Forecasting and Alert Levels",
 "group": "Compounded",
 "ladder_rank": 7,
 "ladder_tier": "compounded",
 "description": (
  "Eruption forecasting is pattern recognition under uncertainty: "
  "observatories combine seismicity, deformation, gas, and thermal data "
  "into probabilistic statements, not dates. The USGS uses four ground "
  "alert levels - Normal, Advisory, Watch, Warning - paired with aviation "
  "color codes (Green, Yellow, Orange, Red), and similar systems run "
  "worldwide. Forecasts succeeded at Pinatubo 1991 (tens of thousands "
  "evacuated, hundreds of lives saved) and failed or stayed ambiguous "
  "elsewhere - unrest often stalls without erupting, and some eruptions "
  "give little warning. The modern goal is honest probabilities: what "
  "is most likely, what is the worst case, and what would change the "
  "assessment."),
 "how_it_works": (
  "Forecasting works by comparing current unrest to the volcano's own "
  "history and to global analogues: accelerating VT swarms plus "
  "inflation plus rising SO2 is the classic pre-eruptive triad. "
  "Bayesian frameworks update eruption probability as new data "
  "arrives; event trees map the branches (no eruption, small "
  "eruption, large eruption) with assigned probabilities. Alert "
  "levels are raised when multiple independent data streams agree - "
  "no single parameter triggers a Warning. Communication is part of "
  "the system: alert levels translate the science into evacuation "
  "decisions, and false alarms are priced in - a missed evacuation "
  "costs lives, a false one costs trust."),
 "key_points": [
  "Forecasts are probabilistic - patterns and likelihoods, never dates.",
  "USGS levels: Normal/Advisory/Watch/Warning + aviation Green/Yellow/Orange/Red.",
  "The pre-eruptive triad: accelerating seismicity + inflation + rising gas.",
  "Pinatubo 1991: forecasting plus evacuation saved tens of thousands.",
  "Unrest often stalls; alert systems price in false alarms vs. missed events."],
 "requirements": [
  "Multi-parameter monitoring (seismic, deformation, gas minimum).",
  "The volcano's eruption history and global analogue cases.",
  "An event-tree or Bayesian framework for transparent probabilities."],
 "standards": [
  "Alert levels follow the national observatory framework in use.",
  "Probabilistic forecasts state the time window and data behind them."],
 "citations": [CIT_TILLING, CIT_USGS],
 "sig_lens": (
  "Signature edition: eruption forecasting reframed as his original "
  "unrest-decision engine - Signature probability ladders, every alert "
  "level a calibrated call in his warning ledger."),
 "demo_kind": "alert_logic",
},
]

ENTRIES += [
{
 "key": "supervolcanoes",
 "name": "Supervolcanoes and Caldera-Forming Eruptions",
 "group": "Advanced",
 "ladder_rank": 8,
 "ladder_tier": "advanced",
 "description": (
  "Supervolcanoes are the volcanoes behind VEI 8 eruptions - events "
  "ejecting over 1,000 cubic kilometers of magma, hundreds of times "
  "Pinatubo. Yellowstone's Huckleberry Ridge eruption 2.1 million years "
  "ago expelled about 2,500 km^3; Toba in Sumatra 74,000 years ago "
  "expelled about 2,800 km^3, possibly bottlenecking early humans; "
  "Taupo's Oruanui eruption 26,500 years ago expelled about 1,170 km^3. "
  "These eruptions collapse giant calderas tens of kilometers across, "
  "bury continents in ignimbrite, and inject enough sulfur to cool the "
  "globe for years. They recur on hundred-thousand-year timescales at "
  "any one system - Yellowstone erupts catastrophically roughly every "
  "600,000-800,000 years - and no VEI 8 has occurred in recorded "
  "history."),
 "how_it_works": (
  "Supervolcano systems are long-lived crustal magma reservoirs where "
  "repeated basaltic recharge melts and accumulates rhyolitic magma "
  "over hundreds of thousands of years. When the overpressure and "
  "buoyancy of the accumulated silicic magma exceed the roof strength, "
  "ring fractures propagate and the eruption begins - often as a "
  "Plinian column that transitions to column collapse, feeding "
  "continent-scale pyroclastic flows while the caldera floor founders. "
  "The sulfur load drives years of global cooling; the ash fertilizes "
  "and chokes ecosystems for decades. Afterward the system recharges: "
  "Yellowstone's caldera floor has risen and fallen meters in recent "
  "decades as magma and hydrothermal fluids move - monitored, but not "
  "an eruption signal by itself."),
 "key_points": [
  "VEI 8: >1,000 km^3 erupted - Yellowstone (2,500), Toba (2,800), Taupo Oruanui (1,170).",
  "Collapse giant calderas tens of km across; bury regions in ignimbrite.",
  "Sulfur injections drive years of global cooling; no VEI 8 in recorded history.",
  "Form by long accumulation of rhyolitic magma above basaltic recharge zones.",
  "Recur on ~10^5-year timescales per system; current unrest is monitored, not alarming."],
 "requirements": [
  "Ignimbrite volume mapping to confirm the >1,000 km^3 threshold.",
  "High-precision dating to establish recurrence intervals.",
  "Continuous monitoring (seismic, deformation, gas) of the active system."],
 "standards": [
  "Supervolcano designation requires VEI 8 volume with documented methodology.",
  "Hazard communication distinguishes background unrest from eruption precursors."],
 "citations": [CIT_MILLER, CIT_SIGURDSSON],
 "sig_lens": (
  "Signature edition: supervolcanoes reframed as his original planetary "
  "reset engines - Signature mega-chambers, every thousand cubic "
  "kilometers a full-system discharge in his deep-time ledger."),
 "demo_kind": "supervolcano_scale",
},
{
 "key": "magma-chamber-dynamics",
 "name": "Magma Chamber Dynamics",
 "group": "Advanced",
 "ladder_rank": 8,
 "ladder_tier": "advanced",
 "description": (
  "Magma chambers are not static tanks - they convect, recharge, cool, "
  "and crystallize continuously. Hotter, denser recharge magma ponds "
  "beneath cooler resident magma, driving compositional convection; "
  "the Rayleigh number for a kilometer-scale basaltic chamber exceeds "
  "the convective threshold by many orders of magnitude, so chambers "
  "stir themselves. Cooling at the walls crystallizes margins "
  "inward, concentrating volatiles and silica in the remaining melt. "
  "Recharge events show up as banded crystals - minerals recording "
  "each new injection like tree rings - and as the mixed magmas that "
  "trigger many eruptions. Understanding this dynamics is what turns a "
  "static 'chamber' picture into a working, forecastable system."),
 "how_it_works": (
  "Convection starts when buoyancy overcomes viscosity: the dimensionless "
  "Rayleigh number Ra = (alpha g delta-T d^3)/(kappa nu) must exceed "
  "about 1,708, and magma chambers clear it enormously - thermal and "
  "compositional gradients both drive overturn. Dense recharge magma "
  "fountains into the chamber base, entraining resident melt and "
  "sometimes triggering eruption by overpressure or volatile "
  "destabilization. Meanwhile conductive cooling grows a crystalline "
  "rind; the shrinking melt fraction enriches the remainder in silica "
  "and volatiles (second boiling), raising the explosive potential "
  "even without new magma. Crystal zoning records each chapter: "
  "resorption surfaces mark recharge, growth bands mark quiet "
  "intervals."),
 "key_points": [
  "Chambers convect vigorously - Rayleigh numbers far above the convective threshold.",
  "Recharge ponds, fountains, and mixes; banded crystals record each injection.",
  "Wall cooling crystallizes margins, enriching residual melt in silica and gas.",
  "Recharge-triggered overpressure starts many eruptions.",
  "Crystal zoning reads the chamber's history like tree rings."],
 "requirements": [
  "Crystal-scale petrology (zoning, resorption textures) from erupted products.",
  "Thermal and compositional modeling of the specific chamber geometry.",
  "Monitoring data (deformation, seismicity) for the active dynamics."],
 "standards": [
  "Convection claims state the assumed viscosity, size, and driving gradient.",
  "Recharge interpretations require textural or chemical evidence, not assertion."],
 "citations": [CIT_SIGURDSSON, CIT_SCHMINCKE],
 "sig_lens": (
  "Signature edition: chamber dynamics reframed as his original "
  "subsurface stirring engine - Signature convection cells, every "
  "recharge a fresh fuel delivery in his magma logistics."),
 "demo_kind": "rayleigh_number",
},
{
 "key": "crystal-fractionation",
 "name": "Crystal Fractionation and Magma Differentiation",
 "group": "Advanced",
 "ladder_rank": 8,
 "ladder_tier": "advanced",
 "description": (
  "Crystal fractionation is the engine that turns basalt into rhyolite: "
  "as magma cools, minerals crystallize in sequence - olivine and "
  "pyroxene first, then plagioclase, then quartz and alkali feldspar "
  "(Bowen's reaction series) - and if the crystals separate from the "
  "liquid, the remaining melt grows richer in silica and incompatible "
  "elements. The Rayleigh fractionation equation (C = C0 * F^(D-1)) "
  "quantifies it: an element excluded from crystals (D near 0) doubles "
  "in the melt with each halving of melt fraction. This single process "
  "explains why arc volcanoes erupt andesite from basaltic parents, why "
  "rhyolite caps long-lived systems, and why trace-element patterns are "
  "the petrologist's tape recorder of differentiation."),
 "how_it_works": (
  "Crystals separate by settling (dense olivine sinks), by flotation, "
  "by filter-pressing in compacting mush, or by flow segregation - any "
  "mechanism that removes early mafic crystals drives the liquid toward "
  "silica enrichment. The partition coefficient D sets each element's "
  "fate: compatible elements (nickel in olivine, D >> 1) plummet in the "
  "melt, incompatible ones (rubidium, D << 1) climb steeply. Plotting "
  "incompatible-element ratios against silica draws the liquid line of "
  "descent - the differentiation path. Combined with assimilation of "
  "crustal melt (AFC processes), fractionation accounts for the full "
  "basalt-to-rhyolite spectrum from a single mantle parent."),
 "key_points": [
  "Bowen's series: olivine/pyroxene first, quartz/feldspar last.",
  "Rayleigh equation C = C0 F^(D-1) quantifies enrichment and depletion.",
  "Incompatible elements climb as melt fraction shrinks - the petrologic tape recorder.",
  "Explains andesite from basaltic parents and rhyolite atop old systems.",
  "With crustal assimilation (AFC), covers the full compositional spectrum."],
 "requirements": [
  "Mineral assemblages and compositions to identify the fractionating phases.",
  "Trace-element analyses to fit the Rayleigh model.",
  "Isotopic data to separate fractionation from assimilation."],
 "standards": [
  "D values are cited from experimental partitioning literature for the stated conditions.",
  "AFC models state the assimilant composition and the r (assimilation/fractionation) ratio."],
 "citations": [CIT_SCHMINCKE, CIT_SIGURDSSON],
 "sig_lens": (
  "Signature edition: fractionation reframed as his original magma "
  "refinery - Signature crystal separation, every enriched melt a "
  "refined product in his differentiation ledger."),
 "demo_kind": "rayleigh_fractionation",
},
{
 "key": "volcanic-hazard-maps-risk",
 "name": "Volcanic Hazard Maps and Risk Assessment",
 "group": "Advanced",
 "ladder_rank": 8,
 "ladder_tier": "advanced",
 "description": (
  "Volcanic hazard maps translate geology into decisions: they zone the "
  "landscape by what each area could experience - pyroclastic-flow "
  "inundation, lahar pathways, ashfall thickness, lava-flow advance, "
  "ballistic impact - usually for a reference eruption scenario and "
  "sometimes probabilistically. Risk assessment goes further, "
  "multiplying hazard by exposure and vulnerability: how many people, "
  "what buildings, what infrastructure lie in each zone. The maps at "
  "Rainier, Vesuvius, and Merapi drive land-use planning and evacuation "
  "routing. Their honesty matters: a hazard map that understates the "
  "worst case, like the one that left Armero unprotected in 1985, "
  "fails at its only job."),
 "how_it_works": (
  "Hazard mappers start from the volcano's deposit record - the past is "
  "the template - then run physics-based models: energy-cone runouts "
  "for pyroclastic flows, flow-routing for lahars down drainages, "
  "dispersion models for ashfall under prevailing winds. Each hazard "
  "gets its zone; overlapping zones make the composite map. "
  "Probabilistic assessments attach annual exceedance probabilities "
  "using eruption recurrence statistics. Risk then folds in exposure "
  "(census, infrastructure) and vulnerability (building types, warning "
  "time): risk = hazard x exposure x vulnerability. Maps are living "
  "documents, revised as the volcano's behavior and the exposed "
  "population change."),
 "key_points": [
  "Hazard maps zone by phenomenon: flows, lahars, ashfall, lava, ballistics.",
  "Built from deposit history plus physics-based runout and dispersion models.",
  "Risk = hazard x exposure x vulnerability - people and buildings included.",
  "Drive land-use planning and evacuation routing (Rainier, Vesuvius, Merapi).",
  "Understated worst cases kill - Armero 1985 is the cautionary tale."],
 "requirements": [
  "Complete eruptive history with mapped deposits for each hazard type.",
  "Calibrated runout, flow-routing, and dispersion models.",
  "Current exposure data (population, infrastructure, building stock)."],
 "standards": [
  "Maps state the reference scenario or probability basis explicitly.",
  "Zones follow modeled processes, not fixed-radius buffers."],
 "citations": [CIT_TILLING, CIT_USGS],
 "sig_lens": (
  "Signature edition: hazard mapping reframed as his original risk-"
  "zoning atlas - Signature exposure ledgers, every zone a priced "
  "entry in his protection accounting."),
 "demo_kind": "hazard_probability",
},
{
 "key": "pdc-modeling",
 "name": "Pyroclastic Density Current Modeling",
 "group": "Advanced",
 "ladder_rank": 9,
 "ladder_tier": "advanced",
 "description": (
  "Modeling pyroclastic density currents means solving how a hot, "
  "particle-laden gravity current moves over real terrain. The workhorse "
  "is the energy-cone (energy line) model: the flow is assumed to lose "
  "energy with distance at a fixed slope (the Heim coefficient, about "
  "0.2), so runout follows from collapse height - simple, fast, and "
  "surprisingly effective for hazard zoning. Depth-averaged numerical "
  "models (like VolcFlow and PDAC) solve mass and momentum over digital "
  "terrain, capturing channelization and overtopping. Full multiphase "
  "simulations resolve the dense base and dilute cloud separately but "
  "demand supercomputers. All models are calibrated against deposits: "
  "if it cannot reproduce the mapped ignimbrite, it is not trusted."),
 "how_it_works": (
  "The energy cone draws a cone from the collapse point with slope tan "
  "phi (phi ~ 11 degrees, Heim coefficient 0.2); terrain poking above "
  "the cone is safe, terrain below is inundated - a geometric proxy for "
  "energy loss to friction. Numerical models go further: they integrate "
  "the shallow-water-like equations for a granular-fluid mixture over a "
  "digital elevation model, with basal friction laws tuned to "
  "laboratory and field data. Model inputs are collapse height or "
  "mass flux, grain size, and temperature; outputs are inundation "
  "footprint, dynamic pressure, and arrival time. Uncertainty is "
  "handled with ensembles - hundreds of runs over parameter ranges - "
  "to give probabilistic footprints."),
 "key_points": [
  "Energy-cone model: runout from collapse height at ~0.2 energy slope - the zoning workhorse.",
  "Depth-averaged models solve flow over real terrain (channelization, overtopping).",
  "Multiphase models separate dense base from dilute cloud at supercomputer cost.",
  "Calibration is against mapped deposits - no deposit match, no trust.",
  "Ensembles over parameter ranges give probabilistic footprints."],
 "requirements": [
  "Digital elevation model of the edifice and surroundings.",
  "Calibrated friction parameters from analogue eruptions.",
  "Deposit maps of past flows for validation."],
 "standards": [
  "Model choice is justified against the question (zoning vs. research).",
  "Probabilistic outputs state the ensemble size and parameter ranges."],
 "citations": [CIT_FISHER, CIT_SPARKS],
 "sig_lens": (
  "Signature edition: PDC modeling reframed as his original hot-"
  "avalanche solver - Signature energy accounting, every runout a "
  "balanced equation in his flow ledger."),
 "demo_kind": "energy_cone",
},
{
 "key": "volcano-tsunamis",
 "name": "Volcano-Generated Tsunamis",
 "group": "Advanced",
 "ladder_rank": 9,
 "ladder_tier": "advanced",
 "description": (
  "Volcanoes make tsunamis three ways: flank collapse (a mountainside "
  "sliding into the sea), underwater explosions, and caldera-collapse "
  "displacement. The 1883 Krakatau eruption generated waves that killed "
  "about 36,000 people on the coasts of Java and Sumatra; the 2018 "
  "Anak Krakatau flank collapse - just 0.3 cubic kilometers of rock - "
  "made a tsunami that killed over 430. Sector collapses are the big "
  "fear: Hawaii's ancient collapses moved thousands of cubic kilometers, "
  "and Cumbre Vieja in the Canaries is debated as a future source. "
  "Unlike earthquake tsunamis, volcanic ones give little seismic "
  "warning and arrive within minutes - monitoring the unstable flank "
  "is the only defense."),
 "how_it_works": (
  "A flank collapse dumps rock into the sea in minutes; the displaced "
  "water radiates as waves whose initial height scales with slide "
  "volume and speed - even sub-cubic-kilometer collapses make "
  "tens-of-meters waves locally. Explosive eruptions couple "
  "atmospheric pressure waves and direct water displacement into "
  "tsunamis, as at Krakatau 1883 and Hunga Tonga 2022. Caldera "
  "collapse displaces the water column above the foundering block. "
  "The waves then propagate like any tsunami, shoaling and "
  "amplifying at distant shores. Warning relies on detecting the "
  "collapse itself - seismic signals of the landslide, or better, "
  "deformation showing the flank accelerating before it fails."),
 "key_points": [
  "Three mechanisms: flank collapse, underwater explosion, caldera displacement.",
  "Krakatau 1883: ~36,000 tsunami deaths; Anak Krakatau 2018: 0.3 km^3 collapse, 430+ dead.",
  "Even small collapses make tens-of-meters waves locally.",
  "Little seismic warning; arrival in minutes - flank monitoring is the defense.",
  "Hunga Tonga 2022 showed explosive coupling can reach across ocean basins."],
 "requirements": [
  "Flank-stability assessment (deformation, seismicity, bathymetry).",
  "Slide-volume and runout estimates for wave-generation modeling.",
  "Tsunami propagation modeling for exposed coastlines."],
 "standards": [
  "Wave-height estimates state the slide volume and model used.",
  "Warning plans account for the minutes-scale arrival times."],
 "citations": [CIT_KRAKATAU, CIT_TILLING],
 "sig_lens": (
  "Signature edition: volcano tsunamis reframed as his original "
  "flank-failure wave ledger - Signature collapse accounting, every "
  "cubic kilometer of slide a wave-height entry."),
 "demo_kind": "tsunami_wave",
},
{
 "key": "geothermal-energy",
 "name": "Geothermal Energy from Volcanic Systems",
 "group": "Advanced",
 "ladder_rank": 9,
 "ladder_tier": "advanced",
 "description": (
  "Volcanic heat is a power source: where magma sits shallow, "
  "groundwater becomes steam that can drive turbines. Iceland gets "
  "about a quarter to a third of its electricity from geothermal, "
  "drilling into volcanic rift zones; The Geysers in California is "
  "the world's largest geothermal field; Kenya's Olkaria field taps "
  "the East African Rift. High-temperature fields (>200 C) generate "
  "electricity at 10-20 percent thermal efficiency; lower-temperature "
  "resources heat buildings and greenhouses directly. Exploration is "
  "volcanology applied: mapping heat flow, resistivity (clay caps "
  "over reservoirs), and microseismicity to find the steam before "
  "drilling the million-dollar well."),
 "how_it_works": (
  "Rainwater percolates down, is heated by the magmatic system, and "
  "rises as steam through fractured rock; an impermeable clay cap "
  "traps it in a reservoir. Production wells tap the steam, "
  "separators split steam from brine, turbines convert it to "
  "electricity, and injection wells return the cooled fluid to "
  "sustain pressure - the reservoir is managed, not mined. "
  "Exploration uses magnetotellurics to image the conductive clay "
  "cap, gravity and seismic surveys for structure, and geothermometers "
  "from hot-spring chemistry to estimate reservoir temperature before "
  "a drill bit turns. Enhanced geothermal systems (EGS) engineer "
  "reservoirs in hot dry rock by fracturing it - volcanology's heat "
  "without the volcano's plumbing."),
 "key_points": [
  "Volcanic heat drives steam turbines: Iceland (~25-30% of electricity), The Geysers, Olkaria.",
  "High-temp fields make electricity (10-20% efficiency); low-temp heats directly.",
  "Exploration: heat flow, resistivity clay-cap mapping, microseismicity, geothermometers.",
  "Reservoirs are managed with reinjection, not mined.",
  "EGS engineers reservoirs in hot dry rock - heat without natural plumbing."],
 "requirements": [
  "Heat-flow and hot-spring geochemistry surveys to prove the resource.",
  "Magnetotelluric/resistivity imaging of the clay cap and reservoir.",
  "Production and injection well design with reservoir modeling."],
 "standards": [
  "Resource estimates follow standard geothermal classification (measured/indicated/inferred).",
  "Induced-seismicity monitoring is required for EGS operations."],
 "citations": [CIT_FRANCIS, CIT_STD],
 "sig_lens": (
  "Signature edition: geothermal energy reframed as his original "
  "planetary power tap - Signature heat harvesting, every megawatt a "
  "metered draw from his volcanic furnace."),
 "demo_kind": "geothermal_power",
},
{
 "key": "magma-mixing",
 "name": "Magma Mixing and Assimilation",
 "group": "Advanced",
 "ladder_rank": 9,
 "ladder_tier": "advanced",
 "description": (
  "Magmas rarely evolve alone: hot mafic recharge mixes with cooler "
  "silicic residents, and magmas melt and absorb wall rock "
  "(assimilation). Mixing shows up as banded pumice - streaks of dark "
  "basalt in pale rhyolite - as enclaves of quenched mafic blobs, and "
  "as linear element trends between end members on variation diagrams. "
  "Assimilation leaves an isotopic fingerprint: crustal strontium and "
  "oxygen ratios contaminating the mantle signature. Both processes "
  "can trigger eruptions - mixing injects heat and volatiles, "
  "assimilation adds fusible, gas-rich material - and both complicate "
  "the simple fractionation story, which is why real volcanoes need "
  "the full AFC (assimilation-fractional-crystallization) treatment."),
 "how_it_works": (
  "When magmas of contrasting temperature and viscosity meet, they "
  "mingle first (streaks, enclaves) and mix toward homogeneity only "
  "with vigorous convection - viscosity contrast is the barrier, which "
  "is why quenched mafic enclaves freeze before dissolving. On an "
  "element-element plot, binary mixing draws a straight line between "
  "end members: the mixture composition is the weighted average, and "
  "the lever rule reads the proportions. Assimilation is thermal work: "
  "the magma must supply the latent heat to melt wall rock, so it "
  "proceeds together with crystallization (AFC), and the ratio r of "
  "assimilated to crystallized mass sets the isotopic shift. Together "
  "they explain the 'messy' chemistry of real arc volcanoes."),
 "key_points": [
  "Mixing: mafic recharge + silicic resident - banded pumice, enclaves, linear trends.",
  "Assimilation: wall-rock melting leaves isotopic (Sr, O) fingerprints.",
  "Binary mixing follows the lever rule on element plots.",
  "Both can trigger eruptions via heat, volatiles, and fusible material.",
  "Real systems need AFC - fractionation alone is too clean."],
 "requirements": [
  "End-member compositions from enclaves, bands, or inferred parents.",
  "Isotopic analyses (Sr, Nd, O) to detect crustal assimilation.",
  "Thermal modeling to check the AFC energy budget."],
 "standards": [
  "Mixing proportions state the end members and the elements used.",
  "AFC models report the r value and assimilant composition."],
 "citations": [CIT_SCHMINCKE, CIT_SIGURDSSON],
 "sig_lens": (
  "Signature edition: mixing and assimilation reframed as his original "
  "magma blending ledger - Signature batch mixing, every enclave a "
  "measured ingredient in his recipe."),
 "demo_kind": "mixing_line",
},
{
 "key": "vesuvius-79ad",
 "name": "Vesuvius 79 AD: The Pompeii Eruption",
 "group": "Advanced",
 "ladder_rank": 10,
 "ladder_tier": "advanced",
 "description": (
  "The 79 AD eruption of Vesuvius is history's most documented ancient "
  "eruption, thanks to Pliny the Younger's letters describing the "
  "'pine-tree' cloud - the original Plinian column. After a day of "
  "ashfall that buried Pompeii under meters of pumice, pyroclastic "
  "surges swept through the city, killing those who had stayed - the "
  "famous plaster casts preserve their final moments. Herculaneum, "
  "closer to the vent, was buried under 20 meters of flow deposits. "
  "Modern work puts the eruption at VEI 5, about 3-4 cubic kilometers "
  "of magma, with column heights near 30 kilometers. Vesuvius remains "
  "one of the world's most dangerous volcanoes: three million people "
  "live in its hazard zones today."),
 "how_it_works": (
  "The eruption began with a sustained Plinian column that rained "
  "pumice lapilli on Pompeii for about 18 hours - roofs collapsed "
  "under the load, but most residents escaped. Then the column "
  "faltered and collapsed, sending pyroclastic surges across the "
  "city; the surges' heat (hundreds of degrees) killed within "
  "minutes, and fine ash preserved bodies, buildings, food, and "
  "frescoes in extraordinary detail. Deposit stratigraphy reads the "
  "sequence: white then gray pumice fall (two magma batches), capped "
  "by surge and flow units. Isopach maps of the fall deposit give "
  "the volume; the surge deposits' extent gives the collapse "
  "dynamics. Vesuvius has erupted since - notably 1631 and 1944 - "
  "and its current quiet is the dormancy between chapters."),
 "key_points": [
  "Pliny the Younger's letters are the original Plinian eruption account.",
  "Sequence: ~18 hours of pumice fall, then column collapse and lethal surges.",
  "VEI 5, ~3-4 km^3, column ~30 km; casts preserve the surge victims.",
  "Deposit stratigraphy (white/gray pumice, surge units) reads the eruption sequence.",
  "Three million people live in Vesuvius's hazard zones today."],
 "requirements": [
  "Deposit stratigraphy correlating fall and surge units across the Bay of Naples.",
  "Pliny's letters cross-checked against the physical stratigraphy.",
  "Current monitoring data and evacuation planning for the modern hazard."],
 "standards": [
  "Volume estimates integrate isopach maps with stated DRE conversion.",
  "Historical accounts are treated as hypotheses tested against deposits."],
 "citations": [CIT_PLINY, CIT_SIGURDSSON],
 "sig_lens": (
  "Signature edition: Vesuvius 79 AD reframed as his original "
  "Plinian case file - Signature eruption number one, every pumice "
  "layer a dated exhibit in his ancient-eruption archive."),
 "demo_kind": "plinian_dispersal",
},
{
 "key": "tambora-krakatau",
 "name": "Tambora 1815 and Krakatau 1883",
 "group": "Advanced",
 "ladder_rank": 10,
 "ladder_tier": "advanced",
 "description": (
  "Tambora 1815 (VEI 7, ~150 km^3) is the largest eruption in recorded "
  "history: it removed the volcano's summit, killed about 90,000 people "
  "through eruption and famine, and injected so much sulfur that 1816 "
  "became the 'Year Without a Summer' - snow in July in New England, "
  "failed harvests across Europe. Krakatau 1883 (VEI 6, ~20 km^3) is "
  "the most famous: its explosions were heard 3,000 miles away, its "
  "tsunamis killed about 36,000, and its sunsets - painted by artists "
  "worldwide - came from stratospheric aerosols. Together they are the "
  "twin case studies in eruption-climate coupling and far-field "
  "tsunami hazard."),
 "how_it_works": (
  "Tambora's eruption column reached the stratosphere and its "
  "pyroclastic flows swept the Sanggar Peninsula; the caldera that "
  "remains is 6 kilometers across and over a kilometer deep. The "
  "climate response followed the aerosol physics: tropical SO2 spread "
  "to both hemispheres, global temperatures fell roughly half a degree "
  "or more, and the following year's weather lurched - the cold, wet "
  "summer of 1816 is recorded in diaries, grain prices, and tree "
  "rings. Krakatau's tsunamis came from caldera collapse displacing "
  "the sea and from the explosive blasts themselves; tide gauges "
  "worldwide recorded the waves, and the atmospheric pressure wave "
  "circled the planet. Both eruptions are dated and quantified from "
  "deposits plus the global instrumental and documentary record."),
 "key_points": [
  "Tambora 1815: VEI 7, ~150 km^3, ~90,000 dead, 'Year Without a Summer' 1816.",
  "Krakatau 1883: VEI 6, ~20 km^3, heard 3,000 miles away, ~36,000 tsunami deaths.",
  "Twin case studies in eruption-climate coupling and far-field tsunami hazard.",
  "Tambora's caldera: 6 km across, >1 km deep - the collapse signature.",
  "Both quantified from deposits plus global documentary and instrumental records."],
 "requirements": [
  "Deposit volumes (ignimbrite + fall) for both eruptions.",
  "Documentary and instrumental records (tide gauges, barographs, diaries).",
  "Ice-core sulfate and tree-ring records for the climate response."],
 "standards": [
  "Death tolls cite the historical-demographic source and its uncertainty.",
  "Climate anomalies are referenced to pre-eruption baselines."],
 "citations": [CIT_TAMBORA, CIT_KRAKATAU],
 "sig_lens": (
  "Signature edition: Tambora and Krakatau reframed as his original "
  "twin cataclysm files - Signature VEI 7 and 6 benchmarks, every "
  "famine and sunset logged in his global-impact ledger."),
 "demo_kind": "climate_impact",
},
{
 "key": "st-helens-pinatubo",
 "name": "Mount St. Helens 1980 and Pinatubo 1991",
 "group": "Advanced",
 "ladder_rank": 10,
 "ladder_tier": "advanced",
 "description": (
  "Mount St. Helens 1980 and Pinatubo 1991 are the two eruptions that "
  "taught modern volcanology its trade. St. Helens (VEI 5) began with "
  "two months of swelling - a cryptodome bulging the north flank 5 "
  "feet per day - until a magnitude 5.1 earthquake uncorked it: the "
  "flank slid away in the largest landslide in recorded history and "
  "the lateral blast flattened 600 square kilometers of forest, "
  "killing 57. Pinatubo (VEI 6, ~10 km^3) was the forecasting "
  "triumph: weeks of escalating seismicity, deformation, and SO2 drove "
  "the evacuation of tens of thousands, and the June 15 climax - the "
  "second-largest eruption of the 20th century - injected ~20 megatons "
  "of SO2 and cooled the planet ~0.5 C. One taught blast mechanics; "
  "the other taught that monitoring plus evacuation saves lives."),
 "how_it_works": (
  "At St. Helens, magma intruded as a cryptodome, destabilizing the "
  "flank; the earthquake-triggered landslide depressurized the "
  "shallow hydrothermal-magmatic system in seconds, and the lateral "
  "blast - a directed explosion, not a vertical column - expanded at "
  "hundreds of km/h, with a Plinian column following for nine hours. "
  "The deposit sequence (blast, then fall, then flows) is the textbook "
  "for directed blasts. At Pinatubo, the forecast worked because the "
  "signals were textbook and the scientists acted: escalating VT "
  "swarms, harmonic tremor, dome growth, and soaring SO2 flux, "
  "communicated through alert levels to civil authorities running "
  "evacuations. The eruption's energy (~10 km^3 DRE) and sulfur load "
  "were quantified from deposits plus satellite SO2 - closing the "
  "loop from monitoring to climate impact."),
 "key_points": [
  "St. Helens 1980: flank bulge, landslide, directed blast - 600 km^2 flattened, 57 dead.",
  "Pinatubo 1991: VEI 6, ~10 km^3, ~20 Mt SO2, ~0.5 C global cooling.",
  "Pinatubo is the forecasting triumph - monitoring plus evacuation saved tens of thousands.",
  "St. Helens taught directed-blast mechanics; its deposits are the textbook.",
  "Both closed the loop from monitoring signals to deposits to climate."],
 "requirements": [
  "Pre-eruption monitoring records (seismic, deformation, gas) for both events.",
  "Deposit mapping: blast zone, fall isopachs, flow units.",
  "Evacuation and decision timelines for the Pinatubo case study."],
 "standards": [
  "Blast-zone mapping distinguishes directed-blast from fall and flow deposits.",
  "Forecasting case studies document the decision chain, not just the science."],
 "citations": [CIT_LIPMAN, CIT_PINATUBO],
 "sig_lens": (
  "Signature edition: St. Helens and Pinatubo reframed as his original "
  "modern-eruption masterclasses - Signature blast mechanics and "
  "Signature forecasting triumph, both fully worked in his ledger."),
 "demo_kind": "blast_energy",
},
{
 "key": "frontiers-volcanology",
 "name": "Frontiers of Volcanology",
 "group": "Advanced",
 "ladder_rank": 10,
 "ladder_tier": "advanced",
 "description": (
  "Volcanology's frontiers are about seeing more and forecasting "
  "better. Distributed fiber-optic sensing turns telecom cables into "
  "thousands of seismometers, imaging magma movement at unprecedented "
  "resolution. Machine learning sifts decades of monitoring data for "
  "precursor patterns humans miss, feeding Bayesian eruption-"
  "probability updates in near real time. Satellite constellations now "
  "watch every volcano on Earth for thermal and deformation anomalies, "
  "including the unmonitored ones. Submarine volcanology - two-thirds "
  "of Earth's volcanism happens underwater - is opening up with "
  "autonomous vehicles mapping the mid-ocean ridges. And the "
  "Hunga Tonga 2022 eruption showed the field its blind spots: "
  "shallow submarine calderas can couple the ocean and atmosphere in "
  "ways the models missed."),
 "how_it_works": (
  "The frontier method is data fusion: seismic, geodetic, gas, thermal, "
  "and satellite streams feed probabilistic models that update "
  "eruption odds as each new datum arrives - Bayes' rule as an "
  "operational tool, with the prior set by the volcano's history and "
  "the likelihood by the precursor statistics. Fiber-optic DAS gives "
  "meter-scale strain sampling along kilometers of cable, resolving "
  "dike propagation in detail impossible with sparse stations. "
  "Autonomous underwater vehicles and seafloor observatories extend "
  "the network to the ridges. The research loop is the same as ever: "
  "new sensors reveal new signals, new signals demand new physics, new "
  "physics improves the forecast."),
 "key_points": [
  "Fiber-optic sensing turns cables into thousands of seismometers.",
  "Machine learning + Bayesian updating move forecasting toward real-time probabilities.",
  "Satellite constellations watch every volcano, including unmonitored ones.",
  "Submarine volcanology (two-thirds of Earth's volcanism) is opening via autonomous vehicles.",
  "Hunga Tonga 2022 exposed blind spots in shallow submarine caldera models."],
 "requirements": [
  "Access to multi-parameter monitoring data streams for model training.",
  "Bayesian/event-tree frameworks to make probabilities operational.",
  "Sustained observatory funding - frontiers need continuous data, not campaigns."],
 "standards": [
  "ML precursor claims are validated out-of-sample, never on training data.",
  "Probabilistic forecasts state priors, likelihoods, and update cadence."],
 "citations": [CIT_SIGURDSSON, CIT_USGS],
 "sig_lens": (
  "Signature edition: the frontiers reframed as his original next-"
  "generation watchtower - Signature sensing and Signature forecasting, "
  "every new instrument a sharper eye in his planetary monitoring."),
 "demo_kind": "forecast_bayes",
},
]

SIG_TAIL = ("Signature editions are his original Signature interpretation "
            "of volcanology: clearly labeled Signature-made, never "
            "presented as authentic public record.")

assert len(ENTRIES) == 36, "need 36 volcanology entries, have %d" % len(ENTRIES)
ranks = [e["ladder_rank"] for e in ENTRIES]
assert ranks == sorted(ranks), "entries must be in ladder order"
tiers = [e["ladder_tier"] for e in ENTRIES]
assert tiers == sorted(tiers, key=lambda t: {"foundations": 0, "compounded": 1, "advanced": 2}[t]), "tiers must be ladder-ordered"
for e in ENTRIES:
    for k in ("key", "name", "group", "ladder_rank", "ladder_tier", "description",
              "how_it_works", "key_points", "requirements", "standards",
              "citations", "sig_lens", "demo_kind"):
        assert k in e, "missing %s in %s" % (k, e.get("key"))
    assert len(e["description"]) > 200, "stub description in %s" % e["key"]
