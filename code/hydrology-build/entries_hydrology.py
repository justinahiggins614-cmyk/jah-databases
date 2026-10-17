#!/usr/bin/env python3
"""Seed entries for the Hydrology field build (field #14, taxonomy order).

Verified 2026-10-17: NO database covers hydrology as a discipline.
- 'water-systems' (10,001 records): water cycles, treatment, infrastructure,
  conservation - utility engineering, not the science of water.
- 'oceanography' (10,000 records): ocean processes.
- 'rivers' (56 records): short river entries.
- 'climatology' (34 records, field #12): covers the water cycle at the
  climate scale ('The Water Cycle' record exists there) - not discipline
  machinery.
- 'atmospheric-science' (36 records, field #13): precipitation physics,
  cloud processes - not surface/groundwater hydrology.
- occupation DBs ('hydrologists', 'hydrologic-technicians',
  'water-resource-specialists', 'water-wastewater-engineers'): 4-5-record
  occupation cards.

So this build creates two NEW databases:

  hydrology             - The Hydrology Database
                          (public-harvest: real, fact-checked hydrology)
  hydrology-signature   - The Hydrology Signature Database
                          (his original Signature interpretation;
                          src signature, titles suffixed
                          " (Signature Edition)", never presented
                          as authentic public record)

36 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

CIT_DINGMAN = ("Dingman, S. L. (2015). 'Physical Hydrology', 3rd ed. "
               "Waveland Press.")
CIT_CHOW = ("Chow, V. T., Maidment, D. R. & Mays, L. W. (1988). "
            "'Applied Hydrology'. McGraw-Hill.")
CIT_FREEZE = ("Freeze, R. A. & Cherry, J. A. (1979). 'Groundwater'. "
              "Prentice-Hall.")
CIT_BRUTSAERT = ("Brutsaert, W. (2005). 'Hydrology: An Introduction'. "
                 "Cambridge University Press.")
CIT_FETTER = ("Fetter, C. W. (2001). 'Applied Hydrogeology', 4th ed. "
              "Prentice Hall.")
CIT_MAIDMENT = ("Maidment, D. R. (ed.) (1993). 'Handbook of Hydrology'. "
                "McGraw-Hill.")
CIT_DUNNE = ("Dunne, T. & Leopold, L. B. (1978). 'Water in Environmental "
             "Planning'. W. H. Freeman.")
CIT_HENDERSON = ("Henderson, F. M. (1966). 'Open Channel Flow'. Macmillan.")
CIT_WARD = ("Ward, A. D. & Trimble, S. W. (2004). 'Environmental Hydrology', "
            "2nd ed. CRC Press.")
CIT_MAYS = ("Mays, L. W. (2010). 'Water Resources Engineering', 2nd ed. "
            "Wiley.")
CIT_GRAY = ("Gray, D. M. & Male, D. H. (eds.) (1981). 'Handbook of Snow: "
            "Principles, Processes, Management and Use'. Pergamon Press.")
CIT_SINGH = ("Singh, V. P. (1992). 'Elementary Hydrology'. Prentice Hall.")

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "hydrology, clearly labeled Signature-made, never presented as "
            "authentic public record.")

ENTRIES = [
    # ================= FOUNDATIONS =================
    {
        "key": "what_is_hydrology",
        "name": "What Hydrology Is",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Hydrology is the science of water's occurrence, movement, and "
            "distribution on and beneath the Earth's surface - where water "
            "goes, how fast it gets there, and how much is available. "
            "Meteorology studies the weather overhead and climatology studies "
            "the long-term statistics of the climate system, but hydrology "
            "starts where rain hits the ground: how much soaks in, how much "
            "runs off, how streams rise and fall, how groundwater moves "
            "through rock, how snowpacks store winter for summer, and how "
            "reservoirs are managed through drought. The discipline splits "
            "into branches. Surface-water hydrology studies rivers, lakes, "
            "and floods. Groundwater hydrology (hydrogeology) studies "
            "aquifers, wells, and springs. Snow and ice hydrology studies "
            "snowpacks and glaciers. Urban hydrology studies how pavement "
            "and pipes rewrite the water budget. Ecohydrology studies how "
            "water shapes living systems and vice versa. Water-resources "
            "hydrology turns all of it into decisions: how much a reservoir "
            "can safely promise, how big a culvert must be, how far a well "
            "field can be pumped."
        ),
        "how_it_works": (
            "Hydrology works as bookkeeping plus physics. The bookkeeping "
            "is the water budget: precipitation in, evapotranspiration and "
            "streamflow out, storage change making up the difference, "
            "measured for a watershed, an aquifer, or the planet. The "
            "physics is conservation of mass and momentum applied to water "
            "in motion: Darcy's law for groundwater creeping through pores, "
            "the Saint-Venant equations for flood waves racing down rivers, "
            "energy balances for snowmelt, the Penman-Monteith equation for "
            "evapotranspiration. Hydrologists instrument watersheds with "
            "rain gauges, stream gauges, wells, and snow pillows, then "
            "calibrate models so the simulated river matches the measured "
            "river. Prediction is the product: flood forecasts, drought "
            "outlooks, reservoir rule curves, and the 100-year flood maps "
            "that decide where a town may build."
        ),
        "key_points": [
            "Hydrology is the science of water on and beneath the land surface: occurrence, movement, distribution, and availability.",
            "It starts where rain hits the ground - infiltration, runoff, streamflow, groundwater, snowpack, reservoirs - while meteorology and climatology handle the atmosphere.",
            "Branches: surface water, groundwater (hydrogeology), snow and ice, urban, ecohydrology, and water-resources decision-making.",
            "The method is bookkeeping (the water budget) plus physics (conservation laws for water in motion), calibrated against instruments.",
            "The products are forecasts and decisions: flood warnings, drought outlooks, reservoir operations, floodplain maps.",
        ],
        "requirements": [
            "Comfort with the water budget equation as the universal hydrologic ledger.",
            "Basic algebra and unit discipline: millimeters, cubic meters per second, hectare-meters.",
            "A habit of asking 'where does the water go?' for every landscape feature you see.",
        ],
        "standards": [
            "SI units: precipitation and evapotranspiration in millimeters, discharge in cubic meters per second, storage in cubic meters.",
            "World Meteorological Organization standards govern hydrologic observation networks and data exchange.",
        ],
        "citations": [CIT_DINGMAN, CIT_CHOW],
        "sig_lens": (
            "Signature edition: water reframed as his great planetary "
            "circulatory system, every watershed a labeled Signature basin "
            "with its own pulse."
        ),
        "demo_kind": "hydro_branches",
    },
    {
        "key": "water_budget_equation",
        "name": "The Water Budget Equation",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The water budget equation is hydrology's universal ledger: "
            "what comes in must go out or be stored. For a watershed over "
            "any time period it reads P = ET + Q + change in S, where P is "
            "precipitation, ET is evapotranspiration, Q is streamflow out of "
            "the basin, and the change in S is the change in storage - soil "
            "moisture, groundwater, snowpack, lakes, reservoirs. Nothing "
            "about the equation is approximate; it is mass conservation, "
            "and every hydrologic model is at heart a machine for tracking "
            "these four terms through time. Over a long enough period the "
            "storage term averages to zero, so mean annual streamflow is "
            "simply precipitation minus evapotranspiration - the reason "
            "deserts have no rivers and wet mountains do. Applied at the "
            "global scale, the equation closes over the oceans and the "
            "continents together: about 505,000 cubic kilometers of water "
            "evaporate from the oceans each year, 458,000 fall back on them, "
            "and the 47,000-cubic-kilometer surplus rides the atmosphere "
            "onto land, where it becomes the world's river flow."
        ),
        "how_it_works": (
            "The equation works by choosing a control volume and an "
            "accounting period, then measuring or estimating every term. "
            "For a watershed, precipitation comes from a gauge network "
            "averaged by Thiessen polygons or isohyets. Streamflow comes "
            "from the outlet gauge. Evapotranspiration is rarely measured "
            "directly, so it is estimated from weather data with the "
            "Penman-Monteith equation, or solved as the residual when the "
            "other terms are known and storage is assumed steady. Storage "
            "change is tracked with soil-moisture sensors, observation "
            "wells, snow surveys, and reservoir levels. The budget is then "
            "checked for closure: if the terms do not balance, something "
            "is wrong - a missed groundwater inflow, an ungauged "
            "diversion, a bad gauge. Closure errors are not embarrassments; "
            "they are the diagnostic that finds hidden water."
        ),
        "key_points": [
            "P = ET + Q + change in S: precipitation equals evapotranspiration plus streamflow plus storage change. Pure mass conservation.",
            "Over long periods storage change averages to zero, so mean streamflow is precipitation minus evapotranspiration.",
            "Each term is measured for a chosen control volume and period: gauges, stream gauges, Penman-Monteith, wells, snow surveys, reservoir levels.",
            "Failure to close the budget diagnoses hidden water: groundwater inflows, ungauged diversions, bad gauges.",
            "Globally the budget moves ~47,000 cubic kilometers per year from ocean to land - the world's river supply.",
        ],
        "requirements": [
            "Algebraic comfort rearranging the four terms to solve for whichever is unknown.",
            "Consistent units: convert millimeters over an area to cubic meters before balancing.",
            "Skepticism: a budget that closes too perfectly usually has a hidden fudge.",
        ],
        "standards": [
            "Express basin budgets in millimeters of water over the basin area, alongside volumetric totals in cubic meters.",
            "Report the accounting period explicitly; a budget without its period is meaningless.",
        ],
        "citations": [CIT_DINGMAN, CIT_BRUTSAERT],
        "sig_lens": (
            "Signature edition: the planetary ledger rendered as his own "
            "Signature water accounts, every basin balanced like a vault."
        ),
        "demo_kind": "water_budget",
    },
    {
        "key": "watersheds_drainage_basins",
        "name": "Watersheds and Drainage Basins",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A watershed - also called a drainage basin or catchment - is "
            "the land area that drains to a single outlet point, bounded by "
            "the drainage divide: the topographic ridge from which water on "
            "one side flows to your river and water on the other side flows "
            "elsewhere. It is the fundamental accounting unit of hydrology, "
            "because the divide makes the basin a closed system for surface "
            "water: everything that runs off inside must exit through the "
            "outlet. Hydrologists describe basins with a handful of "
            "measures. Drainage area sets the scale of floods. Stream "
            "order (Strahler's system) numbers the network: headwater "
            "tributaries with no branches are order 1, two order-1 streams "
            "joining make order 2, and so on up to the great rivers at "
            "order 10 and above. Drainage density - total channel length "
            "divided by basin area - reveals the geology: high density in "
            "impermeable clays, low density in permeable sands. Basin shape, "
            "slope, and land cover then modulate how violently the basin "
            "responds to rain: steep, round, paved basins flash; flat, "
            "elongated, forested basins dawdle."
        ),
        "how_it_works": (
            "Watersheds are delineated from topography: trace the highest "
            "ground enclosing the outlet, following ridgelines and crossing "
            "contours at right angles, since water flows perpendicular to "
            "contour lines. Modern practice does this with digital elevation "
            "models: fill the spurious pits, compute flow direction for "
            "every cell, accumulate the upstream cells, and extract the "
            "network above a channel-initiation threshold. Stream order is "
            "assigned by Strahler's rule on the extracted network. Basin "
            "morphometry - area, perimeter, length, relief, mean slope, "
            "drainage density - is computed from the same grid. These "
            "numbers feed regional flood formulas and unit-hydrograph "
            "synthesis for ungauged basins: two basins with similar area, "
            "slope, and land cover respond to similar storms similarly. "
            "Groundwater divides need not match surface divides, which is "
            "why careful studies verify the budget closes before trusting "
            "the boundary."
        ),
        "key_points": [
            "A watershed is the land draining to one outlet, bounded by the drainage divide - hydrology's closed accounting system.",
            "Strahler stream order numbers the network: order-1 headwaters up through order-10+ great rivers.",
            "Drainage density (channel length per area) reveals geology: high in impermeable clay, low in permeable sand.",
            "Shape, slope, and land cover set flashiness: steep round paved basins flash; flat elongated forested basins dawdle.",
            "Digital elevation models delineate basins by flow accumulation; groundwater divides may not match surface divides.",
        ],
        "requirements": [
            "Ability to read a contour map: water flows perpendicular to contours, divides follow ridges.",
            "Basic GIS or map skills for delineation from elevation data.",
            "Careful unit conversion between square kilometers, hectares, and square miles.",
        ],
        "standards": [
            "Report basin area in square kilometers with the outlet point and delineation method stated.",
            "Use Strahler ordering when reporting stream order; state the ordering system explicitly.",
        ],
        "citations": [CIT_DINGMAN, CIT_DUNNE],
        "sig_lens": (
            "Signature edition: every basin drawn as a Signature catchment "
            "with its divide, order, and signature stamped at the outlet."
        ),
        "demo_kind": "watershed",
    },
    {
        "key": "measuring_precipitation",
        "name": "Measuring Precipitation",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Precipitation is hydrology's main input, and measuring it is "
            "surprisingly hard: rain varies more over a kilometer than most "
            "people imagine, and every gauge has a personality. The "
            "tipping-bucket gauge funnels rain into a tiny seesaw bucket "
            "that tips every 0.2 or 0.25 millimeters, logging the time of "
            "each tip - cheap and ubiquitous, but it undercatches in wind "
            "and struggles with intense downpours and snow. The weighing "
            "gauge sits on a scale and records the mass of everything that "
            "lands, liquid or frozen, with antifreeze and oil to keep it "
            "honest through winter. The disdrometer listens to or "
            "photographs falling drops to measure drop-size distributions, "
            "which is what radar reflectivity actually depends on. Because "
            "one gauge represents only its small patch, hydrologists average "
            "gauge networks over a basin with Thiessen polygons - each "
            "gauge weighted by the area closer to it than to any other - or "
            "draw isohyets, lines of equal rainfall, and average between "
            "them. Wind shields, siting rules, and dense networks all exist "
            "because the first question of every flood study is 'how much "
            "rain really fell?'"
        ),
        "how_it_works": (
            "A gauge network works by sampling a spatially variable field "
            "and interpolating it to the basin. Each gauge reports depth "
            "per time interval. Thiessen polygons partition the basin so "
            "every point is assigned to its nearest gauge; basin-average "
            "precipitation is the area-weighted sum. The isohyetal method "
            "draws contours of equal rainfall and weights each band by its "
            "area, which handles orographic patterns the polygons miss. "
            "Errors come from wind undercatch (gauge rims disturb the "
            "airflow, and snow blows clean past), splash, evaporation from "
            "the funnel, and tipping-bucket losses in heavy rain when water "
            "spills mid-tip. Corrections apply wind-speed factors and "
            "cross-check against radar and neighboring gauges. For flood "
            "modeling, the hyetograph - rainfall intensity versus time - "
            "matters as much as the total, because a basin responds to the "
            "tempo of the rain, not just its sum."
        ),
        "key_points": [
            "Rain gauges are point samplers of a highly variable field: tipping-bucket (cheap, poor in wind/snow), weighing (all-weather), disdrometer (drop sizes).",
            "Basin averages come from Thiessen polygons (area-weighted nearest gauge) or isohyetal contours.",
            "Wind undercatch is the dominant error - snow can blow past a gauge almost entirely; shields and corrections help.",
            "The hyetograph (intensity vs time) drives the flood response, not just the storm total.",
            "Radar and satellites extend gauges but never replace a well-sited ground network.",
        ],
        "requirements": [
            "Field discipline: level gauges, clear funnels, logged tip times, regular calibration.",
            "Area-weighting arithmetic: polygons or isohyetal bands times depths.",
            "Skepticism about single-gauge storm totals in convective weather.",
        ],
        "standards": [
            "Report precipitation in millimeters; intensity in millimeters per hour.",
            "Site gauges per WMO exposure rules: twice the obstacle height from obstructions, wind shields in snow country.",
        ],
        "citations": [CIT_CHOW, CIT_MAIDMENT],
        "sig_lens": (
            "Signature edition: his Signature rain ledger - every drop "
            "counted, weighed, and assigned to its basin."
        ),
        "demo_kind": "precip_gauge",
    },
    {
        "key": "infiltration_soil_water",
        "name": "Infiltration and Soil Water",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Infiltration is water soaking into the soil, and it decides the "
            "most basic question in hydrology: does this rain become "
            "groundwater and gentle streamflow, or does it become a flash "
            "flood? Dry soil drinks fast at first through capillary suction, "
            "then slows as the pores fill and gravity takes over - Horton's "
            "equation captures this decay from a high initial rate to a "
            "steady final rate. The Green-Ampt model pictures a sharp wetting "
            "front advancing downward like a piston, driven by ponded depth "
            "plus suction. Beneath the surface, soil water lives in three "
            "states: gravitational water drains away within a day or two, "
            "capillary water is held against gravity and is what plants "
            "actually use, and hygroscopic water clings so tightly to soil "
            "particles that only oven heat removes it. Field capacity is "
            "the water left after gravity drainage; the wilting point is "
            "where plants can no longer pull it out. The difference is the "
            "plant-available water - the soil's savings account, typically "
            "100 to 250 millimeters per meter of soil. When rainfall "
            "intensity exceeds the infiltration capacity, the excess ponds "
            "and runs off: this Hortonian overland flow is the classic "
            "mechanism of flash floods on dry, crusted, or paved ground."
        ),
        "how_it_works": (
            "Infiltration works through the physics of unsaturated flow: "
            "water moves down gradients of total head - elevation plus "
            "pressure - but in unsaturated soil the pressure is negative "
            "(suction), and the hydraulic conductivity collapses as pores "
            "empty, which is the content of Richards' equation. In practice, "
            "hydrologists measure infiltration capacity with ring "
            "infiltrometers or rainfall simulators, then fit Horton's "
            "decaying curve or Green-Ampt's piston-front parameters. Soil "
            "texture controls everything: sands infiltrate fast and hold "
            "little, clays infiltrate slowly and hold much, loams sit in "
            "the productive middle. Land use rewrites the rates - "
            "compaction, crusting, and pavement slash infiltration, while "
            "roots, worms, and mulch open macropores that bypass the matrix "
            "entirely. Flood models compare the storm hyetograph against "
            "the infiltration curve minute by minute; whatever the soil "
            "cannot take becomes runoff."
        ),
        "key_points": [
            "Infiltration decides the fate of rain: soak in (groundwater, gentle flow) or run off (flash flood).",
            "Horton's equation: infiltration capacity decays from a high initial rate to a steady final rate as soil wets.",
            "Soil water states: gravitational (drains), capillary (plant-available), hygroscopic (unavailable); field capacity minus wilting point is the savings account.",
            "Texture rules: sand fast/little storage, clay slow/much storage, loam in the productive middle.",
            "Rainfall intensity above infiltration capacity becomes Hortonian overland flow - the flash-flood mechanism.",
        ],
        "requirements": [
            "Soil texture by feel or lab: sand, silt, clay fractions set every parameter.",
            "Ring infiltrometer or rainfall-simulator measurements to fit Horton or Green-Ampt.",
            "Unit care: rates in mm/h, cumulative depth in mm, time in hours.",
        ],
        "standards": [
            "Report infiltration rates in millimeters per hour with the measurement method and antecedent moisture stated.",
            "Classify soils by USDA texture triangle when reporting infiltration parameters.",
        ],
        "citations": [CIT_DINGMAN, CIT_BRUTSAERT],
        "sig_lens": (
            "Signature edition: the soil as his Signature sponge - every "
            "pore a counted reservoir, every storm an audition."
        ),
        "demo_kind": "infiltration",
    },
    {
        "key": "evapotranspiration",
        "name": "Evapotranspiration: How Water Returns to the Sky",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Evapotranspiration - ET for short - is the combined return of "
            "water to the atmosphere: evaporation from soil and open water "
            "plus transpiration, the water plants pump from roots to leaves "
            "and exhale through stomata. Globally it is the giant term in "
            "the water budget, returning roughly two-thirds of land "
            "precipitation to the sky; a single large oak can transpire "
            "hundreds of liters on a hot day. Hydrologists distinguish "
            "potential ET, the atmosphere's demand under unlimited water, "
            "from actual ET, what really happens given the soil's supply - "
            "a desert has enormous potential ET and tiny actual ET. The "
            "workhorse estimator is the Penman-Monteith equation, which "
            "combines the energy available (net radiation) with the air's "
            "drying power (vapor-pressure deficit and wind) and the surface's "
            "resistance (stomata, canopy). Reference ET is computed for a "
            "standard clipped-grass surface, then scaled by crop "
            "coefficients for each crop and growth stage - the basis of "
            "irrigation scheduling worldwide. Lysimeters, giant soil tanks "
            "on scales, weigh the truth directly; eddy-covariance towers "
            "measure the turbulent vapor flux in the air above a canopy."
        ),
        "how_it_works": (
            "ET works as an energy and plumbing problem. Sunlight provides "
            "the latent heat - about 2.45 megajoules per kilogram of water "
            "evaporated - and the atmosphere provides the sink, carrying "
            "vapor away by turbulence. The Penman-Monteith equation balances "
            "these: net radiation minus ground heat flux supplies energy, "
            "the vapor-pressure deficit times an aerodynamic conductance "
            "drives the flux, and surface resistance (stomatal control) "
            "throttles it. Plants regulate transpiration by opening and "
            "closing stomata, trading water loss for carbon dioxide uptake "
            "- the central bargain of ecohydrology. In practice, weather "
            "stations feed temperature, humidity, wind, and solar radiation "
            "into the equation daily to produce reference ET; farmers "
            "multiply by crop coefficients and subtract effective rainfall "
            "to get the irrigation dose. Where water is limiting, actual ET "
            "is capped by soil moisture, and the deficit shows up as "
            "agricultural drought."
        ),
        "key_points": [
            "ET = evaporation + transpiration; globally it returns ~2/3 of land precipitation to the atmosphere.",
            "Potential ET is atmospheric demand; actual ET is what the soil's supply allows - the gap is drought.",
            "The Penman-Monteith equation combines net radiation, vapor-pressure deficit, wind, and surface resistance.",
            "Reference ET (standard grass) times crop coefficients schedules irrigation worldwide.",
            "Measured directly by lysimeters (weighing tanks) and eddy-covariance towers (turbulent flux).",
        ],
        "requirements": [
            "Daily weather data: temperature, humidity, wind speed, solar radiation.",
            "Latent heat of vaporization (2.45 MJ/kg) for energy-to-depth conversion.",
            "Crop coefficients matched to crop and growth stage for irrigation use.",
        ],
        "standards": [
            "Use the FAO-56 Penman-Monteith formulation for reference ET (mm/day) to keep studies comparable.",
            "Report whether ET is reference, crop, potential, or actual - they are different quantities.",
        ],
        "citations": [CIT_DINGMAN, CIT_MAIDMENT],
        "sig_lens": (
            "Signature edition: his Signature sky-pump - every leaf a "
            "metered valve returning the basin's water upward."
        ),
        "demo_kind": "evapotranspiration",
    },
    {
        "key": "measuring_streamflow",
        "name": "Measuring Streamflow",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Streamflow - discharge, Q - is the volume of water passing a "
            "cross-section per second, and measuring it is hydrology's "
            "central field craft. The definition is simple, Q equals area "
            "times velocity, but a river's velocity varies across every "
            "cross-section: fastest near the surface at mid-channel, near "
            "zero at the banks and bed. The classic method divides the "
            "cross-section into 20 to 30 vertical slices, measures depth "
            "and velocity in each with a current meter or an acoustic "
            "Doppler current profiler (ADCP), and sums the slice "
            "discharges - the mid-section method. Weirs and flumes force "
            "the flow through a known geometry so that a single water-level "
            "reading gives discharge from a calibrated formula; they are "
            "the standard for small streams and irrigation canals. Dilution "
            "gauging injects a salt or dye tracer upstream and measures its "
            "dilution downstream - the method of choice in turbulent "
            "mountain torrents where meters cannot survive. Continuous "
            "records come from stage sensors (pressure transducers, radar, "
            "bubblers) converted through the rating curve, telemetered in "
            "real time to flood forecasters."
        ),
        "how_it_works": (
            "A discharge measurement works by discretizing the "
            "cross-section. The hydrographer stretches a tagline across the "
            "river, sounds depths at stations, and measures velocity at "
            "0.6 of the depth (or the average of 0.2 and 0.8 depths in deep "
            "water) with a propeller or electromagnetic current meter, or "
            "runs an ADCP across on a boat or tether to profile the whole "
            "section acoustically in minutes. Each panel's discharge is "
            "its width times depth times mean velocity; the sum is Q, with "
            "an uncertainty of 5 to 10 percent for a careful measurement. "
            "Weirs work differently: the nappe over a sharp crest follows a "
            "theoretical head-discharge relation, so leveled weirs read "
            "discharge from head alone. Because rivers change - scour, "
            "fill, weed growth - measurements are repeated through the "
            "range of flows to build and maintain the rating curve, and "
            "every flood forecaster's model ultimately stands on these "
            "wading-boots measurements."
        ),
        "key_points": [
            "Discharge Q = area x velocity, measured by slicing the cross-section (mid-section method) and summing panel flows.",
            "Current meters, ADCPs (acoustic profilers), weirs/flumes (known geometry), and dilution gauging (tracers) are the four tool families.",
            "Velocity varies across every section: fastest at mid-channel near the surface, near zero at banks and bed.",
            "A careful measurement carries 5-10% uncertainty; rivers shift, so ratings need repeated check measurements.",
            "Continuous stage sensors plus the rating curve produce the real-time records flood forecasters use.",
        ],
        "requirements": [
            "Wading safety discipline: taglines, sounding weights, never wading above safe depth-velocity products.",
            "Cross-section arithmetic: widths, depths, and panel velocities summed without unit slips.",
            "Repeated measurements across the flow range to anchor the rating curve.",
        ],
        "standards": [
            "Report discharge in cubic meters per second with the method, date, and stage stated.",
            "Follow USGS or WMO current-meter protocols for station spacing (20-30 verticals) and velocity sampling.",
        ],
        "citations": [CIT_CHOW, CIT_DINGMAN],
        "sig_lens": (
            "Signature edition: his Signature river audit - every slice "
            "of the current measured, summed, and stamped."
        ),
        "demo_kind": "streamflow",
    },
    {
        "key": "rating_curve",
        "name": "The Rating Curve: Stage to Discharge",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A rating curve is the Rosetta Stone of every stream gauge: the "
            "relation that translates water level (stage), which is cheap "
            "and continuous to measure, into discharge, which is expensive "
            "and episodic. It is built empirically from dozens of discharge "
            "measurements plotted against their stages, then fitted - "
            "usually as a power law, Q equals a times (h minus h-zero) to "
            "the b, where h-zero is the stage of zero flow. Ratings shift: "
            "scour deepens the channel and lowers the curve, fill and weed "
            "growth raise it, ice jams and debris break it entirely, and "
            "backwater from a downstream tributary or reservoir flattens it. "
            "Flood waves add hysteresis - for the same stage, discharge is "
            "higher on the rising limb than the falling limb, because the "
            "water-surface slope is steeper while the wave approaches. The "
            "extrapolated top end of the curve, beyond the highest measured "
            "flow, is where flood estimates live and where the greatest "
            "uncertainty hides; extending it with hydraulic modeling or "
            "slope-area surveys is standard practice after major floods."
        ),
        "how_it_works": (
            "A rating works by pairing measurements. Each discharge "
            "measurement is plotted against the concurrent stage on "
            "log-log paper, where the power law becomes a straight line "
            "whose slope is the exponent b and intercept gives a. The "
            "zero-flow stage h-zero is found by trial or from channel "
            "surveys. Control sections - a rock riffle, a weir, a stable "
            "reach - anchor the curve; shifting sand reaches need "
            "segmented or time-varying ratings. In operation, the stage "
            "recorder logs level every 15 minutes, the rating converts "
            "each value to discharge, and the result is the continuous "
            "hydrograph. Quality control compares new measurements against "
            "the curve: consistent departures signal a shift and trigger "
            "a rating revision. During floods, when gauges are drowned or "
            "destroyed, hydrologists reconstruct peaks from high-water "
            "marks with slope-area computations to extend the rating where "
            "it matters most."
        ),
        "key_points": [
            "The rating curve converts cheap continuous stage into discharge: usually Q = a(h-h0)^b, fitted to field measurements.",
            "Ratings shift with scour, fill, weeds, ice, and debris - consistent departures from the curve trigger revisions.",
            "Backwater flattens ratings; flood-wave hysteresis makes rising-limb discharge higher than falling-limb at the same stage.",
            "The extrapolated high end carries the most uncertainty - exactly where flood estimates live.",
            "Post-flood slope-area surveys from high-water marks extend ratings beyond measured flows.",
        ],
        "requirements": [
            "A spread of discharge measurements across low, medium, and high flows.",
            "Log-log fitting skill and a surveyed zero-flow stage.",
            "Ongoing check measurements - a rating is a living document, not a monument.",
        ],
        "standards": [
            "Document the rating equation, its period of validity, and the highest measured discharge it rests on.",
            "Flag estimated or extrapolated portions of the record explicitly in published data.",
        ],
        "citations": [CIT_CHOW, CIT_MAIDMENT],
        "sig_lens": (
            "Signature edition: his Signature stage-to-flow cipher - one "
            "reading on the staff, the river's full discharge revealed."
        ),
        "demo_kind": "rating_curve",
    },
    # ================= COMPOUNDED =================
    {
        "key": "hydrograph",
        "name": "The Hydrograph: Reading a River's Pulse",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A hydrograph is the river's pulse trace: discharge plotted "
            "against time through a storm. It has anatomy worth learning. "
            "The rising limb climbs as runoff arrives, steep in flashy "
            "urban basins, gradual in forested ones. The peak (crest) is "
            "the maximum discharge - the number flood warnings are written "
            "in. The recession limb falls as the basin drains, first "
            "quickly as surface runoff ends, then slowly along the "
            "groundwater recession, which decays exponentially with a "
            "characteristic recession constant. Lag time - from the "
            "centroid of rainfall to the peak - measures the basin's "
            "sluggishness. Beneath every storm hydrograph runs baseflow, "
            "the groundwater-fed discharge that keeps rivers alive between "
            "storms; hydrograph separation peels the storm's direct runoff "
            "away from this baseflow so each can be studied. In snow country "
            "the annual hydrograph has two personalities: the spring "
            "snowmelt flood and the late-summer groundwater low. Reading "
            "hydrographs is how hydrologists diagnose basins: a double "
            "peak means two tributaries arriving out of sync; a fat "
            "recession means a big aquifer is feeding the river."
        ),
        "how_it_works": (
            "Hydrograph analysis works by decomposing the observed trace. "
            "Baseflow separation - by straight line, fixed base, or "
            "recursive digital filter - splits total flow into quick storm "
            "runoff and slow groundwater discharge. The direct-runoff "
            "volume divided by basin area gives the runoff depth, which "
            "compared against rainfall depth yields the runoff coefficient. "
            "The recession limb is fitted to an exponential to extract the "
            "recession constant, a basin signature that also estimates "
            "aquifer properties. Unit-hydrograph theory then treats the "
            "basin as a linear system: the direct-runoff hydrograph is the "
            "convolution of effective rainfall with the basin's unit "
            "response. In operations, forecasters compare the rising limb "
            "against forecast hydrographs from rainfall-runoff models, "
            "issuing warnings when the projected crest crosses flood stage "
            "with enough lead time to act."
        ),
        "key_points": [
            "Anatomy: rising limb, peak (crest), recession limb, lag time - each diagnoses the basin.",
            "Baseflow (groundwater-fed) underlies every storm hydrograph; separation isolates the storm's direct runoff.",
            "The recession limb decays exponentially; its constant fingerprints the feeding aquifer.",
            "Runoff depth over basin area vs rainfall depth gives the runoff coefficient.",
            "Double peaks, fat recessions, and flashy limbs each tell a story about tributaries, aquifers, and land cover.",
        ],
        "requirements": [
            "A continuous discharge record at 15-minute to hourly resolution through the event.",
            "Baseflow separation technique (straight-line, fixed-base, or digital filter) applied consistently.",
            "Rainfall hyetograph for the same storm to compute lag and runoff coefficients.",
        ],
        "standards": [
            "Report hydrograph timing in the gauge's local time zone with the datum stated.",
            "State the separation method; different methods give different direct-runoff volumes.",
        ],
        "citations": [CIT_CHOW, CIT_DINGMAN],
        "sig_lens": (
            "Signature edition: the river's cardiogram in his Signature "
            "clinic - every beat of rise and recession diagnosed."
        ),
        "demo_kind": "hydrograph",
    },
    {
        "key": "unit_hydrograph",
        "name": "Rainfall-Runoff and the Unit Hydrograph",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The unit hydrograph is one of hydrology's most elegant ideas, "
            "proposed by Sherman in 1932: the direct-runoff hydrograph that "
            "results from one unit (say 10 millimeters) of effective "
            "rainfall falling uniformly over the basin in a specified "
            "duration. Once you know a basin's unit hydrograph, you can "
            "predict its response to any storm by scaling and shifting: "
            "double the rain, double the ordinates; two bursts of rain, add "
            "the two shifted responses - the principles of proportionality "
            "and superposition, treating the basin as a linear system. "
            "Effective rainfall is the storm rainfall minus losses "
            "(infiltration, interception, depression storage), commonly "
            "estimated with the SCS curve-number method, which converts "
            "soil and land-cover into a single runoff potential number. The "
            "unit hydrograph itself can be derived from observed "
            "rainfall-runoff events, or synthesized for ungauged basins "
            "from basin characteristics - Snyder's method from lag and "
            "peaking coefficients, the SCS dimensionless hydrograph from "
            "time of concentration. Convolution - multiplying each burst of "
            "effective rain by the unit response and summing - is the "
            "arithmetic engine inside countless flood studies."
        ),
        "how_it_works": (
            "The method works in three steps. First, compute effective "
            "rainfall: subtract losses from the hyetograph, often with the "
            "SCS curve-number equation, which makes runoff a nonlinear "
            "function of rainfall and the curve number. Second, obtain the "
            "unit hydrograph: from a measured event by deconvolution, or "
            "synthetically from basin lag, area, and slope. Third, "
            "convolve: for each time step, multiply the effective rainfall "
            "depth by the unit hydrograph ordinates, shift by the step, and "
            "accumulate - then add baseflow back to get the total predicted "
            "hydrograph. The linear assumption breaks for extreme floods "
            "where the basin's response speeds up, which is why design "
            "floods get checked against nonlinear models and regional "
            "envelopes. For ungauged basins, regional regression equations "
            "predict the synthetic unit hydrograph's peak and timing from "
            "area, slope, and land cover."
        ),
        "key_points": [
            "The unit hydrograph: the basin's direct-runoff response to one unit of effective rainfall in a given duration (Sherman, 1932).",
            "Proportionality and superposition: scale ordinates with rain depth, add shifted responses for multi-burst storms.",
            "Effective rainfall = storm rain minus losses, often via the SCS curve-number method.",
            "Synthetic unit hydrographs (Snyder, SCS) bring the method to ungauged basins from area, slope, and lag.",
            "Convolution is the engine; linearity frays in extreme floods, so check against nonlinear models.",
        ],
        "requirements": [
            "Effective-rainfall hyetograph (losses removed) at the unit duration's time step.",
            "A unit hydrograph: derived from observations or synthesized from basin characteristics.",
            "Baseflow estimate to add back for the total hydrograph.",
        ],
        "standards": [
            "State the unit duration and depth explicitly (e.g., 1-hour, 10-mm unit hydrograph).",
            "Document the loss method (e.g., SCS curve number with its value and antecedent condition).",
        ],
        "citations": [CIT_CHOW, CIT_SINGH],
        "sig_lens": (
            "Signature edition: his Signature basin fingerprint - one "
            "unit of rain in, the river's whole signature out."
        ),
        "demo_kind": "unit_hydrograph",
    },
    {
        "key": "vadose_zone",
        "name": "Soil Moisture and the Vadose Zone",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The vadose zone - the unsaturated ground between the land "
            "surface and the water table - is where hydrology's hardest "
            "traffic flows: every drop of recharge must cross it, every "
            "plant drinks from it, and every contaminant spill filters "
            "(or fails to filter) through it. Water here is held by "
            "capillary suction, negative pressure that can reach many "
            "atmospheres in dry soil, and it moves down gradients of total "
            "head according to Richards' equation, the unsaturated twin of "
            "Darcy's law with a conductivity that collapses by orders of "
            "magnitude as the soil dries. The soil-moisture retention "
            "curve - water content versus suction, fitted by the van "
            "Genuchten equation - is the zone's master characteristic: it "
            "sets how much water a soil holds at each dryness and how fast "
            "water moves. Preferential flow through root channels, worm "
            "holes, and cracks can short-circuit the whole matrix, "
            "delivering storm water to depth in minutes. Hydrologists "
            "monitor the zone with tensiometers (suction), time-domain "
            "reflectometry probes (water content), and neutron probes, and "
            "the data feed irrigation scheduling, landslide warning, and "
            "groundwater recharge estimates."
        ),
        "how_it_works": (
            "Vadose-zone hydrology works by solving Richards' equation for "
            "water content and pressure head through the soil profile, with "
            "the retention curve and unsaturated conductivity functions "
            "closing the system. In practice, models like HYDRUS discretize "
            "the profile into layers, apply rainfall and ET at the surface "
            "boundary, and compute drainage to the water table at the "
            "bottom - the recharge flux. Field monitoring pairs "
            "tensiometers (measuring suction) with water-content sensors; "
            "together they trace the in-situ retention curve and reveal "
            "whether flow is uniform or preferential. For irrigation, the "
            "management-allowed depletion is the fraction of plant-available "
            "water a grower lets the crop use before watering again - "
            "typically half. For contaminant studies, the zone's travel "
            "time sets whether a spill reaches the aquifer in days or "
            "decades, and sorption and degradation in the biologically "
            "active root zone are the main attenuation mechanisms."
        ),
        "key_points": [
            "The vadose zone (surface to water table) is the gatekeeper: all recharge crosses it, all plants drink from it.",
            "Richards' equation governs unsaturated flow; conductivity collapses as soil dries, suction does the pulling.",
            "The van Genuchten retention curve (water content vs suction) is the master characteristic of any soil.",
            "Preferential flow through macropores can bypass the matrix and deliver storm water to depth in minutes.",
            "Monitored by tensiometers, TDR probes, and neutron probes; modeled by HYDRUS-type solvers.",
        ],
        "requirements": [
            "Soil hydraulic parameters: retention-curve and conductivity fits for each horizon.",
            "Surface boundary data: rainfall/irrigation in, ET out, at daily or finer steps.",
            "Field sensors to verify: modeled moisture profiles must meet measured ones.",
        ],
        "standards": [
            "Report water content volumetrically (cubic meters per cubic meter) and suction in kilopascals or cm of water.",
            "State the retention-curve model (e.g., van Genuchten) with fitted parameters when publishing.",
        ],
        "citations": [CIT_DINGMAN, CIT_BRUTSAERT],
        "sig_lens": (
            "Signature edition: his Signature root-zone ledger - every "
            "millimeter of the unsaturated vault accounted."
        ),
        "demo_kind": "vadose",
    },
    {
        "key": "darcy_law",
        "name": "Darcy's Law: Groundwater in Motion",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Darcy's law is the Ohm's law of groundwater: discharge through "
            "a porous medium is proportional to the hydraulic gradient and "
            "the cross-sectional area, Q equals minus K times A times dh "
            "over dl. Henry Darcy found it in 1856 watching water filter "
            "through sand columns for the fountains of Dijon, and it has "
            "governed hydrogeology ever since. K, the hydraulic "
            "conductivity, is the medium's permeability to water - gravels "
            "conduct meters per day, clays conduct millimeters per year, a "
            "range of ten orders of magnitude. The hydraulic gradient, dh "
            "over dl, is the slope of the water table or potentiometric "
            "surface, measured from wells. The minus sign says water flows "
            "downhill in head, from high to low. Divide discharge by area "
            "to get the Darcy flux, then divide by porosity to get the "
            "actual pore-water velocity - the speed a contaminant plume "
            "really travels, often meters per year, which is why "
            "groundwater pollution is a multi-generational problem. Darcy's "
            "law assumes laminar flow through a saturated, homogeneous "
            "medium; it breaks near wells at high pumping rates, in "
            "fractures and karst conduits where flow turns turbulent, and "
            "in clays where other forces intrude."
        ),
        "how_it_works": (
            "Darcy's law works as a field measurement program. Drill "
            "observation wells, measure water levels to map the "
            "potentiometric surface, compute the gradient between wells, "
            "estimate or measure hydraulic conductivity from pumping tests "
            "or slug tests, and multiply: Q equals K times A times gradient "
            "gives the groundwater discharge through any cross-section. "
            "Flow nets - hand-drawn or modeled grids of equipotentials and "
            "flow lines - visualize the pattern: flow lines cross "
            "equipotentials at right angles, and the discharge between any "
            "two adjacent flow lines is equal. For contaminant work, the "
            "pore velocity (Darcy flux divided by effective porosity) times "
            "time gives plume travel distance, and dispersion spreads the "
            "plume around that center of mass. Aquifer tests refine K at "
            "scale: pump a well at a constant rate, watch drawdown in "
            "observation wells, and fit the Theis curve."
        ),
        "key_points": [
            "Q = -K A (dh/dl): discharge proportional to conductivity, area, and head gradient (Darcy, 1856).",
            "Hydraulic conductivity spans ~10 orders of magnitude: gravels at m/day, clays at mm/year.",
            "Pore-water velocity = Darcy flux / porosity: the true speed of plumes, often meters per year.",
            "Flow nets visualize the pattern: flow lines perpendicular to equipotentials, equal discharge between lines.",
            "Assumes laminar saturated flow; breaks near high-rate wells, in fractures, karst, and clays.",
        ],
        "requirements": [
            "Water-level measurements from at least three non-collinear wells to define the gradient.",
            "Hydraulic conductivity from pumping tests, slug tests, or calibrated estimates.",
            "Effective porosity to convert Darcy flux to pore velocity for transport problems.",
        ],
        "standards": [
            "Report K in meters per day (or m/s) with the test method and scale stated.",
            "Reference water levels to a common datum; report the measurement date - heads change with seasons.",
        ],
        "citations": [CIT_FREEZE, CIT_FETTER],
        "sig_lens": (
            "Signature edition: his Signature seep-law - every pore's "
            "contribution tallied in the underground ledger."
        ),
        "demo_kind": "darcy",
    },
    {
        "key": "aquifers_wells",
        "name": "Aquifers, Wells, and the Water Table",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "An aquifer is a geologic formation that stores and transmits "
            "usable quantities of water - sands and gravels, sandstones, "
            "fractured limestones and basalts. The water table is the top "
            "of the saturated zone in an unconfined aquifer, where pore "
            "pressure equals atmospheric; above it lies the capillary "
            "fringe, below it every pore is full. A confined aquifer is "
            "sandwiched between impermeable layers, and its water is under "
            "pressure: the potentiometric surface - the level water would "
            "rise to in a well - can stand far above the aquifer top, "
            "producing flowing artesian wells where it exceeds the land "
            "surface. Wells are hydrology's windows and straws at once. "
            "Pumping a well creates a cone of depression, and the Theis "
            "(1935) solution describes how drawdown spreads with time: "
            "early on, water comes from storage near the well; later, the "
            "cone expands until it captures recharge or a boundary. "
            "Specific capacity - pumping rate divided by drawdown - is the "
            "well's report card. Aquifer storage is quantified by "
            "storativity (confined) or specific yield (unconfined, the "
            "drainable pore fraction, typically 0.1 to 0.3)."
        ),
        "how_it_works": (
            "Aquifer hydraulics works through pumping tests. Pump at a "
            "constant rate, record drawdown versus time in the pumped well "
            "and observation wells, and match the data to the Theis "
            "type curve - the well function W of u - to solve for "
            "transmissivity (K times aquifer thickness) and storativity. "
            "Boundaries reveal themselves as departures from the type "
            "curve: a recharge boundary flattens drawdown, an impermeable "
            "boundary steepens it. Well design then follows: screen placed "
            "across the productive zone, gravel pack sized to the "
            "formation, pump set below the lowest expected pumping level, "
            "and a step-drawdown test to pick the efficient operating rate. "
            "Sustainable yield is set not by the aquifer's total storage "
            "but by capture - pumping must intercept recharge or discharge "
            "that can be taken without drying streams, collapsing land "
            "(subsidence), or inviting seawater inland. Long-term "
            "observation-well networks watch water levels for the verdict."
        ),
        "key_points": [
            "Unconfined aquifers have a water table; confined aquifers have a potentiometric surface that can drive artesian flow.",
            "The Theis (1935) solution: drawdown spreads with time following the well function W(u), yielding transmissivity and storativity.",
            "Specific capacity (Q/drawdown) grades the well; specific yield (0.1-0.3) grades the unconfined aquifer's drainable storage.",
            "Type-curve departures diagnose boundaries: recharge flattens drawdown, barriers steepen it.",
            "Sustainable yield is about capture of recharge/discharge - not mining storage - lest streams dry, land subside, or seas intrude.",
        ],
        "requirements": [
            "A controlled-rate pumping test with drawdown logged in observation wells at log-spaced times.",
            "Well construction details: screened interval, aquifer thickness, distances to observation wells.",
            "Long-term water-level records to separate pumping effects from climate.",
        ],
        "standards": [
            "Report transmissivity in m2/day and storativity dimensionless, with the analysis method (Theis, Cooper-Jacob) stated.",
            "Log water levels to a fixed datum; report pumping rate and duration with every test.",
        ],
        "citations": [CIT_FREEZE, CIT_FETTER],
        "sig_lens": (
            "Signature edition: his Signature underground reservoir - "
            "each aquifer mapped, each well a metered tap."
        ),
        "demo_kind": "theis",
    },
    {
        "key": "groundwater_recharge_discharge",
        "name": "Groundwater Recharge and Discharge",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Recharge is water arriving at the water table; discharge is "
            "water leaving the groundwater system - to streams as baseflow, "
            "to springs and seeps, to wells, to the sea, or upward to the "
            "atmosphere by evapotranspiration where the water table is "
            "shallow. The two must balance over the long term or water "
            "levels fall (overdraft) or rise (waterlogging). Recharge is "
            "notoriously hard to measure directly, so hydrologists triangulate: "
            "the water-table fluctuation method multiplies the seasonal "
            "rise by specific yield; chloride mass balance compares "
            "rainfall chloride to groundwater chloride (what ET leaves "
            "behind concentrates the salt); baseflow separation of stream "
            "hydrographs estimates the groundwater contribution; and "
            "Darcy calculations across a cross-section give the flux. "
            "Recharge concentrates in space and time: coarse soils, "
            "fractured rock, losing stream reaches, and playas recharge "
            "far more than their area suggests, and most recharge arrives "
            "in wet years and wet seasons. Managed aquifer recharge - "
            "spreading basins, injection wells, dry wells - deliberately "
            "banks surplus surface water underground for dry times, "
            "treating aquifers as reservoirs with near-zero evaporation."
        ),
        "how_it_works": (
            "Recharge estimation works by closing the unsaturated-zone and "
            "aquifer budgets together. The water-table fluctuation method "
            "reads recharge from the rise: R equals specific yield times "
            "the water-level rise, corrected for the recession that would "
            "have continued without the rain. Chloride mass balance uses "
            "the atmosphere's salt: recharge equals precipitation times "
            "rainfall chloride divided by groundwater chloride, since ET "
            "leaves chloride behind. Baseflow analysis treats the stream "
            "as the aquifer's drain: the groundwater discharge is the "
            "separated baseflow at the basin outlet. Discharge is mapped "
            "the other way: seepage runs (discharge measured along a "
            "stream reach) locate gaining and losing reaches, and "
            "temperature or seepage meters pinpoint spring inflows. For "
            "management, numerical models integrate all of it, and the "
            "sustainability test is simple: long-term mean water levels "
            "must not trend down."
        ),
        "key_points": [
            "Recharge in must balance discharge out over the long term, or water levels trend down (overdraft) or up (waterlogging).",
            "Estimated four ways: water-table fluctuation x specific yield, chloride mass balance, baseflow separation, Darcy flux.",
            "Recharge concentrates in coarse soils, fractures, losing reaches, and wet years - the average misleads.",
            "Streams are the aquifer's drain: seepage runs map gaining vs losing reaches.",
            "Managed aquifer recharge banks surplus surface water underground - a reservoir with near-zero evaporation.",
        ],
        "requirements": [
            "Observation-well hydrographs spanning wet and dry seasons for the fluctuation method.",
            "Specific yield of the aquifer material and chloride data for mass-balance checks.",
            "Streamflow records for baseflow separation at the basin outlet.",
        ],
        "standards": [
            "Report recharge in mm/year with the method and period; compare at least two independent methods.",
            "State whether recharge is gross (arriving at the water table) or net (minus groundwater ET).",
        ],
        "citations": [CIT_FREEZE, CIT_DINGMAN],
        "sig_lens": (
            "Signature edition: his Signature aquifer banking - deposits "
            "of recharge logged, withdrawals of discharge audited."
        ),
        "demo_kind": "recharge",
    },
    {
        "key": "springs_seeps",
        "name": "Springs and Seeps",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Springs and seeps are where groundwater becomes surface water: "
            "a spring is a concentrated natural discharge, a seep its "
            "diffuse cousin. They form where the water table meets the "
            "land surface - in a valley bottom, at a geologic contact "
            "where permeable rock meets impermeable, along a fault or "
            "fracture zone, or where a confined aquifer's potentiometric "
            "surface exceeds the ground. Karst springs can roar at cubic "
            "meters per second after storms; desert seeps may barely wet "
            "the sand. Springs are hydrologic instruments in their own "
            "right: their discharge hydrographs and recession curves "
            "fingerprint the aquifer feeding them, their temperature is "
            "nearly constant year-round (a clue to flow-path depth), and "
            "their chemistry and isotopes trace the recharge area. Many "
            "of the world's great rivers begin as springs, and through "
            "history springs have sited cities, shrines, and spas - Bath, "
            "Saratoga, and countless desert oases are spring towns. "
            "Because they integrate their whole recharge area, springs are "
            "early warners: declining spring flow is often the first "
            "visible symptom of aquifer overdraft."
        ),
        "how_it_works": (
            "Spring hydrology works by treating the spring as a gauged "
            "outlet of its aquifer. Discharge is measured with weirs, "
            "flumes, or current meters at the orifice; continuous stage "
            "recorders give the spring hydrograph. The recession limb "
            "after storms is fitted to exponential decay, and the "
            "recession constant characterizes the aquifer's storage and "
            "transmissivity - karst springs show fast, flashy recessions "
            "with multiple components (conduit flow draining first, "
            "matrix flow later). Temperature logging separates shallow, "
            "seasonally varying flow paths from deep, constant-temperature "
            "ones. Water chemistry and stable isotopes (oxygen-18, "
            "deuterium) are compared against the local meteoric water line "
            "to identify recharge elevation and area. Protection follows "
            "the science: the capture zone feeding the spring is mapped, "
            "and land use within it is managed, because a spring's water "
            "quality is only as good as its recharge area."
        ),
        "key_points": [
            "Springs form where the water table or potentiometric surface meets the land: valley bottoms, geologic contacts, faults, karst conduits.",
            "Spring hydrographs and recession curves fingerprint the feeding aquifer - flashy multi-component recessions mean karst.",
            "Near-constant temperature indicates deep flow paths; chemistry and isotopes trace the recharge area.",
            "Great rivers and historic cities begin at springs; declining flow is the first visible symptom of overdraft.",
            "Protection means mapping and managing the spring's capture zone, not just the orifice.",
        ],
        "requirements": [
            "Discharge measurements at the orifice across seasons and storm responses.",
            "Temperature and specific-conductance logging to separate flow components.",
            "Isotope or chemistry data to identify recharge source areas.",
        ],
        "standards": [
            "Report spring discharge in L/s or m3/s with measurement method and date.",
            "Classify springs by Meinzer magnitude (flow rate classes) when comparing systems.",
        ],
        "citations": [CIT_FETTER, CIT_FREEZE],
        "sig_lens": (
            "Signature edition: his Signature fountains - each spring a "
            "metered spout from the underground accounts."
        ),
        "demo_kind": "springs",
    },
    {
        "key": "snow_hydrology",
        "name": "Snow Hydrology: Reading the Snowpack",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "In the world's mountain water towers - the western Americas, "
            "the Alps, the Himalayas, Central Asia - the snowpack is the "
            "largest reservoir, storing winter precipitation and releasing "
            "it as spring and summer melt. Snow hydrology is the science "
            "of that storage: how snow accumulates, how it metamorphoses, "
            "and how it melts. The key variable is snow water equivalent "
            "(SWE): the depth of water the snowpack would yield if melted, "
            "equal to snow depth times snow density divided by water "
            "density - a meter of 30-percent-dense snow holds 300 "
            "millimeters of water. Melt is an energy-balance problem: net "
            "solar and longwave radiation, sensible heat from warm air, "
            "latent heat from condensation, ground heat, and the heat of "
            "warm rain all contribute, with radiation usually dominant. In "
            "practice, the degree-day method - melt proportional to air "
            "temperature above a threshold - predicts melt surprisingly "
            "well from temperature data alone. Snow courses (manual depth "
            "and density surveys), automated SNOTEL-style pillows that "
            "weigh the pack, and satellite snow-cover mapping feed the "
            "water-supply forecasts that allocate irrigation water months "
            "before it flows."
        ),
        "how_it_works": (
            "Snow hydrology works by tracking the pack's mass and energy. "
            "Accumulation is measured as depth and density profiles; SWE "
            "is the product. The pack ripens through winter: grains "
            "round and bond, density climbs from 0.1 toward 0.4 or more, "
            "and liquid water is held by capillarity until the pack is "
            "isothermal at 0 C and saturated - then any energy input "
            "becomes meltwater output. The full energy balance sums "
            "radiation, turbulent fluxes, ground heat, and rain heat; the "
            "degree-day shortcut multiplies positive degree-days by a melt "
            "factor (typically 2-5 mm per degree-day). Forecast models "
            "assimilate pillow, course, and satellite data into the "
            "accumulation season, then run melt scenarios to produce "
            "April-through-July runoff volumes - the numbers behind "
            "western water allocation. Rain-on-snow events are the "
            "dangerous exception: warm rain plus turbulent heat can melt "
            "the pack catastrophically and trigger the region's worst "
            "floods."
        ),
        "key_points": [
            "The snowpack is the mountain regions' largest reservoir; SWE (depth x density) is its account balance.",
            "Melt is an energy-balance process (radiation dominant); the degree-day method approximates it from temperature.",
            "A ripe pack is isothermal at 0 C and saturated - then every energy input becomes runoff.",
            "Measured by snow courses, weighing pillows, and satellite snow-cover mapping.",
            "Snowmelt forecasts allocate irrigation water months ahead; rain-on-snow events cause the worst floods.",
        ],
        "requirements": [
            "Depth and density profiles (or pillow weights) to compute SWE.",
            "Temperature data for degree-day melt; radiation data for full energy balance.",
            "Satellite or aerial snow-cover extent to constrain the modeled pack.",
        ],
        "standards": [
            "Report SWE in millimeters of water; report density as a fraction of water density.",
            "State the melt-factor value and calibration period when using degree-day methods.",
        ],
        "citations": [CIT_GRAY, CIT_DINGMAN],
        "sig_lens": (
            "Signature edition: his Signature winter vault - every flake "
            "weighed, every degree-day of melt scheduled."
        ),
        "demo_kind": "snow",
    },
    {
        "key": "glacier_mass_balance",
        "name": "Glacier Mass Balance and Meltwater",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Glaciers are snowpacks that survived the summer: where annual "
            "accumulation exceeds ablation year after year, snow compacts "
            "to firn and then ice, and the ice flows downhill. Glacier "
            "mass balance - accumulation minus ablation over a year - is "
            "the glacier's annual profit or loss, measured in meters of "
            "water equivalent. The equilibrium line divides the upper "
            "accumulation zone from the lower ablation zone; its altitude "
            "migrates with climate. For downstream hydrology, glaciers are "
            "both reservoir and regulator: they store water on "
            "multi-decadal timescales and release meltwater in late summer "
            "exactly when snowpack-fed rivers run low - the reason the "
            "Himalayas' rivers, the Andes' rivers, and Alaska's rivers keep "
            "flowing in August. A glacier in negative balance contributes "
            "extra 'deglaciation discharge' beyond its sustainable yield, "
            "a temporary bonus that vanishes as the ice shrinks - the "
            "'peak water' problem facing glacier-fed regions. Glaciologists "
            "measure balance with stake networks (ablation stakes drilled "
            "into the ice, snow pits in the accumulation zone), repeated "
            "topographic or geodetic surveys, and increasingly with "
            "satellite altimetry and gravimetry."
        ),
        "how_it_works": (
            "Mass-balance hydrology works by differencing the ledger. The "
            "glaciological method sums point measurements: snow-pit SWE in "
            "the accumulation zone minus stake melt in the ablation zone, "
            "extrapolated over the glacier's area bands. The geodetic "
            "method differences digital elevation models from two dates "
            "and converts volume change to mass with a density assumption. "
            "Melt modeling adapts the snow energy balance to ice, with "
            "lower albedo (dirty ice melts faster) and the degree-day "
            "method calibrated separately for snow and ice. Runoff "
            "forecasting routes melt through the glacier's drainage "
            "system - supraglacial streams, englacial conduits, subglacial "
            "channels - which evolves through the season from inefficient "
            "distributed flow (spring, high pressure, fast sliding) to "
            "efficient channelized flow (summer). Outburst floods "
            "(jokulhlaups) from ice-dammed lakes are the catastrophic "
            "failure mode, monitored by lake-level sensors."
        ),
        "key_points": [
            "Mass balance = accumulation minus ablation (m water equivalent/yr); the equilibrium line divides the two zones.",
            "Glaciers regulate late-summer flow, releasing melt when snow-fed rivers run low.",
            "Negative balance pays temporary 'deglaciation discharge' - the peak-water bonus that ends as ice shrinks.",
            "Measured by stake networks, snow pits, repeat DEMs, satellite altimetry and gravimetry.",
            "Subglacial drainage evolves seasonally; ice-dammed lake outbursts (jokulhlaups) are the catastrophic mode.",
        ],
        "requirements": [
            "Stake and snow-pit networks spanning accumulation and ablation zones, or repeat elevation surveys.",
            "Separate melt factors (or energy-balance parameters) for snow vs exposed ice.",
            "Glacier area and hypsometry to scale point measurements to the whole glacier.",
        ],
        "standards": [
            "Report mass balance in meters of water equivalent per year, with the method (glaciological/geodetic) stated.",
            "Reference the hydrological year consistently; state the density assumption for geodetic conversions.",
        ],
        "citations": [CIT_DINGMAN, CIT_MAIDMENT],
        "sig_lens": (
            "Signature edition: his Signature ice accounts - centuries "
            "of winter banked, each summer's withdrawal metered."
        ),
        "demo_kind": "glacier",
    },
    {
        "key": "lakes_reservoirs",
        "name": "Lakes and Reservoirs: Still-Water Hydrology",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Lakes and reservoirs are hydrology's capacitors: they smooth "
            "the spiky inflow hydrograph into a steadier outflow, and "
            "their water budgets read P plus Qin equals E plus Qout plus "
            "change in storage, with seepage often a quiet extra term. The "
            "residence time - volume divided by outflow rate - sets a "
            "lake's personality: days for a run-of-river impoundment, "
            "centuries for the great tectonic lakes. Thermal stratification "
            "organizes deep lakes each summer into the warm surface "
            "epilimnion, the sharp thermocline, and the cold deep "
            "hypolimnion; fall cooling overturns the stack and mixes "
            "nutrients upward. Reservoirs add human operation to the "
            "physics: storage is partitioned into dead storage (below the "
            "outlet), conservation storage (the usable water-supply and "
            "power pool), and flood-control storage (kept empty to catch "
            "floods), with rule curves dictating the target level through "
            "the year. Bathymetric surveys map the storage-elevation "
            "curve that converts a staff-gauge reading into acre-feet. "
            "Sedimentation is the slow enemy: reservoirs trap the river's "
            "sediment load and lose capacity year by year - the world's "
            "reservoirs have already lost a significant fraction of their "
            "original storage."
        ),
        "how_it_works": (
            "Reservoir hydrology works through level-pool routing: with "
            "the storage-elevation and outflow-elevation curves known, "
            "each time step's inflow is added, outflow is computed from "
            "the operating rules, and storage is updated - the same "
            "arithmetic whether routing a flood wave or planning a "
            "drought. Operators balance competing objectives with rule "
            "curves: keep the pool high for water supply and power, keep "
            "it low for flood space, release pulses for downstream "
            "ecology and water rights. Evaporation from the surface - "
            "estimated by pan coefficients or energy-balance methods - is "
            "a major loss in arid regions, motivating floating covers and "
            "underground storage alternatives. Sediment surveys with echo "
            "sounders track capacity loss; sustainable designs add "
            "sediment bypass tunnels or schedule flushing flows. Dam "
            "safety hydrology sizes the spillway for the probable maximum "
            "flood, because overtopping is the failure mode that must "
            "never happen."
        ),
        "key_points": [
            "Water budget: P + inflow = evaporation + outflow + storage change; residence time (volume/outflow) sets the lake's personality.",
            "Summer stratification (epilimnion/thermocline/hypolimnion) organizes deep lakes; fall overturn mixes nutrients up.",
            "Reservoir storage is partitioned: dead, conservation (supply/power), and flood-control pools, run by rule curves.",
            "Level-pool routing (storage + outflow curves, timestep accounting) is the operational arithmetic.",
            "Sedimentation steadily steals capacity; spillways are sized for the probable maximum flood - overtopping must never happen.",
        ],
        "requirements": [
            "Bathymetric survey giving the storage-elevation and surface-area curves.",
            "Inflow records, operating rules, and evaporation estimates.",
            "Downstream constraints: water rights, flood limits, ecological flow requirements.",
        ],
        "standards": [
            "Report storage in cubic meters (or acre-feet with conversion) referenced to a fixed elevation datum.",
            "Publish rule curves with their effective dates; operations must be auditable against them.",
        ],
        "citations": [CIT_DINGMAN, CIT_MAYS],
        "sig_lens": (
            "Signature edition: his Signature still-water vaults - each "
            "reservoir a leveled, ruled, Signature capacitor."
        ),
        "demo_kind": "reservoir",
    },
    {
        "key": "wetlands_hydrology",
        "name": "Wetlands Hydrology",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Wetlands - marshes, swamps, bogs, fens, floodplains - are "
            "landscapes defined by their hydrology: water at or near the "
            "surface long enough to shape the soils and the life. The "
            "master variable is the hydroperiod: the depth, duration, "
            "frequency, and timing of inundation and saturation. A "
            "millimeter-scale difference in water level decides whether a "
            "site is marsh or meadow. Bogs are rain-fed, acidic, and "
            "nutrient-poor, building peat from sphagnum; fens are "
            "groundwater-fed, mineral-rich, and far more diverse. "
            "Hydrologically, wetlands are multi-taskers: they store flood "
            "water and release it slowly, recharge or discharge "
            "groundwater depending on the setting, trap sediment and "
            "nutrients (nature's water-treatment plants), and "
            "evapotranspire prodigiously. The water budget of a wetland "
            "reads like any other - precipitation plus surface and "
            "groundwater inflow, minus ET, outflow, and storage change - "
            "but with the water table hovering near the surface, small "
            "fluxes make big ecological differences. Drained wetlands "
            "lose all of it at once: flood storage, filtration, habitat, "
            "and carbon - peat drainage alone is a major global carbon "
            "source."
        ),
        "how_it_works": (
            "Wetland hydrology works by instrumenting the shallow system: "
            "staff gauges and pressure transducers log surface water, "
            "piezometer nests log the water table and deeper heads, and "
            "the vertical head gradients reveal whether the wetland is "
            "recharging the aquifer, discharging it, or perched. The "
            "hydroperiod is distilled into statistics - mean depth, days "
            "inundated per year, timing of drawdown - that predict the "
            "plant community with surprising sharpness. Water budgets "
            "quantify the services: flood attenuation from the storage "
            "volume between normal and spill levels, nutrient removal "
            "from inflow-outflow concentration differences times flow, "
            "groundwater exchange from the head gradients. Restoration "
            "design inverts the analysis: set the target hydroperiod for "
            "the desired community, then grade the land, plug the drains, "
            "and reconnect the water source to deliver it. Success is "
            "judged hydrologically first - right water, right time - "
            "because the biology follows the water."
        ),
        "key_points": [
            "Wetlands are defined by hydrology: the hydroperiod (depth, duration, frequency, timing of wetness) decides marsh vs meadow.",
            "Bogs are rain-fed and acidic; fens are groundwater-fed and diverse - water source sets the ecology.",
            "Services: flood storage, groundwater exchange, sediment/nutrient trapping, carbon storage in peat.",
            "Piezometer nests reveal recharge vs discharge vs perched conditions from vertical head gradients.",
            "Restoration designs the hydroperiod first - the biology follows the water.",
        ],
        "requirements": [
            "Shallow wells and surface gauges logging at daily or finer resolution through wet and dry cycles.",
            "Topographic survey at centimeter precision - millimeters of level decide the community.",
            "Inflow/outflow water-quality data to quantify filtration services.",
        ],
        "standards": [
            "Report hydroperiod statistics (depth, duration, timing) alongside any wetland classification.",
            "Reference all water levels to a common datum; report the monitoring period's wetness relative to normal.",
        ],
        "citations": [CIT_DINGMAN, CIT_WARD],
        "sig_lens": (
            "Signature edition: his Signature shallow-water gardens - "
            "every hydroperiod tuned, every service tallied."
        ),
        "demo_kind": "wetland",
    },
    {
        "key": "flood_frequency",
        "name": "Floods and Flood-Frequency Analysis",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Flood-frequency analysis answers the question every floodplain "
            "map, bridge, and levee depends on: how big is the flood with "
            "a given chance of happening in any year? The '100-year "
            "flood' is not a flood that comes every century - it is the "
            "flood with a 1 percent chance each year, meaning a 26 percent "
            "chance of occurring at least once in a 30-year mortgage. The "
            "method fits a probability distribution to the series of "
            "annual maximum flows (or peaks-over-threshold) and reads off "
            "quantiles: the US federal standard is the Log-Pearson Type "
            "III distribution, fitted to the logarithms of the annual "
            "peaks with their mean, standard deviation, and skew. Floods "
            "come in flavors with different physics: flash floods from "
            "intense convective rain on small basins, riverine floods from "
            "long-duration rain or snowmelt on large basins, coastal floods "
            "from storm surge, and urban floods where pavement turns "
            "modest rain into mayhem. The analysis assumes stationarity - "
            "that the past represents the future - an assumption climate "
            "change, urbanization, and regulation increasingly violate, "
            "pushing practice toward nonstationary methods and "
            "climate-adjusted estimates."
        ),
        "how_it_works": (
            "The analysis works by ranking history. Assemble the annual "
            "maximum series (one peak per year, at least 10 years, more "
            "is far better), compute the mean, standard deviation, and "
            "skew of the base-10 logarithms, and evaluate the Log-Pearson "
            "III quantile function at the desired exceedance probability - "
            "with adjustments for low outliers, historic mega-floods, and "
            "regional skew information. Plotting positions (Weibull: rank "
            "over n-plus-1) let the fitted curve be checked against the "
            "data's own empirical frequencies. The resulting quantiles - "
            "Q10, Q50, Q100, Q500 - size bridges and culverts, draw "
            "floodplain boundaries, and price flood insurance. Because "
            "short records make the rare quantiles wobbly, regional "
            "regression pools data from similar basins to stabilize "
            "estimates at ungauged sites. Nonstationary extensions let "
            "the distribution's parameters trend with time or climate "
            "indices, so the '100-year' flood can grow as the climate "
            "warms."
        ),
        "key_points": [
            "The 100-year flood = 1% annual chance (26% in 30 years) - a probability, not a schedule.",
            "US standard: Log-Pearson Type III fitted to logs of annual maxima (mean, std dev, skew).",
            "Flood flavors: flash (convective, small basins), riverine (long rain/snowmelt), coastal surge, urban pavement floods.",
            "Plotting positions (Weibull) check the fitted curve against empirical frequencies.",
            "Stationarity is failing under climate change and urbanization - nonstationary methods adjust the quantiles.",
        ],
        "requirements": [
            "Annual maximum flow series, 10+ years (longer is far better), checked for regulation and diversion changes.",
            "Historic flood information and regional skew to stabilize the rare quantiles.",
            "Consistent datum and rating history - a shifted rating corrupts the whole series.",
        ],
        "standards": [
            "Follow Bulletin 17C procedures for Log-Pearson III fitting in US federal practice.",
            "Report quantiles with confidence limits and the record length behind them.",
        ],
        "citations": [CIT_CHOW, CIT_MAIDMENT],
        "sig_lens": (
            "Signature edition: his Signature flood odds - every return "
            "period priced, every floodplain line drawn in Signature ink."
        ),
        "demo_kind": "flood_freq",
    },
    {
        "key": "drought_hydrology",
        "name": "Drought Hydrology",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Drought is the quiet disaster: a slow, creeping deficit of "
            "water that causes more economic damage than floods but never "
            "makes the dramatic photograph. Hydrologists sort drought into "
            "three cascading types. Meteorological drought is the rainfall "
            "deficit itself. Agricultural (soil-moisture) drought follows "
            "as soils dry below what crops need. Hydrological drought "
            "arrives last, as streamflow, reservoir storage, and "
            "groundwater fall - and it lingers longest, because aquifers "
            "and reservoirs refill slowly. Indices translate the deficit "
            "into numbers: the Standardized Precipitation Index (SPI) "
            "expresses rainfall as standard deviations from normal over "
            "chosen timescales; the Palmer Drought Severity Index (PDSI) "
            "runs a soil-water budget; streamflow drought is read from "
            "flow-duration percentiles and reservoir storage. The "
            "timescale matters enormously: 1-month SPI tracks flash "
            "meteorological drought, 12-month SPI tracks the hydrological "
            "kind. Drought planning uses the drought of record - the worst "
            "in the gauge history - as the design test for water-supply "
            "systems, and increasingly stress-tests against synthetic "
            "droughts worse than anything observed."
        ),
        "how_it_works": (
            "Drought analysis works by standardizing deficits. SPI fits a "
            "gamma distribution to precipitation accumulated over the "
            "chosen timescale, then transforms to a standard normal: "
            "minus 2 is extreme drought, plus 2 extreme wet. PDSI "
            "maintains a running soil-water account with Thornthwaite "
            "potential ET, accumulating moisture anomaly into severity "
            "classes. Hydrological drought is monitored through "
            "percentile flows (e.g., 7-day low flows), reservoir storage "
            "relative to rule curves, and observation-well levels against "
            "their historical distributions. Triggers convert indices to "
            "action: staged drought contingency plans tighten outdoor "
            "watering, then allocations, then emergency supplies as "
            "indicators cross thresholds. Forecasting blends seasonal "
            "climate outlooks with hydrologic initial conditions - a full "
            "reservoir forgives a dry forecast; an empty one does not. "
            "The recovery question is asymmetric: one wet month can end "
            "meteorological drought while aquifers need years."
        ),
        "key_points": [
            "Three cascading droughts: meteorological (rain deficit) -> agricultural (soil moisture) -> hydrological (streams, reservoirs, groundwater).",
            "SPI standardizes rainfall over chosen timescales (1-month vs 12-month track different droughts); PDSI runs a soil-water budget.",
            "Hydrological drought arrives last and lingers longest - aquifers and reservoirs refill slowly.",
            "Staged contingency plans convert index thresholds into tightening restrictions.",
            "Design against the drought of record, then stress-test with synthetic droughts worse than observed.",
        ],
        "requirements": [
            "Long precipitation and streamflow records (30+ years ideal) to define 'normal'.",
            "Soil-water holding parameters for PDSI-type accounting; reservoir and well records for hydrological drought.",
            "Agreed triggers and stages before the drought arrives - plans written in crisis fail.",
        ],
        "standards": [
            "Report the index, timescale, and baseline period with every drought classification.",
            "Use WMO-recommended SPI computation procedures for comparability across regions.",
        ],
        "citations": [CIT_DINGMAN, CIT_MAIDMENT],
        "sig_lens": (
            "Signature edition: his Signature dry-ledger - every deficit "
            "standardized, every stage of thirst named."
        ),
        "demo_kind": "drought",
    },
    {
        "key": "water_quality_rivers",
        "name": "Water Quality in Rivers",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "River water quality is hydrology with chemistry: the same "
            "discharge that moves water moves everything dissolved and "
            "suspended in it. Dissolved oxygen (DO) is the master variable "
            "for aquatic life - fish need roughly 5 milligrams per liter "
            "or more. Organic waste feeds bacteria that consume oxygen "
            "(biochemical oxygen demand, BOD), and the Streeter-Phelps "
            "equations describe the resulting oxygen sag downstream of a "
            "discharge: DO falls to a minimum at the sag point, then "
            "recovers as reaeration outpaces demand. Nutrients (nitrogen, "
            "phosphorus) fertilize algae into blooms that die, decay, and "
            "suffocate - eutrophication. Sediment is the other great "
            "pollutant by mass: suspended load clouds water and smothers "
            "habitat, bedload reshapes channels, and both are estimated "
            "with sediment rating curves (load versus discharge). Point "
            "sources (pipes) are regulated at the outfall; nonpoint "
            "sources (fields, streets, mines) arrive with the rain and "
            "are managed at the watershed scale. Total Maximum Daily "
            "Loads (TMDLs) are the regulatory arithmetic: the river's "
            "assimilative capacity divided among dischargers with a "
            "margin of safety."
        ),
        "how_it_works": (
            "Water-quality hydrology works by coupling hydraulics to "
            "kinetics. The Streeter-Phelps model balances deoxygenation "
            "(first-order BOD decay) against reaeration (proportional to "
            "the oxygen deficit and the reaeration coefficient, which "
            "rises with velocity and falls with depth) to predict the DO "
            "sag curve and locate its minimum. Modern models (QUAL2K and "
            "its descendants) add nutrients, algae, pH, and temperature "
            "in a one-dimensional river network. Loads are computed as "
            "concentration times discharge, integrated over time - which "
            "is why continuous flow records plus storm-chasing water "
            "samples beat occasional grab samples: most of a river's "
            "annual sediment and nutrient load moves in a few storms. "
            "Sediment rating curves (power laws of load vs discharge) "
            "extend sparse samples across the flow record. Management "
            "then targets the budget: upgrade treatment plants for point "
            "sources, buffer strips and detention for nonpoint, and TMDL "
            "allocations to keep the sag above the standard."
        ),
        "key_points": [
            "Dissolved oxygen is the master variable; the Streeter-Phelps sag curve locates the DO minimum below organic discharges.",
            "BOD decay vs reaeration (faster in shallow swift water) sets the sag's depth and position.",
            "Nutrients drive eutrophication; sediment (by mass the biggest pollutant) moves mostly in a few storms.",
            "Load = concentration x discharge integrated over time - storm-chasing samples beat grab samples.",
            "TMDLs divide the river's assimilative capacity among sources with a margin of safety.",
        ],
        "requirements": [
            "Continuous discharge record plus concentration samples covering the flow range, especially storms.",
            "BOD decay and reaeration coefficients (measured or estimated from hydraulics) for DO modeling.",
            "Water-quality standards for the designated uses (fisheries, drinking water, recreation).",
        ],
        "standards": [
            "Report concentrations in mg/L with detection limits and the analytical method.",
            "Calibrate water-quality models to both low-flow (worst dilution) and storm conditions.",
        ],
        "citations": [CIT_CHOW, CIT_WARD],
        "sig_lens": (
            "Signature edition: his Signature river assay - every liter "
            "graded, every load accounted at the outfall."
        ),
        "demo_kind": "water_quality",
    },
    # ================= ADVANCED =================
    {
        "key": "manning_open_channel",
        "name": "Manning's Equation: Flow in Open Channels",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Manning's equation is the workhorse of river engineering: Q "
            "equals (1/n) times A times R to the two-thirds times S to "
            "the one-half. Discharge from channel geometry alone - "
            "cross-sectional area A, hydraulic radius R (area over wetted "
            "perimeter), energy slope S - and one gloriously empirical "
            "number, Manning's n, the roughness coefficient. Clean "
            "excavated earth runs about 0.022; weedy natural channels "
            "0.035 to 0.05; floodplains with dense brush 0.10 or more. "
            "The equation describes uniform flow, where gravity pulling "
            "down the slope exactly balances boundary friction - the "
            "normal depth. Real rivers rarely oblige, so engineers use "
            "it stepwise: gradually varied flow computations march the "
            "water surface upstream or downstream from a control, "
            "accounting for friction reach by reach. The Froude number "
            "decides the regime: below 1, tranquil subcritical flow where "
            "disturbances travel upstream; above 1, shooting supercritical "
            "flow; at 1, critical flow - the minimum-energy state that "
            "controls weirs and flumes. Getting n right is the art: "
            "tables, photographs of calibrated reaches, and inverse "
            "computation from measured floods all serve."
        ),
        "how_it_works": (
            "Manning's equation works by equating the downslope weight of "
            "water to boundary resistance, empirically. For uniform flow, "
            "pick n from calibrated tables or photo guides, survey the "
            "cross-section for A and R, measure the slope, and compute Q - "
            "or invert to find normal depth for a given Q. For natural "
            "rivers, the standard-step method applies Manning reach by "
            "reach: starting from a known water surface at a control "
            "(critical depth at a weir, normal depth far downstream), "
            "solve the energy equation across each cross-section, "
            "iterating depth until energy balances. Compound channels are "
            "split into main channel and floodplains with separate n "
            "values, because floodplain brush resists far more than the "
            "clean channel. Calibration adjusts n until computed profiles "
            "match observed high-water marks - the standard post-flood "
            "forensic. The equation's empirical heart means extrapolating "
            "far beyond calibrated flows is done with humility and "
            "sensitivity tests."
        ),
        "key_points": [
            "Q = (1/n) A R^(2/3) S^(1/2): discharge from geometry plus Manning's roughness n.",
            "n ranges ~0.02 (clean earth) to 0.10+ (brushy floodplain); getting n right is the art.",
            "Uniform flow gives normal depth; the standard-step method marches gradually varied profiles from controls.",
            "Froude number < 1 subcritical (tranquil), > 1 supercritical (shooting), = 1 critical (minimum energy).",
            "Compound channels split main channel from floodplain with separate n values.",
        ],
        "requirements": [
            "Surveyed cross-sections: area, wetted perimeter, hydraulic radius at multiple stations.",
            "Calibrated Manning's n values (tables, photo guides, or inverse computation from floods).",
            "Boundary condition: a control section or known downstream water surface to start the computation.",
        ],
        "standards": [
            "Report n values with their source (table, calibrated, photo-matched) and the flow range they cover.",
            "State whether English (1.486/n) or SI (1.0/n) form is used - the constant differs.",
        ],
        "citations": [CIT_HENDERSON, CIT_CHOW],
        "sig_lens": (
            "Signature edition: his Signature channel code - every "
            "cross-section solved, every roughness catalogued."
        ),
        "demo_kind": "manning",
    },
    {
        "key": "sediment_transport",
        "name": "Sediment Transport",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Rivers are conveyor belts of rock: the world's rivers carry "
            "roughly 15 to 20 billion tonnes of sediment to the oceans "
            "each year. Sediment moves in three modes. Dissolved load "
            "rides invisibly in solution. Suspended load - silts and "
            "clays, plus fine sand in turbulence - travels within the "
            "flow, clouding the water. Bedload - sand and gravel - hops, "
            "rolls, and slides along the bed. Motion starts when the "
            "flow's shear stress exceeds the critical Shields stress, a "
            "dimensionless threshold around 0.03 to 0.06 for gravel: below "
            "it the bed sleeps, above it the river rebuilds itself. "
            "Transport formulas (Meyer-Peter and Mueller for bedload, "
            "Engelund-Hansen for total load, and their many cousins) "
            "relate the excess shear to transport rate as power laws - "
            "useful, approximate, and famously disagreeing with each "
            "other by factors of two. The sediment budget rules "
            "morphology: reaches with more supply than capacity aggrade "
            "(fill), with less they degrade (incise) - the reason dams, "
            "which trap sediment, starve downstream reaches and erode "
            "deltas worldwide. Reservoir sedimentation, channel "
            "restoration, and delta survival are all sediment-transport "
            "problems first."
        ),
        "how_it_works": (
            "Sediment-transport analysis works from shear stress up. "
            "Compute the boundary shear from depth and slope (tau = rho g "
            "R S), compare against the critical Shields value for the "
            "bed's grain size, and apply a transport formula to the "
            "excess. Suspended load is sampled with depth-integrating "
            "samplers across the cross-section; bedload with pressure-"
            "difference or pit samplers, or tracked acoustically. "
            "Sediment rating curves - power laws of load versus discharge "
            "- extend sparse samples across the continuous flow record, "
            "because, again, most load moves in floods. The Exner "
            "equation (sediment continuity: bed elevation change equals "
            "the divergence of transport) turns transport gradients into "
            "predictions of aggradation and degradation. Management "
            "follows the budget: sediment bypass tunnels and flushing "
            "flows for reservoirs, environmental flow releases to mobilize "
            "spawning gravels below dams, and setback levees that let "
            "rivers rebuild floodplains with their own sediment."
        ),
        "key_points": [
            "Three modes: dissolved, suspended (silts/clays in the flow), bedload (sand/gravel hopping along the bed).",
            "Motion starts above the critical Shields stress (~0.03-0.06 dimensionless for gravel).",
            "Transport formulas are power laws of excess shear - useful, approximate, mutually disagreeing by ~2x.",
            "Sediment budget rules morphology: surplus supply aggrades, deficit degrades (dams starve downstream).",
            "Most annual load moves in a few floods - rating curves extend sparse samples across the flow record.",
        ],
        "requirements": [
            "Bed grain-size distribution (D50 and friends) from pebble counts or sieve analysis.",
            "Hydraulics: depth, slope, velocity - the shear stress drivers.",
            "Suspended and bedload samples across the flow range, weighted toward floods.",
        ],
        "standards": [
            "Report loads in tonnes per day with the formula and grain-size basis stated.",
            "Size sediment in millimeters with the phi scale for distributions; state the sampling method.",
        ],
        "citations": [CIT_DUNNE, CIT_CHOW],
        "sig_lens": (
            "Signature edition: his Signature rock conveyor - every "
            "grain's journey from mountain to sea tallied."
        ),
        "demo_kind": "sediment",
    },
    {
        "key": "urban_hydrology",
        "name": "Urban Hydrology",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Urban hydrology studies what pavement does to water: it seals "
            "the soil, so infiltration collapses, depression storage "
            "shrinks, and rainfall that once soaked in becomes runoff "
            "almost instantly. The result is the urban stream syndrome - "
            "flashier floods, lower baseflows, eroded channels, warmer "
            "water, and a cocktail of oils, metals, and nutrients. A "
            "meadow might convert 10 percent of a storm to runoff; a "
            "parking lot converts 95 percent, and delivers it in minutes "
            "through gutters and storm drains instead of hours through "
            "soil. The rational method - Q equals C times i times A, with "
            "C the runoff coefficient, i the rainfall intensity for the "
            "time of concentration, A the area - sizes small urban "
            "drainage for the design storm, and remains the most used "
            "equation in the field despite its simplicity. Larger systems "
            "are modeled with SWMM (Storm Water Management Model), which "
            "routes rainfall through subcatchments, gutters, pipes, and "
            "storage with full hydraulics. The modern answer is low-impact "
            "development (LID): bioretention, permeable pavement, green "
            "roofs, and rain gardens that restore infiltration and make "
            "the city behave a little more like the meadow."
        ),
        "how_it_works": (
            "Urban hydrologic design works from the design storm down. "
            "Delineate subcatchments, assign impervious percentages and "
            "runoff coefficients, compute the time of concentration (the "
            "travel time from the hydraulically farthest point - often "
            "minutes in piped systems), read the intensity-duration-"
            "frequency curve for that duration, and apply the rational "
            "formula for peak flow at each inlet. Pipes are sized with "
            "Manning's equation for the design flow; inlets are spaced so "
            "gutter spread stays within limits. SWMM extends this to "
            "continuous simulation: nonlinear reservoir routing on each "
            "subcatchment, kinematic or dynamic wave routing in the pipe "
            "network, storage and pump controls, and pollutant buildup-"
            "washoff. LID is designed as distributed storage and "
            "infiltration: bioretention cells sized to capture the water-"
            "quality storm (often the first 25 mm), permeable pavements "
            "with stone reservoirs beneath. Performance is verified by "
            "monitoring: inflow-outflow hydrographs that prove the "
            "flashiness was tamed."
        ),
        "key_points": [
            "Pavement collapses infiltration: meadow ~10% runoff, parking lot ~95%, delivered in minutes via drains.",
            "Urban stream syndrome: flashier floods, lower baseflows, eroded channels, polluted warm water.",
            "Rational method Q = CiA sizes small drainage; SWMM routes full hydraulics for larger systems.",
            "Design flows come from IDF curves at the time of concentration - minutes in piped catchments.",
            "Low-impact development (bioretention, permeable pavement, green roofs) restores infiltration at the source.",
        ],
        "requirements": [
            "Subcatchment delineation with impervious percentages and runoff coefficients.",
            "IDF curves for the locale and time-of-concentration computations.",
            "Pipe network geometry and LID storage/infiltration parameters for SWMM modeling.",
        ],
        "standards": [
            "State the design-storm return period and duration with every sized facility.",
            "Report imperviousness as directly connected vs total - disconnected impervious behaves differently.",
        ],
        "citations": [CIT_MAYS, CIT_CHOW],
        "sig_lens": (
            "Signature edition: his Signature city-sponge - every roof "
            "and road taught to drink like a meadow again."
        ),
        "demo_kind": "urban",
    },
    {
        "key": "stormwater_detention",
        "name": "Stormwater Detention Design",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Detention basins are the shock absorbers of urban hydrology: "
            "they catch the flood peak and meter it out slowly, so the "
            "downstream pipe or stream sees a gentle release instead of a "
            "hammer blow. A detention pond stores the inflow hydrograph's "
            "volume above the allowable outflow and releases it through a "
            "carefully sized outlet - typically a multi-stage riser: small "
            "orifices for the water-quality storm, a weir for the design "
            "flood, an emergency spillway for the extreme. Retention "
            "ponds (wet ponds) keep a permanent pool for settling and "
            "biology; dry detention basins empty completely between storms. "
            "Design is level-pool routing: given the inflow hydrograph, "
            "the stage-storage curve (from grading plans), and the "
            "stage-discharge curve (orifice and weir equations), route "
            "the flood through and check that the peak outflow meets the "
            "target - often the pre-development peak, so the development "
            "adds no new flooding downstream. Underground vaults, "
            "oversized pipes, and rooftop storage do the same job where "
            "land is precious. Maintenance is the unglamorous half of "
            "design: forebays trap the sediment, or the basin fills and "
            "the shock absorber goes flat."
        ),
        "how_it_works": (
            "Detention design works by routing. Build the stage-storage "
            "curve from the basin grading (volume at each elevation) and "
            "the stage-discharge curve from the outlet hydraulics "
            "(orifice equation for low flows, weir equation for high). "
            "Route the design inflow hydrograph with the storage-"
            "indication (Puls) method: each time step, storage change "
            "equals inflow minus outflow, with outflow read from the "
            "curves - iterating until the outflow hydrograph's peak and "
            "timing satisfy the target. Multi-stage outlets are tuned so "
            "the frequent storms get extended detention (24-48 hours for "
            "settling) while the rare flood passes safely below the "
            "embankment crest with freeboard. Water-quality volume - the "
            "first flush carrying most pollutants - gets its own "
            "treatment volume and drawdown time. As-built surveys verify "
            "the storage; outlet inspections verify the orifices are not "
            "clogged, because a blocked orifice turns detention into a "
            "bathtub."
        ),
        "key_points": [
            "Detention basins catch the flood peak and meter it out - downstream sees a gentle release, not a hammer blow.",
            "Multi-stage outlets: orifices for frequent storms, weirs for design floods, emergency spillways for extremes.",
            "Design = level-pool (Puls) routing of the inflow hydrograph through stage-storage and stage-discharge curves.",
            "Target is often the pre-development peak: the development must add no new downstream flooding.",
            "Forebays and maintenance keep sediment from flattening the shock absorber.",
        ],
        "requirements": [
            "Design inflow hydrograph (from rational method, unit hydrograph, or SWMM).",
            "Stage-storage curve from grading plans; stage-discharge from outlet hydraulics.",
            "Downstream peak-flow target and water-quality volume/drawdown requirements.",
        ],
        "standards": [
            "Provide freeboard above the extreme-flood water surface per local dam-safety rules.",
            "Document outlet dimensions and discharge curves on the as-built drawings; inspect annually.",
        ],
        "citations": [CIT_MAYS, CIT_CHOW],
        "sig_lens": (
            "Signature edition: his Signature shock absorbers - every "
            "peak caught, every release metered to the Signature spec."
        ),
        "demo_kind": "detention",
    },
    {
        "key": "reservoir_operation_yield",
        "name": "Reservoir Operation and Water-Supply Yield",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "How much water can a reservoir promise? That is the yield "
            "question, and hydrology answers it with the sequent-peak "
            "(Rippl mass-curve) method: plot cumulative inflow minus "
            "cumulative demand over the historical record, and the "
            "maximum cumulative deficit is the storage required to meet "
            "that demand without fail. The firm (safe) yield is the "
            "largest constant demand the reservoir can meet through the "
            "drought of record; anything promised above it is paper "
            "water. Operation is guided by rule curves - target storage "
            "through the year that balances flood space against supply: "
            "draw down before the flood season, refill after. In "
            "multi-reservoir systems, operating rules coordinate releases "
            "so the system behaves as one virtual reservoir, hedging "
            "releases when storage is low (accept small shortages now to "
            "avoid catastrophic ones later). Evaporation and sedimentation "
            "tax the yield silently year after year. And the cruelest "
            "lesson of reservoir hydrology: the drought that defines the "
            "yield is always the one in the record - until a worse one "
            "arrives, which is why modern planning stress-tests against "
            "paleoclimate droughts and climate projections, not just the "
            "gauge history."
        ),
        "how_it_works": (
            "Yield analysis works on the mass curve. Assemble the monthly "
            "(or daily) inflow series, subtract evaporation and the "
            "candidate demand, accumulate the residuals, and find the "
            "maximum drawdown of the cumulative curve - that is the "
            "required storage; iterate demand until required storage "
            "equals available storage to find firm yield. Simulation "
            "models then operate the reservoir through the historical "
            "and synthetic sequences with the rule curves, tallying "
            "shortages, spills, and flood-control performance. Hedging "
            "rules formalize caution: when storage falls into zones, "
            "releases are cut by fractions to stretch the remaining "
            "water. Optimization (linear and dynamic programming) finds "
            "the operating policy maximizing benefits across hydropower, "
            "supply, flood control, and ecology - though operators "
            "rightly distrust black-box rules they cannot explain in a "
            "drought meeting. Climate stress-testing reruns the whole "
            "apparatus on downscaled projections to see where the firm "
            "yield cracks."
        ),
        "key_points": [
            "Sequent-peak (Rippl) method: maximum cumulative deficit of inflow-minus-demand sets required storage.",
            "Firm yield = the constant demand met through the drought of record; above it is paper water.",
            "Rule curves balance flood space vs supply through the year; hedging stretches water when storage runs low.",
            "Multi-reservoir rules coordinate the system as one virtual reservoir.",
            "Stress-test beyond the gauge record: paleodroughts and climate projections reveal where yield cracks.",
        ],
        "requirements": [
            "Long inflow series (monthly or better) plus evaporation and demand projections.",
            "Storage-elevation curve and operating constraints (flood pool, minimum pool, release capacities).",
            "Agreed shortage-sharing rules before the drought - allocation by crisis fails.",
        ],
        "standards": [
            "Report firm yield with the drought of record, reliability percentage, and analysis period.",
            "Publish rule curves and hedging triggers; operations must be auditable.",
        ],
        "citations": [CIT_MAYS, CIT_MAIDMENT],
        "sig_lens": (
            "Signature edition: his Signature water promise - every "
            "acre-foot of yield backed by Signature arithmetic."
        ),
        "demo_kind": "reservoir_yield",
    },
    {
        "key": "hydropower_hydrology",
        "name": "Hydropower Hydrology: Head and Flow",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Hydropower is hydrology converted to watts: power equals "
            "water density times gravity times discharge times head times "
            "efficiency - P = rho g Q H eta. Every term is hydrology. "
            "Discharge comes from the flow-duration curve, which sorts the "
            "historical record from highest to lowest and reads the "
            "exceedance: Q90 (exceeded 90 percent of the time) is the "
            "dependable low flow, Q50 the median. Head is the elevation "
            "drop the plant exploits - hundreds of meters in mountain "
            "diversion schemes, tens of meters at big river dams. "
            "Efficiency (0.85-0.93 for modern turbines) depends on "
            "matching turbine type to the head-flow combination: Pelton "
            "wheels for high head and low flow, Francis for the middle, "
            "Kaplan and bulb turbines for low head and high flow. Firm "
            "power is what the plant delivers through the critical dry "
            "period; secondary power is the bonus in wet seasons. "
            "Pumped storage closes the loop hydrologically: off-peak "
            "electricity pumps water uphill, peak demand lets it fall - "
            "a water battery with 70-85 percent round-trip efficiency. "
            "Environmental hydrology constrains it all: minimum "
            "instream flows, ramping rates that do not strand fish, and "
            "sediment passage."
        ),
        "how_it_works": (
            "Hydropower assessment works from the duration curve. Build "
            "the flow-duration curve from the gauge record, choose the "
            "design flow (often Q30-Q40 for run-of-river, balancing energy "
            "against turbine cost), survey the head, select the turbine "
            "family, and compute the power-duration curve - then integrate "
            "for annual energy. Storage projects add reservoir simulation: "
            "the mass curve sizes storage to firm up the dry-season flow, "
            "and the operating rule maximizes energy value across seasons "
            "(peaking vs base-load). Head is not constant: reservoir "
            "drawdown and tailwater variation change it, so power is "
            "recomputed at each storage level. Economic analysis divides "
            "annualized cost by firm energy for the unit cost, and climate "
            "stress-testing reruns the duration curves on projected flows "
            "- glacier-fed schemes face the peak-water decline, "
            "monsoon schemes face shifting seasonality. Licensing then "
            "writes the hydrology into law: minimum flows, ramping limits, "
            "and reservoir levels become permit conditions."
        ),
        "key_points": [
            "P = rho g Q H eta: discharge from the flow-duration curve, head from the drop, efficiency 0.85-0.93.",
            "Flow-duration curve: Q90 dependable low flow, Q50 median - the design flow balances energy vs turbine cost.",
            "Turbine families match head-flow: Pelton (high head), Francis (medium), Kaplan/bulb (low head, high flow).",
            "Firm power through the critical dry period; secondary power in wet seasons; pumped storage as a water battery.",
            "Environmental constraints - minimum flows, ramping rates, sediment - are written into licenses.",
        ],
        "requirements": [
            "Flow-duration curve from a representative gauge record (adjust for diversions and regulation).",
            "Surveyed head (gross minus hydraulic losses) across the operating range.",
            "Turbine efficiency curves matched to the head-flow combination.",
        ],
        "standards": [
            "Report power in MW and energy in GWh/yr with the exceedance basis (firm vs average) stated.",
            "Document environmental flow and ramping constraints as binding design inputs, not afterthoughts.",
        ],
        "citations": [CIT_MAYS, CIT_MAIDMENT],
        "sig_lens": (
            "Signature edition: his Signature water-to-watts ledger - "
            "every head metered, every flow firmed."
        ),
        "demo_kind": "hydropower",
    },
    {
        "key": "irrigation_hydrology",
        "name": "Irrigation Hydrology",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Irrigation is humanity's largest use of water - about 70 "
            "percent of global freshwater withdrawals - and its hydrology "
            "is the art of delivering the right water at the right time "
            "with the least waste. The crop's need is its "
            "evapotranspiration: reference ET times the crop coefficient "
            "for its growth stage, minus effective rainfall, equals the "
            "net irrigation requirement. Duty expresses the inverse: the "
            "area one unit of flow can irrigate. Water is lost at every "
            "step - conveyance seepage in canals, evaporation, deep "
            "percolation below the root zone, runoff at the field's end - "
            "so gross requirement equals net divided by the overall "
            "efficiency: 0.35-0.5 for old flood systems, 0.7-0.9 for "
            "drip. Scheduling answers 'when and how much': refill the "
            "root zone when depletion reaches the management-allowed "
            "level, applying just enough to return to field capacity. "
            "Salinity is the shadow over it all: irrigation water leaves "
            "its salts behind as crops drink, so a leaching fraction - "
            "extra water to flush salts below the roots - is part of "
            "every sound design in arid lands. Modern precision "
            "irrigation closes the loop with soil-moisture sensors and "
            "weather-based ET controllers."
        ),
        "how_it_works": (
            "Irrigation design works down the delivery chain. Compute net "
            "crop requirement from ET and effective rain for each growth "
            "stage; divide by field, conveyance, and project efficiencies "
            "for the gross diversion; size canals or pipes for the peak-"
            "month flow with Manning's equation. At the field, choose the "
            "method to fit soil, crop, and water cost: level basins for "
            "flat heavy soils, furrows for row crops, sprinklers for "
            "undulating land, drip for orchards and water scarcity. "
            "Scheduling runs the soil-water budget daily: depletion "
            "accumulates with ET and drains with rain or irrigation, and "
            "the irrigation event fires at the management-allowed "
            "depletion. Drainage design handles the excess: subsurface "
            "tile drains hold the water table below the root zone and "
            "carry leached salts away. Basin-scale management then "
            "allocates the river among projects by water rights, rotating "
            "deliveries in shortage - the warabandi-style turns that have "
            "governed irrigated civilizations for millennia."
        ),
        "key_points": [
            "Irrigation is ~70% of global freshwater withdrawals; net requirement = crop ET minus effective rainfall.",
            "Gross diversion = net / overall efficiency: 0.35-0.5 flood systems, 0.7-0.9 drip.",
            "Scheduling refills the root zone at management-allowed depletion - the soil-water budget run daily.",
            "Salinity demands a leaching fraction: extra water flushing salts below the roots in arid lands.",
            "Method follows conditions: basins, furrows, sprinklers, drip - matched to soil, crop, topography, water cost.",
        ],
        "requirements": [
            "Reference ET and crop coefficients by growth stage; effective rainfall estimates.",
            "System efficiencies (field, conveyance) honestly measured, not catalog-quoted.",
            "Water-quality analysis for salinity and sodicity hazards.",
        ],
        "standards": [
            "Report requirements in mm per growth stage and m3/ha; state efficiencies used.",
            "Design drainage for the leaching fraction - irrigation without drainage salinizes.",
        ],
        "citations": [CIT_MAIDMENT, CIT_DINGMAN],
        "sig_lens": (
            "Signature edition: his Signature field-watering - every "
            "crop's thirst computed, every drop delivered on schedule."
        ),
        "demo_kind": "irrigation",
    },
    {
        "key": "groundwater_modeling",
        "name": "Groundwater Modeling: The MODFLOW Approach",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Groundwater models turn Darcy's law and mass conservation "
            "into maps of the future: where will the water table be in "
            "ten years at this pumping rate, where will the plume go, "
            "which wells will interfere? MODFLOW, the US Geological "
            "Survey's finite-difference code released in 1984 and the "
            "world's most used groundwater model, discretizes the aquifer "
            "into a grid of cells, writes the flow equation for each "
            "cell - inflow minus outflow equals storage change - and "
            "solves the resulting system for heads everywhere. Boundary "
            "conditions are the model's contract with reality: specified "
            "head (a connected river or lake), specified flux (recharge, "
            "pumping wells), and head-dependent flux (a stream that "
            "gains or loses depending on the head difference). "
            "Calibration adjusts hydraulic conductivity, storage, and "
            "recharge until simulated heads and fluxes match observation "
            "wells and stream gains - the non-uniqueness of this fit is "
            "the model's central humility: many parameter sets fit the "
            "past, and they diverge in the future. Particle tracking "
            "(MODPATH) then traces flow paths and travel times for "
            "capture-zone delineation and plume forecasting."
        ),
        "how_it_works": (
            "Modeling works in a disciplined sequence. Build the "
            "conceptual model first: hydrostratigraphy, recharge zones, "
            "boundaries, the question the model must answer - a model "
            "without a question is a toy. Discretize: grid resolution "
            "fine enough to represent wells, streams, and gradients "
            "(telescoping grids refine near features). Assign parameters "
            "by zone from tests and geology. Calibrate to steady-state "
            "then transient targets - heads, fluxes, and their trends - "
            "adjusting parameters within plausible ranges, and quantify "
            "the misfit. Validate against data withheld from calibration. "
            "Then run scenarios: new well fields, climate recharge "
            "changes, remediation designs - and report the uncertainty, "
            "because decision-makers deserve the cone of possibilities, "
            "not a single line. Capture zones from reverse particle "
            "tracking define wellhead protection areas; forward tracking "
            "forecasts plume arrival at receptors. A model is never "
            "'validated' once and for all - it is a living hypothesis "
            "updated as new heads arrive."
        ),
        "key_points": [
            "MODFLOW discretizes aquifers into cells and solves the flow equation for heads everywhere (USGS, 1984).",
            "Boundary conditions are the contract with reality: specified head, specified flux, head-dependent (streams).",
            "Calibration matches heads and fluxes - but many parameter sets fit the past and diverge in the future (non-uniqueness).",
            "Particle tracking (MODPATH) maps capture zones for wellhead protection and plume paths to receptors.",
            "Report uncertainty as a cone of scenarios; a model is a living hypothesis, updated with new data.",
        ],
        "requirements": [
            "Conceptual model: hydrostratigraphy, recharge, boundaries, and the decision the model serves.",
            "Calibration targets: observation-well hydrographs and stream gain/loss measurements.",
            "Parameter ranges from tests and geology - calibration must stay inside plausibility.",
        ],
        "standards": [
            "Document the conceptual model, discretization, boundaries, calibration misfit, and limitations with every model.",
            "Archive model files and inputs so results are reproducible and auditable.",
        ],
        "citations": [CIT_FREEZE, CIT_FETTER],
        "sig_lens": (
            "Signature edition: his Signature aquifer simulator - the "
            "whole underground gridded, solved, and stamped."
        ),
        "demo_kind": "gw_model",
    },
    {
        "key": "karst_hydrology",
        "name": "Karst Hydrology",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Karst is hydrology with the rulebook torn up: in soluble "
            "rock - limestone, dolomite, gypsum - slightly acidic water "
            "dissolves conduits, caves, and sinkholes, creating "
            "underground drainage systems that behave more like surface "
            "rivers than aquifers. A quarter of the world's population "
            "depends partly on karst water. Flow is triple-porosity: "
            "slow seepage through the rock matrix, faster flow through "
            "fractures, and turbulent pipe flow through conduits that "
            "can carry storm pulses for kilometers in hours. Springs are "
            "the outlets, and their hydrographs are karst's signature: "
            "flashy multi-peak responses with distinct recession "
            "components as conduits drain first and the matrix later. "
            "Dye tracing maps the hidden plumbing - injected fluorescein "
            "reappearing at a spring kilometers away proves the "
            "connection, and travel times reveal conduit velocities. The "
            "dark side is vulnerability: contaminants enter through "
            "sinkholes with zero filtration and arrive at springs in "
            "hours, and sinkhole collapse swallows roads and buildings "
            "where cover collapses into voids. Karst demands its own "
            "methods because Darcy's law, calibrated for porous media, "
            "simply does not apply inside a cave stream."
        ),
        "how_it_works": (
            "Karst hydrology works by tracing and listening. Dye-trace "
            "studies inject fluorescent dyes at sinkholes and monitor "
            "springs with field fluorometers or charcoal receptors, "
            "mapping conduit connections and velocities. Spring "
            "hydrograph analysis decomposes recessions into quick-flow "
            "(conduit) and slow-flow (matrix/fracture) components, "
            "quantifying the system's dual personality. Water-level "
            "monitoring in wells distinguishes conduit-dominated wells "
            "(flashy, storm-responsive) from matrix wells (damped). "
            "Geophysics (electrical resistivity, ground-penetrating "
            "radar) and cave mapping fill the geometry. Vulnerability "
            "mapping combines travel time, dilution, and land use to "
            "zone protection: the most sensitive areas get the strictest "
            "controls, because in karst there is no second chance - "
            "what enters a sinkhole reaches the spring. Engineering in "
            "karst means probing every foundation, grouting voids, and "
            "designing drainage that never concentrates water where "
            "collapse would be catastrophic."
        ),
        "key_points": [
            "Karst: soluble rock dissolved into conduits, caves, sinkholes - underground rivers, not porous aquifers; ~1/4 of humanity uses karst water.",
            "Triple porosity: matrix seepage, fracture flow, turbulent conduit flow carrying storm pulses for km in hours.",
            "Dye tracing proves connections and measures conduit velocities; spring recessions decompose into quick and slow components.",
            "Extreme vulnerability: sinkhole inputs reach springs unfiltered in hours - protection zoning is by travel time.",
            "Darcy's law fails inside conduits; karst needs its own methods, and engineering must probe every foundation.",
        ],
        "requirements": [
            "Dye-trace program: injection points, spring monitoring network, fluorometers or receptors.",
            "Spring hydrographs through storms for recession decomposition.",
            "Geologic mapping of soluble units, sinkholes, and structural controls.",
        ],
        "standards": [
            "Report dye-trace results as proven connections with travel times and recovery rates, not assumed flow paths.",
            "Zone karst protection by vulnerability (travel time + attenuation), with the strictest controls nearest inputs.",
        ],
        "citations": [CIT_FETTER, CIT_FREEZE],
        "sig_lens": (
            "Signature edition: his Signature cave-water atlas - every "
            "conduit traced, every spring's plumbing proven in dye."
        ),
        "demo_kind": "karst",
    },
    {
        "key": "tracer_isotope_hydrology",
        "name": "Tracer Hydrology and Isotopes",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Tracer hydrology reads water's hidden biography from the "
            "signatures it carries. Stable isotopes of water - oxygen-18 "
            "and deuterium - fractionate with every phase change: heavy "
            "isotopes prefer the liquid, so rain gets progressively "
            "lighter inland, uphill, and poleward, and each storm leaves "
            "a fingerprint. Reported as delta values (per mil deviation "
            "from ocean water), isotopes identify a water sample's "
            "origin: high-elevation recharge plots lighter than valley "
            "rain, evaporated lake water plots off the meteoric water "
            "line. Mixing models unmix the blends: a stream at baseflow "
            "is groundwater plus recent rain, and two isotopes solve the "
            "two-component split. Age tracers date the water: tritium "
            "(bomb-peak, 1960s), CFCs and SF6 (atmospheric histories), "
            "carbon-14 (millennia), noble gases (recharge temperature). "
            "Mean transit time - how long water spends in a catchment - "
            "is the master variable linking hydrology to water quality: "
            "young water carries this year's fertilizer, old water "
            "carries the legacy of decades past. Artificial tracers "
            "(dyes, salts, DNA-tagged particles) are injected "
            "deliberately to clock flow paths and prove connections."
        ),
        "how_it_works": (
            "Isotope hydrology works by comparison against standards. "
            "Sample rain, snow, streams, wells, and springs through "
            "seasons; analyze delta-18O and delta-2H by laser "
            "spectroscopy or mass spectrometry; plot against the local "
            "meteoric water line. Deviations diagnose process: "
            "evaporation pulls samples below the line, high-elevation "
            "sources plot lighter. End-member mixing analysis solves "
            "the linear system - stream isotope equals the fraction-"
            "weighted sum of source isotopes - to split hydrographs "
            "into event water vs pre-event water (the classic result: "
            "stormflow is mostly old water pushed out, not the rain "
            "itself). Age dating matches measured tracer concentrations "
            "to atmospheric input histories through lumped-parameter "
            "models (piston flow, exponential mixing), yielding mean "
            "transit times. Young-water fractions from seasonal isotope "
            "cycles quantify vulnerability: catchments with high young-"
            "water fractions transmit this year's contamination fast."
        ),
        "key_points": [
            "delta-18O and delta-2H fingerprint water's origin: lighter inland, uphill, poleward; evaporation pulls samples off the meteoric water line.",
            "Mixing models split streamflow into sources - stormflow is mostly old pre-event water pushed out, not the rain itself.",
            "Age tracers (tritium, CFCs/SF6, carbon-14, noble gases) date groundwater from years to millennia.",
            "Mean transit time links hydrology to water quality: young water carries this year's fertilizer.",
            "Artificial tracers (dyes, salts) clock flow paths and prove connections on demand.",
        ],
        "requirements": [
            "Isotope analyses of precipitation (seasonal), streamflow (event), and groundwater (spatial).",
            "Local meteoric water line from at least a year of precipitation sampling.",
            "Atmospheric input histories for age tracers; lumped-parameter models for transit times.",
        ],
        "standards": [
            "Report deltas in per mil vs VSMOW with analytical precision.",
            "State mixing-model assumptions (end-members, conservativeness) - unmixing is only as good as the end-members.",
        ],
        "citations": [CIT_DINGMAN, CIT_BRUTSAERT],
        "sig_lens": (
            "Signature edition: his Signature water biography - every "
            "drop's origin, age, and journey read from its signature."
        ),
        "demo_kind": "isotopes",
    },
    {
        "key": "ecohydrology",
        "name": "Ecohydrology and Environmental Flows",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Ecohydrology is the two-way street between water and life: "
            "hydrology shapes ecosystems, and ecosystems shape hydrology. "
            "A river's flow regime - its magnitude, frequency, duration, "
            "timing, and rate of change - is the master variable of river "
            "ecology: floods cue fish spawning and rebuild floodplains, "
            "low flows concentrate predators and stress juveniles, the "
            "spring freshet scours algae and moves gravel. Riparian zones, "
            "the green ribbons along channels, run on shallow groundwater "
            "and flood pulses; their roots armor banks and their shade "
            "cools water. Environmental flows (e-flows) translate this "
            "science into water management: the quantity, timing, and "
            "quality of flows reserved for ecosystems, set by methods "
            "from the simple (Tennant's percentages of mean annual flow) "
            "to the holistic (building-block methods assembling "
            "ecologically critical flow components). Vegetation feeds "
            "back on hydrology at every scale: canopies intercept rain, "
            "roots open macropores, forests transpire whole rivers' "
            "worth of water - deforest the Amazon's flying rivers and "
            "downwind rainfall falters. Wetland hydroperiods, vernal "
            "pools, and desert waterholes are all ecohydrologic systems "
            "where getting the water timing wrong collapses the ecology."
        ),
        "how_it_works": (
            "Ecohydrology works by linking flow statistics to ecological "
            "response. Characterize the natural flow regime with Indicators "
            "of Hydrologic Alteration (magnitude, timing, duration, "
            "frequency, rate of change across 30+ metrics), then relate "
            "ecological data - fish assemblages, invertebrate indices, "
            "riparian vegetation - to the altered metrics. E-flow "
            "assessment convenes the science into flow recommendations: "
            "baseflows for habitat, small floods for channel maintenance, "
            "large floods for floodplain connection, each with magnitude, "
            "duration, timing, and frequency. Implementation writes them "
            "into reservoir operating rules and water rights as protected "
            "flows. Monitoring closes the loop: did the managed flood "
            "recruit cottonwoods, did the baseflow sustain the fishery? "
            "The vegetation feedback is modeled through coupled "
            "soil-plant-atmosphere schemes where rooting depth, stomatal "
            "control, and interception set the actual ET that closes the "
            "catchment water budget."
        ),
        "key_points": [
            "The flow regime (magnitude, frequency, duration, timing, rate of change) is the master variable of river ecology.",
            "Environmental flows reserve ecologically critical flows: baseflows, channel-maintenance floods, floodplain-connection floods.",
            "Methods range from Tennant's % of mean annual flow to holistic building-block approaches.",
            "Vegetation feeds back: interception, macropores, transpiration - forests move rivers' worth of water to the sky.",
            "E-flows are written into reservoir rules and water rights, then monitored for ecological response.",
        ],
        "requirements": [
            "Naturalized flow series to characterize the unaltered regime (Indicators of Hydrologic Alteration).",
            "Ecological response data tied to flow metrics (fish, invertebrates, riparian vegetation).",
            "Stakeholder process: e-flows reallocate water, so the science must survive negotiation.",
        ],
        "standards": [
            "Report e-flow recommendations as full regimes (magnitude, timing, duration, frequency), not single minimum flows.",
            "Monitor ecological outcomes, not just flow compliance - the river is the judge.",
        ],
        "citations": [CIT_DUNNE, CIT_WARD],
        "sig_lens": (
            "Signature edition: his Signature living-river compact - "
            "every ecosystem's flow share reserved in Signature water."
        ),
        "demo_kind": "ecohydrology",
    },
    {
        "key": "flood_inundation_modeling",
        "name": "Flood Inundation Modeling",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Flood inundation modeling turns a discharge number into a "
            "map: which streets go under, how deep, how fast - the "
            "information evacuations and insurance are built on. The "
            "classic engine is one-dimensional step-backwater hydraulics "
            "(HEC-RAS and its kin): surveyed cross-sections, Manning's n "
            "values, and the energy equation marched upstream from a "
            "downstream control to compute the water-surface profile for "
            "the design flood. Two-dimensional models (shallow-water "
            "equations on a grid) take over where flow leaves the "
            "channel: across floodplains, through streets, around "
            "buildings - computing depth and velocity in every cell. "
            "Terrain is everything: airborne lidar elevation models at "
            "sub-meter resolution made modern flood mapping possible, "
            "and a bad DEM makes a bad map regardless of the hydraulics. "
            "Models are calibrated to historic high-water marks and "
            "validated against independent events; uncertainty comes "
            "from terrain, roughness, the hydrologic input, and "
            "structures (bridges, culverts, levees) that the model must "
            "represent. The products are regulatory floodplain maps "
            "(the 1%-annual-chance boundary), real-time forecast "
            "inundation from forecast hydrographs, and scenario maps for "
            "levee breaches and dam failures."
        ),
        "how_it_works": (
            "Inundation modeling works in a pipeline. Build the terrain: "
            "lidar DEM fused with channel bathymetry (lidar does not see "
            "under water). Build the mesh or cross-sections, assign "
            "roughness by land cover, and represent every bridge, "
            "culvert, weir, and levee - structures control urban "
            "flooding. Set boundaries: the design hydrograph upstream, "
            "normal depth or a stage hydrograph downstream. Run steady "
            "(peak flow) for regulatory maps or unsteady (full "
            "hydrograph) for real events. Calibrate Manning's n and "
            "structure coefficients until computed profiles match "
            "observed high-water marks within tolerance. Map depth and "
            "velocity grids, intersect with buildings and roads for "
            "exposure, and publish with the hydrologic basis stated. "
            "Forecast operations couple the hydraulic model to hydrologic "
            "forecasts: each new rainfall forecast re-runs the "
            "inundation, pushing updated depth maps to emergency "
            "managers. Levee-breach and dam-break scenarios use the "
            "same machinery with the structure removed - the maps no "
            "one wants to need."
        ),
        "key_points": [
            "Turns discharge into maps: 1D step-backwater (HEC-RAS) in channels, 2D shallow-water grids across floodplains.",
            "Terrain is everything: lidar DEMs plus channel bathymetry make or break the map.",
            "Structures (bridges, culverts, levees) control urban flooding and must be represented explicitly.",
            "Calibrate to historic high-water marks; validate against independent events.",
            "Products: regulatory 1% floodplain maps, real-time forecast inundation, breach and dam-failure scenarios.",
        ],
        "requirements": [
            "High-resolution terrain (lidar) fused with surveyed channel bathymetry.",
            "Structure data: bridge/culvert geometry, levee alignments and crest elevations.",
            "Calibration events with high-water marks; design or forecast hydrographs as input.",
        ],
        "standards": [
            "Report the hydrologic basis (return period, hydrograph) and terrain source/date on every map.",
            "Publish depth AND velocity - deep slow water and shallow fast water are different hazards.",
        ],
        "citations": [CIT_HENDERSON, CIT_CHOW],
        "sig_lens": (
            "Signature edition: his Signature flood atlas - every street's "
            "depth mapped before the water arrives."
        ),
        "demo_kind": "inundation",
    },
    {
        "key": "hydrologic_forecasting",
        "name": "Hydrologic Forecasting",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Hydrologic forecasting predicts river futures: the crest "
            "next Thursday, the spring runoff volume, whether the "
            "reservoir will fill. Short-range flood forecasting chains "
            "quantitative precipitation forecasts through rainfall-"
            "runoff models and channel routing, updating with real-time "
            "gauge data via data assimilation - the model's states "
            "(soil moisture, snowpack, channel storage) are nudged toward "
            "observations so the forecast starts from the truth. "
            "Ensemble forecasting runs the chain many times with "
            "perturbed weather inputs, producing probability distributions "
            "instead of single lines: a 30 percent chance of exceeding "
            "flood stage is actionable in a way a single deterministic "
            "crest is not. Seasonal water-supply forecasting leans on "
            "initial conditions - snowpack SWE, soil moisture, reservoir "
            "storage - plus climate signals like ENSO, using ensemble "
            "streamflow prediction (ESP): run the historical weather "
            "years through today's basin states and let the distribution "
            "of outcomes be the forecast. Forecast skill is scored "
            "ruthlessly against climatology and persistence; a forecast "
            "only earns its keep by beating 'tomorrow like today'. "
            "Communication is the final hydrology: probabilities, "
            "uncertainty cones, and plain-language impacts."
        ),
        "how_it_works": (
            "Forecasting works as a chained system. Ingest observations: "
            "precipitation, temperature, streamflow, snow, soil moisture, "
            "reservoir levels. Run the hydrologic model to the present "
            "with data assimilation (Kalman-style updating of states) so "
            "initial conditions match reality. Force the future with "
            "weather-model ensembles (days) or historical meteorology "
            "conditioned on climate forecasts (seasons). Route flows "
            "through the channel network with hydraulic or hydrologic "
            "routing. Post-process: bias-correct against past forecast "
            "errors, and verify with scores like the continuous ranked "
            "probability score. Disseminate as exceedance probabilities "
            "for flood stages and volume outlooks with uncertainty "
            "bands. Operations act on thresholds: forecast crest vs "
            "flood stage triggers warnings; volume outlook vs reservoir "
            "capacity triggers release decisions. The whole chain is "
            "re-run on schedule - typically every 6 hours for floods - "
            "because each new observation sharpens the next forecast."
        ),
        "key_points": [
            "Chains precipitation forecasts through rainfall-runoff models and routing, updated by data assimilation of real-time gauges.",
            "Ensembles produce probabilities (e.g., 30% chance of exceeding flood stage), not single lines.",
            "Seasonal outlooks (ESP) run historical weather years through today's basin states - initial conditions are the skill.",
            "Skill is scored against climatology and persistence; communication in plain impacts closes the loop.",
            "Flood chains re-run every ~6 hours; each new observation sharpens the next forecast.",
        ],
        "requirements": [
            "Real-time observation network (precip, streamflow, snow, soil moisture) with telemetry.",
            "Calibrated rainfall-runoff and routing models with data-assimilation updating.",
            "Ensemble weather inputs and a verification archive to prove skill.",
        ],
        "standards": [
            "Issue forecasts as probabilities with lead times; never imply more certainty than the ensemble holds.",
            "Verify every forecast product against observations and publish the skill scores.",
        ],
        "citations": [CIT_CHOW, CIT_MAIDMENT],
        "sig_lens": (
            "Signature edition: his Signature river futures desk - every "
            "crest called with honest odds, every outlook stamped."
        ),
        "demo_kind": "forecasting",
    },
    {
        "key": "frontiers_hydrology",
        "name": "Frontiers of Hydrology",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Hydrology's frontiers are being redrawn by new eyes and new "
            "questions. From orbit, GRACE gravimetry weighs changes in "
            "total water storage - watching aquifers deplete from space - "
            "and the SWOT mission maps river heights, widths, and slopes "
            "globally, bringing discharge estimates to rivers that never "
            "had a gauge. The PUB (Predictions in Ungauged Basins) "
            "decade taught the field to transfer knowledge: regionalize "
            "parameters from gauged to ungauged basins by similarity, so "
            "the world's ungauged majority gets science too. Hyper-"
            "resolution modeling pushes grids toward 100 meters globally, "
            "resolving the hillslopes the old models averaged away. "
            "Nonstationarity is the conceptual frontier: with climate "
            "change, urbanization, and regulation rewriting the rules, "
            "the stationarity assumption behind flood-frequency analysis "
            "and yield studies is retired in favor of time-varying "
            "distributions and scenario ensembles. Socio-hydrology "
            "closes the loop with people: reservoirs, irrigation, and "
            "policy co-evolve with the water cycle, and models now "
            "include the human as a dynamic component. Tracer-enabled, "
            "satellite-constrained, human-aware: the frontier is "
            "hydrology that sees the whole system at once."
        ),
        "how_it_works": (
            "Frontier hydrology works by fusing scales and disciplines. "
            "Satellite gravimetry (GRACE) gives monthly total-water-"
            "storage anomalies; subtracting modeled soil moisture and "
            "snow isolates groundwater change - depletion mapped from "
            "orbit, validated against well networks. SWOT's water-"
            "surface elevations and slopes feed Manning-based discharge "
            "algorithms for ungauged rivers. PUB regionalization groups "
            "basins by climate, geology, and land cover, transferring "
            "calibrated parameters with uncertainty bands. Hyper-"
            "resolution models run continental domains at hectometer "
            "grids on supercomputers, assimilating satellite soil "
            "moisture, snow, and evapotranspiration. Nonstationary "
            "frequency analysis lets distribution parameters trend with "
            "covariates (time, temperature, urbanization), so design "
            "floods evolve with the world. Socio-hydrologic models couple "
            "reservoir operating rules and farmer decisions to the water "
            "cycle, simulating the feedbacks that make the Anthropocene "
            "water cycle a coupled human-natural system."
        ),
        "key_points": [
            "GRACE weighs aquifer depletion from orbit; SWOT maps river heights and slopes globally for ungauged rivers.",
            "PUB regionalization transfers parameters from gauged to ungauged basins by similarity.",
            "Hyper-resolution modeling pushes toward 100-m global grids, resolving hillslopes.",
            "Nonstationarity retires the old assumption: design floods and yields now evolve with climate and land use.",
            "Socio-hydrology couples human decisions (reservoirs, irrigation, policy) into the water cycle itself.",
        ],
        "requirements": [
            "Satellite data literacy: gravimetry, altimetry, soil-moisture and ET products with their error bars.",
            "High-performance computing for hyper-resolution domains; data-assimilation frameworks.",
            "Humility about uncertainty: frontier products carry wide, honestly reported bands.",
        ],
        "standards": [
            "Validate satellite-derived hydrology against ground networks before operational use.",
            "Report nonstationary analyses with the covariates and scenarios - the future assumed must be explicit.",
        ],
        "citations": [CIT_BRUTSAERT, CIT_MAIDMENT],
        "sig_lens": (
            "Signature edition: his Signature whole-system hydrology - "
            "weighed from orbit, modeled to the hillslope, stamped for "
            "the century ahead."
        ),
        "demo_kind": "frontiers",
    },
]
