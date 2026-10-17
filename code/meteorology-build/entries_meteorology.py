#!/usr/bin/env python3
"""Seed entries for the Meteorology field build (field #15, taxonomy order).

Verified 2026-10-17: NO database covers meteorology as a discipline.
- 'weather-climate' (10,000 records): raw station observations (timestamped
  synthetic readings) - observations only, no science.
- 'weather' (38 records): thin stubs - 'Weather Forecasting (overview)',
  'Cold Fronts (examples)', 'Hurricanes (detailed)', 'The Barometer (faq)'
  style cards, not full discipline records.
- 'weather-control' (150 records): Signature fun/futures 'weather control'
  creations - speculative, not the discipline.
- 'climatology' (34 records, field #12): long-term climate - energy balance,
  forcings, ice ages, climate models. Covers 'Jet Streams' as a climate
  feature, not as a forecasting tool.
- 'atmospheric-science' (36 records, field #13): physics and chemistry of
  the atmosphere - hydrostatic balance, lapse rates, cloud physics, CAPE,
  lightning electrification, radiative transfer. Touches radar, satellites,
  NWP, and tropical cyclones as physical systems, not as forecaster
  practice: no synoptic chart analysis, no sounding interpretation as a
  daily tool, no radar/satellite image interpretation, no forecast methods,
  no verification, no warnings process, no aviation/marine/mountain/fire/
  agricultural meteorology, no tornadoes or winter-storm forecasting.

So this build creates two NEW databases:

  meteorology             - The Meteorology Database
                            (public-harvest: real, fact-checked
                            meteorology)
  meteorology-signature   - The Meteorology Signature Database
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

CIT_WALLACE = ("Wallace, J. M. & Hobbs, P. V. (2006). 'Atmospheric Science: "
               "An Introductory Survey', 2nd ed. Academic Press.")
CIT_AHRENS = ("Ahrens, C. D. (2012). 'Meteorology Today', 10th ed. "
              "Brooks/Cole.")
CIT_BLUESTEIN = ("Bluestein, H. B. (1993). 'Synoptic-Dynamic Meteorology in "
                 "Midlatitudes', Vols. 1-2. Oxford University Press.")
CIT_HOLTON = ("Holton, J. R. (2004). 'An Introduction to Dynamic "
              "Meteorology', 4th ed. Academic Press.")
CIT_MARKOWSKI = ("Markowski, P. & Richardson, Y. (2010). 'Mesoscale "
                 "Meteorology in Midlatitudes'. Wiley.")
CIT_DOVIAK = ("Doviak, R. J. & Zrnic, D. S. (2006). 'Doppler Radar and "
              "Weather Observations', 2nd ed. Dover.")
CIT_KIDDER = ("Kidder, S. Q. & Vonder Haar, T. H. (1995). 'Satellite "
              "Meteorology: An Introduction'. Academic Press.")
CIT_KALNAY = ("Kalnay, E. (2003). 'Atmospheric Modeling, Data Assimilation "
              "and Predictability'. Cambridge University Press.")
CIT_WILKS = ("Wilks, D. S. (2011). 'Statistical Methods in the Atmospheric "
             "Sciences', 3rd ed. Academic Press.")
CIT_BARRY = ("Barry, R. G. & Chorley, R. J. (2009). 'Atmosphere, Weather and "
             "Climate', 9th ed. Routledge.")
CIT_LUTGENS = ("Lutgens, F. K. & Tarbuck, E. J. (2016). 'The Atmosphere: An "
               "Introduction to Meteorology', 13th ed. Pearson.")
CIT_VASQUEZ = ("Vasquez, T. (2013). 'Weather Analysis and Forecasting "
               "Handbook', 2nd ed. Weather Graphics Technologies.")
CIT_DOSWELL = ("Doswell, C. A. (ed.) (2001). 'Severe Convective Storms'. "
               "American Meteorological Society.")
CIT_EMANUEL = ("Emanuel, K. (2005). 'Divine Wind: The History and Science of "
               "Hurricanes'. Oxford University Press.")
CIT_STULL = ("Stull, R. B. (1988). 'An Introduction to Boundary Layer "
             "Meteorology'. Kluwer.")
CIT_WMO = ("World Meteorological Organization. 'International "
           "Meteorological Vocabulary' (WMO-No. 182).")

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "meteorology, clearly labeled Signature-made, never presented as "
            "authentic public record.")

ENTRIES = [
    # ================= FOUNDATIONS =================
    {
        "key": "what_is_meteorology",
        "name": "What Meteorology Is",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Meteorology is the science and practice of understanding the "
            "atmosphere and predicting its weather - what the air is doing "
            "now, why it is doing it, and what it will do next. It sits "
            "between atmospheric science, which studies the physics and "
            "chemistry of the air, and climatology, which studies the "
            "long-term statistics of the climate system: meteorology is "
            "the applied discipline that turns observation and theory into "
            "forecasts people can act on. Its branches cover every scale. "
            "Synoptic meteorology reads the big picture from weather maps "
            "spanning continents. Mesoscale meteorology handles storms, "
            "fronts, sea breezes, and lake-effect snow on the scale of "
            "tens to hundreds of kilometers. Microscale meteorology studies "
            "turbulence and fog in the lowest meters of air. Applied "
            "branches serve aviation, the sea, agriculture, fire management, "
            "and air quality. The forecaster's loop never changes: observe, "
            "analyze, diagnose the processes at work, predict, and then "
            "verify the forecast against what actually happened so the "
            "next one is better."
        ),
        "how_it_works": (
            "Meteorology works as a cycle. Observation networks - surface "
            "stations, weather balloons, radar, satellites, aircraft, buoys, "
            "and ships - measure the atmosphere's current state: temperature, "
            "pressure, humidity, wind, and precipitation. Analysis turns "
            "millions of scattered reports into coherent maps: isobars, "
            "fronts, jet streams, and upper-air height fields that reveal "
            "the atmosphere's structure. Diagnosis applies physical "
            "reasoning - air-mass contrasts, vorticity, instability, "
            "moisture transport - to explain why the weather is behaving "
            "as it is. Prediction blends forecaster judgment with "
            "numerical weather prediction models, ensembles, and "
            "statistical guidance to project the state forward in time. "
            "Verification scores the forecast against observations, and "
            "communication turns the result into watches, warnings, and "
            "plain-language forecasts. Every branch of the discipline is "
            "this same loop tuned to its scale and its users."
        ),
        "key_points": [
            "Meteorology is the science and practice of understanding the atmosphere and forecasting its weather - observation turned into actionable prediction.",
            "It sits between atmospheric science (the physics of air) and climatology (long-term climate statistics) as the applied forecasting discipline.",
            "Scales: synoptic (continental weather maps), mesoscale (storms, fronts, lake-effect snow), microscale (turbulence, fog).",
            "Applied branches serve aviation, marine operations, agriculture, fire management, air quality, and energy.",
            "The forecaster's loop: observe, analyze, diagnose, predict, verify, communicate - then repeat better.",
        ],
        "requirements": [
            "Comfort with maps as the primary language: isobars, fronts, and height contours.",
            "Basic algebra and unit fluency: hectopascals, knots, degrees, millimeters of rain.",
            "A habit of asking 'what is the air doing, why, and what happens next?'",
        ],
        "standards": [
            "SI units with operational conventions: pressure in hectopascals, wind in knots or meters per second, temperature in Celsius.",
            "World Meteorological Organization standards govern observation codes, station networks, and data exchange worldwide.",
        ],
        "citations": [CIT_AHRENS, CIT_WALLACE],
        "sig_lens": ("Signature edition: the sky reframed as his great "
                     "weather engine, every forecast a Signature readout of "
                     "the atmosphere's mood."),
        "demo_kind": "meteo_branches",
    },
    {
        "key": "weather_instruments",
        "name": "Observing the Sky: Weather Instruments and the Observer's Toolkit",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Every forecast begins with measurement, and measurement begins "
            "with instruments. The thermometer reports air temperature, "
            "housed in a ventilated shelter so the sun never cooks the "
            "reading. The barometer reports atmospheric pressure - mercury, "
            "aneroid, or digital - and pressure is the single most powerful "
            "diagnostic of coming weather. The hygrometer reports humidity: "
            "the dew point, the temperature at which the air saturates, is "
            "the number forecasters watch most. The anemometer measures "
            "wind speed and the wind vane its direction. The rain gauge "
            "catches precipitation; the snow board and ruler measure "
            "snowfall. The ceilometer finds cloud-base height with a laser; "
            "the present-weather sensor tells rain from snow from fog. Each "
            "instrument has siting rules - thermometers 1.25 to 2 meters "
            "over natural ground, rain gauges away from buildings and "
            "trees, anemometers 10 meters up in open exposure - because a "
            "badly sited instrument reports its own microclimate instead of "
            "the weather."
        ),
        "how_it_works": (
            "Instruments convert the atmosphere's state into numbers a "
            "forecaster can trust. A liquid-in-glass or electronic "
            "thermometer equilibrates with the air inside a louvered "
            "Stevenson screen; the daily maximum and minimum are reset "
            "each day. A barometer senses the weight of the air column - "
            "an aneroid cell flexes with pressure changes, a digital "
            "sensor measures capacitance - and the station pressure is "
            "reduced to sea level so stations at different elevations can "
            "be compared on one map. A hygrometer measures the vapor "
            "content directly or derives it from wet-bulb depression; the "
            "dew point follows from temperature and relative humidity. A "
            "cup or sonic anemometer samples the wind; direction is the "
            "compass point the wind comes FROM. A tipping-bucket rain gauge "
            "counts 0.2-millimeter tips of its little seesaw buckets. The "
            "ceilometer times a laser pulse's round trip to the cloud base. "
            "All of it is calibrated, sited to WMO exposure rules, and "
            "quality-controlled before it ever reaches a weather map."
        ),
        "key_points": [
            "Forecasts begin with instruments: thermometer, barometer, hygrometer, anemometer and vane, rain gauge, ceilometer, present-weather sensor.",
            "The dew point is the humidity number forecasters watch most - it sets fog, frost, and storm fuel.",
            "Station pressure is reduced to sea-level pressure so stations at different elevations share one map.",
            "Siting rules (thermometer 1.25-2 m over grass, anemometer 10 m in the open) keep instruments reporting the weather, not their own microclimate.",
            "Calibration and quality control happen before any reading reaches a forecast.",
        ],
        "requirements": [
            "Unit conversions: Celsius/Fahrenheit, hectopascals/inches of mercury, knots/mph/m/s.",
            "Knowing which instrument measures which variable and its standard exposure.",
            "Reading a thermometer shelter, not the sun-baked wall beside it.",
        ],
        "standards": [
            "WMO exposure and siting standards for meteorological instruments.",
            "SI units with operational conventions: Celsius, hectopascals, meters per second or knots.",
        ],
        "citations": [CIT_AHRENS, CIT_WMO],
        "sig_lens": ("Signature edition: every instrument a Signature sense "
                     "organ, the station a living creature feeling the sky."),
        "demo_kind": "unit_conversions",
    },
    {
        "key": "observing_network",
        "name": "The Observing Network: ASOS, Radiosondes, and the Global System",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "One station is a anecdote; ten thousand stations are the "
            "atmosphere. The surface network anchors everything: automated "
            "stations such as the US ASOS and AWOS units report temperature, "
            "dew point, wind, pressure, visibility, sky cover, and present "
            "weather every minute at airports and key sites, while staffed "
            "and volunteer cooperative observers extend coverage into rural "
            "areas with daily readings stretching back over a century. "
            "Above the surface, radiosondes - instrument packages carried "
            "by weather balloons - profile temperature, humidity, pressure, "
            "and wind from the ground to the stratosphere twice a day from "
            "roughly 900 stations worldwide, at 00 and 12 UTC. Aircraft "
            "report winds and temperatures along flight routes. Buoys and "
            "ships cover the oceans. Satellites and radar fill the gaps "
            "between. All of it flows into telecommunications networks and "
            "data assimilation systems within minutes to hours, becoming "
            "the initial conditions every forecast model starts from."
        ),
        "how_it_works": (
            "The network works by standardization and speed. Every surface "
            "station encodes its report in METAR, the international "
            "aviation observation code, so a forecaster in Tokyo reads a "
            "Denver report without translation. Radiosondes transmit their "
            "profiles by radio as the balloon rises about 5 meters per "
            "second, bursting near 30 kilometers; the TEMP code carries "
            "mandatory and significant levels. Automated stations sample "
            "continuously and report at fixed intervals, with algorithms "
            "detecting precipitation type, obstructions to vision, and "
            "cloud layers. Quality control flags impossible values and "
            "suspect jumps. Then data assimilation blends the fresh "
            "observations with the model's short forecast - the background "
            "- to produce the analysis: the best possible estimate of the "
            "atmosphere's current state on the model grid. The denser and "
            "fresher the observations, the less the model has to guess."
        ),
        "key_points": [
            "The surface network (ASOS/AWOS, cooperative observers) anchors forecasting; radiosondes profile the full column twice daily at 00 and 12 UTC.",
            "Aircraft, buoys, ships, satellites, and radar fill the gaps between fixed stations.",
            "METAR and TEMP codes standardize reports so every nation reads every other nation's weather.",
            "Quality control and data assimilation blend observations with model background into the analysis.",
            "Observations become model initial conditions - the forecast can only be as good as its starting picture.",
        ],
        "requirements": [
            "Knowing the major platforms: surface, upper-air, aircraft, marine, satellite, radar.",
            "Reading a METAR's basic fields: wind, visibility, sky, temperature/dew point, altimeter.",
            "Understanding that observation density and timeliness limit forecast skill.",
        ],
        "standards": [
            "WMO codes: METAR/SPECI for surface, TEMP for upper-air soundings.",
            "Synoptic observation hours at 00 and 12 UTC for the global radiosonde network.",
        ],
        "citations": [CIT_WALLACE, CIT_WMO],
        "sig_lens": ("Signature edition: the planet wired with Signature "
                     "nerves, every station a pulse point on the living map."),
        "demo_kind": "network_coverage",
    },
    {
        "key": "surface_analysis",
        "name": "Reading a Weather Map: The Surface Analysis",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The surface analysis is meteorology's master picture: a map of "
            "sea-level pressure drawn as isobars - lines of equal pressure, "
            "usually every 4 hectopascals - with highs, lows, fronts, troughs, "
            "and ridges marked in the standard symbols every forecaster on "
            "Earth recognizes. Blue triangles for cold fronts, red semicircles "
            "for warm fronts, alternating purple for occluded fronts, and the "
            "big blue H and red L for the pressure centers. Around each "
            "station sits the station model: temperature upper left, dew "
            "point lower left, sea-level pressure upper right, pressure "
            "change lower right, wind as a shaft with feathers, sky cover as "
            "the center circle's fill, present weather symbols beside it. "
            "Reading the map means reading the wind - air flows nearly "
            "parallel to the isobars, counterclockwise around lows and "
            "clockwise around highs in the Northern Hemisphere - and reading "
            "the pressure pattern for where air rises, where it sinks, and "
            "where the weather will be."
        ),
        "how_it_works": (
            "Analysts build the map from thousands of sea-level pressure "
            "reports. Isobars are interpolated between stations, smoothed "
            "enough to show the real pattern but not every station's noise; "
            "a 4-hectopascal interval is standard, tighter over active "
            "regions. Fronts are drawn where the analysis shows the classic "
            "signatures: a sharp temperature and dew-point contrast, a wind "
            "shift, a pressure trough, and a band of clouds or "
            "precipitation. Highs get the H where anticyclonic outflow and "
            "subsidence promise fair skies; lows get the L where "
            "convergence and lift promise clouds and rain. Troughs - "
            "elongated low-pressure axes - and ridges - elongated high axes "
            "- are drawn as dashed and solid lines. The station model packs "
            "a dozen numbers around each station so the map stays readable "
            "at continental scale. Modern analyses are computer-drawn from "
            "the same assimilation systems that start forecast models, with "
            "human analysts adding the fronts and mesoscale detail the "
            "algorithms still miss."
        ),
        "key_points": [
            "Isobars (usually 4 hPa) plus H/L centers, fronts, troughs, and ridges make the master surface picture.",
            "Standard frontal symbols: blue triangles (cold), red semicircles (warm), alternating purple (occluded).",
            "The station model packs temperature, dew point, pressure, pressure change, wind, sky, and weather around each plot.",
            "Wind flows nearly parallel to isobars - counterclockwise around Northern Hemisphere lows, clockwise around highs.",
            "Fronts are placed where temperature contrast, wind shift, pressure trough, and precipitation band agree.",
        ],
        "requirements": [
            "Decoding a full station model at a glance.",
            "Tracing isobars and judging gradient strength from their spacing.",
            "Recognizing frontal signatures in raw station data, not just drawn lines.",
        ],
        "standards": [
            "WMO standard symbols for fronts, pressure systems, troughs, and ridges.",
            "Sea-level pressure analysis with 4-hectopascal isobar interval as the synoptic standard.",
        ],
        "citations": [CIT_VASQUEZ, CIT_AHRENS],
        "sig_lens": ("Signature edition: the surface map as his Signature "
                     "chessboard, every front a move in the atmosphere's game."),
        "demo_kind": "station_model",
    },
    {
        "key": "air_masses",
        "name": "Air Masses in Practice: Source Regions and Modification",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "An air mass is a huge body of air - often a thousand kilometers "
            "across - that has sat long enough over one region to take on "
            "that region's temperature and humidity as its own uniform "
            "character. Meteorologists classify them by source: cP for "
            "continental polar (cold, dry air from northern land), mP for "
            "maritime polar (cool, moist air from northern oceans), cT for "
            "continental tropical (hot, dry air from desert land), mT for "
            "maritime tropical (warm, humid air from tropical oceans), cA "
            "for continental arctic, and mE for maritime equatorial. In "
            "practice the forecaster watches air masses move and change: a "
            "cP outbreak diving south brings the year's hardest freeze; an "
            "mT surge from the Gulf streams moisture that fuels "
            "thunderstorms; a cT dome over the desert Southwest bakes into "
            "a heat wave. Air masses modify as they travel - cP air crossing "
            "the relatively warm Great Lakes in winter picks up heat and "
            "moisture and dumps lake-effect snow - so the forecaster tracks "
            "not just the label but the trajectory and the transformation."
        ),
        "how_it_works": (
            "Air masses form in source regions where the air stagnates: "
            "the Siberian and Canadian arctic for cP and cA, the subtropical "
            "oceans for mT, the Sahara and the desert Southwest for cT. "
            "While parked, the air equilibrates with the surface below, "
            "gaining uniform temperature and moisture through its depth. "
            "When the upper flow dislodges it, the mass advects downstream "
            "largely intact, and its leading edge becomes a front. "
            "Modification works through surface fluxes: cold air over warm "
            "water gains heat and moisture from below, destabilizing into "
            "cumuliform clouds and snow bands; warm air over cold ground "
            "loses heat from below, stabilizing into stratus and fog. "
            "Forecasters track air masses on trajectory maps and water-vapor "
            "satellite imagery, watching the dew-point field - the true "
            "fingerprint of an air mass - to time the arrival of freezes, "
            "heat, humidity surges, and the storm fuel each one carries."
        ),
        "key_points": [
            "Air masses take their source region's character: cP cold/dry, mP cool/moist, cT hot/dry, mT warm/humid, cA bitter, mE sultry.",
            "Source regions are stagnant zones - arctic land, subtropical oceans, deserts - where air equilibrates with the surface.",
            "Air masses modify along their trajectory: cP over warm lakes becomes a snow machine; mT over cool land becomes fog and stratus.",
            "The dew-point field is the forecaster's fingerprint for tracking air-mass boundaries.",
            "Fronts are simply the leading edges of moving air masses.",
        ],
        "requirements": [
            "The six classic air-mass codes and what each implies for temperature and humidity.",
            "Reading dew-point and temperature advection on surface maps.",
            "Tracing 24-48 hour trajectories to anticipate modification.",
        ],
        "standards": [
            "Bergeron air-mass classification (cP, mP, cT, mT, cA, mE) as the international standard.",
            "Dew point in Celsius as the operational moisture variable.",
        ],
        "citations": [CIT_AHRENS, CIT_BARRY],
        "sig_lens": ("Signature edition: air masses as his Signature "
                     "provinces, each with its own climate passport."),
        "demo_kind": "airmass_classify",
    },
    {
        "key": "fronts_practice",
        "name": "Fronts in Practice: Cold, Warm, Occluded, and Stationary",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A front is the battle line between two air masses, and nearly "
            "all mid-latitude weather drama happens along one. The cold "
            "front is the aggressive one: dense cold air wedges under warm "
            "air, lifting it sharply, so the signature is a narrow band of "
            "towering clouds, gusty shifting winds, a sudden temperature "
            "drop, and often a squall line of thunderstorms - then clearing "
            "and cooler air behind. The warm front is the gradual one: warm "
            "air slides gently up over retreating cold air along a shallow "
            "slope, so the signature is a broad shield of stratiform clouds "
            "and steady rain arriving hours before the surface front, with "
            "warming and clearing behind. The occluded front forms when the "
            "fast cold front catches the warm front and lifts the warm "
            "sector entirely off the ground - the classic mature cyclone. "
            "The stationary front is the standoff: neither air mass "
            "advancing, a persistent rain band that can flood when it "
            "stalls for days. Forecasters read the frontal slope, the "
            "temperature contrast, and the wind shift to time each one's "
            "passage to the hour."
        ),
        "how_it_works": (
            "Fronts work through density contrast and forced lift. Cold "
            "air is denser, so at a cold front it undercuts the warm air "
            "like a wedge; the frontal surface slopes about 1:50 to 1:100, "
            "steep enough to fire vigorous updrafts along a narrow line. "
            "At a warm front the warm air overruns the cold along a gentle "
            "1:100 to 1:200 slope, so lift is broad and gentle - stratiform "
            "clouds, steady precipitation, the classic cloud sequence from "
            "cirrus to nimbostratus as the front approaches. Frontogenesis - "
            "the strengthening of the temperature gradient by converging "
            "winds - sharpens fronts; frontolysis weakens them. The "
            "Norwegian cyclone model strings them together: cold and warm "
            "fronts joined at the low center, the warm sector between, "
            "occlusion as the endgame. Forecasters locate fronts by "
            "converging evidence - temperature and dew-point discontinuity, "
            "wind shift, pressure trough, precipitation band - and a front "
            "is only drawn where at least several agree."
        ),
        "key_points": [
            "Cold fronts: steep wedge, narrow violent band, gusty shift, then clearing and cooler. Warm fronts: shallow overrun, broad steady rain, warming behind.",
            "Occluded fronts mark the mature cyclone - warm sector lifted entirely aloft. Stationary fronts stall and flood.",
            "Frontal slopes: roughly 1:50-1:100 for cold fronts, 1:100-1:200 for warm fronts.",
            "Frontogenesis (converging flow) sharpens fronts; frontolysis dissolves them.",
            "A front is drawn only where temperature contrast, wind shift, pressure trough, and precipitation band converge.",
        ],
        "requirements": [
            "The four frontal types, their symbols, slopes, and weather signatures.",
            "Reading temperature advection and wind shifts in station data.",
            "Timing frontal passage from the cloud and pressure sequence.",
        ],
        "standards": [
            "WMO frontal symbols: triangles (cold), semicircles (warm), alternating (occluded).",
            "The Norwegian cyclone model as the standard conceptual framework.",
        ],
        "citations": [CIT_BLUESTEIN, CIT_VASQUEZ],
        "sig_lens": ("Signature edition: fronts as his Signature battle "
                     "lines, each clash choreographed across the map."),
        "demo_kind": "frontal_slope",
    },
    {
        "key": "cyclone_norwegian",
        "name": "The Mid-Latitude Cyclone in Practice: The Norwegian Model",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The mid-latitude cyclone - the great rotating storm of the "
            "temperate zones, a thousand kilometers wide - is the engine "
            "of day-to-day weather across North America, Europe, and Asia. "
            "The Norwegian model, built by Bjerknes and colleagues a century "
            "ago, still describes its life in four acts. Birth: a wave "
            "forms on a stationary front, cold air pushing south on one "
            "side, warm air pushing north on the other. Growth: the wave "
            "amplifies, the pressure falls at the center, cold and warm "
            "fronts sharpen, and the warm sector's conveyor belt feeds "
            "moisture into a comma-shaped cloud shield. Maturity: the cold "
            "front catches the warm front, occlusion begins, and the "
            "strongest winds and heaviest precipitation wrap around the "
            "center. Death: fully occluded, cut off from its warm fuel, "
            "the low fills and drifts away. Forecasters time each act - "
            "cyclogenesis location, deepening rate, occlusion timing - "
            "because the cyclone's stage sets the weather for hundreds of "
            "kilometers around it."
        ),
        "how_it_works": (
            "Cyclones grow by converting the atmosphere's available "
            "potential energy - the north-south temperature contrast - "
            "into the kinetic energy of swirling wind. Baroclinic "
            "instability is the mechanism: a small wave on the polar front "
            "grows when warm air rises poleward and cold air sinks "
            "equatorward, lowering the system's center of gravity. Aloft, "
            "the jet stream's entrance and exit regions provide divergence "
            "that evacuates mass from the column, dropping surface "
            "pressure - this upper support is why some waves explode into "
            "'bombs' deepening 24 hectopascals in 24 hours while others "
            "fizzle. The warm conveyor belt streams warm moist air up and "
            "over the warm front, producing the broad precipitation "
            "shield; the cold conveyor belt wraps cold air around the "
            "low's north side; the dry slot of descending stratospheric "
            "air carves the comma head. Forecasters watch 500-millibar "
            "vorticity advection and jet-stream divergence to judge whether "
            "a wave will deepen, and they track the occlusion process to "
            "time the storm's peak and decay."
        ),
        "key_points": [
            "The Norwegian model: frontal wave, amplification, occlusion, decay - still the working framework after a century.",
            "Cyclones convert the north-south temperature contrast (available potential energy) into wind via baroclinic instability.",
            "Upper-level divergence from the jet stream evacuates mass and deepens the surface low; without it, waves fizzle.",
            "The warm conveyor belt feeds the comma cloud shield; the dry slot carves its head; the cold conveyor wraps the north side.",
            "'Bomb' cyclones deepen at least 24 hPa in 24 hours at 60 degrees latitude.",
        ],
        "requirements": [
            "The four life-cycle stages and their cloud/precipitation signatures.",
            "Linking 500-mb vorticity and jet divergence to surface deepening.",
            "Recognizing the comma cloud and dry slot on satellite imagery.",
        ],
        "standards": [
            "Bergeron-Sanders bomb criterion: 24 hPa/24 h at 60N (scaled by latitude).",
            "The Norwegian cyclone model as the standard conceptual framework.",
        ],
        "citations": [CIT_BLUESTEIN, CIT_WALLACE],
        "sig_lens": ("Signature edition: each cyclone a Signature vortex "
                     "engine, wound up by his temperature-contrast spring."),
        "demo_kind": "cyclone_stages",
    },
    {
        "key": "upper_air_charts",
        "name": "Upper-Air Charts: The 500-Millibar Map and Steering",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "If the surface map is the weather's face, the upper-air charts "
            "are its skeleton. Instead of pressure at a fixed height, "
            "upper-air maps show height at a fixed pressure: the 500-"
            "millibar chart plots the height of the 500-hPa surface - "
            "roughly 5.5 kilometers up, in the steering layer - as contours "
            "every 60 meters (decameters). Where the contours bunch, the "
            "wind screams; where they bow, the flow turns. Troughs aloft "
            "(southward dips) sit above surface storm development; ridges "
            "aloft (northward bulges) sit above surface fair weather. The "
            "850-millibar chart (~1.5 km) shows low-level temperature "
            "advection and moisture transport; the 700-millibar chart "
            "shows vertical motion; the 300/250-millibar chart shows the "
            "jet stream. Forecasters read the upper air first and the "
            "surface second, because the flow aloft steers everything "
            "below: surface lows travel with the 500-mb flow at roughly "
            "half its speed, and today's upper trough is tomorrow's "
            "surface storm."
        ),
        "how_it_works": (
            "Height contours on a constant-pressure chart play the same "
            "role isobars play at the surface: the geostrophic wind blows "
            "parallel to them with low heights to the left in the Northern "
            "Hemisphere, at a speed proportional to the gradient. Tightly "
            "packed 500-mb contours mark the jet stream and the storm "
            "track. Vorticity - the spin of the flow - is read from the "
            "curvature and shear: positive vorticity advection ahead of a "
            "trough forces air to rise, dropping surface pressure and "
            "spawning cyclones. Thickness - the vertical distance between "
            "two pressure surfaces, proportional to the layer's mean "
            "temperature - is contoured to find warm and cold air masses "
            "aloft. Forecasters overlay the 500-mb vorticity pattern on "
            "the surface map: where strong positive vorticity advection "
            "overruns a surface frontal wave, cyclogenesis is favored; "
            "where the flow is zonal and flat, the weather stays "
            "unremarkable. Steering is literal: the 500-mb wind field is "
            "the current that carries surface systems along."
        ),
        "key_points": [
            "Upper-air charts plot height of a pressure surface (500 mb ~ 5.5 km) contoured every 60 m; wind parallels the contours.",
            "Troughs aloft sit over surface storm development; ridges aloft over surface fair weather.",
            "850 mb shows low-level advection and moisture; 700 mb vertical motion; 300/250 mb the jet stream.",
            "Positive vorticity advection ahead of upper troughs forces rising motion and surface cyclogenesis.",
            "Surface systems are steered by the 500-mb flow at roughly half its speed.",
        ],
        "requirements": [
            "Reading height contours as wind: direction, speed from packing, trough/ridge identification.",
            "The 850/700/500/300 mb levels and what each diagnoses.",
            "Linking vorticity advection aloft to surface pressure falls.",
        ],
        "standards": [
            "Standard pressure levels: 850, 700, 500, 300/250, 200 hPa for synoptic analysis.",
            "Geostrophic wind as the reference balance for upper-air flow.",
        ],
        "citations": [CIT_BLUESTEIN, CIT_HOLTON],
        "sig_lens": ("Signature edition: the upper air as his Signature "
                     "scaffolding, invisible rails guiding every storm."),
        "demo_kind": "geostrophic_wind",
    },
    {
        "key": "jet_streams_practice",
        "name": "Jet Streams in Practice: Steering, Storm Tracks, and Turbulence",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The jet streams are rivers of air screaming eastward near the "
            "tropopause - the polar jet around 9 to 12 kilometers up with "
            "core speeds routinely past 100 knots and sometimes past 200, "
            "and the subtropical jet weaker and steadier. For the working "
            "forecaster the jet is three tools in one. First, a steering "
            "current: the fastest winds sit in the jet core, and the "
            "500-millibar flow beneath it carries surface storms along the "
            "storm track. Second, a storm maker: where the jet streaks - "
            "segments of maximum wind - the entrance region (air speeding "
            "up) and exit region (air slowing down) create divergence aloft, "
            "evacuating mass and deepening surface lows beneath the left-"
            "exit and right-entrance quadrants. Third, a hazard: the sharp "
            "wind shear on the jet's edges breeds clear-air turbulence that "
            "rattles airliners, and the jet's meanders - Rossby waves "
            "circling the hemisphere - decide whether a region gets zonal "
            "fast-moving weather or a stuck meridional pattern of blocking "
            "highs and cutoff lows. Forecasters plot the jet at 250/300 "
            "millibars every shift, because its position is the first draft "
            "of the week's weather."
        ),
        "how_it_works": (
            "Jet streams are thermal-wind creatures: the pole-to-equator "
            "temperature contrast means pressure falls faster with height "
            "in cold air than warm air, so the height gradient - and the "
            "wind it drives - strengthens with altitude, peaking at the "
            "tropopause where the contrast ends. Conservation of angular "
            "momentum and the meandering of Rossby waves then shape the "
            "jet into troughs and ridges. In a jet streak, air parcels "
            "accelerate into the core and decelerate out of it; the "
            "ageostrophic cross-stream circulation this demands produces "
            "divergence in the left-exit and right-entrance quadrants - "
            "the four-quadrant model every synoptic forecaster memorizes. "
            "Divergence aloft forces convergence and rising motion below, "
            "dropping surface pressure. Where the jet dives south it drags "
            "cold air and storms; where it bulges north it builds heat and "
            "fair skies. Aviation forecasters add turbulence diagnostics - "
            "the Ellrod index and its cousins - because the jet's flanks "
            "are where clear-air turbulence lives."
        ),
        "key_points": [
            "Polar jet (9-12 km, 100-200+ kt) and subtropical jet: thermal-wind products of the pole-equator temperature contrast, peaking at the tropopause.",
            "The jet steers surface storms along the storm track; its meanders (Rossby waves) set zonal vs blocked regimes.",
            "Jet-streak quadrants: divergence in left-exit and right-entrance regions deepens surface lows beneath.",
            "The jet's sheared flanks are the home of clear-air turbulence - an aviation forecast staple.",
            "Plotted at 250/300 mb every shift; its position is the first draft of the week's weather.",
        ],
        "requirements": [
            "The thermal-wind relationship linking temperature contrast to wind increasing with height.",
            "The four-quadrant jet-streak divergence model.",
            "Reading 250/300-mb isotachs for core position and streak quadrants.",
        ],
        "standards": [
            "Jet-stream analysis at the 250 and 300 hPa levels with isotach intervals in knots.",
            "Rossby-wave dynamics as the framework for large-scale meanders.",
        ],
        "citations": [CIT_HOLTON, CIT_BLUESTEIN],
        "sig_lens": ("Signature edition: the jet as his Signature river in "
                     "the sky, carving the week's weather downstream."),
        "demo_kind": "jet_core",
    },
    {
        "key": "diurnal_local_winds",
        "name": "The Diurnal Cycle and Local Winds: Sea Breezes to Mountain Breezes",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The sun is weather's daily metronome, and the diurnal cycle - "
            "the 24-hour rhythm of heating and cooling - drives the most "
            "predictable winds on Earth. By day the land heats faster than "
            "water; the warm air over the coast rises and cooler marine air "
            "flows in to replace it: the sea breeze, typically 10 to 20 "
            "knots by mid-afternoon, with a sharp sea-breeze front that can "
            "trigger lines of thunderstorms. By night the cycle reverses "
            "into the weaker land breeze. In mountains the same physics "
            "tilts vertical: daytime upslope (anabatic) winds climb heated "
            "slopes while nighttime downslope (katabatic) winds drain cold "
            "dense air into valleys - the mountain-valley breeze system. "
            "Where terrain funnels the flow, local winds get names and "
            "reputations: the chinook and foehn plunging warm and dry off "
            "the lee slopes, the mistral screaming down the Rhone valley, "
            "the Santa Anas driving fire weather in California. Forecasters "
            "treat the diurnal cycle as the baseline forecast and local "
            "winds as its most reliable modifiers."
        ),
        "how_it_works": (
            "Differential heating is the whole mechanism. Land's low heat "
            "capacity lets its surface temperature swing 15 to 25 Celsius "
            "in a day; water's enormous heat capacity holds nearly steady. "
            "The warmer column over land expands, raising pressure aloft "
            "and lowering it at the surface relative to the water - the "
            "resulting pressure gradient drives the sea breeze onshore, "
            "strongest when the land-sea temperature contrast peaks in "
            "afternoon. At night, radiational cooling chills the land "
            "surface, the gradient reverses, and the land breeze sighs "
            "offshore. On slopes, daytime heating makes air buoyant along "
            "the incline (anabatic), while nighttime cooling creates dense "
            "air that slides downhill (katabatic), pooling in valleys as "
            "cold-air drainage that breeds frost and fog. Gap and downslope "
            "winds accelerate through terrain constrictions by the Venturi "
            "effect and by isentropic drawdown - air sinking from ridge "
            "crest warms at the dry adiabatic rate, arriving in the lee "
            "dramatically warmer and drier than it started."
        ),
        "key_points": [
            "The diurnal cycle is the baseline forecast: land heats/cools fast, water holds steady, and the contrast drives daily wind reversals.",
            "Sea breeze (day, onshore, 10-20 kt, with a convective front) reverses to land breeze (night, weaker) by the same physics.",
            "Mountain-valley breezes: anabatic upslope by day, katabatic drainage by night, pooling cold air and fog in valleys.",
            "Terrain-funneled winds - chinook/foehn, mistral, Santa Ana - get names because they get dangerous.",
            "Downslope warming at the dry adiabatic rate makes lee winds warm, dry, and fire-prone.",
        ],
        "requirements": [
            "Differential heating and the pressure gradients it creates.",
            "Anabatic vs katabatic circulation and cold-air pooling.",
            "Dry adiabatic warming (9.8 C/km) for downslope wind estimation.",
        ],
        "standards": [
            "Local wind names follow WMO regional usage and climatological convention.",
            "Wind reported as direction FROM which it blows, in knots or m/s.",
        ],
        "citations": [CIT_AHRENS, CIT_BARRY],
        "sig_lens": ("Signature edition: the daily breathing of his "
                     "Signature landscape, inhale by day and exhale by night."),
        "demo_kind": "diurnal_breeze",
    },
    # ================= COMPOUNDED =================
    {
        "key": "skewt_sounding",
        "name": "The Skew-T Log-P Diagram: A Forecaster's Sounding",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The Skew-T log-P diagram is the forecaster's X-ray of the "
            "atmosphere: temperature and dew point plotted against the "
            "logarithm of pressure, with the temperature lines skewed at "
            "45 degrees so the whole troposphere fits on one readable "
            "page. The red line is the environmental temperature profile "
            "from the radiosonde; the green line is the dew point. Where "
            "they pinch together, the air is saturated - a cloud layer. "
            "Where they gape apart, dry air that will evaporate "
            "precipitation or cap convection. Overlaid are the dry "
            "adiabats, moist adiabats, and saturation mixing-ratio lines "
            "that let the forecaster lift a surface parcel on paper and "
            "read its fate: the lifting condensation level where cloud "
            "forms, the level of free convection where the parcel becomes "
            "warmer than its environment, and the equilibrium level where "
            "the thunderstorm's top stops. CAPE - the area between parcel "
            "and environment - reads as storm fuel; CIN - the negative "
            "area near the ground - reads as the cap that must break. "
            "Twice a day, every forecaster on Earth reads the same "
            "diagram, because the sounding is the only direct look at the "
            "atmosphere's vertical structure."
        ),
        "how_it_works": (
            "The diagram works because pressure falls exponentially with "
            "height, so a logarithmic pressure axis spaces the atmosphere "
            "evenly, and skewing the isotherms keeps the lines from "
            "bunching at the top. The forecaster lifts a parcel mentally "
            "(or in software): from the surface it cools at the dry "
            "adiabatic lapse rate (9.8 C per km) until saturation at the "
            "LCL, then at the slower moist rate as condensation releases "
            "latent heat. Where the parcel path crosses the environmental "
            "profile going warm, that's the LFC - free convection begins. "
            "Where it crosses back to cold, the EL - the updraft's ceiling. "
            "The area between, integrated as buoyancy, is CAPE in joules "
            "per kilogram: under 1000 is modest, over 2500 is volatile. "
            "The negative area below the LFC is CIN, the cap; strong CIN "
            "with huge CAPE is the classic loaded-gun sounding that waits "
            "for one trigger. Wind barbs on the diagram's edge give the "
            "shear profile - speed and directional turning with height - "
            "that decides whether storms stay upright single cells or "
            "organize into supercells."
        ),
        "key_points": [
            "Skew-T log-P: temperature and dew point vs log-pressure, isotherms skewed 45 degrees - the atmosphere's X-ray.",
            "Pinched lines mean saturated cloud layers; wide gaps mean dry air, caps, and virga.",
            "Parcel lifting reads the LCL (cloud base), LFC (free convection), and EL (storm top) straight off the diagram.",
            "CAPE (positive area) is storm fuel; CIN (negative area) is the cap - the loaded-gun sounding has both.",
            "Wind barbs on the sounding give the shear profile that organizes - or disorganizes - storms.",
        ],
        "requirements": [
            "Dry vs moist adiabatic lapse rates and why they differ (latent heat).",
            "LCL, LFC, EL, CAPE, CIN definitions and typical thresholds.",
            "Reading wind barbs and hodographs for shear.",
        ],
        "standards": [
            "Radiosonde profiles encoded in WMO TEMP code at mandatory and significant levels.",
            "CAPE/CIN in J/kg as the standard instability metrics.",
        ],
        "citations": [CIT_WALLACE, CIT_VASQUEZ],
        "sig_lens": ("Signature edition: the sounding as his Signature "
                     "medical chart, each layer a vital sign of the sky."),
        "demo_kind": "parcel_lcl",
    },
    {
        "key": "thunderstorm_forecasting",
        "name": "Thunderstorm Forecasting: Ingredients and Severe Parameters",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Forecasting thunderstorms is forecasting a recipe: the "
            "ingredients are moisture, instability, lift, and shear, and "
            "the forecaster's job is judging how much of each is on the "
            "counter. Moisture in the low levels is the fuel supply - "
            "dew points in the upper 60s Fahrenheit and higher mean a "
            "juicy boundary layer. Instability (CAPE) is the energy: "
            "1000 to 2500 J/kg brews strong storms, past 2500 the "
            "atmosphere is primed for violence. Lift is the trigger - a "
            "cold front, dryline, outflow boundary, or daytime heating "
            "that breaks the cap. Shear - wind changing with height - is "
            "the organizer: 0-6 km shear past 35 knots tilts updrafts and "
            "separates rain-cooled downdrafts from the inflow, letting "
            "storms live for hours as supercells instead of raining "
            "themselves out in 30 minutes. Modern severe forecasting "
            "compresses ingredients into parameters: the Significant "
            "Tornado Parameter, the Supercell Composite, the Significant "
            "Hail Parameter. The Storm Prediction Center issues "
            "convective outlooks days ahead using exactly this logic, "
            "upgrading from slight to enhanced to moderate to high risk "
            "as the ingredients align."
        ),
        "how_it_works": (
            "The ingredients method works because each one gates a "
            "physical necessity. Without low-level moisture there is no "
            "condensation and no latent-heat engine. Without instability "
            "parcels cannot accelerate upward; CAPE is literally the "
            "vertical integral of buoyancy. Without lift, even a volatile "
            "profile sits capped - CIN must be overcome by a front, "
            "boundary, or thermal. Without shear, the storm's own cold "
            "pool undercuts its updraft and it dies young; with shear, "
            "the updraft stays erect over the inflow and the storm "
            "becomes a long-lived rotating supercell. Composite parameters "
            "multiply normalized ingredients: the Significant Tornado "
            "Parameter combines CAPE, low-level shear, storm-relative "
            "helicity, and LCL height - values above 1 flag tornado "
            "potential. Forecasters overlay the parameters on surface "
            "maps, watch for boundaries that focus lift, and nowcast "
            "initiation by tracking cumulus towers on visible satellite "
            "and the first 35-dBZ echoes on radar."
        ),
        "key_points": [
            "Four ingredients: moisture, instability (CAPE), lift (trigger), and shear (organizer) - all four must be present.",
            "CAPE 1000-2500 J/kg strong, >2500 volatile; 0-6 km shear >35 kt organizes supercells.",
            "Composite parameters (Significant Tornado, Supercell Composite, Significant Hail) multiply the ingredients into single numbers.",
            "The Storm Prediction Center's convective outlooks scale slight/enhanced/moderate/high with ingredient overlap.",
            "Initiation nowcasting: watch cumulus towers on visible satellite and first 35-dBZ radar echoes.",
        ],
        "requirements": [
            "CAPE, CIN, LCL, and shear definitions from the sounding.",
            "Surface boundaries (fronts, drylines, outflow) as lift sources.",
            "Reading SPC convective outlook categories.",
        ],
        "standards": [
            "SPC convective outlook risk categories as the US operational standard.",
            "Severe thresholds: hail 1 inch+, wind 58 mph+, tornado.",
        ],
        "citations": [CIT_MARKOWSKI, CIT_DOSWELL],
        "sig_lens": ("Signature edition: storm ingredients as his Signature "
                     "recipe cards, each severe day a dish he plates."),
        "demo_kind": "storm_ingredients",
    },
    {
        "key": "tornadoes",
        "name": "Tornadoes: Formation, the Enhanced Fujita Scale, and Warning Signs",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The tornado is meteorology's most violent and most local "
            "phenomenon: a violently rotating column of air, sometimes "
            "only tens of meters wide, with winds that can exceed 300 "
            "miles per hour in the strongest cases. Most significant "
            "tornadoes are born inside supercell thunderstorms, where a "
            "deep rotating updraft - the mesocyclone, kilometers wide - "
            "tightens and stretches downward until rotation reaches the "
            "ground. Forecasters cannot see tornadoes forming directly, "
            "so they read the precursors: a hook echo on radar reflectivity "
            "wrapping precipitation around the mesocyclone, a tight "
            "velocity couplet of inbound and outbound winds side by side, "
            "a debris ball of high reflectivity and low correlation "
            "coefficient when the tornado is lofting wreckage. Damage is "
            "rated after the fact on the Enhanced Fujita scale, EF0 to "
            "EF5, from 28 damage indicators - houses, schools, trees, "
            "towers - each with degrees of damage tied to estimated "
            "3-second gust speeds. Warnings rest on this chain: "
            "environment, radar precursor, spotter confirmation."
        ),
        "how_it_works": (
            "Tornadogenesis works through stretching. Horizontal vorticity "
            "generated by low-level shear gets tilted into the vertical by "
            "the storm's updraft; the mesocyclone forms. Then the "
            "rear-flank downdraft wraps around, and as the circulation "
            "contracts, conservation of angular momentum spins it faster - "
            "the ice-skater effect - until a funnel descends. "
            "Non-supercell tornadoes (landspouts, waterspouts) form "
            "differently: from pre-existing boundary-layer spin stretched "
            "by a growing cumulus, usually weaker. The EF scale works "
            "backwards from damage: surveyors match observed damage to "
            "the indicator list - for example, a one- or two-family "
            "residence with its roof and walls collapsed maps to "
            "EF3-range winds - and assign the rating from the highest "
            "credible degree of damage. Radar detection works on the "
            "velocity couplet: adjacent gates showing strongly inbound "
            "and outbound radial velocities mark rotation, and the "
            "tornadic debris signature confirms a tornado is doing "
            "damage. Lead time averages around 13 minutes nationally; "
            "the warning is only as good as the lowest link in the "
            "chain."
        ),
        "key_points": [
            "Most violent tornadoes form in supercell mesocyclones via tilting and stretching of vorticity - the ice-skater effect.",
            "Radar precursors: hook echo, tight velocity couplet, tornadic debris signature (high reflectivity, low correlation coefficient).",
            "The Enhanced Fujita scale rates damage EF0-EF5 via 28 damage indicators tied to estimated 3-second gusts (EF5: >200 mph).",
            "Landspouts and waterspouts form from boundary-layer spin, not mesocyclones - usually weaker.",
            "Warning chain: environment, radar precursor, spotter confirmation; national average lead time ~13 minutes.",
        ],
        "requirements": [
            "Mesocyclone vs tornado-scale rotation and the stretching mechanism.",
            "Reading velocity couplets and debris signatures on radar.",
            "EF-scale damage indicators and wind-speed ranges.",
        ],
        "standards": [
            "Enhanced Fujita scale (2007): 28 damage indicators, degrees of damage, 3-second gust estimates.",
            "NWS tornado warning criteria: radar-indicated rotation or confirmed tornado.",
        ],
        "citations": [CIT_MARKOWSKI, CIT_DOVIAK],
        "sig_lens": ("Signature edition: the tornado as his Signature "
                     "drill bit, boring the sky's fury into the ground."),
        "demo_kind": "ef_scale",
    },
    {
        "key": "hail_derecho",
        "name": "Hail, Damaging Winds, and Derechos: Supercells and Squall Lines",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Tornadoes get the headlines, but straight-line wind and hail "
            "do most of severe weather's economic damage. Hail grows "
            "inside a thunderstorm's updraft: supercooled droplets freeze "
            "onto an ice nucleus, and the stone is lofted and recycled "
            "through the updraft's supercooled water, adding onion-like "
            "layers until it outgrows the updraft's support and crashes "
            "down - golf-ball hail needs roughly 60-knot updrafts, "
            "softball-sized stones need updrafts past 100 knots, found "
            "only in the strongest supercells. Damaging winds come in two "
            "families: the downburst, a localized column of sinking "
            "rain-cooled air that slams the ground and spreads out "
            "(microbursts under 4 km are the aviation killers), and the "
            "derecho, a widespread, long-lived windstorm - at least 240 "
            "miles long with gusts over 58 mph - produced by a bow-echo "
            "squall line's rear-inflow jet. Forecasters read the same "
            "signs for all three: intense reflectivity cores (70+ dBZ for "
            "giant hail), bow echoes and rear-inflow notches for damaging "
            "winds, and storm-top divergence for the updraft strength "
            "behind it all."
        ),
        "how_it_works": (
            "Hail growth is a suspension problem: a stone stays aloft while "
            "the updraft exceeds its terminal fall speed, growing by "
            "accretion each pass through supercooled liquid water, until "
            "gravity wins. Strong shear tilts the storm so the hail core "
            "separates from the rain-cooled downdraft - the classic "
            "supercell hail shaft falls beside the updraft, not through "
            "it. Downbursts work by negative buoyancy: rain evaporating "
            "into dry air and melting hail chill a downdraft that "
            "accelerates downward, hits the surface, and spreads as a "
            "gust front - the damage pattern fans outward in straight "
            "lines, which is how surveyors distinguish it from tornado "
            "damage. Derechos are downbursts organized at scale: a squall "
            "line's cold pool surges forward, the rear-inflow jet feeds "
            "the system from behind, and the line bows into the classic "
            "bow echo that can rake hundreds of miles. Forecasters watch "
            "for the three-body scatter spike (giant hail aloft), "
            "descending reflectivity cores, and bow-echo bookend vortices "
            "to warn on each hazard."
        ),
        "key_points": [
            "Hail grows by recycling through supercooled updrafts; softball hail needs 100+ knot updrafts found only in strong supercells.",
            "Downbursts: rain-cooled sinking air slams down and spreads out; damage fans in straight lines (vs tornado's convergent swirl).",
            "Derechos: bow-echo squall lines with rear-inflow jets, 240+ miles long, gusts 58+ mph - inland hurricanes.",
            "Microbursts (<4 km) are the aviation killers - sudden performance loss on final approach.",
            "Radar tells: 70+ dBZ cores and three-body spikes for giant hail; bow echoes and rear-inflow notches for wind.",
        ],
        "requirements": [
            "Updraft vs terminal-velocity balance for hail sizing.",
            "Cold-pool and rear-inflow-jet dynamics of squall lines.",
            "Distinguishing straight-line from tornadic damage patterns.",
        ],
        "standards": [
            "Severe hail threshold: 1.00 inch diameter; severe wind: 58 mph (50 kt).",
            "Derecho definition: 240+ mile swath of 58+ mph gusts (Johns and Hirt).",
        ],
        "citations": [CIT_DOSWELL, CIT_MARKOWSKI],
        "sig_lens": ("Signature edition: hail as his Signature ice shot, "
                     "downbursts as his hammer falling straight down."),
        "demo_kind": "hail_updraft",
    },
    {
        "key": "lightning_practice",
        "name": "Lightning in Practice: Detection Networks and Safety",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Lightning kills more Americans in an average year than "
            "tornadoes and hurricanes combined - not because it is exotic, "
            "but because it is everywhere and people underestimate it. "
            "The practice of lightning meteorology has two halves: "
            "detection and safety. Detection networks like the US National "
            "Lightning Detection Network triangulate every cloud-to-ground "
            "stroke from the radio sferics it emits, locating strikes to "
            "within hundreds of meters and reporting polarity and peak "
            "current in near-real time; satellite mappers now watch total "
            "lightning - including in-cloud flashes - from geostationary "
            "orbit, revealing intensifying updrafts before radar shows "
            "them. Forecasters use flash-rate trends as a nowcasting tool: "
            "a sudden jump in total lightning often precedes severe "
            "weather by 10 to 20 minutes. Safety is simpler and "
            "non-negotiable: the 30-30 rule - shelter if flash-to-bang is "
            "under 30 seconds, wait 30 minutes after the last thunder - "
            "because lightning can strike 10 miles from the rain shaft, "
            "and no place outside is safe when thunder roars."
        ),
        "how_it_works": (
            "Detection works on radio physics: a return stroke radiates a "
            "powerful very-low-frequency pulse, and a network of sensors "
            "times its arrival - time-of-arrival triangulation fixes the "
            "strike location, while magnetic direction finding cross-"
            "checks the bearing. Peak current follows from signal "
            "strength; positive strokes (from the anvil or stratiform "
            "region) carry higher currents and start more fires. From "
            "space, the Geostationary Lightning Mapper stares at "
            "oxygen-emission flickers at 777 nanometers, mapping total "
            "lightning day and night. The lightning-jump algorithm "
            "watches flash rates: when a storm's total flash rate "
            "accelerates sharply, the updraft is intensifying and severe "
            "weather - large hail, damaging wind, tornadoes - often "
            "follows within minutes. Safety works on sound: thunder is "
            "audible roughly 10 miles out, and light travels effectively "
            "instantly, so counting seconds between flash and bang and "
            "dividing by 5 gives miles (by 3 for kilometers). If you hear "
            "thunder, you are in range - get inside a substantial building "
            "or hard-topped vehicle and stay there."
        ),
        "key_points": [
            "Lightning kills more people annually than tornadoes and hurricanes combined - familiarity breeds underestimation.",
            "Ground networks triangulate strokes from radio sferics (location, polarity, peak current); satellites map total lightning from orbit.",
            "Lightning jumps - sudden flash-rate accelerations - precede severe weather by 10-20 minutes: a nowcasting tool.",
            "The 30-30 rule: shelter if flash-to-bang < 30 s; wait 30 min after the last thunder.",
            "If you hear thunder you are in strike range - substantial building or hard-topped vehicle, no exceptions.",
        ],
        "requirements": [
            "Flash-to-bang distance math: seconds/5 = miles, seconds/3 = kilometers.",
            "Reading total-lightning trends as updraft diagnostics.",
            "The 30-30 rule and why 'bolt from the blue' strikes happen.",
        ],
        "standards": [
            "NWS lightning safety guidance: 'When thunder roars, go indoors.'",
            "Lightning-jump algorithm thresholds used in operational nowcasting research.",
        ],
        "citations": [CIT_DOVIAK, CIT_AHRENS],
        "sig_lens": ("Signature edition: lightning as his Signature "
                     "welding arc, stitching cloud to ground in white fire."),
        "demo_kind": "flash_bang",
    },
    {
        "key": "fog_forecasting",
        "name": "Fog Forecasting: Radiation, Advection, and Valley Fog",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Fog is a cloud with its base on the ground, and it is "
            "aviation's and highway travel's quietest killer - a dense "
            "fog bank can drop visibility below a quarter mile with no "
            "drama and no warning to drivers. Forecasting fog is "
            "forecasting saturation at the surface, and the forecaster "
            "sorts it by mechanism. Radiation fog forms on clear calm "
            "nights when the ground radiates heat to space, cooling the "
            "air to its dew point from below - the classic autumn valley "
            "fog that burns off by mid-morning. Advection fog forms when "
            "warm moist air slides over a colder surface, cooling to "
            "saturation from below - the persistent pea-soupers off cold "
            "ocean currents. Upslope fog forms as moist air is forced up "
            "a gentle slope and cools adiabatically. Valley fog is "
            "radiation fog plus terrain: cold dense air drains downhill "
            "and pools, deepening the saturated layer. Steam fog wisps "
            "off warm water into frigid air; freezing fog coats everything "
            "in rime. The forecaster's inputs are always the same: the "
            "temperature-dew-point spread, the wind (too much mixes fog "
            "away, calm lets it form), the sky (clouds block the "
            "radiational cooling), and the terrain."
        ),
        "how_it_works": (
            "Fog forecasting is applied saturation arithmetic. The key "
            "number is the evening temperature-dew-point spread: a spread "
            "under about 2-3 Celsius at sunset with light winds and clear "
            "skies is the classic radiation-fog setup, because "
            "radiational cooling of 1-3 degrees per hour will close the "
            "gap by morning. Forecasters compute the 'fog point' - the "
            "temperature to which the air must cool - and compare it "
            "against the expected overnight low; if the low reaches the "
            "fog point, fog forms. Wind is the gatekeeper: under about 5 "
            "knots the layer stays stratified and fog thickens; 5-10 "
            "knots can mix it into low stratus; stronger wind mixes drier "
            "air down and prevents fog entirely. Moisture advection "
            "matters too - a fresh influx of humid air lowers the cooling "
            "needed. Valley fog adds drainage: katabatic flow piles cold "
            "air into the valley, so valley stations fog in hours before "
            "the ridge. Burn-off is forecast from solar heating: roughly "
            "an hour or two after sunrise per 100 meters of fog depth, "
            "faster with a breeze, slower under an inversion lid."
        ),
        "key_points": [
            "Fog is saturation at the surface; the evening temperature-dew-point spread is the forecaster's master variable.",
            "Radiation fog: clear calm nights, ground cools air to dew point, burns off mid-morning. Advection fog: warm moist air over cold surface, persistent.",
            "Wind gates fog: calm lets it form, 5-10 kt mixes it to stratus, stronger wind prevents it.",
            "Valley fog adds katabatic drainage - valleys fog in hours before ridges.",
            "Burn-off timing: solar heating erodes roughly 100 m of fog depth per 1-2 hours after sunrise.",
        ],
        "requirements": [
            "Temperature-dew-point spread and the fog-point concept.",
            "Radiational cooling rates and inversion formation.",
            "Terrain effects: drainage, pooling, and upslope saturation.",
        ],
        "standards": [
            "Dense fog advisory: visibility 1/4 mile or less (US operational standard).",
            "Fog vs mist: visibility below/above 1 km (WMO).",
        ],
        "citations": [CIT_AHRENS, CIT_STULL],
        "sig_lens": ("Signature edition: fog as his Signature breath on "
                     "the landscape, exhaled cold and white."),
        "demo_kind": "fog_point",
    },
    {
        "key": "winter_storms",
        "name": "Winter Storm Forecasting: Snow Ratios, Blizzards, and Ice Storms",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Winter storms are temperature-profile puzzles: the same "
            "storm drops fluffy powder, crippling ice, or plain rain "
            "depending on a few degrees in a layer a kilometer thick. "
            "The forecaster's first tool is the snow ratio - how many "
            "inches of snow each inch of liquid water makes. The textbook "
            "10-to-1 is only an average: cold Arctic air with dendritic "
            "crystals can run 20 or 30 to 1, while wet spring snow near "
            "freezing falls at 5 to 1 and snaps power lines. The ratio "
            "follows the crystal type, which follows the temperature in "
            "the dendritic growth zone around -12 to -18 Celsius. Then "
            "comes the precipitation-type profile: snow all the way down "
            "means snow; a warm nose aloft (above freezing) over "
            "subfreezing air at the surface means freezing rain if the "
            "warm layer fully melts the flakes, or sleet if it only "
            "partly melts them. A quarter inch of ice accretion downs "
            "power lines - the ice-storm criterion - while a blizzard "
            "needs 35-mph winds with visibility under a quarter mile in "
            "snow for three hours, regardless of how much falls. "
            "Nor'easters wrap all of it together: bombing coastal lows "
            "with rain-snow lines that wobble for a hundred miles."
        ),
        "how_it_works": (
            "The forecast works layer by layer on the sounding. The "
            "forecaster reads the 850-millibar temperature (the rain-snow "
            "line lives near the freezing line there), the depth and "
            "strength of any warm nose aloft, and the surface temperature. "
            "Snow ratios are estimated from the forecast profile: the "
            "colder the cloud, the fluffier the ratio, with adjustments "
            "for wind (which fragments crystals) and riming. "
            "Thunder-snow and banded structures - single intense snow "
            "bands that can drop 2-4 inches per hour under a 20-mile-wide "
            "strip - are diagnosed from frontogenesis and CSI (conditional "
            "symmetric instability) on cross-sections. Ice accretion is "
            "modeled from the warm-nose depth: a deep warm layer with a "
            "shallow subfreezing surface layer is the classic freezing-"
            "rain setup, and accretion rates follow precipitation rate "
            "times the freezing fraction. Blizzard forecasting adds the "
            "wind: pressure gradients behind the departing low drive the "
            "35-mph criterion, and blowing snow - new or old - provides "
            "the visibility collapse. The rain-snow line is drawn where "
            "the 850-mb zero-degree isotherm crosses the precipitation, "
            "then nudged for evaporative cooling and intensity."
        ),
        "key_points": [
            "Snow ratios: 10:1 is the average; 20-30:1 in cold dendritic snow, 5:1 in wet spring snow - the profile decides.",
            "Precipitation type follows the temperature profile: warm nose aloft + subfreezing surface = freezing rain or sleet.",
            "Ice-storm criterion: 0.25 inch of ice accretion. Blizzard: 35+ mph winds, <1/4 mile visibility in snow, 3+ hours.",
            "Banded heavy snow (2-4 in/hr) is diagnosed from frontogenesis and symmetric instability on cross-sections.",
            "Nor'easters are bombing coastal lows where the rain-snow line wobbles across a hundred miles.",
        ],
        "requirements": [
            "Reading warm noses and freezing layers on soundings.",
            "Snow-ratio estimation from the dendritic growth zone (-12 to -18 C).",
            "Blizzard vs heavy-snow vs ice-storm warning criteria.",
        ],
        "standards": [
            "NWS winter warning criteria: ice accretion 0.25 in+, blizzard wind/visibility/duration thresholds.",
            "Snow measurement standards: snow board, 6-hourly clearing.",
        ],
        "citations": [CIT_VASQUEZ, CIT_AHRENS],
        "sig_lens": ("Signature edition: winter storms as his Signature "
                     "ice foundry, casting snow, sleet, and freezing rain."),
        "demo_kind": "snow_ratio",
    },
    {
        "key": "lake_effect",
        "name": "Lake-Effect Snow: The Great Lakes Snow Machine",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Some of the heaviest snow on Earth falls in narrow bands "
            "downwind of the Great Lakes, where Arctic air crossing "
            "relatively warm water turns into a snow factory. The recipe "
            "is strict: the lake must be unfrozen, the temperature "
            "difference between the lake surface and the air at 850 "
            "millibars must reach about 13 Celsius (23 Fahrenheit), the "
            "wind must blow along the lake's long axis (fetch) for at "
            "least 100 kilometers, and the atmosphere must be unstable "
            "enough to convect. When it all aligns, the results are "
            "astonishing: single storms dropping 3 to 6 feet, snowfall "
            "rates of 2 to 4 inches per hour, and bands so narrow that "
            "one town gets buried while the next town ten miles away "
            "sees sunshine. The Tug Hill Plateau east of Lake Ontario "
            "averages over 200 inches a season. Forecasters watch the "
            "fetch, the delta-T, the inversion height (which caps the "
            "cloud depth), and the wind direction to the degree - a 20-"
            "degree shift moves the band off a city and the forecast "
            "busts. Lake-effect snow is mesoscale meteorology's purest "
            "demonstration that geography makes weather."
        ),
        "how_it_works": (
            "The machine runs on surface heat and moisture fluxes. Cold "
            "air streaming over the warmer lake gains sensible heat and "
            "evaporated moisture from below; the layer destabilizes, "
            "convection organizes into horizontal rolls aligned with the "
            "wind, and the rolls become snow bands. Fetch is the "
            "accelerator: the longer the over-water trajectory, the more "
            "heat and moisture the air collects, which is why the long "
            "axes of the lakes aim their worst bands at specific "
            "shorelines. The inversion height sets the cloud-top limit - "
            "a low inversion means shallow clouds and lighter snow; a "
            "deep unstable layer means towering bands and thundersnow. "
            "Wind direction is everything: bands lock onto the flow, so "
            "forecasters nowcast band position with radar and adjust "
            "hourly. Orographic lift where the bands hit higher terrain "
            "(the Tug Hill, the Chautauqua Ridge) multiplies totals. The "
            "season ends when the lakes freeze over - ice shuts off the "
            "fluxes - which is why a warming climate's shorter ice "
            "season is lengthening the lake-effect calendar."
        ),
        "key_points": [
            "Recipe: unfrozen lake, lake-to-850mb delta-T of ~13 C, 100+ km fetch along the wind, unstable profile.",
            "Bands are narrow and intense: 2-4 in/hr rates, feet per storm, sunshine ten miles away.",
            "Wind direction to the degree positions the band - a 20-degree shift busts the city forecast.",
            "Inversion height caps cloud depth; terrain downwind (Tug Hill) multiplies totals past 200 in/season.",
            "Ice cover shuts the machine off; shorter ice seasons lengthen the lake-effect calendar.",
        ],
        "requirements": [
            "Delta-T computation and the 13 C threshold.",
            "Fetch geometry: why lake orientation picks the victim shoreline.",
            "Nowcasting band position with radar and wind shifts.",
        ],
        "standards": [
            "Lake-effect snow warning criteria (local NWS thresholds, commonly 6-8 in/12 hr).",
            "Delta-T in Celsius between lake surface and 850-mb temperature.",
        ],
        "citations": [CIT_MARKOWSKI, CIT_AHRENS],
        "sig_lens": ("Signature edition: the lakes as his Signature snow "
                     "engines, stoked with Arctic air each winter."),
        "demo_kind": "lake_effect_check",
    },
    {
        "key": "mountain_weather",
        "name": "Mountain Weather: Orographic Lift, Chinook Winds, and Mountain Waves",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Mountains make their own weather, and mountain forecasters "
            "read terrain the way synoptic forecasters read isobars. "
            "Windward slopes force air upward - orographic lift - cooling "
            "it to saturation and wringing out precipitation: the windward "
            "side of the Cascades gets 100+ inches a year while the lee "
            "side sits in rain shadow with a tenth of that. Air crossing "
            "the crest then plunges down the lee slopes, warming at the "
            "dry adiabatic rate: the chinook of the Rockies and the "
            "foehn of the Alps can raise temperatures 30 Fahrenheit in "
            "an hour, vaporizing snowpack and spiking fire danger. When "
            "the flow is strong and stable, the mountain launches "
            "atmospheric waves - mountain waves with lenticular clouds "
            "stacked like plates marking the crests, and violent rotors "
            "tumbling beneath them that have torn aircraft apart. Valley "
            "fog, gap winds, and cold-air pooling complete the toolkit. "
            "Mountain forecasts are written slope by slope, elevation by "
            "elevation, because two trailheads ten miles apart can live "
            "in different climates."
        ),
        "how_it_works": (
            "Orographic lift is forced ascent: horizontal wind meets a "
            "slope and has nowhere to go but up, cooling at the moist "
            "adiabatic rate once saturated, condensing cloud and "
            "precipitation on the windward side. The rain shadow follows "
            "from descent: leeward air sinks, warms, and dries, often "
            "dropping below its original humidity. Chinook/foehn dynamics "
            "add latent-heat bookkeeping: moisture lost as precipitation "
            "on the windward side means the descending air warms dry-"
            "adiabatically all the way down, arriving far warmer than "
            "equivalent upwind air. Mountain waves form when stably "
            "stratified flow crosses a ridge: the air is displaced "
            "upward, gravity pulls it back, and it oscillates downstream "
            "like a plucked string, with wavelength set by the wind and "
            "stability profile (the Scorer parameter). Lenticular clouds "
            "condense at the wave crests where lift cools air to "
            "saturation; rotors - horizontal vortices under the crests - "
            "hold the worst turbulence. Forecasters use cross-barrier "
            "wind components, freezing levels, and stability profiles to "
            "time each phenomenon."
        ),
        "key_points": [
            "Orographic lift wrings precipitation from windward slopes; the lee sits in rain shadow - 100+ in/yr vs a tenth of that.",
            "Chinook/foehn: descending air warms dry-adiabatically, arriving 30 F warmer in an hour - snow-eater and fire wind.",
            "Mountain waves: stable flow over ridges oscillates downstream; lenticular clouds mark crests, rotors hold violent turbulence.",
            "Valley fog and cold-air pooling come from katabatic drainage; gap winds accelerate through passes.",
            "Mountain forecasts are written slope by slope and elevation by elevation.",
        ],
        "requirements": [
            "Moist vs dry adiabatic rates applied to upslope/downslope flow.",
            "The Scorer parameter concept for wave trapping.",
            "Reading freezing level and cross-barrier flow for precipitation type.",
        ],
        "standards": [
            "Orographic precipitation enhancement estimated from upslope wind component and moisture flux.",
            "Aviation mountain-wave turbulence guidance (AIRMETs, PIREPs).",
        ],
        "citations": [CIT_BARRY, CIT_MARKOWSKI],
        "sig_lens": ("Signature edition: mountains as his Signature "
                     "bellows, pumping air up one side and fire down the other."),
        "demo_kind": "orographic_lift",
    },
    {
        "key": "marine_meteorology",
        "name": "Marine Meteorology: The Beaufort Scale, Waves, and Marine Forecasts",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "At sea there are no fences, no shelters, and no second "
            "chances - which is why marine meteorology is its own "
            "discipline with its own language. The Beaufort scale, "
            "devised in 1805 for sailing ships, still grades wind by "
            "its effects on the sea: force 4 (11-16 knots) with small "
            "waves and frequent whitecaps, force 8 (34-40 knots) a gale "
            "with moderately high waves, force 12 (64+ knots) hurricane "
            "force with the air filled with foam and spray. The marine "
            "forecaster thinks in wave physics: wind sea (locally "
            "generated chop), swell (waves that have outrun their storm "
            "and travel thousands of miles), and combined seas that are "
            "the vector sum mariners actually ride. Wave height follows "
            "wind speed, duration, and fetch - a 40-knot wind blowing "
            "for a day over 500 miles of ocean builds 20-foot seas. "
            "Marine forecasts are zoned by waters, carry wave heights "
            "and periods rather than temperatures, and warn with gale, "
            "storm, and hurricane-force wind warnings that send ships "
            "to harbor or around the storm."
        ),
        "how_it_works": (
            "Wave forecasting models solve the energy balance: wind "
            "pumps energy into the sea surface, nonlinear interactions "
            "shift it to longer periods, and dissipation (whitecapping) "
            "bleeds it off. Given wind speed, duration, and fetch, "
            "empirical relations (Sverdrup-Munk-Bretschneider) estimate "
            "significant wave height - the average of the highest third "
            "of waves, the number mariners feel. Swell propagates with "
            "little loss, so a North Pacific storm's 18-second swell "
            "arrives in Hawaii days later, forecast from spectral wave "
            "models like WaveWatch III. The forecaster blends model "
            "guidance with buoy observations - wave height, dominant "
            "period, and direction from moored buoys - and ship reports. "
            "Marine warnings key off sustained winds: small-craft "
            "advisory (25-33 kt), gale warning (34-47 kt), storm warning "
            "(48+ kt), hurricane-force wind warning (64+ kt). Fog "
            "forecasts use sea-surface vs dew-point spreads; icing "
            "forecasts use air temperature, sea temperature, and wind "
            "for superstructure icing that can capsize small vessels."
        ),
        "key_points": [
            "The Beaufort scale (1805) grades wind by sea effects: force 8 gale, force 12 hurricane force (64+ kt).",
            "Wind sea is locally generated; swell outruns its storm and travels thousands of miles; mariners ride the combined seas.",
            "Wave height follows wind speed, duration, and fetch - 40 kt over 500 miles for a day builds ~20-ft seas.",
            "Significant wave height (highest third) comes from spectral models verified against buoys.",
            "Marine warnings: small craft 25-33 kt, gale 34-47 kt, storm 48+ kt, hurricane-force 64+ kt.",
        ],
        "requirements": [
            "Beaufort forces and their sea-state descriptions.",
            "Fetch/duration-limited vs fully developed seas.",
            "Reading buoy spectra: height, period, direction.",
        ],
        "standards": [
            "Beaufort wind scale as the international marine standard (WMO).",
            "NWS marine warning thresholds by sustained wind speed.",
        ],
        "citations": [CIT_BARRY, CIT_WMO],
        "sig_lens": ("Signature edition: the ocean as his Signature "
                     "proving ground, every wave a Signature stress test."),
        "demo_kind": "beaufort_waves",
    },
    {
        "key": "tropical_meteorology",
        "name": "Tropical Meteorology in Practice: The ITCZ, Tropical Waves, and Monsoons",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "In the tropics there are no fronts and no jet-stream storms - "
            "the temperature barely changes from day to day - yet the "
            "tropics drive the planet's weather engine. Tropical "
            "meteorology studies the systems that organize convection "
            "where the Coriolis force is too weak to spin mid-latitude "
            "cyclones. The Intertropical Convergence Zone (ITCZ) is the "
            "planet's thermal equator: trade winds from both hemispheres "
            "converge, air rises in towering clusters, and the rain belt "
            "migrates with the sun, bringing wet and dry seasons instead "
            "of summer and winter. Easterly (tropical) waves - troughs in "
            "the trade-wind flow marching westward at 10 to 15 knots - "
            "are the seedlings of most Atlantic hurricanes; forecasters "
            "track each wave off Africa across the ocean. Monsoons are "
            "the seasonal extreme of the same physics: the continent "
            "heats, a thermal low forms, moist ocean air surges in, and "
            "months of rain follow - the Indian monsoon waters a billion "
            "people and fails at the cost of famine. The Madden-Julian "
            "Oscillation, a 30-60-day pulse of convection circling the "
            "globe, modulates it all."
        ),
        "how_it_works": (
            "Tropical systems run on latent heat, not temperature "
            "contrast. In the ITCZ, surface convergence forces ascent; "
            "condensation releases latent heat that fuels deeper "
            "convection - a positive feedback called conditional "
            "instability of the second kind (CISK) in its classic "
            "formulation. Easterly waves grow by combined barotropic and "
            "baroclinic instability of the African easterly jet; the "
            "wave's trough axis concentrates convection on its east "
            "side, and forecasters watch for the closed low-level "
            "circulation that marks the step toward tropical "
            "cyclogenesis. Monsoons work on the continental scale: "
            "summer heating drops surface pressure over land, the "
            "pressure gradient pulls in moist oceanic air, and the "
            "moisture converges into months of rain; the Tibetan "
            "Plateau's elevated heating amplifies the Asian monsoon. "
            "Forecasters track waves on 700-mb streamline analyses and "
            "satellite loops, monitor the MJO phase for windows of "
            "enhanced or suppressed convection, and watch sea-surface "
            "temperatures - the ocean must be at least about 26.5 "
            "Celsius to sustain tropical cyclones."
        ),
        "key_points": [
            "The tropics have no fronts - convection is organized by convergence, waves, and the ITCZ, powered by latent heat.",
            "The ITCZ is the rain belt where trade winds converge, migrating seasonally with the sun.",
            "Easterly waves move west at 10-15 kt off Africa - most Atlantic hurricanes start as one; forecasters track each.",
            "Monsoons are seasonal land-sea circulation reversals; the Indian monsoon waters a billion people.",
            "The Madden-Julian Oscillation (30-60 day pulse) modulates tropical convection worldwide; SSTs above ~26.5 C fuel cyclones.",
        ],
        "requirements": [
            "Why the Coriolis force's weakness changes tropical dynamics.",
            "Reading 700-mb streamlines and satellite loops for waves and the ITCZ.",
            "Monsoon onset criteria and MJO phase interpretation.",
        ],
        "standards": [
            "Tropical wave tracking on NHC Tropical Weather Outlooks.",
            "26.5 C sea-surface temperature as the cyclogenesis energy threshold.",
        ],
        "citations": [CIT_WALLACE, CIT_EMANUEL],
        "sig_lens": ("Signature edition: the tropics as his Signature "
                     "boiler room, steam rising to drive the whole planet."),
        "demo_kind": "wave_track",
    },
    {
        "key": "hurricane_forecasting",
        "name": "Hurricane Forecasting: Track Models, the Cone, and Storm Surge",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Hurricane forecasting is the most consequential prediction "
            "meteorology makes: a single landfall decision evacuates "
            "millions or strands them. The track forecast has become a "
            "triumph - 72-hour errors have fallen by more than half since "
            "2000 - because hurricanes are steered by the deep-layer "
            "environmental flow, which global models now capture well. "
            "Forecasters blend dynamical models (HWRF, HAFS, the global "
            "GFS and ECMWF) into consensus aids like TVCN, then draw the "
            "famous cone of uncertainty: circles at each forecast hour "
            "sized from the previous five years' official errors, "
            "containing two-thirds of historical tracks. The cone is "
            "about the CENTER, not the impacts - hazards extend hundreds "
            "of miles outside it. Intensity forecasting lags track "
            "skill: rapid intensification over warm eddies or under low "
            "shear still surprises. The Saffir-Simpson scale (Category 1: "
            "74-95 mph through Category 5: 157+ mph) rates wind only; "
            "storm surge - the ocean dome pushed ashore, often the "
            "deadliest hazard - gets its own warnings and inundation "
            "maps, because a Category 1's surge can out-kill a Category "
            "4's wind."
        ),
        "how_it_works": (
            "Track models work because a hurricane is largely a cork in "
            "the environmental stream: the deep-layer mean wind (850 to "
            "200 mb) advects the vortex, and global models resolve that "
            "flow well. Consensus forecasting averages the best "
            "performers, canceling individual biases - the consensus "
            "routinely beats any single model. The cone is built from "
            "honest statistics: at each lead time, the radius equals the "
            "historical mean track error, so roughly two-thirds of "
            "past storms stayed inside. Intensity models add inner-core "
            "physics: ocean coupling (a storm's own upwelling can cool "
            "the water and choke it), eyewall replacement cycles that "
            "temporarily weaken then re-strengthen, and vertical shear "
            "that tilts and ventilates the core. Storm-surge models "
            "(SLOSH and successors) solve the shallow-water equations "
            "over coastal bathymetry for thousands of hypothetical "
            "tracks, producing the Maximum Envelope of Water. "
            "Forecasters issue the track, the intensity, the wind "
            "hazards, the rainfall, and the surge as separate products - "
            "because the public must prepare for all of them, not just "
            "the category number."
        ),
        "key_points": [
            "Track skill has soared: hurricanes are steered by deep-layer flow that global models capture; consensus aids beat single models.",
            "The cone holds the center track with 2/3 historical probability - hazards extend far outside it.",
            "Intensity lags track: rapid intensification, eyewall cycles, and shear keep it the hard problem.",
            "Saffir-Simpson (Cat 1: 74-95 mph ... Cat 5: 157+ mph) rates WIND only.",
            "Storm surge - the ocean dome pushed ashore - is often the deadliest hazard and gets its own warnings and inundation maps.",
        ],
        "requirements": [
            "Deep-layer steering concept and consensus forecasting.",
            "Reading the cone, wind-speed probabilities, and surge inundation maps as separate products.",
            "Rapid-intensification ingredients: warm deep water, low shear, moist mid-levels.",
        ],
        "standards": [
            "Saffir-Simpson Hurricane Wind Scale (74-95/96-110/111-129/130-156/157+ mph).",
            "NHC cone construction from 5-year official track errors.",
        ],
        "citations": [CIT_EMANUEL, CIT_KALNAY],
        "sig_lens": ("Signature edition: hurricanes as his Signature "
                     "heat engines, wound tight and aimed by the sky's currents."),
        "demo_kind": "hurricane_scale",
    },
    {
        "key": "heat_cold_extremes",
        "name": "Heat and Cold Extremes: The Heat Index, Wind Chill, and Extreme Warnings",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Temperature alone does not describe what the air does to a "
            "human body - humidity and wind rewrite it. The heat index "
            "combines temperature and humidity into 'feels like' "
            "degrees: at 90 Fahrenheit with 70 percent humidity the body "
            "feels 105, because sweat cannot evaporate into saturated "
            "air and the body's cooling system stalls. Prolonged exposure "
            "marches through heat cramps, heat exhaustion, and heat "
            "stroke - the last a medical emergency. The wind chill does "
            "the mirror calculation for cold: at 20 Fahrenheit with a "
            "30-mph wind, exposed skin feels near zero and frostbite "
            "can begin in 30 minutes, because wind strips the warm "
            "boundary layer from the skin. Forecasters warn on thresholds, "
            "not records: excessive-heat warnings when the heat index "
            "threatens vulnerable populations for consecutive days "
            "(heat waves kill more Americans than any other weather "
            "hazard), wind-chill warnings when frostbite times drop "
            "under about 30 minutes. The ingredients are forecast days "
            "ahead from the same models as everything else - the art is "
            "translating physics into human impact."
        ),
        "how_it_works": (
            "The heat index is an empirical regression (Rothfusz) fitted "
            "to human heat-balance modeling: it estimates the apparent "
            "temperature from air temperature and relative humidity, "
            "with adjustments for very dry or very humid extremes. "
            "Physiologically it tracks the wet-bulb temperature's "
            "approach to the skin's 35-Celsius limit - past a wet-bulb of "
            "about 35 C, humans cannot shed metabolic heat even at rest. "
            "Wind chill is a heat-transfer model of exposed skin: the "
            "formula combines temperature and wind speed to estimate "
            "cooling rate, then inverts it to the calm-air temperature "
            "that would cool equally fast. Forecasters compute both "
            "from model grids, map the hours above thresholds, and "
            "layer vulnerability - the elderly, outdoor workers, the "
            "unhoused, those without cooling - into impact-based "
            "warnings. Heat-wave forecasting adds the synoptic pattern: "
            "a stagnant upper ridge (the 'heat dome') with subsidence "
            "that suppresses clouds and cooks day after day. Cold waves "
            "add the arctic-airmass trajectory and the wind profile "
            "behind the front."
        ),
        "key_points": [
            "Heat index: temperature + humidity as 'feels like' - sweat fails in saturated air; heat waves are the deadliest weather hazard.",
            "Wind chill: temperature + wind as cooling rate on exposed skin; frostbite timing is the warning metric.",
            "Wet-bulb 35 C is the physiological ceiling - past it, the body cannot shed heat even at rest.",
            "Warnings key off impact thresholds and duration, layered with vulnerability (elderly, outdoor workers).",
            "Heat domes (stagnant upper ridges) and arctic outbreaks are the synoptic patterns behind the extremes.",
        ],
        "requirements": [
            "Computing heat index (Rothfusz) and wind chill from T, RH, and wind.",
            "Frostbite-time estimation and heat-illness progression.",
            "Recognizing heat-dome and arctic-outbreak patterns aloft.",
        ],
        "standards": [
            "NWS heat-index and wind-chill formulas and warning thresholds.",
            "Wet-bulb temperature as the physiological heat-stress metric.",
        ],
        "citations": [CIT_AHRENS, CIT_BARRY],
        "sig_lens": ("Signature edition: extremes as his Signature stress "
                     "tests, the body measured against the sky's limits."),
        "demo_kind": "feels_like",
    },
    {
        "key": "fire_weather",
        "name": "Fire Weather: Red Flag Warnings and the Haines Index",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Fire-weather meteorology exists because weather decides "
            "whether a spark becomes an incident or a catastrophe. The "
            "fire-behavior triangle - fuel, topography, weather - puts "
            "weather in charge of the uncontrollable leg: wind drives "
            "the head fire, low humidity cures the fine fuels, high "
            "temperatures preheat them, and atmospheric instability lets "
            "the fire build its own thunderstorm. The Red Flag Warning "
            "is the operational product: issued when warm temperatures, "
            "very low humidities (often under 15-20 percent), and strong "
            "winds (often 25+ mph) will combine over critically dry "
            "fuels - the exact thresholds tuned per region. The Haines "
            "Index distills lower-atmosphere stability and dryness into "
            "a 2-to-6 number: high Haines means the air above the fire "
            "is unstable and dry enough for plume-dominated, erratic "
            "behavior and long-range spotting. Forecasters also watch "
            "dry lightning (strikes with little rain), foehn wind events "
            "like the Santa Anas and Diablo winds, and overnight humidity "
            "recovery - poor recovery means the fire never sleeps."
        ),
        "how_it_works": (
            "Fire-weather forecasting quantifies fuel moisture through "
            "weather. Fine dead fuels (grass, needles) equilibrate with "
            "the air in hours, so relative humidity and temperature "
            "directly set their flammability; forecasters compute fine-"
            "fuel moisture from the forecast RH and temperature curve. "
            "Wind is forecast at multiple levels: surface wind drives "
            "spread rate, while ridgetop and mid-level winds set spotting "
            "distance and plume tilt. The Haines Index combines a "
            "stability term (temperature lapse between two pressure "
            "levels, e.g. 850 and 700 mb) with a moisture term (dew-point "
            "depression at the lower level): high lapse plus dry air "
            "scores 5-6, flagging plume-dominated fires. Red Flag "
            "criteria are Boolean combinations tuned locally - for "
            "example, RH below 15 percent AND sustained winds above 25 "
            "mph for hours over dry fuels. Incident meteorologists "
            "deployed to fires run spot forecasts for the burn area, "
            "updating wind shifts - the deadly moment when a flanking "
            "fire becomes a head fire - to the hour."
        ),
        "key_points": [
            "Weather controls fire's uncontrollable leg: wind drives spread, low RH cures fuels, instability builds fire thunderstorms.",
            "Red Flag Warnings fire on combined thresholds (e.g. RH <15-20%, winds 25+ mph over dry fuels), tuned per region.",
            "The Haines Index (2-6) scores lower-atmosphere stability + dryness; 5-6 flags plume-dominated, erratic fires.",
            "Fine dead fuels track the air in hours - forecast RH and temperature set flammability directly.",
            "Dry lightning, foehn winds, and poor overnight humidity recovery are the forecaster's red flags before the Red Flag.",
        ],
        "requirements": [
            "Fine-fuel moisture response to RH and temperature.",
            "Computing the Haines Index from lapse rate and dew-point depression.",
            "Local Red Flag criteria and wind-shift timing for incidents.",
        ],
        "standards": [
            "NWS Red Flag Warning criteria (regionally tuned thresholds).",
            "Haines Index 2-6 scale (low/moderate/high/very high).",
        ],
        "citations": [CIT_AHRENS, CIT_BARRY],
        "sig_lens": ("Signature edition: fire weather as his Signature "
                     "furnace draft, each warning a damper setting."),
        "demo_kind": "haines_index",
    },
    {
        "key": "agricultural_meteorology",
        "name": "Agricultural Meteorology: Growing Degree Days and Frost Forecasting",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Agriculture is applied meteorology with the stakes measured "
            "in harvests. Agricultural meteorologists translate weather "
            "into crop decisions with a handful of purpose-built tools. "
            "Growing degree days (GDD) accumulate heat above a crop's "
            "base temperature - 50 Fahrenheit for corn - so planting, "
            "emergence, pollination, and maturity are scheduled by "
            "thermal time, not calendar dates: corn needs roughly 2700 "
            "GDD to mature. Frost forecasting protects what heat built: "
            "a radiation frost (clear, calm nights) can be fought with "
            "wind machines, irrigation, and orchard heaters, but only "
            "if the forecast gives the hours and the low. The critical "
            "temperatures are crop-specific - 28 Fahrenheit kills most "
            "tender blossoms, 32 damages, 36 with dew near freezing "
            "threatens in calm valleys. Evapotranspiration estimates "
            "schedule irrigation: the crop's water use minus effective "
            "rainfall is the irrigation dose. And phenology models tie "
            "it together, predicting bloom, pest emergence, and harvest "
            "windows from the season's accumulated weather. The farm is "
            "a weather instrument that eats."
        ),
        "how_it_works": (
            "GDD accounting is simple arithmetic with biological meaning: "
            "each day contributes max(0, (Tmax + Tmin)/2 - Tbase), summed "
            "through the season, often capped so extreme heat does not "
            "count extra. Forecasters run GDD accumulations on model "
            "temperature grids to project maturity dates and to time "
            "pesticide applications to pest degree-day models - insects "
            "are thermal-time creatures too. Frost forecasting starts "
            "with the evening temperature-dew-point spread and the "
            "expected cooling rate: on a clear calm night the temperature "
            "falls 3-5 Fahrenheit per hour after sunset toward the dew "
            "point, then more slowly. The forecast low is compared "
            "against crop-critical thresholds, with adjustments for "
            "cold-air drainage (valley floors run 5-10 degrees colder "
            "than slopes) and cloud cover timing. Irrigation scheduling "
            "uses reference evapotranspiration from the Penman-Monteith "
            "equation times a crop coefficient for growth stage. Modern "
            "ag meteorology fuses station networks, soil-moisture probes, "
            "and satellite vegetation indices into decision dashboards "
            "that tell the grower what to do this week."
        ),
        "key_points": [
            "Growing degree days accumulate heat above a crop base (50 F for corn) - thermal time schedules planting to maturity.",
            "Frost forecasting: evening T-Td spread + cooling rate vs crop-critical thresholds (28 F kills blossoms).",
            "Radiation frosts can be fought (wind machines, irrigation, heaters) - but only with hours of warning.",
            "Irrigation dose = crop evapotranspiration minus effective rainfall.",
            "Pests and phenology run on degree days too - insects are thermal-time creatures.",
        ],
        "requirements": [
            "GDD computation with base temperatures and caps.",
            "Nocturnal cooling rates and cold-air drainage adjustments.",
            "Crop coefficients and reference ET for irrigation scheduling.",
        ],
        "standards": [
            "GDD base 50 F (10 C) for corn; crop-specific bases per agronomic standard.",
            "Frost/freeze warning thresholds tied to crop sensitivity.",
        ],
        "citations": [CIT_AHRENS, CIT_BARRY],
        "sig_lens": ("Signature edition: the farm as his Signature "
                     "thermometer that eats, each crop a weather gauge."),
        "demo_kind": "gdd_accumulate",
    },
    {
        "key": "radar_interpretation",
        "name": "Radar Interpretation: Reflectivity, Velocity Couplets, and Hook Echoes",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Weather radar does not see rain - it sees the echo of "
            "microwaves bouncing off raindrops, hailstones, snowflakes, "
            "insects, and birds - and interpreting it is a core "
            "forecaster skill. Reflectivity, in dBZ, grades echo "
            "strength: under 20 dBZ is drizzle or light snow, 35-45 "
            "marks solid rain, past 50 is heavy rain or hail, past 60 "
            "is almost certainly hail, and 70+ means giant hail is "
            "falling somewhere in that core. The classic Z-R relation "
            "(Z = 300 R^1.4) converts reflectivity to rainfall rate, "
            "with different relations for snow and tropical rain. "
            "Doppler velocity adds motion: green toward the radar, red "
            "away, and where bright green sits beside bright red - the "
            "velocity couplet - rotation is happening. The hook echo "
            "wraps precipitation around a mesocyclone; the bow echo "
            "bends a squall line where the damaging winds surge; the "
            "bright band marks the melting layer where snow becomes "
            "rain. Reading radar is reading the storm's anatomy in "
            "real time, updated every few minutes, and every warning "
            "forecaster does it by pattern recognition trained on "
            "thousands of storms."
        ),
        "how_it_works": (
            "Radar works by pulse and echo: the dish emits a microwave "
            "pulse, hydrometeors scatter a fraction back, and the "
            "return time gives range while the Doppler shift gives "
            "radial velocity. Reflectivity factor Z sums the sixth "
            "power of drop diameters per unit volume - which is why a "
            "few big hailstones out-shout a multitude of raindrops - "
            "and dBZ = 10 log10(Z) compresses the enormous range into "
            "readable numbers. Forecasters interrogate volume scans "
            "level by level: the 0.5-degree base reflectivity for "
            "low-level structure (hooks, bows, boundaries), mid-level "
            "slices for bounded weak-echo regions (the BWER, marking "
            "a supercell's violent updraft), storm-top products for "
            "overshooting tops. Velocity couplets are measured as "
            "gate-to-gate shear across the rotation; the tornadic "
            "debris signature adds a correlation-coefficient drop where "
            "lofted wreckage tumbles chaotically. Dual-polarization "
            "variables - differential reflectivity, correlation "
            "coefficient, specific differential phase - let modern "
            "forecasters distinguish rain from hail from debris from "
            "biological scatter, and estimate rainfall far better than "
            "reflectivity alone."
        ),
        "key_points": [
            "Reflectivity in dBZ: <20 drizzle, 35-45 rain, 50+ heavy/hail, 60+ hail likely, 70+ giant hail.",
            "Z-R (Z = 300 R^1.4) converts echo to rain rate; snow and tropical rain use their own relations.",
            "Velocity couplets (adjacent inbound/outbound) mark rotation; hook echoes wrap the mesocyclone.",
            "Bow echoes bend where damaging winds surge; the bright band marks the melting layer.",
            "Dual-polarization separates rain, hail, debris, and biology - and sharpens rainfall estimates.",
        ],
        "requirements": [
            "dBZ scale intuition and Z-R conversion.",
            "Reading base/mid/upper volume-scan products for storm anatomy.",
            "Velocity couplet shear and debris-signature recognition.",
        ],
        "standards": [
            "NEXRAD WSR-88D volume coverage patterns and product suite.",
            "dBZ = 10 log10(Z) with Z in mm^6/m^3.",
        ],
        "citations": [CIT_DOVIAK, CIT_MARKOWSKI],
        "sig_lens": ("Signature edition: radar as his Signature "
                     "flashlight, sweeping the dark inside every storm."),
        "demo_kind": "dbz_rainrate",
    },
    {
        "key": "satellite_interpretation",
        "name": "Satellite Interpretation: Visible, Infrared, Water Vapor, and the Dvorak Technique",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Satellites give forecasters the one view no ground network "
            "can: the whole storm at once, every few minutes. Visible "
            "imagery is sunlight reflected off cloud tops - the "
            "photograph view, best for low clouds, fog, and daytime "
            "convection, dead at night. Infrared imagery measures cloud-"
            "top temperature: the colder (higher) the top, the brighter "
            "the enhancement, so overshooting thunderstorm tops glow "
            "white against gray cirrus - and IR works around the clock. "
            "Water-vapor imagery sees mid- and upper-level moisture: "
            "dark dry slots carve into cyclones, bright moist plumes "
            "feed them, and the swirl of the vapor reveals vorticity "
            "the clouds hide. Forecasters read cloud patterns the way "
            "doctors read X-rays: the comma cloud of a maturing cyclone, "
            "the transverse banding of a jet streak, the enhanced-V "
            "signature of a severe storm's stratospheric fountain. The "
            "Dvorak technique turns this pattern reading into numbers "
            "for tropical cyclones: analysts match the storm's cloud "
            "pattern to archetypes, assign a T-number, and convert to "
            "intensity - the method that has estimated hurricane "
            "strength from space since the 1970s, now automated and "
            "still the backbone of intensity analysis over open ocean."
        ),
        "how_it_works": (
            "Each channel works on different physics. Visible (0.6 "
            "micron) measures reflected solar radiation - thick clouds "
            "are bright, thin cirrus is gray, the ocean is dark. "
            "Infrared (10.3 micron window) measures emitted thermal "
            "radiation; converting brightness temperature to height "
            "with a standard lapse rate puts cloud tops in kilometers, "
            "and color enhancements flag the coldest tops. Water vapor "
            "(6.2 micron) is absorbed and re-emitted by mid-upper "
            "tropospheric moisture - its imagery maps the dynamical "
            "structure: dark regions are descending dry stratospheric "
            "air, the dry slot of a cyclone. Forecasters loop the "
            "imagery to extract motion and evolution: developing "
            "overshooting tops, expanding anvils, wrapping convection. "
            "The Dvorak technique is pattern climatology made rigorous: "
            "the analyst classifies the scene (curved band, shear, eye, "
            "central dense overcast), measures features, assigns the "
            "T-number, applies constraints on how fast intensity may "
            "change, and reads the CI number off to wind speed via the "
            "Dvorak conversion table. Objective algorithms now replicate "
            "the steps, but the human pattern check remains the gold "
            "standard."
        ),
        "key_points": [
            "Visible = reflected sunlight (daytime detail, low clouds/fog). Infrared = cloud-top temperature (24-hour storm tops). Water vapor = mid-upper moisture and dynamics.",
            "IR brightness temperature converts to cloud-top height via the lapse rate; enhancements flag overshooting tops.",
            "Water-vapor dark slots mark descending dry air - the cyclone's dry slot and jet-stream structure.",
            "Cloud-pattern reading: comma clouds, transverse banding, enhanced-V signatures diagnose storm state.",
            "The Dvorak technique converts tropical-cyclone cloud patterns to T-numbers to intensity - the open-ocean standard since the 1970s.",
        ],
        "requirements": [
            "Channel physics: what each band actually measures.",
            "Brightness-temperature to cloud-top-height conversion.",
            "Dvorak pattern types and the T-number to wind conversion.",
        ],
        "standards": [
            "GOES-R series ABI channels as the operational US standard.",
            "Dvorak T/CI number conventions (Dvorak 1984, updated).",
        ],
        "citations": [CIT_KIDDER, CIT_EMANUEL],
        "sig_lens": ("Signature edition: satellites as his Signature "
                     "overlook, the whole weather laid out like a map table."),
        "demo_kind": "ir_cloudtop",
    },
    {
        "key": "nowcasting",
        "name": "Nowcasting: Mesoscale Analysis and Storm-Scale Warning",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Nowcasting is forecasting with the clock running: 0 to 6 "
            "hours, updated every few minutes, aimed at the storm that "
            "is happening now. It is the discipline of the warning "
            "forecaster, the airport tower, and the outdoor stadium - "
            "where a 20-minute tornado warning or a 45-minute hail "
            "warning is the entire product. The method is extrapolation "
            "plus diagnosis: track the storm's motion vector from radar, "
            "extend it forward, and adjust for what the environment "
            "will do to the storm - strengthening over the warm sector, "
            "weakening into the stable air, turning right with the "
            "mean wind. Mesoscale analysis hunts the boundaries that "
            "decide where the next storm fires: outflow boundaries from "
            "old storms, the dryline's moisture gradient, lake-breeze "
            "and sea-breeze fronts, each visible as a fine line on radar "
            "and a wind shift on surface maps. Initiation nowcasting "
            "watches cumulus towers on visible satellite for the first "
            "glaciation and the first 35-dBZ echo. Storm-scale warning "
            "is pattern recognition under time pressure - hook, couplet, "
            "debris - fused with spotter reports and lightning jumps "
            "into a binary decision: warn or wait. Every minute of lead "
            "time is earned here."
        ),
        "how_it_works": (
            "Nowcasting systems blend observation streams that models "
            "cannot wait for. Radar extrapolation advects the current "
            "echo field along storm-motion vectors - simple, and the "
            "best 0-60 minute forecast ever made for existing storms. "
            "Diagnosis adjusts the extrapolation: forecasters overlay "
            "the extrapolated position on mesoscale analyses of "
            "instability, shear, and boundaries to judge intensification "
            "or decay. Convective initiation algorithms track satellite "
            "cloud-top cooling rates - a tower cooling 10+ Celsius in 15 "
            "minutes is about to become a thunderstorm. Warning "
            "decisions follow structured interrogation: reflectivity "
            "structure, velocity couplets, dual-pol debris signatures, "
            "lightning-jump trends, spotter and public reports, each "
            "weighted into the warn/no-warn call. Verification is "
            "immediate and brutal: the storm either produces or it does "
            "not, and the false-alarm rate is the nowcaster's public "
            "report card. Modern warn-on-forecast research aims to "
            "replace extrapolation with storm-scale ensemble models "
            "that predict the next hour's rotation explicitly."
        ),
        "key_points": [
            "Nowcasting: 0-6 hours, updated every few minutes - the warning forecaster's discipline.",
            "Radar extrapolation along storm-motion vectors is the best 0-60 minute forecast for existing storms.",
            "Mesoscale boundaries (outflow, dryline, lake/sea breeze) decide where the NEXT storm fires.",
            "Initiation nowcasting: satellite cloud-top cooling rates and first 35-dBZ echoes.",
            "Warning decisions fuse radar patterns, lightning jumps, and spotter reports under time pressure.",
        ],
        "requirements": [
            "Storm-motion vectors and extrapolation arithmetic.",
            "Boundary identification on radar fine lines and surface analyses.",
            "Structured warning interrogation: reflectivity, velocity, dual-pol, lightning, spotters.",
        ],
        "standards": [
            "NWS storm-based warnings: polygons, not counties, sized to the threat.",
            "Lightning-jump and debris-signature criteria in warning operations.",
        ],
        "citations": [CIT_MARKOWSKI, CIT_DOVIAK],
        "sig_lens": ("Signature edition: nowcasting as his Signature "
                     "reflexes, the sky read and answered in minutes."),
        "demo_kind": "storm_extrapolate",
    },
    # ================= ADVANCED =================
    {
        "key": "nwp_practice",
        "name": "Numerical Weather Prediction in Practice: Models, Grids, and Spin-Up",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Numerical weather prediction is meteorology's moonshot "
            "made routine: the atmosphere's physics, encoded as "
            "equations, stepped forward in time on supercomputers to "
            "predict the weather days ahead. In practice the forecaster "
            "does not run models - the forecaster manages them. Global "
            "models (the American GFS, the European IFS) span the planet "
            "with grid spacing on the order of 9 to 13 kilometers and "
            "reach 10-16 days; convection-allowing models (the HRRR at "
            "3 km) resolve individual thunderstorms but only cover a "
            "region and run 18-48 hours. Every model makes the same "
            "bargains: grid spacing decides which phenomena exist "
            "(a 13-km grid cannot see a 2-km tornado), the timestep must "
            "satisfy the CFL stability condition, and parameterized "
            "physics stands in for sub-grid processes like cumulus "
            "convection and turbulence. Models need spin-up - the first "
            "hours where precipitation and cloud fields organize from "
            "the initial conditions - so forecasters distrust hour 1 "
            "and trust the pattern. The forecaster's practice is model "
            "diagnostics: which model handles this pattern best, where "
            "they agree, where they diverge, and what the spread implies "
            "for confidence."
        ),
        "how_it_works": (
            "NWP solves the primitive equations - conservation of "
            "momentum, mass, energy, and moisture plus the ideal gas "
            "law - on a three-dimensional grid. Data assimilation "
            "builds the starting point: observations blended with the "
            "previous forecast (4D-Var or ensemble Kalman filters at "
            "the major centers) into the analysis. The model steps "
            "forward: dynamics advect the fields, physics parameterizes "
            "radiation, convection, microphysics, and boundary-layer "
            "turbulence at each step. The CFL condition binds the "
            "numerics - information cannot cross more than one grid "
            "cell per timestep, or the solution blows up - so finer "
            "grids demand shorter steps and vastly more computing. "
            "Non-hydrostatic dynamical cores (needed below ~10 km grid "
            "spacing) solve the full vertical momentum equation and "
            "can grow storms explicitly. Forecasters read models as "
            "ensembles of guidance: the deterministic run is one "
            "realization, the ensemble mean is the best single guess, "
            "and the spread is the honest uncertainty. Model biases - "
            "the GFS's convective feedback, every model's terrain "
            "troubles - are learned like colleagues' quirks."
        ),
        "key_points": [
            "NWP solves the primitive equations on a 3D grid; data assimilation builds the starting analysis from observations.",
            "Grid spacing decides what exists: global 9-13 km models miss thunderstorms; 3-km convection-allowing models grow them explicitly.",
            "The CFL condition ties timestep to grid spacing - finer grids cost superlinearly more computing.",
            "Spin-up: distrust the first hours while cloud and precipitation fields organize.",
            "Forecaster practice is model management: biases, agreement, divergence, and spread as confidence.",
        ],
        "requirements": [
            "The primitive equations conceptually: what is conserved and stepped forward.",
            "CFL stability and why resolution costs explode.",
            "Reading deterministic vs ensemble-mean vs spread.",
        ],
        "standards": [
            "WMO global model intercomparison and verification standards.",
            "Operational model cycles (00/06/12/18 UTC) and dissemination formats (GRIB).",
        ],
        "citations": [CIT_KALNAY, CIT_HOLTON],
        "sig_lens": ("Signature edition: the models as his Signature "
                     "orreries, planet-sized clockwork predicting the sky."),
        "demo_kind": "cfl_timestep",
    },
    {
        "key": "ensemble_forecasting",
        "name": "Ensemble Forecasting: Spaghetti Plots and Probabilistic Thinking",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The atmosphere is chaotic - tiny errors in today's analysis "
            "grow into different storms by day five - so the modern "
            "forecast is not one future but many. Ensemble forecasting "
            "runs the same model dozens of times from slightly different "
            "starting points (and with slightly different physics), "
            "producing a bouquet of possible futures. The spaghetti "
            "plot - one contour from each member overlaid - makes "
            "uncertainty visible: tight bundles mean confidence, wild "
            "spray means the atmosphere has not decided. Forecasters "
            "convert ensembles into probabilities: the fraction of "
            "members exceeding a threshold is the forecast probability "
            "of that event, the honest answer to 'will it flood?' The "
            "ensemble mean beats any single run on average; the spread "
            "grows with lead time and shrinks when the flow is "
            "predictable. Spread-skill calibration keeps the system "
            "honest: over a season, events should occur about as often "
            "as the forecast probability said. Probabilistic thinking "
            "is the discipline's maturity - replacing 'it will rain' "
            "with 'there is a 70 percent chance of more than an inch', "
            "the number a farmer, an emergency manager, or a pilot can "
            "actually decide on."
        ),
        "how_it_works": (
            "Ensembles sample the two great uncertainties: initial-"
            "condition error and model error. Initial perturbations are "
            "built to grow - bred vectors or singular vectors target the "
            "fastest-growing instabilities - so the members diverge like "
            "the real atmosphere's uncertainty. Model uncertainty is "
            "sampled with stochastic physics or multi-model ensembles. "
            "Each member is a full forecast; statistics across members "
            "give the mean (the minimum-error single field), the spread "
            "(standard deviation, the uncertainty), and probabilities "
            "(fraction exceeding thresholds). Forecasters read cluster "
            "analysis: when 40 of 50 members take the storm out to sea "
            "and 10 slam the coast, the forecast discusses both "
            "scenarios with weights. Calibration corrects systematic "
            "spread errors - under-dispersive ensembles get their "
            "probabilities widened. Decision science closes the loop: "
            "with a cost-loss model, the optimal action threshold is "
            "the cost-loss ratio, so a 20-percent flood probability "
            "can rationally trigger sandbagging when the loss dwarfs "
            "the cost."
        ),
        "key_points": [
            "Chaos makes one future a lie; ensembles run dozens of perturbed forecasts to sample what's possible.",
            "Spaghetti plots visualize uncertainty: tight bundle = confidence, spray = indecision.",
            "Probability = fraction of members exceeding the threshold - the honest, decidable forecast.",
            "Ensemble mean beats any single run; spread grows with lead time; calibration keeps probabilities honest.",
            "Cost-loss decision theory turns probabilities into actions: act when probability exceeds cost/loss.",
        ],
        "requirements": [
            "Chaos and error growth: why deterministic skill fades with lead time.",
            "Reading spaghetti plots, plume diagrams, and probability maps.",
            "Cost-loss ratios for turning probabilities into decisions.",
        ],
        "standards": [
            "Ensemble probability as member fraction exceeding threshold.",
            "Reliability (calibration) as the probability-forecast quality standard.",
        ],
        "citations": [CIT_KALNAY, CIT_WILKS],
        "sig_lens": ("Signature edition: ensembles as his Signature "
                     "multiverse viewer, every future weighed and priced."),
        "demo_kind": "ensemble_prob",
    },
    {
        "key": "mos_postprocessing",
        "name": "Statistical Post-Processing: Model Output Statistics and Downscaling",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Raw model output is a brilliant but biased colleague: it "
            "knows the atmosphere's physics but systematically runs "
            "warm in valleys, wet on windward slopes, and calm in "
            "stadiums. Statistical post-processing corrects the model "
            "with the model's own history. Model Output Statistics "
            "(MOS) - the classic technique - regresses past model "
            "forecasts against actual observations to learn each "
            "model's habits: when the model says 45 at this station in "
            "this flow, the thermometer really reads 42. The regression "
            "equations are rebuilt regularly as models upgrade, and "
            "separate equations serve every station, variable, and "
            "projection. Modern post-processing goes further: quantile "
            "mapping reshapes whole forecast distributions, machine-"
            "learning corrects spatial patterns, and downscaling bridges "
            "the resolution gap - turning a 13-kilometer grid's valley "
            "average into the frost hollow's actual temperature. The "
            "National Blend of Models fuses many post-processed inputs "
            "into the starting point of the US forecast. Post-processing "
            "is unglamorous and indispensable: it is where model skill "
            "becomes street-level accuracy."
        ),
        "how_it_works": (
            "MOS works as supervised learning on the model's past. For "
            "each station and lead time, years of archived model "
            "forecasts (the predictors: model temperature, humidity, "
            "wind, cloud) are regressed against the observed outcomes "
            "(the predictands: actual high, precipitation occurrence). "
            "Multiple linear regression or logistic regression finds "
            "the weights; the resulting equation corrects systematic "
            "bias and even adds skill the raw model lacks - MOS "
            "precipitation probabilities routinely beat raw model "
            "output. Because models upgrade, MOS equations are re-"
            "derived on reforecast archives: the upgraded model re-run "
            "over past years to build a consistent training set. "
            "Downscaling adds geography: statistical downscaling maps "
            "grid-scale predictors to station scale via the learned "
            "relationships, while dynamical downscaling nests a fine "
            "model inside the coarse one. Forecasters treat post-"
            "processed guidance as the calibrated baseline and add "
            "their own mesoscale judgment on top - the human still "
            "owns the final forecast."
        ),
        "key_points": [
            "Raw models are systematically biased; MOS regresses past forecasts against observations to learn and correct each model's habits.",
            "Separate equations per station, variable, and lead time; reforecast archives retrain them after model upgrades.",
            "MOS precipitation probabilities routinely beat raw model output - statistics add real skill.",
            "Downscaling (statistical and dynamical) bridges grid averages to street-level and frost-hollow reality.",
            "Post-processed guidance is the calibrated baseline; the forecaster's mesoscale judgment goes on top.",
        ],
        "requirements": [
            "Regression intuition: predictors, predictands, and bias correction.",
            "Why model upgrades force MOS redevelopment via reforecasts.",
            "Grid-scale vs station-scale thinking.",
        ],
        "standards": [
            "MOS as the operational US statistical guidance standard (NWS).",
            "Reforecast datasets as the training standard for post-processing.",
        ],
        "citations": [CIT_WILKS, CIT_KALNAY],
        "sig_lens": ("Signature edition: post-processing as his Signature "
                     "editor, polishing the model's rough draft into truth."),
        "demo_kind": "mos_regression",
    },
    {
        "key": "forecast_verification",
        "name": "Forecast Verification: Contingency Tables, POD, FAR, and the Brier Score",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A forecast that is never scored is a story, not a science - "
            "verification is how meteorology keeps its promises honest. "
            "For yes/no events like 'tornado warning' or 'rain tomorrow', "
            "the 2x2 contingency table sorts every forecast into hits, "
            "misses, false alarms, and correct negatives, and the scores "
            "fall out: POD (probability of detection) = hits divided by "
            "all events that happened - did we catch them? FAR (false "
            "alarm ratio) = false alarms divided by all warnings - did "
            "we cry wolf? CSI (critical success index) blends both into "
            "one number. Bias tells whether the system over- or under-"
            "forecasts. For probabilities, the Brier score averages the "
            "squared error between forecast probability and outcome (0 "
            "or 1) - a perfect forecaster scores 0 - and reliability "
            "diagrams check whether 70-percent forecasts really verify "
            "70 percent of the time. Continuous variables get MAE, RMSE, "
            "and anomaly correlation. Verification closes the "
            "forecaster's loop: the scores say which products earn "
            "trust, which need work, and whether the new model actually "
            "beat the old one."
        ),
        "how_it_works": (
            "Verification works by matching forecasts to observations "
            "under strict rules: same location, same valid time, same "
            "threshold, with observations quality-controlled first. The "
            "contingency table fills from the matched pairs, and each "
            "score answers a different question - POD rewards catching "
            "events (at the cost of false alarms), FAR punishes "
            "over-warning, CSI balances both, bias exposes systematic "
            "lean. Skill scores compare against a reference - usually "
            "climatology or persistence - so 'did we beat guessing?' has "
            "a number. The Brier score decomposes into reliability "
            "(calibration), resolution (sorting events from non-events), "
            "and uncertainty (the climate's inherent difficulty) - the "
            "decomposition tells the forecaster exactly what to fix. "
            "For rare high-impact events, verification uses neighborhood "
            "methods that forgive small displacement errors: a "
            "thunderstorm forecast 20 km off is far more useful than the "
            "point-wise score admits. Operational centers verify "
            "everything, publish the scores, and let the numbers - not "
            "reputation - decide which guidance survives."
        ),
        "key_points": [
            "The 2x2 table (hits, misses, false alarms, correct negatives) is the foundation of event verification.",
            "POD = hits/events (did we catch it?); FAR = false alarms/warnings (did we cry wolf?); CSI blends both; bias shows lean.",
            "The Brier score (mean squared probability error) decomposes into reliability, resolution, and uncertainty.",
            "Skill scores measure improvement over climatology or persistence - 'did we beat guessing?'",
            "Neighborhood methods forgive small displacement errors for rare high-impact events.",
        ],
        "requirements": [
            "Building and reading a 2x2 contingency table.",
            "Computing and interpreting POD, FAR, CSI, bias, and Brier score.",
            "Reliability diagrams and what miscalibration looks like.",
        ],
        "standards": [
            "WMO verification standards for forecast quality assessment.",
            "Brier score and contingency-table scores as the categorical/probabilistic standards.",
        ],
        "citations": [CIT_WILKS, CIT_KALNAY],
        "sig_lens": ("Signature edition: verification as his Signature "
                     "audit, every forecast graded against reality."),
        "demo_kind": "verify_scores",
    },
    {
        "key": "aviation_meteorology",
        "name": "Aviation Meteorology: METAR, TAF, and In-Flight Hazards",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Aviation was meteorology's first paying customer and remains "
            "its most demanding: an airliner cannot pull over when the "
            "weather turns. Aviation meteorology speaks in codes built "
            "for speed and unambiguity. The METAR is the hourly surface "
            "observation: 'KJFK 171651Z 28012KT 10SM FEW045 SCT250 22/14 "
            "A2992' decodes to Kennedy Airport, on the 17th at 1651 UTC, "
            "wind 280 at 12 knots, 10 statute miles visibility, few "
            "clouds at 4500 feet, scattered at 25000, temperature 22 C, "
            "dew point 14 C, altimeter 29.92 inches. The TAF is the "
            "aerodrome forecast, typically 24-30 hours, with prevailing "
            "conditions and TEMPO/PROB groups for fluctuations. Aloft, "
            "the hazards are icing (supercooled droplets freezing on "
            "airframes - worst in the 0 to -15 C band), turbulence "
            "(clear-air near jet streams, mountain wave, convective), "
            "thunderstorms, low-level wind shear and microbursts on "
            "approach, and volcanic ash - which melts in engines and is "
            "avoided absolutely via VAAC advisories. SIGMETs warn of "
            "these en route; AIRMETs cover the moderate, widespread "
            "versions. Every flight plan is a weather decision, and the "
            "aviation forecaster's product is measured in diversions "
            "avoided and lives never endangered."
        ),
        "how_it_works": (
            "The system works as a layered information chain. Surface "
            "observations (METAR/SPECI) feed terminal forecasts (TAF) "
            "written by forecasters who blend model guidance with local "
            "knowledge of each airport's terrain traps. En-route "
            "hazards are gridded into world-area forecast products: "
            "icing potential from model temperature and moisture in the "
            "supercooled band, turbulence from shear and stability "
            "diagnostics (Ellrod index, mountain-wave predictors), "
            "convective hazards from storm-top and lightning products. "
            "Pilots receive it as coded text, graphics, and datalinked "
            "updates; dispatchers file routes around the hazards. "
            "Low-level wind shear alert systems and terminal Doppler "
            "radar guard the final approach, where microbursts have "
            "caused historic accidents - the alerts give pilots the "
            "seconds to go around. Volcanic ash advisories from nine "
            "global VAACs draw polygons around ash clouds from "
            "dispersion models, and routes bend around them. The "
            "verification is operational: on-time performance, diversion "
            "rates, and above all the accident record."
        ),
        "key_points": [
            "METAR is the coded hourly observation; TAF the 24-30 hour aerodrome forecast with TEMPO/PROB fluctuations.",
            "In-flight hazards: icing (0 to -15 C supercooled band), clear-air/mountain-wave/convective turbulence, thunderstorms, wind shear, volcanic ash.",
            "SIGMETs warn severe en-route hazards; AIRMETs the moderate widespread ones; VAACs track volcanic ash globally.",
            "Terminal Doppler radar and wind-shear alerts guard final approach against microbursts.",
            "Every flight plan is a weather decision - measured in diversions avoided and the accident record.",
        ],
        "requirements": [
            "Decoding full METARs and TAFs including remarks and change groups.",
            "Icing, turbulence, and wind-shear mechanisms and their forecast products.",
            "SIGMET/AIRMET/VAAC product structure.",
        ],
        "standards": [
            "WMO METAR/SPECI and TAF code forms as the global aviation standard.",
            "ICAO Annex 3 meteorological service for international air navigation.",
        ],
        "citations": [CIT_WMO, CIT_AHRENS],
        "sig_lens": ("Signature edition: aviation weather as his Signature "
                     "flight plan, every airway cleared by his sky."),
        "demo_kind": "metar_decode",
    },
    {
        "key": "outlooks_drought_flood",
        "name": "Hydrologic Outlooks: SPI, Drought, and Flood Forecasting Practice",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Beyond the 7-day forecast lies the outlook business: "
            "weeks-to-seasons predictions of too much and too little "
            "water. Meteorological drought is the starting deficit - "
            "precipitation shortfall - measured on standardized scales "
            "so a dry spell in Seattle and one in Phoenix speak the "
            "same language. The Standardized Precipitation Index (SPI) "
            "fits historical rainfall to a probability distribution and "
            "reports the current anomaly in standard deviations: below "
            "-1.5 is severe drought, below -2 extreme. Different "
            "timescales serve different users: 1-month SPI for "
            "agriculture's flash droughts, 12-month for reservoirs and "
            "groundwater. On the wet side, hydrologic outlooks and "
            "flood watches translate heavy-rain forecasts into river "
            "response: forecasters run quantitative precipitation "
            "forecasts through hydrologic models of each basin, issuing "
            "flood outlooks days ahead and flash-flood warnings when "
            "rain rates overwhelm the landscape's capacity. The "
            "practice links meteorology to hydrology: the atmosphere "
            "supplies the water, the land decides what it becomes."
        ),
        "how_it_works": (
            "Drought monitoring works by standardization: long "
            "precipitation records are fitted (classically to a gamma "
            "distribution), transformed to a standard normal variable, "
            "and the current period's value read off - SPI -2.0 means "
            "drier than about 98 percent of history. The US Drought "
            "Monitor blends SPI with soil moisture, streamflow, and "
            "impact reports into weekly maps with categories D0-D4. "
            "Outlooks use climate signals: ENSO phase, soil-moisture "
            "memory, and seasonal model guidance tilt the odds toward "
            "persistence or relief. Flood outlook practice inverts the "
            "logic: quantitative precipitation forecasts (inches per "
            "basin per 6 hours) feed rainfall-runoff models calibrated "
            "to each watershed; forecast crests are compared against "
            "flood stage, and the products escalate from hydrologic "
            "outlook to flood watch to flood warning as confidence and "
            "imminence grow. Flash-flood guidance - how much rain in "
            "how many hours overwhelms each small basin - is the "
            "nowcaster's tripwire, updated for soil moisture and burn "
            "scars."
        ),
        "key_points": [
            "SPI standardizes precipitation deficits: -1.5 severe drought, -2.0 extreme; timescales match the user (1-month crops, 12-month reservoirs).",
            "The US Drought Monitor blends SPI, soil moisture, streamflow, and impacts into D0-D4 weekly maps.",
            "Seasonal outlooks lean on ENSO, soil-moisture memory, and climate-model guidance.",
            "Flood outlooks run precipitation forecasts through basin hydrologic models; products escalate outlook -> watch -> warning.",
            "Flash-flood guidance (rain per hours per basin, adjusted for soil and burn scars) is the nowcaster's tripwire.",
        ],
        "requirements": [
            "Standardized indices: SPI computation and category thresholds.",
            "Reading Drought Monitor maps and seasonal outlook probabilities.",
            "QPF-to-runoff thinking: how forecast rain becomes forecast crest.",
        ],
        "standards": [
            "SPI categories (McKee et al.): standardized drought severity scale.",
            "NWS hydrologic product suite: outlook, watch, warning, statement.",
        ],
        "citations": [CIT_WILKS, CIT_BARRY],
        "sig_lens": ("Signature edition: drought and flood as his Signature "
                     "ledger of too little and too much, balanced in water."),
        "demo_kind": "spi_category",
    },
    {
        "key": "weather_communication",
        "name": "Weather Communication: Watches, Warnings, Spotters, and the Warning Process",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The finest forecast in the world is worthless if nobody "
            "acts on it - weather communication is the discipline's "
            "final and most human branch. The US watch/warning system "
            "encodes certainty and urgency in two words: a WATCH means "
            "conditions are favorable - be prepared, stay aware; a "
            "WARNING means the hazard is occurring or imminent - take "
            "action now. Tornado watch (the Storm Prediction Center, "
            "county-sized boxes, hours ahead) versus tornado warning "
            "(the local office, storm-based polygon, minutes ahead) is "
            "the canonical pair, mirrored for severe thunderstorms, "
            "flash floods, winter storms, and hurricanes. The warning "
            "process is an integrated system: detection (radar, "
            "satellite, lightning, models), decision (the forecaster's "
            "warn/no-warn call), dissemination (Wireless Emergency "
            "Alerts, NOAA Weather Radio, broadcast, apps), and response "
            "(the public's protective action). SKYWARN spotters - "
            "200,000+ trained volunteers - close the ground-truth loop, "
            "confirming what radar suggests. Social science now rides "
            "along: message wording, false-alarm tolerance, and "
            "understanding how people actually decide are researched "
            "as rigorously as the meteorology."
        ),
        "how_it_works": (
            "The process works as a timed pipeline. Detection fuses "
            "remote sensing with spotter reports: a velocity couplet "
            "plus a trained spotter's funnel report is the gold-standard "
            "warning basis. The decision weighs evidence against cost: "
            "warn too freely and false alarms erode trust (the cry-wolf "
            "effect, measurable in response rates); warn too rarely "
            "and events go unwarned. Storm-based warnings draw polygons "
            "around the threat's path instead of alarming whole "
            "counties, cutting the warned area - and the false-alarm "
            "population - dramatically. Dissemination is redundant by "
            "design: WEA pushes to phones in the polygon, Weather Radio "
            "broadcasts the text, media and apps relay, sirens (where "
            "they exist) are outdoor-only supplements. Impact-based "
            "warnings add damage-threat tags - 'considerable', "
            "'catastrophic' - so a violent tornado's warning reads "
            "differently from a weak one's. Post-event assessment "
            "closes the loop: damage surveys, warning statistics, and "
            "social-science interviews feed back into training, in an "
            "end-to-end system where the last mile is a human being "
            "deciding to shelter."
        ),
        "key_points": [
            "WATCH = conditions favorable (prepare); WARNING = occurring/imminent (act now) - the two-word code of urgency.",
            "The warning pipeline: detection, decision, dissemination (WEA, Weather Radio, media), response.",
            "Storm-based polygon warnings replaced county-wide alerts, slashing false-alarm populations.",
            "SKYWARN's 200,000+ trained spotters supply ground truth that radar cannot.",
            "False-alarm economics and message wording are researched like the meteorology - the last mile is human.",
        ],
        "requirements": [
            "Watch vs warning vs advisory vs outlook for each hazard type.",
            "The detection-decision-dissemination-response pipeline.",
            "Impact-based warning tags and polygon warning logic.",
        ],
        "standards": [
            "NWS watch/warning/advisory product definitions and criteria.",
            "Common Alerting Protocol (CAP) for interoperable dissemination.",
        ],
        "citations": [CIT_AHRENS, CIT_DOSWELL],
        "sig_lens": ("Signature edition: warnings as his Signature alarm "
                     "bells, rung in time for every soul to shelter."),
        "demo_kind": "warn_decision",
    },
    {
        "key": "frontiers_meteorology",
        "name": "Frontiers of Meteorology: AI Forecasting, Warn-on-Forecast, and What's Next",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Meteorology is living through its biggest reinvention since "
            "the first computer forecast in 1950. Machine-learned "
            "weather models - neural networks trained on decades of "
            "reanalysis - now produce 10-day forecasts in minutes on a "
            "single machine, rivaling the physics-based giants on many "
            "scores, and hybrid systems are learning to correct model "
            "bias and downscale to street level. Warn-on-Forecast aims "
            "to replace extrapolation nowcasting with storm-scale "
            "ensemble models that explicitly predict rotation, hail, "
            "and wind 30-60 minutes ahead, giving warnings a model "
            "foundation instead of a radar-only one. Observation "
            "frontiers push downward and outward: phased-array radar "
            "scanning storms in under a minute, geostationary lightning "
            "mappers and hyperspectral sounders watching the pre-storm "
            "environment breathe, dense mesonets and crowd-sourced "
            "pressure sensors filling the gaps between official "
            "stations. Subseasonal-to-seasonal prediction - the "
            "notorious week-2-to-month gap - is yielding to better "
            "ocean-atmosphere coupling and stratospheric pathways. And "
            "the communication frontier treats the forecast as a "
            "decision product: probabilities calibrated to users' "
            "cost-loss realities, delivered where people already look. "
            "The discipline's trajectory is clear: finer, faster, more "
            "probabilistic, and closer to the decision."
        ),
        "how_it_works": (
            "AI forecasting works by learning the atmosphere's evolution "
            "operator from data: trained on reanalysis fields, the "
            "network maps the current state to the state 6 hours ahead, "
            "then iterates - no physics equations, just learned dynamics, "
            "at a fraction of the supercomputing cost. The frontier "
            "problem is physical consistency and extremes: pure data "
            "models can blur the sharp gradients that make weather "
            "dangerous, so hybrid physics-AI systems are the active "
            "research bet. Warn-on-Forecast works by rapid-cycling "
            "storm-scale data assimilation: radar winds are ingested "
            "every few minutes into 1-3 km ensembles, and the short "
            "forecasts explicitly resolve mesocyclones - verification "
            "shows skill at predicting which storms will produce "
            "tornadoes. Phased-array radar works by electronic beam "
            "steering with no moving dish, cutting volume scans from 5 "
            "minutes toward 1 minute. Subseasonal skill works through "
            "slow manifolds: the MJO, sudden stratospheric warmings, "
            "and ocean heat content evolve predictably for weeks and "
            "nudge storm tracks. Each frontier follows the same loop as "
            "the whole discipline: observe better, model smarter, "
            "verify honestly, communicate for decisions."
        ),
        "key_points": [
            "Machine-learned models trained on reanalysis now rival physics models on many scores, in minutes not hours.",
            "Warn-on-Forecast replaces extrapolation with storm-scale ensembles that explicitly predict rotation and hail.",
            "Phased-array radar (sub-minute scans), lightning mappers, and dense mesonets push observation frontiers.",
            "Subseasonal prediction exploits slow manifolds: the MJO, stratospheric warmings, ocean heat content.",
            "The trajectory: finer, faster, more probabilistic, and closer to the user's decision.",
        ],
        "requirements": [
            "How data-driven models learn the evolution operator (conceptually).",
            "Storm-scale data assimilation and ensemble nowcasting concepts.",
            "Slow-manifold sources of subseasonal predictability.",
        ],
        "standards": [
            "Verification standards applied equally to AI and physics-based forecasts.",
            "Reanalysis datasets (ERA5 and successors) as the training record.",
        ],
        "citations": [CIT_KALNAY, CIT_WILKS],
        "sig_lens": ("Signature edition: the frontiers as his Signature "
                     "horizon, the sky's next chapter already being written."),
        "demo_kind": "nowcast_trend",
    },
]
