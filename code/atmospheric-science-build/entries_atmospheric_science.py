#!/usr/bin/env python3
"""Seed entries for the Atmospheric Science field build (field #13, taxonomy order).

Verified 2026-10-17: NO database covers atmospheric science as a discipline.
- 'weather-climate' (10,000 records): deterministic station-observation catalog
  (temperature, humidity, precipitation, wind) - raw observations, no science.
- 'weather' (38 records): short stubs ('Clouds (overview)', 'Weather Radar
  (history)') - no atmospheric science content.
- 'climate' (72 records): 'Essential knowledge: climate' stubs.
- 'climatology' (34 records): climate-system science (energy balance, the
  greenhouse effect, circulation, Koeppen, ENSO, forcings/feedbacks,
  paleoclimate) - shares atmospheric layers and the greenhouse effect at the
  climate level, but none of the discipline machinery: atmospheric
  thermodynamics, parcel theory, lapse rates, stability, cloud microphysics,
  precipitation processes, boundary-layer physics, atmospheric chemistry,
  air quality, atmospheric optics, lightning/electrification, remote sensing,
  numerical weather prediction.
- 'weather-control' (150 records): weather-modification material, not science.

So this build creates two NEW databases:

  atmospheric-science            - The Atmospheric Science Database
                                   (public-harvest: real, fact-checked
                                   atmospheric science - composition,
                                   hydrostatic balance, the gas law,
                                   potential temperature, humidity,
                                   adiabatic lapse rates, stability,
                                   cloud physics, precipitation processes,
                                   thunderstorms, air masses and fronts,
                                   cyclones, scattering, optics,
                                   atmospheric chemistry, aerosols,
                                   air quality, radiative transfer,
                                   the polar vortex, gravity waves,
                                   air-sea exchange, radar, satellites,
                                   numerical weather prediction,
                                   dispersion modeling)
  atmospheric-science-signature  - The Atmospheric Science Signature Database
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

# Shared citation constants (standard atmospheric-science literature)
CIT_WALLACE = ("Wallace, J. M. & Hobbs, P. V. (2006). 'Atmospheric Science: "
               "An Introductory Survey', 2nd ed. Academic Press.")
CIT_HOLTON = ("Holton, J. R. (2004). 'An Introduction to Dynamic Meteorology', "
              "4th ed. Elsevier Academic Press.")
CIT_ROGERS_YAU = ("Rogers, R. R. & Yau, M. K. (1989). 'A Short Course in Cloud "
                  "Physics', 3rd ed. Butterworth-Heinemann.")
CIT_SEINFELD = ("Seinfeld, J. H. & Pandis, S. N. (2016). 'Atmospheric Chemistry "
                "and Physics: From Air Pollution to Climate Change', 3rd ed. "
                "Wiley.")
CIT_PETTY = ("Petty, G. W. (2006). 'A First Course in Atmospheric Radiation', "
             "2nd ed. Sundog Publishing.")
CIT_MARKOWSKI = ("Markowski, P. & Richardson, Y. (2010). 'Mesoscale Meteorology "
                 "in Midlatitudes'. Wiley-Blackwell.")
CIT_STULL = ("Stull, R. B. (1988). 'An Introduction to Boundary Layer "
             "Meteorology'. Kluwer Academic.")
CIT_DOVIAK = ("Doviak, R. J. & Zrnic, D. S. (1993). 'Doppler Radar and Weather "
              "Observations', 2nd ed. Academic Press.")
CIT_EMANUEL = ("Emanuel, K. A. (1994). 'Atmospheric Convection'. Oxford "
               "University Press.")
CIT_BLUESTEIN = ("Bluestein, H. B. (1992). 'Synoptic-Dynamic Meteorology in "
                 "Midlatitudes', vol. 1. Oxford University Press.")
CIT_KIDDER = ("Kidder, S. Q. & Vonder Haar, T. H. (1995). 'Satellite "
              "Meteorology: An Introduction'. Academic Press.")

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "atmospheric science, clearly labeled Signature-made, never "
            "presented as authentic public record.")

ENTRIES = [
    # ================= FOUNDATIONS =================
    {
        "key": "what_is_atmospheric_science",
        "name": "What Atmospheric Science Is",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Atmospheric science is the physics, chemistry, and fluid dynamics "
            "of the thin gas shell wrapped around the planet. Where meteorology "
            "studies day-to-day weather and climatology studies long-term "
            "climate statistics, atmospheric science studies the machinery "
            "underneath both: why pressure falls with height, why warm air can "
            "hold more water vapor than cold air, how a cloud droplet is born, "
            "why lightning separates charge, how sunlight scatters blue. The "
            "field splits into three great branches. Atmospheric dynamics "
            "treats the air as a rotating fluid and derives the winds from "
            "Newton's laws. Atmospheric physics treats radiation, "
            "thermodynamics, and cloud processes - the heat engines that move "
            "energy around. Atmospheric chemistry treats the trace gases and "
            "particles, from the ozone shield to city smog. Observation binds "
            "them together: surface stations, weather balloons, Doppler radar, "
            "and satellites measure the same atmosphere the theory describes, "
            "and numerical models stitch all three branches into forecasts."
        ),
        "how_it_works": (
            "Atmospheric science works by writing conservation laws for a "
            "parcel of air and solving them. Mass conservation says air cannot "
            "vanish: what flows into a box must flow out or pile up. Momentum "
            "conservation gives the wind: pressure gradients push, the "
            "Coriolis force turns, friction slows. Energy conservation gives "
            "the temperature: sunlight heats, infrared cools, rising air "
            "expands and cools, condensation warms. These laws become the "
            "primitive equations, and every forecast model is a numerical "
            "solution of them on a grid. Chemistry adds reaction kinetics for "
            "trace species; microphysics adds the birth and growth of cloud "
            "droplets and ice crystals; radiation adds the sunlight-in, "
            "infrared-out bookkeeping. Each subfield makes predictions that "
            "instruments can check: a parcel theory predicts the cloud base, "
            "radar measures whether the cloud is really there."
        ),
        "key_points": [
            "Atmospheric science is the machinery under both weather and climate: dynamics, physics, and chemistry of the air.",
            "Dynamics: the rotating-fluid equations that produce the winds. Physics: radiation, thermodynamics, clouds. Chemistry: trace gases and particles.",
            "Observation (stations, balloons, radar, satellites) and numerical modeling bind the branches together.",
            "Conservation of mass, momentum, and energy applied to air parcels is the common foundation.",
            "Every theory makes testable predictions: parcel theory predicts cloud bases, radar checks them.",
        ],
        "requirements": [
            "Fluency in the three branches: be able to name which branch any question belongs to.",
            "Basic calculus and physics: derivatives, pressure, density, temperature, energy.",
            "A habit of checking theory against instruments - radar, soundings, satellite images.",
        ],
        "standards": [
            "Quantities use SI units: pressure in hectopascals, temperature in kelvin or Celsius, wind in meters per second.",
            "World Meteorological Organization observation standards govern how atmospheric data is taken and reported.",
        ],
        "citations": [CIT_WALLACE, CIT_BLUESTEIN],
        "sig_lens": (
            "Signature edition: the atmosphere reframed as his great planetary "
            "engine-room, every parcel a labeled Signature unit of sky."
        ),
        "demo_kind": "atm_branches",
    },
    {
        "key": "composition_of_air",
        "name": "The Composition of Air",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Dry air is remarkably constant almost everywhere: about 78.08 "
            "percent nitrogen, 20.95 percent oxygen, 0.93 percent argon, and "
            "then the trace gases that run the show - carbon dioxide near "
            "420 parts per million, neon, helium, methane near 1.9 parts per "
            "million, plus variable water vapor that can range from nearly "
            "zero in a desert to 4 percent in the humid tropics. Turbulent "
            "mixing keeps the major gases uniform up to about 100 kilometers; "
            "above that, the homosphere gives way to the heterosphere where "
            "each gas sorts itself by molecular weight. Water vapor is the "
            "wild card: it is the dominant greenhouse gas, the fuel of "
            "clouds and storms, and the only major constituent that changes "
            "phase in the atmosphere, releasing latent heat when it "
            "condenses. Dalton's law says each gas contributes its own partial "
            "pressure in proportion to its fraction - the total pressure is "
            "simply the sum of the parts."
        ),
        "how_it_works": (
            "Air behaves as an ideal-gas mixture, so each constituent obeys "
            "Dalton's law independently: the partial pressure of nitrogen is "
            "78.08 percent of the total, of oxygen 20.95 percent, and so on. "
            "Because nitrogen and oxygen are chemically inert in the "
            "troposphere and have no sources or sinks fast enough to matter, "
            "turbulent stirring keeps their ratio fixed from the surface to "
            "about 100 kilometers - dry air has one constant mean molecular "
            "weight, 28.97 grams per mole, everywhere. Trace gases differ "
            "because chemistry and sources break the uniformity: ozone is "
            "manufactured by sunlight in the stratosphere, methane leaks from "
            "wetlands and decays by reacting with the hydroxyl radical, and "
            "carbon dioxide rises steadily because fossil-fuel burning outruns "
            "the ocean and land sinks. Water vapor follows temperature, not "
            "mixing: warm air can hold exponentially more of it, which is why "
            "the tropics are humid and the poles are dry."
        ),
        "key_points": [
            "Dry air is 78.08% nitrogen, 20.95% oxygen, 0.93% argon - constant to ~100 km by turbulent mixing.",
            "Trace gases (CO2, methane, ozone) vary because chemistry and sources break uniformity.",
            "Water vapor is the wild card: 0 to 4%, the main greenhouse gas, the fuel of clouds, the only phase-changer.",
            "Dalton's law: each gas adds its own partial pressure in proportion to its fraction.",
            "Mean molecular weight of dry air: 28.97 g/mol - the constant behind every density calculation.",
        ],
        "requirements": [
            "Know the big three fractions (78.08 / 20.95 / 0.93) and today's CO2 level near 420 ppm.",
            "Apply Dalton's law to convert volume fractions to partial pressures.",
            "Separate well-mixed gases (uniform) from chemically active gases (variable).",
        ],
        "standards": [
            "Mixing ratios report dry-air mole fractions; water vapor is quoted separately as specific humidity or mixing ratio.",
            "CO2 reference values follow the standard global monitoring network annual means.",
        ],
        "citations": [CIT_WALLACE, CIT_SEINFELD],
        "sig_lens": (
            "Signature edition: the air as his catalogued mixture, every gas a "
            "labeled Signature constituent with its own partial-pressure share."
        ),
        "demo_kind": "composition",
    },
    {
        "key": "scale_of_the_sky",
        "name": "The Scale of the Sky",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The atmosphere feels bottomless but is thin beyond imagining. "
            "Its total mass is about 5.15 quadrillion kilograms, and the "
            "weight of that column is what a barometer reads: 1013 "
            "hectopascals at sea level, which is just the mass of air above "
            "each square meter pressing down. Half the mass sits below 5.5 "
            "kilometers; 99 percent sits below 32 kilometers. The scale "
            "height - the distance over which pressure falls by a factor of "
            "e, about 8.4 kilometers for typical surface conditions - is the "
            "natural yardstick of the sky: every scale height up, density and "
            "pressure drop to about 37 percent. Space agencies draw the "
            "Karman line at 100 kilometers, where the air is so thin that a "
            "wing would have to fly at orbital speed to make lift. The "
            "temperature profile divides the sky into the troposphere, "
            "stratosphere, mesosphere, and thermosphere, each boundary marked "
            "by a reversal in the temperature trend."
        ),
        "how_it_works": (
            "The scale height comes from hydrostatic balance plus the gas "
            "law: pressure falls exponentially with height, p(z) = p0 exp(-z/"
            "H), where H = R T / g is about 8.4 kilometers at 288 kelvin. "
            "This single number sets the vertical scale of everything - the "
            "tropopause sits near 1.4 scale heights in the tropics, the "
            "stratosphere spans another few, and the mesosphere ends where "
            "the density is a hundred-thousandth of sea level. Because the "
            "exponential compounds, the numbers collapse fast: at 12 "
            "kilometers pressure is a quarter of sea level; at 32 kilometers "
            "it is one percent; at 85 kilometers, the mesopause, it is a "
            "millionth. Pilots, mountaineers, and satellite designers all "
            "live by the scale height - it tells you how much sky is actually "
            "above you, and how quickly it stops mattering."
        ),
        "key_points": [
            "Total atmospheric mass: ~5.15 quadrillion kg; sea-level pressure 1013 hPa is that weight per square meter.",
            "Half the mass is below 5.5 km; 99% below 32 km.",
            "Scale height H = RT/g (~8.4 km): pressure falls by e every H, to ~37% per step.",
            "Temperature reversals define the troposphere, stratosphere, mesosphere, thermosphere.",
            "The Karman line at 100 km marks where wings must fly at orbital speed for lift.",
        ],
        "requirements": [
            "Use the exponential pressure formula p = p0 exp(-z/H) for quick altitude estimates.",
            "Know the mass fractions: half below 5.5 km, 99% below 32 km.",
            "Name the four layers and the pauses (tropopause, stratopause, mesopause) that bound them.",
        ],
        "standards": [
            "The standard atmosphere (1013.25 hPa, 288.15 K at sea level) is the reference every altimeter is calibrated against.",
            "Altitude reports distinguish geometric height from pressure altitude.",
        ],
        "citations": [CIT_WALLACE, CIT_HOLTON],
        "sig_lens": (
            "Signature edition: the sky measured as his layered edifice, each "
            "scale height a catalogued Signature shelf of thinning air."
        ),
        "demo_kind": "scale_height",
    },
    {
        "key": "hydrostatic_balance",
        "name": "Hydrostatic Balance and the Hypsometric Equation",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The atmosphere does not collapse under its own weight or explode "
            "into space because of hydrostatic balance: at every level, the "
            "upward pressure force exactly balances the downward weight of "
            "the air above. In symbols, dp/dz = -rho g - the pressure falls "
            "with height at exactly the rate needed to support the mass "
            "above. This is the single most-used equation in atmospheric "
            "science, and it is why barometers measure altitude: pressure is "
            "the weight of the sky. Integrate it with the gas law and you "
            "get the hypsometric equation, which converts the mean "
            "temperature of a layer into its thickness: a warm layer is "
            "thicker than a cold one, so thickness charts on weather maps are "
            "really temperature maps. When vertical accelerations are "
            "negligible - true almost everywhere except inside violent "
            "updrafts - hydrostatic balance lets forecasters infer the "
            "three-dimensional temperature field from surface pressure alone."
        ),
        "how_it_works": (
            "Consider a thin slab of air: pressure pushes up on its bottom "
            "face, pushes down on its top face, and gravity pulls the slab "
            "down. Balance gives dp = -rho g dz. Substitute density from the "
            "ideal gas law, rho = p / (R T), and integrate between two "
            "pressure levels: the layer thickness delta-z = (R T_mean / g) "
            "ln(p1/p2). That is the hypsometric equation. Forecasters use it "
            "constantly: the thickness between 1000 and 500 hectopascals "
            "grows about 20 meters per degree Celsius of layer warming, so "
            "a thick 1000-500 hPa layer means warm air and a thin one means "
            "cold. The 540-decameter line - 5400 meters of thickness - "
            "roughly separates rain from snow in winter storms. Where "
            "hydrostatic balance breaks down, in thunderstorm cores with "
            "10-meter-per-second-squared accelerations, models must go "
            "non-hydrostatic and resolve the updrafts explicitly."
        ),
        "key_points": [
            "Hydrostatic balance dp/dz = -rho g: pressure force balances weight at every level.",
            "Pressure is literally the weight of the air above - that is why barometers read altitude.",
            "The hypsometric equation turns layer-mean temperature into layer thickness.",
            "Thickness charts are temperature maps: warm layers are thick, cold layers thin.",
            "It breaks down only in violent updrafts, where models must go non-hydrostatic.",
        ],
        "requirements": [
            "Derive dp/dz = -rho g from a force balance on an air slab.",
            "Compute layer thickness from mean temperature with the hypsometric equation.",
            "Know the 540-dam 1000-500 hPa thickness rule for rain versus snow.",
        ],
        "standards": [
            "Thickness is reported in geopotential decameters on standard pressure charts.",
            "The 1000-500 hPa thickness is the standard layer for air-mass identification.",
        ],
        "citations": [CIT_WALLACE, CIT_HOLTON],
        "sig_lens": (
            "Signature edition: the sky weighed layer by layer, every "
            "hectopascal accounted as his Signature ledger of pressure."
        ),
        "demo_kind": "hydrostatic",
    },
    {
        "key": "gas_law_for_air",
        "name": "The Gas Law for Air",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The ideal gas law, p = rho R T, is the equation of state of the "
            "atmosphere: it ties the three measurable state variables - "
            "pressure, density, temperature - into one rigid relationship. "
            "Warm a fixed mass of air and at constant pressure it must "
            "expand and grow less dense; compress it and it warms. The gas "
            "constant for dry air is 287 joules per kilogram per kelvin, "
            "derived from the universal constant divided by air's mean "
            "molecular weight. Moist air gets a correction: water vapor is "
            "lighter than dry air, so humid air is less dense than dry air "
            "at the same temperature and pressure - the reason meteorologists "
            "use virtual temperature, the temperature dry air would need to "
            "match the density of the moist sample. Every density "
            "calculation in atmospheric science - from balloon lift to "
            "aircraft performance to buoyancy of a thunderstorm updraft - "
            "starts here."
        ),
        "how_it_works": (
            "The law works because air at atmospheric pressures is a dilute "
            "gas: molecules rarely interact except in brief collisions, so "
            "pressure is just the momentum of impacts per unit area. Density "
            "follows directly: rho = p / (R T). At sea level, 101325 "
            "pascals divided by (287 times 288.15 kelvin) gives 1.225 "
            "kilograms per cubic meter - the familiar sea-level density. For "
            "moist air, replace T with the virtual temperature Tv = T (1 + "
            "0.61 q), where q is the specific humidity; a tropical airmass "
            "with 20 grams of vapor per kilogram of air is about 1.2 percent "
            "less dense than dry air at the same temperature, enough to "
            "matter for buoyancy. Combined with hydrostatic balance, the gas "
            "law yields the exponential pressure profile and the scale "
            "height; combined with the first law of thermodynamics, it yields "
            "the adiabatic lapse rates."
        ),
        "key_points": [
            "p = rho R T with R = 287 J/(kg K) for dry air ties pressure, density, and temperature.",
            "Sea-level standard: 101325 Pa / (287 x 288.15 K) = 1.225 kg/m3.",
            "Humid air is LESS dense than dry air - water vapor is lighter than N2 and O2.",
            "Virtual temperature Tv = T(1 + 0.61q) lets the dry-air law handle moist air.",
            "With hydrostatic balance it gives the exponential atmosphere; with the first law it gives the adiabats.",
        ],
        "requirements": [
            "Compute density from any (p, T) pair and virtual temperature from specific humidity.",
            "Explain why humid air rises more easily than dry air at the same temperature.",
            "Derive the scale height H = RT/g from the gas law plus hydrostatic balance.",
        ],
        "standards": [
            "R_d = 287.05 J/(kg K) is the standard dry-air gas constant in meteorological computation.",
            "Density altitude for aviation is defined from this law against the standard atmosphere.",
        ],
        "citations": [CIT_WALLACE, CIT_HOLTON],
        "sig_lens": (
            "Signature edition: pressure, density, and temperature bound as "
            "his Signature triple-law, every cubic meter of sky accounted."
        ),
        "demo_kind": "gas_law",
    },
    {
        "key": "potential_temperature",
        "name": "Potential Temperature",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Potential temperature is the temperature a parcel of air would "
            "have if you squeezed it adiabatically - no heat exchanged - "
            "down to a reference pressure of 1000 hectopascals. It is the "
            "atmosphere's way of stripping out the compressional warming "
            "that comes with descent, leaving only the parcel's true heat "
            "content. The formula is theta = T (1000/p)^(R/cp), about T "
            "times a pressure correction. Its power is conservation: for dry "
            "adiabatic motion, potential temperature never changes, so a "
            "parcel keeps its theta as it rises and cools or sinks and "
            "warms. That makes theta the atmosphere's label for air masses - "
            "a polar airmass and a tropical airmass keep their distinct "
            "potential temperatures even as they move - and the vertical "
            "gradient of theta is the cleanest measure of static stability: "
            "theta increasing with height means stable, stratified air."
        ),
        "how_it_works": (
            "Start from the first law for an adiabatic process: the "
            "temperature change of a rising parcel comes only from expansion "
            "work, dT/T = (R/cp) dp/p. Integrate from the parcel's pressure "
            "p up to 1000 hPa and the combination theta = T (1000/p)^kappa, "
            "with kappa = R/cp = 0.286, emerges as the invariant. A parcel at "
            "500 hPa and 250 K has theta near 306 K - squeeze it to 1000 hPa "
            "and it would warm to 306 K. Meteorologists plot theta on "
            "cross-sections because fronts and the tropopause show up as "
            "tightly packed theta surfaces: the tropopause is where the "
            "stratosphere's high-theta air begins. Stability falls out "
            "immediately: if the environment's theta increases with height "
            "faster than a lifted parcel's constant theta, the displaced "
            "parcel is colder and denser than its surroundings and sinks "
            "back - stable. If theta decreases with height, the atmosphere "
            "is convectively unstable."
        ),
        "key_points": [
            "theta = T(1000/p)^0.286: the temperature a parcel would have at 1000 hPa, compressed adiabatically.",
            "Conserved for dry adiabatic motion - the atmosphere's label for tracking air masses.",
            "theta increasing with height = stable; decreasing with height = unstable.",
            "Fronts and the tropopause appear as packed theta surfaces on cross-sections.",
            "The moist equivalent, theta-e, adds latent heat and is conserved in saturated ascent.",
        ],
        "requirements": [
            "Compute theta for any sounding level and interpret a theta profile for stability.",
            "Explain why theta is conserved while ordinary temperature is not.",
            "Read theta cross-sections to locate fronts and the tropopause.",
        ],
        "standards": [
            "The 1000 hPa reference level is the universal convention for potential temperature.",
            "kappa = R/cp = 0.286 for dry air is the standard exponent.",
        ],
        "citations": [CIT_WALLACE, CIT_HOLTON],
        "sig_lens": (
            "Signature edition: potential temperature as his Signature heat-"
            "label, every parcel carrying its immutable thermal identity."
        ),
        "demo_kind": "potential_temp",
    },
    {
        "key": "humidity_measures",
        "name": "Humidity: Vapor Pressure, Dew Point, and Relative Humidity",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Humidity is measured several ways because no single number tells "
            "the whole story. The vapor pressure is the partial pressure of "
            "water vapor, typically a few to a few tens of hectopascals. The "
            "mixing ratio is the mass of vapor per mass of dry air, in grams "
            "per kilogram - conserved when a parcel rises unsaturated, which "
            "makes it the forecaster's favorite. The dew point is the "
            "temperature to which air must be cooled at constant pressure to "
            "reach saturation; the spread between temperature and dew point "
            "is the forecaster's quick read on how close the air is to "
            "making cloud. Relative humidity is the ratio of actual vapor "
            "pressure to the saturation value, and it is famously "
            "misleading: 100 percent RH in cold air holds far less water "
            "than 50 percent in hot air, because saturation vapor pressure "
            "grows exponentially with temperature - the Clausius-Clapeyron "
            "relation, about 7 percent more capacity per degree Celsius."
        ),
        "how_it_works": (
            "Saturation vapor pressure follows the Clausius-Clapeyron "
            "equation, es(T): warmer air can hold exponentially more vapor "
            "because faster molecules escape the liquid surface more "
            "readily. The Magnus approximation, es = 6.112 exp(17.67 T / (T "
            "+ 243.5)) with T in Celsius, is accurate to a fraction of a "
            "percent across meteorological temperatures. Relative humidity "
            "is e/es times 100; cool unsaturated air at constant vapor "
            "pressure and its RH climbs until e equals es - that temperature "
            "is the dew point, found by inverting the Magnus formula. When "
            "a parcel rises, it expands and cools at the dry adiabatic "
            "rate while its mixing ratio stays fixed; saturation arrives "
            "when the falling temperature meets the dew point - the lifting "
            "condensation level, the flat base of every fair-weather cumulus. "
            "The 7-percent-per-degree rule is why a warming world holds more "
            "vapor, fuels heavier downpours, and dries soils faster."
        ),
        "key_points": [
            "Vapor pressure, mixing ratio, dew point, and relative humidity each answer a different question.",
            "Clausius-Clapeyron: saturation capacity rises ~7% per degree C - the exponential behind humidity.",
            "Dew point = the temperature at which cooling air saturates; T-Td spread measures cloud readiness.",
            "Mixing ratio is conserved in unsaturated ascent - the forecaster's conserved humidity variable.",
            "Relative humidity misleads across temperatures: 100% in cold air holds little water.",
        ],
        "requirements": [
            "Compute saturation vapor pressure with the Magnus formula and invert it for dew point.",
            "Convert between vapor pressure, mixing ratio, and relative humidity.",
            "Use the T-Td spread to judge how close air is to saturation.",
        ],
        "standards": [
            "Dew point is reported to 0.1 C; relative humidity as an integer percent in routine observations.",
            "The Magnus/Tetens formula is the WMO-accepted approximation for saturation vapor pressure.",
        ],
        "citations": [CIT_WALLACE, CIT_ROGERS_YAU],
        "sig_lens": (
            "Signature edition: humidity decoded as his Signature moisture "
            "ledger, every gram of vapor tracked against its saturation limit."
        ),
        "demo_kind": "humidity",
    },
    {
        "key": "boundary_layer",
        "name": "The Atmospheric Boundary Layer",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The boundary layer is the lowest kilometer or two of the "
            "atmosphere, the part that feels the ground. Friction, heating, "
            "and evaporation from the surface churn it into turbulence, "
            "while the free atmosphere above glides nearly frictionless. By "
            "day, sunshine heats the ground, thermals rise, and the mixed "
            "layer deepens to 1-2 kilometers; by night, the ground cools, "
            "turbulence collapses, and a shallow stable layer a few hundred "
            "meters deep forms under a residual layer left over from the "
            "day. Wind in the boundary layer spirals with height - the Ekman "
            "spiral: friction slows the surface wind, weakening the Coriolis "
            "force, so the wind turns toward low pressure and speeds up with "
            "altitude until it joins the geostrophic flow at the top. "
            "Everything humans breathe, every pollutant, every gust that "
            "hits a building, lives in this layer."
        ),
        "how_it_works": (
            "Turbulence is the boundary layer's engine: eddies from "
            "millimeters to the layer depth mix momentum, heat, and moisture "
            "far faster than molecular diffusion ever could. The logarithmic "
            "wind profile, u(z) = (u*/k) ln(z/z0), describes the lowest tens "
            "of meters, where u* is the friction velocity and z0 the "
            "roughness length - a few centimeters over grass, meters over a "
            "city. Above that, the Ekman solution balances pressure "
            "gradient, Coriolis, and turbulent drag: the wind vector rotates "
            "about 45 degrees and grows toward geostrophic with height in "
            "the textbook case, less in reality. The daytime convective "
            "mixed layer is capped by an inversion that thermals cannot "
            "pierce; pollutants accumulate beneath that lid, which is why "
            "smog episodes track the mixing depth. At night the surface "
            "inversion decouples the ground from the winds aloft, and a "
            "low-level jet can form just above the inversion, racing at "
            "20-plus meters per second while the surface sits calm."
        ),
        "key_points": [
            "The boundary layer (lowest ~1-2 km) is the turbulent, friction-felt part of the atmosphere.",
            "Day: deep convective mixed layer. Night: shallow stable layer under a residual layer.",
            "Ekman spiral: friction turns the surface wind toward low pressure; it straightens with height.",
            "The log wind profile u = (u*/k) ln(z/z0) governs the lowest tens of meters.",
            "Pollutants pool under the capping inversion - mixing depth controls air quality episodes.",
        ],
        "requirements": [
            "Sketch the diurnal cycle: mixed layer, residual layer, nocturnal stable layer.",
            "Apply the log wind profile given roughness length and friction velocity.",
            "Explain the Ekman spiral as the three-way balance of pressure gradient, Coriolis, and drag.",
        ],
        "standards": [
            "Surface wind is measured at the standard 10-meter height; temperature at 2 meters.",
            "Roughness lengths follow standard land-use tables in dispersion and wind-energy work.",
        ],
        "citations": [CIT_STULL, CIT_WALLACE],
        "sig_lens": (
            "Signature edition: the boundary layer as his Signature ground-"
            "truth zone, the turbulent skin where the sky meets the Earth."
        ),
        "demo_kind": "boundary_layer",
    },
    # ================= COMPOUNDED =================
    {
        "key": "dry_adiabatic_lapse_rate",
        "name": "The Dry Adiabatic Lapse Rate",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Lift a parcel of unsaturated air and it cools at almost exactly "
            "9.8 degrees Celsius per kilometer - the dry adiabatic lapse "
            "rate, one of the most reliable numbers in all of atmospheric "
            "science. No heat enters or leaves the parcel; it simply "
            "expands as the pressure around it falls, and expansion work "
            "costs internal energy, so the temperature drops. Sink the "
            "parcel and the reverse happens: compression warms it at the "
            "same rate, which is why downslope winds like the foehn, the "
            "chinook, and the Santa Ana arrive hot and desiccating. The rate "
            "comes straight from the first law of thermodynamics combined "
            "with hydrostatic balance: Gamma-d = g/cp, gravity divided by "
            "the specific heat of air. It is the baseline every other lapse "
            "rate is judged against - the atmosphere is stable when the "
            "environment cools with height more slowly than this, and "
            "unstable when it cools faster."
        ),
        "how_it_works": (
            "The derivation is clean. First law for an adiabatic change: cp "
            "dT = (1/rho) dp, the heat added equals the work done. Divide "
            "by dz, substitute hydrostatic dp/dz = -rho g, and the density "
            "cancels: dT/dz = -g/cp. With g = 9.81 and cp = 1004 joules per "
            "kilogram per kelvin, the lapse rate is 9.76 K/km, rounded to "
            "9.8. A parcel lifted 2 kilometers cools 19.6 degrees; pushed "
            "back down it recovers every degree. Potential temperature is "
            "conserved along this path by construction - the dry adiabat "
            "is a line of constant theta. Real soundings rarely show the "
            "full 9.8 degrees per kilometer through deep layers, because "
            "any layer steeper than dry-adiabatic overturns within minutes: "
            "convection mixes it back toward the adiabat. That self-"
            "correction is why the dry adiabatic lapse rate is both a "
            "process rate and a stability boundary."
        ),
        "key_points": [
            "Unsaturated rising air cools 9.8 C per km; sinking air warms at the same rate.",
            "Gamma-d = g/cp from the first law plus hydrostatic balance - no tunable parameters.",
            "Downslope winds (foehn, chinook, Santa Ana) are dry-adiabatic warming made destructive.",
            "The dry adiabat is a line of constant potential temperature.",
            "It is also the stability boundary: steeper environmental lapse rates overturn by convection.",
        ],
        "requirements": [
            "Derive Gamma-d = g/cp from the first law and hydrostatic balance.",
            "Compute parcel temperature after any unsaturated vertical displacement.",
            "Use the dry adiabat as the reference for judging environmental stability.",
        ],
        "standards": [
            "cp = 1004 J/(kg K) for dry air is the standard specific heat in lapse-rate work.",
            "Adiabats on thermodynamic diagrams (Skew-T) are drawn for the dry rate below saturation.",
        ],
        "citations": [CIT_WALLACE, CIT_HOLTON],
        "sig_lens": (
            "Signature edition: the dry adiabat as his Signature cooling law, "
            "9.8 degrees per kilometer of his rising sky."
        ),
        "demo_kind": "dry_adiabat",
    },
    {
        "key": "moist_adiabatic_lapse_rate",
        "name": "The Moist Adiabatic Lapse Rate",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Once a rising parcel saturates, the rules change: water vapor "
            "begins condensing, and every gram that condenses releases about "
            "2500 joules of latent heat into the parcel, partially offsetting "
            "the expansion cooling. The moist adiabatic lapse rate is "
            "therefore gentler than the dry rate - typically 4 to 7 degrees "
            "Celsius per kilometer, steepest in cold air (little vapor to "
            "condense) and shallowest in warm tropical air (vapor-rich). This "
            "single fact shapes the planet's temperature profile: the "
            "tropical troposphere follows the moist adiabat almost exactly, "
            "which is why the tropical tropopause is so cold and high. It "
            "also explains why thunderstorms are tropical creatures at "
            "heart - warm moist ascent stays buoyant far longer when "
            "condensation keeps reheating the parcel. The quantity conserved "
            "along a saturated ascent is equivalent potential temperature, "
            "theta-e, which folds the latent heat into the parcel's "
            "accounting."
        ),
        "how_it_works": (
            "The moist rate comes from the same first law, now with a "
            "latent-heating term: cp dT + L dq_s = (1/rho) dp, where dq_s is "
            "the change in saturation mixing ratio. Solving for dT/dz gives "
            "Gamma-m = Gamma-d times a correction factor involving L, the "
            "saturation mixing ratio, and temperature - the correction is "
            "near 1 in cold air and drops toward 0.4 in warm moist air. In "
            "practice meteorologists read the moist adiabat off a Skew-T "
            "diagram as the curved green lines. A saturated parcel lifted "
            "from 20 C at the surface following the moist adiabat reaches "
            "the tropopause still warmer than its environment in the deep "
            "tropics - the engine of the Hadley circulation's rising branch. "
            "Equivalent potential temperature, theta-e = theta exp(L q_s / "
            "cp T), is conserved for reversible saturated ascent and is the "
            "standard tracer for moist air masses and the energy available "
            "to convection."
        ),
        "key_points": [
            "Saturated ascent cools 4-7 C/km, not 9.8 - latent heat release offsets expansion cooling.",
            "Moist rate is shallowest in warm air (vapor-rich) and steepest in cold air.",
            "The tropical troposphere follows the moist adiabat - setting the cold, high tropical tropopause.",
            "Equivalent potential temperature (theta-e) is the conserved quantity for moist ascent.",
            "Thunderstorm buoyancy depends on this: condensation reheats the rising parcel.",
        ],
        "requirements": [
            "Explain why the moist rate varies with temperature while the dry rate is constant.",
            "Read moist adiabats on a Skew-T diagram.",
            "Use theta-e to compare the energy of different moist air masses.",
        ],
        "standards": [
            "L = 2.5 x 10^6 J/kg is the standard latent heat of vaporization at 0 C.",
            "Moist adiabats on standard thermodynamic diagrams assume pseudo-adiabatic (condensate removed) ascent.",
        ],
        "citations": [CIT_WALLACE, CIT_ROGERS_YAU],
        "sig_lens": (
            "Signature edition: the moist adiabat as his Signature reheating "
            "law, condensation paying back the cooling of the climb."
        ),
        "demo_kind": "moist_adiabat",
    },
    {
        "key": "static_stability",
        "name": "Static Stability of the Atmosphere",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Static stability asks one question: if you nudge a parcel of "
            "air upward, does it keep rising, sink back, or hover? The "
            "answer comes from comparing the environment's lapse rate to "
            "the parcel's. If the environment cools with height more slowly "
            "than the dry adiabat, a lifted parcel finds itself colder and "
            "denser than its surroundings and sinks back - stable air, the "
            "smooth flying and layered stratus kind. If the environment "
            "cools faster than the dry adiabat, the parcel stays warmer "
            "than its surroundings and accelerates upward - unstable air, "
            "the towering cumulus kind. Between them lies conditional "
            "instability, the atmosphere's loaded spring: stable for dry "
            "parcels but unstable once saturation unleashes latent heat. "
            "Inversions - layers where temperature increases with height - "
            "are stability incarnate, capping convection and trapping "
            "pollution beneath them."
        ),
        "how_it_works": (
            "The parcel method makes it quantitative. Lift a parcel dry-"
            "adiabatically to some height and compare its temperature to "
            "the environment's: the buoyancy is g (T_parcel - T_env) / "
            "T_env. Positive buoyancy accelerates the parcel upward; "
            "negative pushes it back. Three regimes follow from the "
            "environmental lapse rate Gamma: Gamma < Gamma-m means "
            "absolutely stable; Gamma-m < Gamma < Gamma-d means "
            "conditionally unstable (stable dry, unstable saturated); "
            "Gamma > Gamma-d means absolutely unstable. In potential-"
            "temperature language, stability is d(theta)/dz > 0. The "
            "Brunt-Vaisala frequency, N = sqrt((g/theta) d(theta)/dz), is "
            "the oscillation frequency of a parcel bobbing in stable air - "
            "typically a 5-to-10-minute period - and when N squared goes "
            "negative the atmosphere convects. Forecasters read stability "
            "off soundings in seconds: steep low-level lapse rates plus "
            "moisture mean a volatile day."
        ),
        "key_points": [
            "Stability = environment lapse rate vs parcel lapse rate; buoyancy g(Tp-Te)/Te decides.",
            "Absolutely stable (Gamma < Gamma-m), conditionally unstable (between the adiabats), absolutely unstable (Gamma > Gamma-d).",
            "Conditional instability is the loaded spring behind most thunderstorms.",
            "In potential-temperature terms: d(theta)/dz > 0 is stable.",
            "The Brunt-Vaisala frequency N measures how stiffly stable air resists displacement.",
        ],
        "requirements": [
            "Classify a sounding layer into the three stability regimes from its lapse rate.",
            "Compute parcel buoyancy and the Brunt-Vaisala frequency.",
            "Recognize inversions as stability caps on soundings.",
        ],
        "standards": [
            "Stability indices (Lifted Index, Showalter) are computed from standard mandatory pressure levels.",
            "Inversion strength is reported as the temperature increase across the inversion layer.",
        ],
        "citations": [CIT_WALLACE, CIT_HOLTON],
        "sig_lens": (
            "Signature edition: stability as his Signature verdict on the "
            "sky, every layer judged rising, sinking, or waiting."
        ),
        "demo_kind": "stability",
    },
    {
        "key": "lifting_condensation_level",
        "name": "The Lifting Condensation Level and Cloud Base",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Every fair-weather cumulus has a flat bottom, and that flat "
            "bottom is the lifting condensation level - the height where a "
            "surface parcel, rising and cooling at the dry adiabatic rate, "
            "first reaches saturation. The flatness is no coincidence: "
            "parcels across the whole field start from similar surface "
            "temperature and dew point, so they all saturate at the same "
            "altitude. The rule of thumb is beautifully simple - cloud base "
            "in meters is about 125 times the dew-point depression (T minus "
            "Td) in Celsius - so a 10-degree spread means a cloud base near "
            "1250 meters. Above the LCL the parcel follows the moist "
            "adiabat, and whether the cloud grows into a towering "
            "cumulonimbus or stays a fair-weather puff depends on the "
            "stability found there. The LCL also sets the convective "
            "condensation level and anchors every estimate of thunderstorm "
            "potential."
        ),
        "how_it_works": (
            "The rising parcel cools at 9.8 C per kilometer while its dew "
            "point falls only about 1.8 C per kilometer (the dew-point lapse "
            "rate, since saturation vapor pressure drops with cooling). The "
            "two lines converge: the height where they meet is the LCL. "
            "Dividing the surface dew-point depression by the difference of "
            "the rates, 9.8 minus 1.8 = 8.0 C per kilometer, gives height in "
            "kilometers = (T - Td)/8, or about 125 meters per degree - the "
            "forecaster's rule. On a Skew-T the LCL is found graphically: "
            "follow the dry adiabat up from the surface temperature and the "
            "mixing-ratio line up from the surface dew point; their "
            "intersection is the LCL. If the LCL sits below the level of "
            "free convection, surface parcels can reach it and storms can "
            "fire; if a strong inversion caps below the LCL, the day stays "
            "blue."
        ),
        "key_points": [
            "The LCL is where a rising surface parcel first saturates - the flat base of cumulus clouds.",
            "Rule of thumb: cloud base (m) = 125 x (T - Td in C).",
            "Parcel cools 9.8 C/km; dew point falls ~1.8 C/km - their convergence sets the LCL.",
            "On a Skew-T: dry adiabat from T meets mixing-ratio line from Td at the LCL.",
            "Above the LCL the parcel follows the moist adiabat; stability there decides cloud growth.",
        ],
        "requirements": [
            "Estimate cloud base from surface T and Td with the 125 rule.",
            "Locate the LCL graphically on a Skew-T diagram.",
            "Relate LCL height to the day's convective potential.",
        ],
        "standards": [
            "Cloud-base height is reported in meters above ground level in routine observations.",
            "The 125 m/C factor is the accepted operational approximation (exact value varies slightly).",
        ],
        "citations": [CIT_WALLACE, CIT_ROGERS_YAU],
        "sig_lens": (
            "Signature edition: the cloud base fixed as his Signature "
            "saturation line, every cumulus bottom sharing one altitude."
        ),
        "demo_kind": "lcl",
    },
    {
        "key": "cloud_droplet_growth",
        "name": "Cloud Droplet Growth: Kohler Theory",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Clouds should not exist - and the reason they do is written in "
            "Kohler theory. Pure water vapor needs several hundred percent "
            "relative humidity to nucleate a droplet from nothing, because "
            "curving a surface costs energy (the Kelvin effect): tiny "
            "droplets evaporate faster than they grow. Real clouds cheat "
            "with cloud condensation nuclei - salt, sulfate, dust, and "
            "organic particles, typically a few hundred per cubic centimeter "
            "over land - whose dissolved solute lowers the required humidity "
            "(the Raoult effect). The Kohler curve combines both effects: "
            "for each nucleus size and chemistry there is a critical "
            "supersaturation, usually well under 1 percent, past which the "
            "droplet grows uncontrollably into a cloud droplet. Bigger, "
            "saltier nuclei activate first; the rest wait their turn. This "
            "is why maritime clouds with few nuclei have few large droplets "
            "and rain easily, while polluted continental clouds have many "
            "tiny droplets that stubbornly refuse to rain."
        ),
        "how_it_works": (
            "The Kohler equation gives the equilibrium supersaturation over "
            "a solution droplet: S = a/r - b/r^3, where the a/r Kelvin term "
            "raises the required humidity for small drops and the b/r^3 "
            "solute term lowers it. The curve peaks at the critical radius "
            "r_c = sqrt(3b/a) with critical supersaturation S_c = 2a/(3 "
            "r_c): below the peak a droplet in subsaturated air sits in "
            "stable equilibrium as haze; push the ambient supersaturation "
            "past S_c and no equilibrium exists - the droplet activates and "
            "grows by diffusion. For a 0.1-micron salt nucleus, S_c is about "
            "0.1 percent, trivially reached in any updraft. Growth then "
            "proceeds by vapor diffusion, dr/dt proportional to (S - "
            "S_eq)/r, fast for small drops and slowing as they grow - which "
            "is why condensation alone stalls near 20 microns and "
            "collision-coalescence must take over for rain. Human activity "
            "adds nuclei, brightens clouds, and suppresses drizzle: the "
            "aerosol indirect effect."
        ),
        "key_points": [
            "Homogeneous nucleation needs ~several hundred % RH; real clouds use nuclei to cheat.",
            "Kelvin effect (curvature raises required RH) vs Raoult effect (solute lowers it) = Kohler curve.",
            "Each nucleus has a critical supersaturation (often < 1%); past it, the droplet activates and grows.",
            "Bigger, saltier nuclei activate first - maritime clouds rain easily, polluted ones resist.",
            "Condensation stalls near 20 microns; rain needs collision-coalescence beyond that.",
        ],
        "requirements": [
            "Sketch a Kohler curve and identify the critical radius and supersaturation.",
            "Explain the Kelvin and solute terms and which dominates at small vs large sizes.",
            "Connect nuclei concentration to cloud brightness and rain efficiency.",
        ],
        "standards": [
            "CCN concentrations are reported per cubic centimeter at stated supersaturations (e.g. 0.2%, 1.0%).",
            "Kohler theory uses the standard kappa hygroscopicity parameterization in modern work.",
        ],
        "citations": [CIT_ROGERS_YAU, CIT_SEINFELD],
        "sig_lens": (
            "Signature edition: droplet birth as his Signature activation "
            "law, every cloud droplet earning its growth past the Kohler peak."
        ),
        "demo_kind": "kohler",
    },
    {
        "key": "cloud_types",
        "name": "Cloud Types: The Ten Genera",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Clouds are classified by height and shape into ten genera, a "
            "system formalized by Luke Howard in 1803 and refined ever "
            "since. High clouds (above ~6 km) are the cirrus family - "
            "cirrus, cirrostratus, cirrocumulus - thin veils of ice "
            "crystals. Middle clouds (2-6 km) are altocumulus and altostratus, "
            "the gray sheets that thicken ahead of storms. Low clouds "
            "(below ~2 km) are stratus, stratocumulus, and cumulus, plus the "
            "nimbus pair: nimbostratus, the steady rain sheet, and "
            "cumulonimbus, the thunderstorm king that spans all heights. "
            "The names are Latin shorthand - cirro for curl, alto for high, "
            "stratus for layer, cumulus for heap, nimbus for rain - and they "
            "encode physics: layer clouds mean stable air, heaped clouds "
            "mean convection, ice-crystal veils mean the cold upper "
            "troposphere. Reading clouds is reading the atmosphere's "
            "stability, moisture, and motion at a glance."
        ),
        "how_it_works": (
            "The classification keys off two observables: the cloud's "
            "altitude, which sets its phase (ice above about -20 C, mixed "
            "in between, liquid near the surface), and its texture, which "
            "reveals the formation mechanism. Stratiform clouds form by "
            "broad gentle lifting - a warm front sliding up, or air cooling "
            "to its dew point in place - in stable air that resists "
            "vertical motion, so they spread horizontally. Cumuliform "
            "clouds form by localized buoyant ascent in unstable air, so "
            "they grow vertically: cumulus humilis (fair weather), mediocris, "
            "congestus, then cumulonimbus with its anvil flattened at the "
            "tropopause. Cirrus forms from ice crystals nucleating in the "
            "cold upper troposphere, often as the outflow anvils of distant "
            "storms or in jet-stream turbulence. Observers report cloud "
            "cover in oktas (eighths of sky) by genus, and the sequence of "
            "genera through the day - cirrus thickening to altostratus to "
            "nimbostratus - is the classic visual forecast of an approaching "
            "warm front."
        ),
        "key_points": [
            "Ten genera in three height families: high (cirrus...), middle (alto...), low (stratus, cumulus...) plus nimbostratus and cumulonimbus.",
            "Layer clouds = stable air and broad lifting; heaped clouds = convection and instability.",
            "Altitude sets phase: ice crystals high, supercooled mix in the middle, liquid drops low.",
            "The cirrus-to-nimbostratus sequence is the classic visual warm-front forecast.",
            "Cumulonimbus is the only genus spanning all heights, anvil flattened at the tropopause.",
        ],
        "requirements": [
            "Identify all ten genera from photographs by height and texture.",
            "Infer stability and lifting mechanism from cloud type.",
            "Report cloud cover in oktas by genus as observers do.",
        ],
        "standards": [
            "Cloud genera follow the WMO International Cloud Atlas classification.",
            "Cloud-base heights use the standard high/middle/low etages (thresholds vary by latitude).",
        ],
        "citations": [CIT_WALLACE, CIT_ROGERS_YAU],
        "sig_lens": (
            "Signature edition: the ten genera as his Signature cloud "
            "catalog, every sky readable at a glance."
        ),
        "demo_kind": "cloud_types",
    },
    {
        "key": "warm_rain_process",
        "name": "Warm Rain: Collision and Coalescence",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "In the warm tropics, rain falls from clouds whose tops never "
            "freeze. The warm-rain process builds raindrops purely by "
            "collision and coalescence: cloud droplets around 10-20 microns "
            "drift downward at slightly different speeds, the larger ones "
            "falling faster and sweeping up the smaller ones in their path. "
            "Each merger makes the collector bigger, faster, and hungrier - "
            "a runaway that can grow a millimeter raindrop in 20-30 minutes "
            "in a vigorous updraft. The mathematics is the stochastic "
            "collection equation, balancing the sweep-out volume (pi R^2 "
            "times fall-speed difference) against the cloud's liquid water "
            "content. Collection efficiency matters: tiny droplets flow "
            "around the collector on its airstream instead of colliding, so "
            "a broad droplet spectrum with a few large starter drops rains "
            "far faster than a narrow spectrum of uniform droplets. This is "
            "why maritime clouds rain easily and polluted clouds, full of "
            "tiny uniform droplets, hold their water back."
        ),
        "how_it_works": (
            "Fall speed sets everything. Stokes' law gives small droplets a "
            "fall speed proportional to radius squared: a 10-micron droplet "
            "falls about 1 cm/s, a 100-micron drizzle drop about 27 cm/s, a "
            "1-mm raindrop about 4 m/s. The differential fall speed means a "
            "100-micron collector sweeps a cylinder of cloud at 26 cm/s "
            "relative to the 10-micron background, collecting a fraction E "
            "(the collection efficiency) of the droplets in its path. The "
            "continuous-collection model, dM/dt = pi R^2 (V - v) E w_L, "
            "integrates to raindrop size in tens of minutes for w_L near 1 "
            "g/m^3. But efficiency collapses when collector and collected "
            "are nearly the same size - equal drops fall together and never "
            "meet - so the process needs a broad spectrum to start. Giant "
            "sea-salt nuclei provide the starter drops over oceans; over "
            "polluted continents the spectrum stays narrow and the cloud "
            "must grow taller, colder, and icier before rain can begin."
        ),
        "key_points": [
            "Warm rain needs no ice: differential fall speeds let big drops sweep up small ones.",
            "Fall speed grows with size (Stokes regime ~ r^2), so mergers accelerate - a runaway process.",
            "Collection efficiency collapses for equal-sized drops; a broad spectrum is required.",
            "A millimeter raindrop can grow in 20-30 minutes in liquid water near 1 g/m^3.",
            "Maritime clouds (broad spectra, giant salt nuclei) rain easily; polluted clouds resist.",
        ],
        "requirements": [
            "Compute Stokes fall speeds and explain the r^2 dependence.",
            "Write the continuous-collection growth equation and identify each term.",
            "Explain why narrow droplet spectra suppress warm rain.",
        ],
        "standards": [
            "Droplet sizes are reported as diameter in microns; rain as millimeters.",
            "Liquid water content is reported in grams per cubic meter from standard probes.",
        ],
        "citations": [CIT_ROGERS_YAU, CIT_WALLACE],
        "sig_lens": (
            "Signature edition: warm rain as his Signature merger law, "
            "every raindrop grown by sweeping the sky."
        ),
        "demo_kind": "warm_rain",
    },
    {
        "key": "bergeron_process",
        "name": "Cold Rain: The Bergeron-Findeisen Process",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Outside the tropics, most rain begins as snow. The Bergeron-"
            "Findeisen process exploits a subtle asymmetry: at the same "
            "subfreezing temperature, the saturation vapor pressure over "
            "ice is lower than over liquid water. In a mixed-phase cloud, "
            "the air can be saturated with respect to water yet "
            "supersaturated with respect to ice - so ice crystals grow "
            "rapidly by vapor deposition while neighboring droplets "
            "evaporate to feed them. A crystal that starts at a tenth of a "
            "millimeter can grow to a millimeter snowflake in minutes, then "
            "fall, sweeping up droplets (riming) and aggregating with other "
            "crystals. Melting on the way down through the freezing level "
            "turns the snow into the rain that reaches the ground. Without "
            "this process, mid-latitude precipitation would be a fraction "
            "of what it is; with it, a single ice nucleus per liter can "
            "seed a shower."
        ),
        "how_it_works": (
            "The vapor-pressure difference peaks near -15 C, where the "
            "ice-water saturation gap is largest and the growth rate "
            "maximizes - the dendritic growth zone, where the classic "
            "six-branched snowflakes form. Depositional growth follows dm/"
            "dt = 4 pi C D (rho_v - rho_vs_ice), with capacitance C set by "
            "crystal shape. Ice nuclei are rare - about one per liter at "
            "-20 C, versus hundreds of droplets per cubic centimeter - so "
            "a few crystals feast on abundant vapor, growing hundreds of "
            "microns while droplets merely maintain themselves. Falling "
            "crystals rime: supercooled droplets freeze on contact, building "
            "graupel, and graupel colliding with crystals in updrafts is "
            "the charge-separation engine of lightning. The melting level "
            "appears on radar as the bright band, a ring of enhanced "
            "reflectivity where snowflakes collapse into raindrops. Seed a "
            "supercooled cloud with silver iodide and you add nuclei the "
            "cloud lacked - the entire basis of cloud seeding."
        ),
        "key_points": [
            "Saturation vapor pressure is lower over ice than water: ice grows while droplets evaporate.",
            "The growth-rate peak near -15 C is the dendritic snowflake zone.",
            "Ice nuclei are rare (~1/liter) vs droplets (~100/cm3) - a few crystals feast on abundant vapor.",
            "Riming (droplets freezing onto crystals) builds graupel and drives thunderstorm charging.",
            "The radar bright band marks the melting level where snow becomes rain.",
        ],
        "requirements": [
            "Explain the ice-water vapor-pressure asymmetry and why it peaks near -15 C.",
            "Trace a snowflake's path: nucleation, deposition, riming, aggregation, melting.",
            "Identify the bright band on radar and what it signifies.",
        ],
        "standards": [
            "Ice-nucleus concentrations are reported per liter at stated temperatures.",
            "The melting level is identified operationally by the radar bright band.",
        ],
        "citations": [CIT_ROGERS_YAU, CIT_WALLACE],
        "sig_lens": (
            "Signature edition: cold rain as his Signature ice-theft law, "
            "crystals growing fat on stolen vapor."
        ),
        "demo_kind": "bergeron",
    },
    {
        "key": "thunderstorm_life_cycle",
        "name": "The Thunderstorm Life Cycle",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A single-cell thunderstorm lives about 30-60 minutes and dies "
            "by its own hand. The cumulus stage is pure updraft: warm moist "
            "air rises, condenses, and builds the tower. The mature stage "
            "adds the downdraft: precipitation drags air down, evaporative "
            "cooling accelerates it, and the cold outflow spreads at the "
            "surface as a gust front that can lift new cells. The "
            "dissipating stage is downdraft-dominated: rain-cooled air "
            "chokes off the updraft's warm inflow and the storm collapses. "
            "Wind shear changes everything. With shear, the updraft tilts "
            "away from the downdraft and the storm stops killing itself - "
            "multicell clusters chain new cells along the gust front for "
            "hours, and supercells with rotating updrafts (mesocyclones) "
            "can live for many hours, spawning the most violent tornadoes "
            "and giant hail. The outflow boundary of one storm is the "
            "trigger of the next: thunderstorms breed."
        ),
        "how_it_works": (
            "Buoyancy drives the updraft: CAPE, the integrated positive "
            "buoyancy between the level of free convection and the "
            "equilibrium level, sets the theoretical maximum updraft speed "
            "w = sqrt(2 CAPE) - 2000 J/kg gives about 63 m/s, though water "
            "loading and entrainment cut real updrafts to half that. The "
            "downdraft is driven by precipitation drag plus evaporative "
            "cooling; when rain falls into dry mid-level air, evaporation "
            "can chill the downdraft 5-10 C below the environment, producing "
            "microbursts with surface winds over 50 m/s. Shear organizes: "
            "the cold pool's gust front lifts warm air while mid-level "
            "winds ventilate the updraft, separating it from the rain "
            "shaft. In a supercell, streamwise vorticity is tilted into "
            "the vertical by the updraft, creating the mesocyclone - a "
            "2-10 km rotating updraft visible on Doppler radar as a "
            "velocity couplet. The rear-flank downdraft wraps around the "
            "mesocyclone, and tornadoes form in that embrace."
        ),
        "key_points": [
            "Single cells live 30-60 min in three stages: cumulus, mature, dissipating - killed by their own cold outflow.",
            "CAPE sets the updraft ceiling: w_max = sqrt(2 x CAPE).",
            "Downdrafts come from precipitation drag plus evaporative cooling; microbursts can exceed 50 m/s.",
            "Wind shear separates updraft from downdraft: multicells chain for hours, supercells rotate.",
            "Supercell mesocyclones (rotating updrafts) spawn the most violent tornadoes and giant hail.",
        ],
        "requirements": [
            "Name the three life-cycle stages and what drives each transition.",
            "Estimate maximum updraft speed from CAPE.",
            "Explain how shear and the cold pool organize multicells and supercells.",
        ],
        "standards": [
            "Thunderstorm days are defined by thunder heard at a station; severe thresholds are 58+ mph winds or 1-inch+ hail.",
            "Supercell identification follows standard radar velocity-couplet criteria.",
        ],
        "citations": [CIT_MARKOWSKI, CIT_WALLACE],
        "sig_lens": (
            "Signature edition: the thunderstorm as his Signature engine of "
            "the sky, living and dying by its own cold breath."
        ),
        "demo_kind": "thunderstorm",
    },
    {
        "key": "air_masses_and_fronts",
        "name": "Air Masses and Fronts",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Air masses are continent-sized parcels with uniform "
            "temperature and moisture, named for their source regions: "
            "maritime tropical (warm, moist), continental polar (cold, "
            "dry), arctic, maritime polar, continental tropical, and the "
            "equatorial doldrums. Where two air masses meet, the boundary "
            "is a front - a narrow zone of sharp temperature contrast a "
            "few tens of kilometers wide but thousands long. Cold fronts "
            "wedge under warm air, lifting it violently along a steep slope: "
            "squall lines, gusty winds, sharp temperature drops. Warm "
            "fronts slide gently over the retreating cold air on a shallow "
            "slope: broad shields of steady rain announced hours ahead by "
            "thickening high cloud. When the cold front catches the warm "
            "front, the warm air is lifted bodily off the ground and an "
            "occluded front forms, marking the storm's maturity. Fronts "
            "are where the atmosphere does its heaviest weather."
        ),
        "how_it_works": (
            "Fronts exist because the temperature contrast concentrates. "
            "Frontogenesis - the sharpening of a temperature gradient by "
            "deformation in the wind field - squeezes isotherms together "
            "where confluent flow pushes warm and cold air toward each "
            "other. The cross-front circulation is thermally direct: warm "
            "air rises on the warm side, cold air sinks on the cold side, "
            "with the frontal slope set by the Margules formula balancing "
            "the temperature contrast against the wind shear across the "
            "front. Cold fronts slope about 1:50 to 1:100 (steep, violent "
            "lift); warm fronts about 1:150 to 1:300 (gentle, widespread "
            "lift). The Norwegian cyclone model strings the fronts onto "
            "the low: the warm sector between them, the cold front "
            "trailing, the warm front leading, occlusion wrapping up at "
            "maturity. Upper-level dynamics drive it all: divergence aloft "
            "evacuates mass, surface pressure falls, and the fronts tighten "
            "as the cyclone deepens."
        ),
        "key_points": [
            "Air masses (mT, cP, mP, cT, arctic) are uniform source-region parcels; fronts are their battle lines.",
            "Cold fronts: steep (~1:50), violent lift, squall lines, sharp drops. Warm fronts: shallow (~1:200), broad steady rain.",
            "Frontogenesis sharpens gradients where confluent winds push air masses together.",
            "The Margules formula sets frontal slope from temperature contrast and wind shear.",
            "Occlusion - cold front catching warm front - lifts the warm sector off the ground at storm maturity.",
        ],
        "requirements": [
            "Name the air-mass types and their temperature/moisture signatures.",
            "Contrast cold-front and warm-front slope, weather, and cloud sequences.",
            "Sketch the Norwegian cyclone model with its three fronts.",
        ],
        "standards": [
            "Fronts are analyzed on surface charts using standard symbols (triangles cold, semicircles warm).",
            "Air-mass classification follows the Bergeron scheme (source region + moisture).",
        ],
        "citations": [CIT_BLUESTEIN, CIT_WALLACE],
        "sig_lens": (
            "Signature edition: fronts as his Signature clash-lines, "
            "continent-sized air masses meeting at his drawn boundaries."
        ),
        "demo_kind": "fronts",
    },
    {
        "key": "midlatitude_cyclones",
        "name": "Mid-Latitude Cyclones",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The mid-latitude cyclone is the great weather-maker of the "
            "temperate zones - the comma-shaped cloud swirl on satellite "
            "images that brings a week of weather in two days. It is born "
            "on the polar front where cold polar air meets warm subtropical "
            "air, and it feeds on the temperature contrast: the storm "
            "converts the atmosphere's available potential energy into the "
            "kinetic energy of its winds, exactly like a heat engine "
            "running on the equator-to-pole gradient. A mature cyclone "
            "spans 1000-2000 kilometers, with a warm conveyor belt streaming "
            "moist air up and over the warm front (the rain shield), a cold "
            "conveyor belt wrapping around the low, and a dry intrusion "
            "descending behind the cold front (the clearing slot). Cyclones "
            "travel eastward with the jet stream at 10-20 m/s, deepening "
            "where upper-level divergence evacuates mass faster than "
            "surface convergence replaces it."
        ),
        "how_it_works": (
            "Baroclinic instability is the engine: a wavy perturbation on "
            "the polar-front temperature gradient grows by leaning its "
            "warm air poleward and upward, releasing potential energy. The "
            "quasi-geostrophic omega equation diagnoses the vertical "
            "motion: differential vorticity advection and the Laplacian of "
            "thermal advection force ascent ahead of the upper trough, "
            "lowering surface pressure. The conveyor belts organize the "
            "moisture transport: the warm conveyor belt rises 5-8 "
            "kilometers along the warm front, its condensation heating "
            "feeding back into the ascent; the cold conveyor belt hugs the "
            "surface north of the warm front, overrunning into freezing "
            "rain and ice-storm territory. Cyclogenesis favors the east "
            "coasts of continents and the lee of mountains, where the "
            "temperature gradient is sharpest. The storm occludes as the "
            "cold front overtakes the warm front, cutting off the warm "
            "sector's energy supply; the low then fills and dies over 3-7 "
            "days, having marched a few thousand kilometers."
        ),
        "key_points": [
            "Mid-latitude cyclones are baroclinic heat engines running on the equator-to-pole temperature contrast.",
            "The warm conveyor belt (moist ascent, rain shield), cold conveyor belt, and dry intrusion organize the storm.",
            "Upper-level divergence ahead of the trough deepens the surface low.",
            "Cyclogenesis favors east coasts and mountain lee sides with sharp temperature gradients.",
            "Occlusion cuts off the warm sector; the storm fills over 3-7 days after traveling thousands of km.",
        ],
        "requirements": [
            "Explain baroclinic instability as potential-to-kinetic energy conversion.",
            "Name the three conveyor belts and the weather each produces.",
            "Read a surface + 500 hPa chart pair to locate cyclogenesis regions.",
        ],
        "standards": [
            "Cyclone intensity is reported by minimum central pressure in hectopascals.",
            "Conveyor-belt analysis follows the standard Carlson (1980) airstream framework.",
        ],
        "citations": [CIT_BLUESTEIN, CIT_HOLTON],
        "sig_lens": (
            "Signature edition: the cyclone as his Signature heat engine, "
            "the polar front's contrast converted to wind."
        ),
        "demo_kind": "cyclone",
    },
    {
        "key": "scattering",
        "name": "Scattering: Why the Sky Is Blue",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "The sky is blue because air molecules are picky about which "
            "light they scatter. Rayleigh scattering - scattering by "
            "particles far smaller than the wavelength, like nitrogen and "
            "oxygen molecules - has an intensity proportional to one over "
            "wavelength to the fourth power. Blue light at 450 nanometers "
            "is scattered about 5-6 times more strongly than red light at "
            "650 nanometers, so looking away from the sun you see the "
            "scattered blue from every direction. At sunset the sunlight "
            "crosses ten times more air; the blue has been scattered away "
            "long before the beam reaches you, leaving the transmitted reds "
            "and oranges. Bigger particles - haze, smoke, cloud droplets - "
            "scatter by Mie theory with weak wavelength dependence, which "
            "is why clouds are white and polluted sunsets are milky. The "
            "same physics lets satellites see through the atmosphere in "
            "window wavelengths and be blinded in absorption bands."
        ),
        "how_it_works": (
            "A molecule's electrons oscillate in the light's electric field "
            "and re-radiate as a tiny dipole antenna; the radiated power "
            "scales as the fourth power of the frequency, hence lambda^-4. "
            "The Rayleigh scattering cross-section of air at 550 nm is "
            "about 5 x 10^-31 m^2 per molecule - tiny, but with 2.5 x 10^25 "
            "molecules per cubic meter the optical depth at zenith reaches "
            "about 0.14 in the blue, meaning roughly 13 percent of blue "
            "sunlight is scattered out of the direct beam. The scattered "
            "light is strongly polarized at 90 degrees from the sun - "
            "bees and Viking navigators alike have used the polarization "
            "pattern as a compass. Mie scattering takes over when the size "
            "parameter (2 pi r / lambda) approaches one: the phase function "
            "develops a fierce forward lobe, which is why the aureole "
            "around the sun glares white and why forward-scatter sensors "
            "detect thin cirrus. Volcanic aerosols, at just the wrong size, "
            "scatter blue preferentially forward - the blue moon after "
            "Krakatoa."
        ),
        "key_points": [
            "Rayleigh scattering scales as lambda^-4: blue (~450 nm) scatters ~5-6x more than red (~650 nm).",
            "Blue sky = scattered sunlight from all directions; red sunset = blue removed along a long path.",
            "Zenith optical depth ~0.14 in blue: ~13% of blue sunlight scattered out of the beam.",
            "Mie scattering (particles ~ wavelength) is weakly color-dependent: clouds white, haze milky.",
            "Scattered skylight is polarized at 90 deg from the sun - a natural compass.",
        ],
        "requirements": [
            "Compute the blue-to-red scattering ratio from the lambda^-4 law.",
            "Explain sunset reddening via path length and optical depth.",
            "Distinguish Rayleigh from Mie regimes by the size parameter.",
        ],
        "standards": [
            "Aerosol optical depth is reported at standard wavelengths (440, 550, 870 nm) by sun-photometer networks.",
            "The Angstrom exponent quantifies the wavelength dependence of aerosol scattering.",
        ],
        "citations": [CIT_PETTY, CIT_WALLACE],
        "sig_lens": (
            "Signature edition: the blue sky as his Signature scattering "
            "law, every photon sorted by wavelength."
        ),
        "demo_kind": "scattering",
    },
    {
        "key": "atmospheric_optics",
        "name": "Atmospheric Optics: Rainbows, Halos, and Mirages",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "The atmosphere is a lens, and its optical phenomena are "
            "geometry made visible. The primary rainbow is sunlight "
            "refracted into a raindrop, reflected once inside, and "
            "refracted back out, emerging at 42 degrees from the antisolar "
            "point - red on the outside because red bends least. A second "
            "internal reflection makes the fainter secondary bow at 51 "
            "degrees with colors reversed, and Alexander's dark band "
            "between them where neither bow sends light. Halos are the "
            "ice-crystal equivalent: hexagonal plates and columns in "
            "cirrus refract sunlight into the 22-degree halo, sundogs at "
            "22 degrees left and right of the sun, and the circumzenithal "
            "arc. Mirages are refraction by temperature gradients: hot "
            "road air bends light upward (inferior mirage), while a strong "
            "inversion bends it downward, looming distant ships above the "
            "horizon (superior mirage, the fata morgana). Every one is a "
            "remote-sensing measurement of the air's structure."
        ),
        "how_it_works": (
            "Descartes ray-tracing gives the rainbow angles: for a drop of "
            "refractive index n, the deviation angle for one internal "
            "reflection has a minimum at the rainbow angle, concentrating "
            "light there - 42.0 degrees for red (n=1.331), 40.6 for violet "
            "(n=1.344), the spread making the color separation. Two "
            "reflections give the secondary at 50.6 degrees, reversed. "
            "Ice halos use the 60-degree prism angle of hexagonal ice: "
            "minimum deviation through a 60-degree prism is 21.8 degrees "
            "for red, 22.4 for blue - the 22-degree halo. Sundogs need "
            "plate crystals falling with faces horizontal, refracting "
            "through alternate faces. Mirages follow Snell's law in a "
            "continuous gradient: rays curve toward denser (colder) air, "
            "with curvature radius R = n / (dn/dz); when the curvature "
            "matches Earth's curvature, rays duct and objects hundreds of "
            "kilometers away become visible. Coronas around the moon - "
            "diffraction by uniform small droplets - even measure droplet "
            "size from the ring's angular radius."
        ),
        "key_points": [
            "Primary rainbow: one internal reflection, 42 deg from antisolar point, red outside.",
            "Secondary bow: two reflections, 51 deg, colors reversed; Alexander's dark band between.",
            "22-degree halo and sundogs: refraction through 60-degree hexagonal ice prisms in cirrus.",
            "Inferior mirages bend light up over hot surfaces; superior mirages loom over inversions.",
            "Corona ring size measures cloud droplet diameter by diffraction.",
        ],
        "requirements": [
            "Derive the 42-degree rainbow angle from refraction plus one internal reflection.",
            "Explain the 22-degree halo via the hexagonal ice prism.",
            "Distinguish inferior from superior mirages by the temperature profile.",
        ],
        "standards": [
            "Halo phenomena are classified by the standard halo nomenclature (22 deg, 46 deg, parhelia...).",
            "Refractive index of water (1.33) and ice (1.31) are the standard optical constants.",
        ],
        "citations": [CIT_PETTY, CIT_WALLACE],
        "sig_lens": (
            "Signature edition: sky optics as his Signature light-geometry, "
            "every bow and halo a measured angle of his atmosphere."
        ),
        "demo_kind": "optics",
    },
    # ================= ADVANCED =================
    {
        "key": "cape_and_cin",
        "name": "CAPE and CIN: Reading a Sounding",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "CAPE - convective available potential energy - is the fuel "
            "gauge of thunderstorms: the total buoyant energy a parcel "
            "would gain rising from the level of free convection to the "
            "equilibrium level, measured in joules per kilogram. Values "
            "under 1000 mean garden-variety showers; 1000-2500 mean "
            "scattered severe storms; above 2500-4000 the atmosphere is "
            "loaded for supercells. CIN - convective inhibition - is the "
            "lid: the negative buoyant energy in the cap inversion that a "
            "parcel must punch through, and it is why high-CAPE days can "
            "stay blue until a front or outflow boundary provides the "
            "lift. Forecasters read both off the Skew-T diagram as areas "
            "between the parcel's temperature curve and the environment's: "
            "CAPE is the positive area, CIN the negative. The level of "
            "free convection, the equilibrium level (cloud top), the "
            "lifted condensation level, and the lifted index all come "
            "from the same sounding - one balloon flight, the whole "
            "convective story."
        ),
        "how_it_works": (
            "CAPE is the vertical integral of parcel buoyancy: integral "
            "from LFC to EL of g (T_v,parcel - T_v,env)/T_v,env dz, using "
            "virtual temperature to include moisture. Graphically it is "
            "the area between the moist adiabat the parcel follows and the "
            "environmental temperature curve on a Skew-T. The updraft "
            "speed limit follows from energy conservation: w_max = "
            "sqrt(2 CAPE), so 2000 J/kg implies ~63 m/s before water "
            "loading and entrainment drag it down to 20-30 m/s in real "
            "storms. CIN is the same integral over the capped layer near "
            "the surface, typically 0 to -200 J/kg; a CIN of -50 needs a "
            "trigger with about 50 J/kg of lift energy, which a gust front "
            "or terrain feature can supply. The most dangerous setup is "
            "high CAPE with modest CIN and strong shear: the cap holds "
            "until late afternoon, suppressing weak storms, then breaks "
            "all at once into discrete explosive supercells instead of a "
            "messy squall line."
        ),
        "key_points": [
            "CAPE (J/kg) is the integrated positive buoyancy: <1000 garden variety, 1000-2500 severe, 2500+ extreme.",
            "CIN is the cap: negative buoyancy that must be overcome before CAPE can release.",
            "On a Skew-T, CAPE is the positive area and CIN the negative area between parcel and environment curves.",
            "w_max = sqrt(2 CAPE): 2000 J/kg implies ~63 m/s theoretical, ~20-30 m/s real.",
            "High CAPE + modest CIN + strong shear = discrete explosive supercells when the cap breaks.",
        ],
        "requirements": [
            "Compute CAPE and CIN by integrating buoyancy from a sounding.",
            "Identify LFC, EL, and LCL on a Skew-T and read the positive/negative areas.",
            "Assess severe potential from the CAPE/CIN/shear combination.",
        ],
        "standards": [
            "CAPE is computed with virtual-temperature correction as the operational standard.",
            "Sounding indices (Lifted Index, SWEAT, STP) derive from standard mandatory-level data.",
        ],
        "citations": [CIT_EMANUEL, CIT_MARKOWSKI],
        "sig_lens": (
            "Signature edition: CAPE as his Signature fuel gauge, every "
            "joules-per-kilogram of sky tallied before the storm."
        ),
        "demo_kind": "cape_cin",
    },
    {
        "key": "lightning_electrification",
        "name": "Lightning and Atmospheric Electrification",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Thunderstorms are electric generators. Inside the mixed-phase "
            "region, graupel pellets falling through a blizzard of small "
            "ice crystals collide and steal charge: below about -15 C the "
            "graupel takes negative charge, above it positive, building the "
            "classic tripole - a main negative charge center near -10 C, "
            "positive above and a small positive pocket below. Updrafts "
            "and gravity separate the charges until the electric field "
            "tops 3 million volts per meter and air breaks down. A stepped "
            "leader zigzags down in 50-meter jumps; when it nears the "
            "ground, upward streamers reach to meet it, and the return "
            "stroke blasts 30,000 amperes upward at a third the speed of "
            "light, heating the channel to 30,000 kelvin - five times the "
            "sun's surface - the thunder you hear. Earth is struck about "
            "100 times per second, and the whole system closes a global "
            "electric circuit: thunderstorms charge the ionosphere to "
            "+250,000 volts relative to the ground, and fair-weather air "
            "leaks the current back down everywhere else."
        ),
        "how_it_works": (
            "The non-inductive charging mechanism is collisional: when a "
            "graupel pellet rebounds off an ice crystal, the contact "
            "transfers charge with a sign that flips near -15 C (the "
            "charge-reversal temperature), depending on liquid water "
            "content. Heavy graupel falls, light crystals rise in the "
            "updraft, and the storm-scale field grows at roughly 10-100 "
            "volts per meter per second. Breakdown begins as corona from "
            "ice crystals, then the stepped leader advances ~50 m per "
            "1-microsecond step with 20-50 microsecond pauses, forking as "
            "it seeks the path of least resistance. The return stroke "
            "discharges the channel in ~100 microseconds; subsequent dart "
            "leaders reuse the hot channel for the flickering strokes that "
            "follow. Intracloud flashes outnumber cloud-to-ground about 3 "
            "to 1; positive ground flashes, though only ~10 percent, carry "
            "ten times the charge and start most lightning fires. "
            "Lightning mapping arrays locate every branch in 3D by its "
            "radio pulses, turning storms into wiring diagrams."
        ),
        "key_points": [
            "Graupel-ice collisions separate charge with a sign flip near -15 C, building the storm tripole.",
            "Breakdown at ~3 MV/m: stepped leader descends, return stroke carries ~30 kA at 30,000 K.",
            "Earth is struck ~100 times per second; intracloud flashes outnumber ground flashes ~3:1.",
            "Positive ground flashes (~10%) carry ~10x the charge and start most lightning fires.",
            "Thunderstorms hold the ionosphere at +250 kV; fair-weather air completes the global circuit.",
        ],
        "requirements": [
            "Explain the non-inductive charging mechanism and the charge-reversal temperature.",
            "Trace a flash: stepped leader, attachment, return stroke, dart leaders.",
            "Describe the global electric circuit and the ionospheric potential.",
        ],
        "standards": [
            "Lightning flash density is reported per square kilometer per year by detection networks.",
            "Peak current and polarity follow standard lightning-location-system reporting.",
        ],
        "citations": [CIT_WALLACE, CIT_MARKOWSKI],
        "sig_lens": (
            "Signature edition: lightning as his Signature discharge law, "
            "every coulomb of sky accounted from cloud to ground."
        ),
        "demo_kind": "lightning",
    },
    {
        "key": "atmospheric_chemistry",
        "name": "Atmospheric Chemistry and Photochemistry",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Atmospheric chemistry is kinetics at planetary scale: "
            "sunlight breaks molecules apart and the fragments react in "
            "chains that build and destroy the trace gases. The Chapman "
            "cycle is the founding example - ultraviolet light splits O2, "
            "the oxygen atoms join other O2 to make ozone, and ozone "
            "absorbs the very UV that made it, which is why the ozone "
            "layer shields the surface. The hydroxyl radical, OH, is the "
            "atmosphere's detergent: made when excited oxygen atoms from "
            "ozone photolysis meet water vapor, it oxidizes methane, "
            "carbon monoxide, and most pollutants, setting their "
            "lifetimes. Catalytic cycles multiply small causes: one "
            "chlorine atom from a CFC destroys ~100,000 ozone molecules "
            "because the catalyst is regenerated each loop. Chemical "
            "lifetimes span ten orders of magnitude - seconds for OH, a "
            "decade for methane, millennia for some CFCs - so the "
            "atmosphere is a patchwork of local chemistry and global "
            "mixing."
        ),
        "how_it_works": (
            "Every reaction obeys mass-action kinetics: rate = k [A][B], "
            "with the rate constant k often in Arrhenius form k = A "
            "exp(-Ea/RT). Photolysis rates come from the actinic flux "
            "times the absorption cross-section times the quantum yield. "
            "The Chapman cycle's four reactions - O2 + hv -> 2O, O + O2 + "
            "M -> O3, O3 + hv -> O2 + O, O + O3 -> 2O2 - predict an ozone "
            "layer, but pure Chapman overpredicts ozone by a factor of "
            "two: catalytic cycles (HOx, NOx, ClOx) do the rest of the "
            "destroying. Steady state sets concentrations: for methane, "
            "emission flux divided by the OH sink gives ~1.9 ppm and a "
            "~9-year lifetime. Box models integrate these coupled "
            "differential equations; 3D chemical transport models add "
            "winds. The Antarctic ozone hole appears each spring because "
            "polar stratospheric clouds convert reservoir chlorine into "
            "active forms on their ice surfaces, and sunlight returns to "
            "drive the catalytic destruction - chemistry, temperature, "
            "and dynamics in one phenomenon."
        ),
        "key_points": [
            "Photolysis starts the chains; OH (the detergent) sets the lifetimes of methane, CO, and pollutants.",
            "Chapman cycle makes the ozone layer; catalytic cycles (ClOx, NOx, HOx) destroy it far faster.",
            "One chlorine atom destroys ~100,000 ozone molecules - catalysts regenerate each loop.",
            "Lifetimes span 10 orders of magnitude: seconds (OH) to millennia (some CFCs).",
            "The ozone hole = polar stratospheric clouds activating chlorine + returning spring sunlight.",
        ],
        "requirements": [
            "Write the Chapman cycle reactions and explain the ozone steady state.",
            "Apply mass-action kinetics and the Arrhenius form to an atmospheric reaction.",
            "Explain catalytic destruction and why chlorine is so efficient.",
        ],
        "standards": [
            "Rate constants follow the standard JPL/NASA evaluated kinetic data recommendations.",
            "Ozone column is reported in Dobson Units (300 DU = 3 mm at surface pressure).",
        ],
        "citations": [CIT_SEINFELD, CIT_WALLACE],
        "sig_lens": (
            "Signature edition: atmospheric chemistry as his Signature "
            "reaction ledger, every radical and catalyst balanced."
        ),
        "demo_kind": "chemistry",
    },
    {
        "key": "smog_chemistry",
        "name": "Smog Chemistry: Photochemical Smog",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Photochemical smog is sunshine weaponized by pollution. "
            "Traffic and industry emit nitrogen oxides (NOx) and volatile "
            "organic compounds (VOCs); sunlight photolyzes NO2, releasing "
            "an oxygen atom that makes ozone - but in clean air the ozone "
            "just reacts back with NO and nothing accumulates. VOCs break "
            "the stalemate: their oxidation produces peroxy radicals that "
            "convert NO to NO2 without consuming ozone, so ozone piles up "
            "hour by hour through a stagnant sunny afternoon. The classic "
            "Los Angeles smog of the 1940s-70s was the discovery case: "
            "ozone above 200 parts per billion, eye-stinging peroxyacetyl "
            "nitrate (PAN), visibility cut to blocks. The chemistry has "
            "two regimes - NOx-limited (rural, ozone rises with NOx) and "
            "VOC-limited (urban cores, cutting NOx alone can raise ozone) "
            "- which is why smog control strategies must be tuned to the "
            "local regime. Catalytic converters, low-VOC fuels, and "
            "power-plant scrubbers have cut peak ozone dramatically where "
            "applied."
        ),
        "how_it_works": (
            "The core loop: NO2 + hv -> NO + O; O + O2 + M -> O3; O3 + NO "
            "-> NO2 + O2 (the null cycle, no net ozone). VOC oxidation "
            "inserts RO2 + NO -> RO + NO2, converting NO to NO2 while "
            "bypassing the ozone-destroying step - each VOC molecule can "
            "drive many ozone-forming loops before it is consumed. The "
            "Leighton relationship, [O3] = j[NO2]/(k[NO]), gives the "
            "photostationary ozone from the null cycle alone; measured "
            "ozone above the Leighton value diagnoses peroxy-radical "
            "activity. Ozone production efficiency - molecules of O3 per "
            "NOx molecule before it is lost to nitric acid - reaches 5-10 "
            "in rural air. Meteorology gates everything: smog needs sun, "
            "stagnation, and a capping inversion - the boundary layer at "
            "its worst, a shallow mixed layer trapping emissions under a "
            "lid. Night brings the nitrate radical, NO3, which oxidizes "
            "VOCs in the dark and seeds morning chemistry."
        ),
        "key_points": [
            "NOx + VOCs + sunlight = ozone: VOC peroxy radicals break the null cycle so O3 accumulates.",
            "Two regimes: NOx-limited (rural) vs VOC-limited (urban cores) - control strategy must match.",
            "The Leighton relationship gives null-cycle ozone; excess diagnoses radical chemistry.",
            "Ozone production efficiency: 5-10 O3 molecules per NOx in rural air.",
            "Smog needs sun + stagnation + capping inversion - the boundary layer trapping emissions.",
        ],
        "requirements": [
            "Write the photostationary null cycle and explain how VOCs break it.",
            "Apply the Leighton relationship to diagnose ozone production.",
            "Distinguish NOx-limited from VOC-limited regimes and their policy implications.",
        ],
        "standards": [
            "Ozone is reported in parts per billion; the standard is an 8-hour average.",
            "VOC reactivity scales follow the standard Maximum Incremental Reactivity (MIR) tables.",
        ],
        "citations": [CIT_SEINFELD, CIT_WALLACE],
        "sig_lens": (
            "Signature edition: smog chemistry as his Signature sunlight "
            "ledger, every ozone molecule traced to its radical."
        ),
        "demo_kind": "smog",
    },
    {
        "key": "aerosols",
        "name": "Aerosols: Particles in the Air",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Aerosols are the atmosphere's suspended particles - sea salt, "
            "desert dust, sulfate from volcanoes and power plants, black "
            "carbon from fires, organics from forests and tailpipes - "
            "spanning nanometers to tens of microns. They are few by mass "
            "but mighty in effect: they scatter and absorb sunlight "
            "(the direct effect, cooling where they reflect, warming where "
            "black carbon absorbs), they seed every cloud droplet (the "
            "indirect effect, brightening clouds and suppressing rain), and "
            "the fine ones penetrate deep into lungs. Aerosol optical "
            "depth - the total dimming along a sunbeam - runs ~0.05 in "
            "clean maritime air to above 1.0 in dust storms and smoke "
            "plumes; the 1991 Pinatubo eruption pushed the global mean up "
            "enough to cool the planet ~0.5 C for two years. Lifetimes are "
            "days to weeks, so aerosols are patchy and near their sources "
            "- the opposite of long-lived greenhouse gases - which makes "
            "them the largest uncertainty in the forcing ledger."
        ),
        "how_it_works": (
            "Sources split into primary (emitted as particles: dust, sea "
            "salt, soot) and secondary (gas-to-particle: SO2 oxidizing to "
            "sulfate, VOCs to secondary organics). Size distributions are "
            "lognormal modes: nucleation (<10 nm), Aitken, accumulation "
            "(0.1-1 micron, the optically and health-critical mode), and "
            "coarse (>1 micron, fast-settling dust and salt). Removal is "
            "by dry deposition, sedimentation, and wet scavenging - rain "
            "washes the sky, which is why air is cleanest after storms. "
            "The direct effect follows Mie theory: sulfate scatters "
            "efficiently (cooling), black carbon absorbs (warming, "
            "especially over bright snow). The first indirect effect "
            "(Twomey): more nuclei make more, smaller droplets - brighter "
            "clouds at fixed water. The second (Albrecht): smaller "
            "droplets rain less efficiently, lengthening cloud lifetime. "
            "Sun photometers measure optical depth by the dimming of the "
            "direct sun; satellites map the plumes globally."
        ),
        "key_points": [
            "Sources: primary (dust, salt, soot) and secondary (SO2->sulfate, VOCs->organics); sinks: deposition + rain washout.",
            "Accumulation mode (0.1-1 micron) dominates both optical effects and health impacts.",
            "Direct effect: sulfate scatters (cooling), black carbon absorbs (warming).",
            "Indirect effects: more nuclei -> brighter clouds (Twomey) that rain less and live longer (Albrecht).",
            "Pinatubo 1991: global optical depth spike cooled the planet ~0.5 C for ~2 years.",
        ],
        "requirements": [
            "Name the major aerosol types, their sources, and their size modes.",
            "Explain direct vs first and second indirect effects.",
            "Interpret aerosol optical depth values from clean to extreme.",
        ],
        "standards": [
            "Aerosol optical depth is reported at 550 nm by standard sun-photometer networks.",
            "PM2.5/PM10 size cuts follow the standard EPA/WHO definitions (2.5 and 10 microns).",
        ],
        "citations": [CIT_SEINFELD, CIT_PETTY],
        "sig_lens": (
            "Signature edition: aerosols as his Signature particle census, "
            "every mote weighed for its dimming and its seeding."
        ),
        "demo_kind": "aerosols",
    },
    {
        "key": "air_quality",
        "name": "Air Quality and the AQI",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Air quality science turns chemistry into public guidance. The "
            "criteria pollutants - fine particles (PM2.5), coarse particles "
            "(PM10), ground-level ozone, nitrogen dioxide, sulfur dioxide, "
            "and carbon monoxide - each have health-based standards, and the "
            "Air Quality Index compresses the worst of them into one "
            "0-500+ number the public can act on: 0-50 good (green), 51-100 "
            "moderate (yellow), 101-150 unhealthy for sensitive groups "
            "(orange), 151-200 unhealthy (red), 201-300 very unhealthy "
            "(purple), 300+ hazardous (maroon). PM2.5 is the deadliest "
            "widespread pollutant - particles under 2.5 microns lodge deep "
            "in lungs and cross into blood, and chronic exposure tracks "
            "with millions of premature deaths yearly worldwide. Ozone "
            "peaks downwind of cities on hot stagnant afternoons; PM2.5 "
            "peaks in winter inversions and wildfire smoke. Monitoring "
            "networks, dispersion models, and now low-cost sensors and "
            "satellites feed the forecasts behind every air-quality alert."
        ),
        "how_it_works": (
            "The AQI is piecewise linear: each pollutant's concentration "
            "maps through breakpoint tables to a sub-index, and the "
            "overall AQI is the maximum sub-index - the worst pollutant "
            "rules. For PM2.5, 12.0 ug/m3 is AQI 50 and 35.4 is 100; the "
            "formula is I = (I_hi - I_lo)/(C_hi - C_lo) x (C - C_lo) + "
            "I_lo within the bracketing breakpoints. Standards set the "
            "breakpoints: the WHO guideline is 5 ug/m3 annual mean for "
            "PM2.5, far below most cities' reality. Forecasting blends "
            "chemical transport models (emissions + chemistry + winds) "
            "with observations: persistence, climatology, and machine "
            "learning correct the raw model. Wildfire smoke is the new "
            "dominant US episode type - a single fire can push AQI past "
            "300 hundreds of kilometers downwind, and smoke PM2.5 carries "
            "its own toxicity profile. Indoor air, where people spend 90 "
            "percent of their time, follows the same physics with "
            "different sources: cooking, gas stoves, radon, and "
            "infiltration of outdoor pollution."
        ),
        "key_points": [
            "AQI 0-500+: worst-pollutant-wins sub-index; color-coded from green (good) to maroon (hazardous).",
            "PM2.5 is the deadliest widespread pollutant: deep-lung penetration, millions of premature deaths yearly.",
            "Ozone peaks on hot stagnant afternoons downwind of cities; PM2.5 peaks in winter inversions and fire smoke.",
            "WHO guideline: 5 ug/m3 annual PM2.5 - below what most cities breathe.",
            "Forecasts blend chemical transport models with observations; wildfire smoke now dominates US episodes.",
        ],
        "requirements": [
            "Compute an AQI sub-index from a concentration via the breakpoint formula.",
            "Name the six criteria pollutants and their characteristic episode meteorology.",
            "Explain why PM2.5 dominates the health burden.",
        ],
        "standards": [
            "AQI breakpoints and colors follow the standard EPA technical guidance.",
            "PM2.5 is measured by federal reference or equivalent methods; WHO guidelines set the health benchmarks.",
        ],
        "citations": [CIT_SEINFELD, CIT_WALLACE],
        "sig_lens": (
            "Signature edition: air quality as his Signature breath-ledger, "
            "every microgram of sky scored for health."
        ),
        "demo_kind": "aqi",
    },
    {
        "key": "radiative_transfer",
        "name": "Radiative Transfer: Beer's Law and Absorption Bands",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Radiative transfer is the accounting of every photon's journey "
            "through the atmosphere: emitted, absorbed, scattered, "
            "transmitted. Its workhorse is Beer's law - transmittance falls "
            "exponentially with optical depth, T = exp(-tau) - so a gas "
            "that is opaque at line center lets radiation through only in "
            "the line wings. Molecules absorb in bands, not lines alone: "
            "water vapor owns the near-infrared and much of the thermal "
            "infrared, CO2 owns 15 microns, ozone owns the ultraviolet "
            "Hartley band. Band saturation is why adding CO2 has a "
            "logarithmic effect: the band center is already black, so new "
            "molecules only widen the wings. Weighting functions tell "
            "satellites which layer they are seeing: a channel's measured "
            "radiance is the temperature profile weighted by where the "
            "optical depth changes fastest. Every greenhouse calculation, "
            "every satellite temperature retrieval, every climate-model "
            "radiation code is Beer's law integrated over millions of "
            "spectral lines."
        ),
        "how_it_works": (
            "Start with the Schwarzschild equation for a non-scattering "
            "atmosphere: dI/d(tau) = I - B(T), intensity relaxing toward "
            "the Planck function of the local temperature with optical "
            "depth as the coordinate. Integrate upward and the outgoing "
            "radiance is the surface term attenuated by exp(-tau*) plus the "
            "atmospheric emission integrated against the weighting function "
            "W = d(transmittance)/d(ln p), which peaks where the channel "
            "goes from transparent to opaque. Line-by-line codes sum "
            "millions of HITRAN lines with pressure-broadened Lorentz "
            "profiles (wide at the surface, narrow aloft); fast models use "
            "correlated-k distributions that preserve the band statistics "
            "at 1 percent of the cost. The 15-micron CO2 band's weighting "
            "function peaks in the mid-troposphere for the band wings and "
            "the stratosphere at band center - which is why stratospheric "
            "cooling accompanies tropospheric warming: more CO2 emits more "
            "efficiently to space from the cold stratosphere. Two-stream "
            "approximations split radiation into up and down hemispheres "
            "for climate models."
        ),
        "key_points": [
            "Beer's law T = exp(-tau): transmittance falls exponentially with optical depth.",
            "Molecules absorb in bands (H2O, CO2 at 15 um, O3 in UV); band saturation makes CO2 forcing logarithmic.",
            "Weighting functions peak where a channel turns opaque - that layer is what the satellite sees.",
            "Line-by-line codes sum HITRAN lines; correlated-k preserves band statistics cheaply.",
            "Stratospheric cooling + tropospheric warming is the radiative fingerprint of more CO2.",
        ],
        "requirements": [
            "Apply Beer's law to compute transmittance from optical depth.",
            "Explain band saturation and the logarithmic CO2 forcing.",
            "Interpret a weighting function to name the layer a satellite channel senses.",
        ],
        "standards": [
            "Spectral line data follow the HITRAN database standard.",
            "Radiative forcing is reported at the tropopause after stratospheric adjustment.",
        ],
        "citations": [CIT_PETTY, CIT_WALLACE],
        "sig_lens": (
            "Signature edition: radiative transfer as his Signature photon "
            "ledger, every ray tracked from emission to space."
        ),
        "demo_kind": "radiative",
    },
    {
        "key": "polar_vortex",
        "name": "The Polar Vortex and Sudden Stratospheric Warmings",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The polar vortex is a continent-scale cyclone parked over "
            "each pole in the winter stratosphere, 15-50 kilometers up - "
            "a westerly jet circling the pole at up to 100 m/s, fenced by "
            "the sharp temperature contrast between the cold polar night "
            "and warmer mid-latitudes. A strong vortex bottles up Arctic "
            "air and keeps mid-latitudes mild and zonal; a weak, wavy "
            "vortex lets frigid air spill south in the cold-air outbreaks "
            "that freeze Texas. The vortex can be shattered by planetary "
            "waves propagating up from the troposphere: in a sudden "
            "stratospheric warming, the polar stratosphere can warm 50 "
            "kelvin in days, the westerlies reverse to easterly, and the "
            "vortex splits or is displaced off the pole. Weeks later the "
            "signal descends to the surface, flipping the Arctic "
            "Oscillation negative and loading the dice for cold, snowy "
            "regimes over North America and Eurasia. The Antarctic "
            "vortex's cold isolation is also what makes the ozone hole "
            "possible."
        ),
        "how_it_works": (
            "The vortex is thermal-wind balance at planetary scale: the "
            "pole-to-midlatitude temperature gradient in the stratosphere "
            "demands westerly shear with height, and the jet sits at the "
            "gradient's edge. Planetary (Rossby) waves generated by "
            "topography and land-sea contrast propagate upward when the "
            "westerlies are moderate; as they break in the stratosphere "
            "they deposit easterly momentum, decelerating the vortex - "
            "the wave-mean-flow interaction formalized by the Eliassen-"
            "Palm flux. A major warming meets the WMO criterion: the "
            "zonal-mean zonal wind at 60 N and 10 hPa reverses from "
            "westerly to easterly with a simultaneous polar temperature "
            "spike. The disrupted vortex then radiatively recovers over "
            "weeks, but the troposphere feels the changed wave guide: "
            "the negative Arctic Oscillation pattern that follows raises "
            "the odds of blocking highs and cold-air outbreaks for 4-8 "
            "weeks. Forecast models now capture the downward coupling, "
            "giving subseasonal forecasts their best winter skill source."
        ),
        "key_points": [
            "The polar vortex: winter-stratosphere westerly jet (~100 m/s) ringing the pole at 15-50 km.",
            "Strong vortex = bottled Arctic air, mild zonal mid-latitudes; weak wavy vortex = cold-air outbreaks.",
            "Sudden stratospheric warming: ~50 K in days, wind reversal at 60 N / 10 hPa, vortex split or displaced.",
            "The surface feels it weeks later as a negative Arctic Oscillation: blocking, cold, snow.",
            "The Antarctic vortex's cold isolation enables the spring ozone hole.",
        ],
        "requirements": [
            "Explain the vortex as thermal-wind balance on the stratospheric temperature gradient.",
            "State the WMO major-warming criterion (wind reversal at 60 N, 10 hPa).",
            "Trace the downward coupling: warming -> negative AO -> cold regimes weeks later.",
        ],
        "standards": [
            "Vortex strength is monitored via zonal-mean zonal wind at 60 degrees latitude, 10 hPa.",
            "Major vs minor warmings follow the WMO wind-reversal criterion.",
        ],
        "citations": [CIT_HOLTON, CIT_WALLACE],
        "sig_lens": (
            "Signature edition: the polar vortex as his Signature winter "
            "wheel, its breaking the herald of his cold outbreaks."
        ),
        "demo_kind": "polar_vortex",
    },
    {
        "key": "gravity_waves",
        "name": "Atmospheric Gravity Waves and Tides",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Displace stable air vertically and buoyancy pulls it back - "
            "overshoot, oscillate, and you have an atmospheric gravity "
            "wave, the atmosphere's version of ripples on a pond, with "
            "gravity (buoyancy) as the restoring force. Mountains launch "
            "them when wind blows over ridges; thunderstorms punch them "
            "upward from convective overshoot; jet-stream shear radiates "
            "them sideways. The waves carry momentum upward, and when they "
            "break in the thin upper atmosphere they drag the mean flow - "
            "this wave drag is what closes the mesospheric jets and drives "
            "the summer-to-winter-pole circulation that makes the summer "
            "mesopause the coldest place on Earth. On the grandest scale, "
            "solar heating drives atmospheric tides - global-scale waves "
            "with 24-hour and 12-hour periods - whose pressure signal "
            "(~1-2 hPa) is visible in every tropical barometer record. "
            "Lenticular clouds stacked like plates over peaks are gravity "
            "waves made visible."
        ),
        "how_it_works": (
            "The intrinsic frequency is bounded by the Brunt-Vaisala "
            "frequency N: waves oscillate at omega = N cos(theta), where "
            "theta is the angle of the wave vector from vertical, so no "
            "gravity wave oscillates faster than the local buoyancy "
            "frequency (~10-minute period in the troposphere). The "
            "dispersion relation ties frequency to wavelength: short "
            "horizontal wavelengths mean steep phase lines and slow "
            "vertical energy propagation. A mountain wave is stationary "
            "relative to the ground (phase speed zero), so its intrinsic "
            "frequency equals kU; if the wind U changes with height to "
            "match, the wave meets a critical level and breaks, dumping "
            "momentum - the mechanism behind clear-air turbulence and "
            "stratospheric sudden warmings alike. Breaking is parameterized "
            "in models by Lindzen-style schemes that deposit the wave's "
            "momentum flux where the amplitude saturates. Tides are the "
            "wavelength-equals-planet limit: the migrating diurnal tide "
            "follows the sun, the semidiurnal tide rings the globe twice "
            "daily, both shaped by the atmosphere's resonant structure."
        ),
        "key_points": [
            "Gravity waves: buoyancy-restored oscillations; mountains, storms, and jets are the sources.",
            "Frequency bounded by N: omega = N cos(theta); periods of minutes in the troposphere.",
            "Breaking waves deposit momentum aloft - the drag that closes mesospheric jets.",
            "Critical levels (wind matching phase speed) absorb waves and generate turbulence.",
            "Atmospheric tides: global 24-h and 12-h waves; the tropical barometer shows their 1-2 hPa pulse.",
        ],
        "requirements": [
            "Write the gravity-wave dispersion relation and the N frequency bound.",
            "Explain mountain-wave breaking at critical levels and its momentum deposit.",
            "Distinguish gravity waves from tides by scale and period.",
        ],
        "standards": [
            "Wave momentum flux is reported in millipascals in middle-atmosphere studies.",
            "Tidal components are named by period: diurnal (24 h), semidiurnal (12 h), terdiurnal (8 h).",
        ],
        "citations": [CIT_HOLTON, CIT_WALLACE],
        "sig_lens": (
            "Signature edition: gravity waves as his Signature sky-ripples, "
            "every oscillation spending its momentum on schedule."
        ),
        "demo_kind": "gravity_waves",
    },
    {
        "key": "air_sea_exchange",
        "name": "Air-Sea Exchange: Fluxes Across the Interface",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The ocean and atmosphere trade momentum, heat, and moisture "
            "across a skin barely millimeters thick, and the bulk formulas "
            "are the ledger: stress tau = rho C_D U^2, sensible heat H = "
            "rho cp C_H U (Ts - Ta), latent heat LE = rho L C_E U (qs - "
            "qa). The transfer coefficients C_D, C_H, C_E are order 10^-3, "
            "rising with wind speed as the sea roughens - whitecaps at "
            "~7 m/s mark the transition to spray-mediated exchange. Latent "
            "heat dominates the tropical budget: evaporation carries ~80 "
            "W/m^2 out of the warm pool, the fuel of the Hadley cell and "
            "every hurricane. Gas exchange follows too - CO2 in and out "
            "by solubility and wind-driven mixing - making the ocean the "
            "largest carbon sink. In hurricanes the feedback closes: "
            "stronger winds evaporate more, the storm's heat engine roars "
            "hotter, winds strengthen further - the WISHE mechanism, "
            "wind-induced surface heat exchange."
        ),
        "how_it_works": (
            "Monin-Obukhov similarity theory grounds the bulk formulas: "
            "in the surface layer, fluxes are constant with height and "
            "profiles follow log laws corrected for stability. The drag "
            "coefficient grows with wind: C_D ~ 1.1 x 10^-3 at light winds, "
            "rising toward 2.5 x 10^-3 in gales as waves steepen - though "
            "at hurricane force, spray and flow separation cap it, a "
            "mercy that limits storm intensity. The Dalton number C_E and "
            "Stanton number C_H track C_D closely (Reynolds analogy) with "
            "stability corrections. The COARE algorithm iterates these "
            "with cool-skin and warm-layer corrections to the sea surface "
            "temperature - the millimeter cool skin is typically 0.2-0.5 "
            "C colder than the water below, enough to bias fluxes if "
            "ignored. Buoys, ships, and eddy-covariance towers measure the "
            "fluxes directly by correlating vertical wind with temperature "
            "and humidity fluctuations at 10 Hz."
        ),
        "key_points": [
            "Bulk formulas: tau = rho Cd U^2; H and LE scale with U times the sea-air contrast.",
            "Transfer coefficients ~10^-3, rising with wind as the sea roughens; capped at hurricane force.",
            "Latent heat (~80 W/m^2 from the warm pool) is the tropical atmosphere's main fuel.",
            "WISHE: hurricane winds boost evaporation, evaporation boosts the storm - a closed feedback.",
            "COARE-style algorithms correct for the cool skin and diurnal warm layer.",
        ],
        "requirements": [
            "Write the three bulk flux formulas and name every term.",
            "Explain why transfer coefficients rise with wind and cap in hurricanes.",
            "Describe the WISHE feedback loop.",
        ],
        "standards": [
            "Fluxes are referenced to the standard 10-meter wind and 2-meter temperature/humidity.",
            "The COARE bulk algorithm is the community standard for open-ocean fluxes.",
        ],
        "citations": [CIT_STULL, CIT_WALLACE],
        "sig_lens": (
            "Signature edition: air-sea exchange as his Signature trade "
            "ledger, every watt and every gust settled at the interface."
        ),
        "demo_kind": "air_sea",
    },
    {
        "key": "doppler_radar",
        "name": "Doppler Radar and Remote Sensing of Storms",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Weather radar sees storms by their echoes. A transmitter fires "
            "microwave pulses; raindrops, snowflakes, and hail scatter a "
            "fraction back, and the returned power - the reflectivity, in "
            "dBZ - scales with the sixth power of drop diameter, so a few "
            "big hailstones outshout a cloud of drizzle. The Doppler shift "
            "of successive pulses measures radial velocity: motion toward "
            "the radar shifts the phase one way, away the other, revealing "
            "rotation, convergence, and the mesocyclone's velocity "
            "couplet. Dual-polarization radars transmit horizontal and "
            "vertical pulses and compare them: the differential reflectivity "
            "and correlation coefficient distinguish rain from hail, snow "
            "from debris - the tornado debris signature is a dual-pol "
            "discovery. The radar equation ties it together: received power "
            "falls with range squared and grows with target size, which is "
            "why calibration and attenuation correction (especially at "
            "shorter wavelengths) make or break quantitative rainfall "
            "estimates."
        ),
        "how_it_works": (
            "Reflectivity Z = sum of D^6 per cubic meter; dBZ = 10 log10(Z), "
            "so 20 dBZ is light rain, 40 heavy rain, 55+ hail cores, 70+ "
            "extreme hail. The Z-R relation (Z = 300 R^1.4, Marshall-"
            "Palmer) converts reflectivity to rain rate, though drop-size "
            "variations make it approximate - dual-pol specific "
            "differential phase (Kdp) does better, being immune to "
            "calibration and partial beam blockage. Doppler velocity comes "
            "from the phase shift between pulses: v = (lambda/4 pi) "
            "d(phi)/dt, unambiguous only within the Nyquist interval "
            "(lambda x PRF / 4) - faster winds alias, folding into false "
            "opposite velocities that analysts must unfold. The mesocyclone "
            "appears as adjacent inbound/outbound couplets; the bounded "
            "weak-echo region marks the supercell's updraft vault. Phased-"
            "array radars now scan volumes in under a minute versus 4-6 "
            "for dish antennas, catching tornado genesis that WSR-88Ds "
            "miss."
        ),
        "key_points": [
            "Reflectivity (dBZ) scales with D^6: 20 light rain, 40 heavy, 55+ hail.",
            "Doppler shift gives radial velocity - rotation, convergence, mesocyclone couplets.",
            "Nyquist interval (lambda x PRF / 4) bounds unambiguous velocity; faster winds alias.",
            "Dual-pol distinguishes hydrometeor types: rain, hail, snow, tornado debris.",
            "Z = 300 R^1.4 converts reflectivity to rain rate; dual-pol Kdp improves it.",
        ],
        "requirements": [
            "Convert between Z and dBZ and interpret standard reflectivity thresholds.",
            "Compute the Nyquist velocity and explain aliasing.",
            "Read a velocity couplet as rotation and name the dual-pol debris signature.",
        ],
        "standards": [
            "Reflectivity is reported in dBZ; velocity in m/s or knots with dealiasing applied.",
            "The WSR-88D network's volume coverage patterns are the operational US standard.",
        ],
        "citations": [CIT_DOVIAK, CIT_MARKOWSKI],
        "sig_lens": (
            "Signature edition: radar as his Signature storm-sight, every "
            "echo a measured drop, every couplet a turning wind."
        ),
        "demo_kind": "radar",
    },
    {
        "key": "weather_satellites",
        "name": "Weather Satellites: Eyes Above the Storms",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Two constellations watch the sky. Geostationary satellites "
            "park 35,786 kilometers over the equator, orbiting once per "
            "sidereal day so they hover over one spot - staring at the "
            "same hemisphere with full-disk images every 10 minutes, "
            "lightning mappers, and rapid-scan mesoscale sectors for "
            "erupting storms. Polar orbiters fly low (~850 km), pole to "
            "pole, seeing every spot twice daily with sharper eyes: "
            "visible and infrared imagers, microwave sounders that profile "
            "temperature and humidity through clouds, and scatterometers "
            "that read ocean winds from radar backscatter. The channels "
            "are the science: visible shows cloud texture by day, infrared "
            "window shows cloud-top temperature (colder = taller = "
            "stronger storm) day and night, water-vapor channels show "
            "mid-upper tropospheric moisture and the jet stream's dry "
            "intrusions. Satellite data now supplies the majority of the "
            "observations that initialize forecast models - the forecast "
            "you check begins in orbit."
        ),
        "how_it_works": (
            "Geostationary orbit falls out of Kepler's third law: the "
            "period matching Earth's rotation demands r = (G M T^2 / 4 "
            "pi^2)^(1/3), which is 42,164 km from Earth's center, 35,786 "
            "km above the equator. Imagers scan by sweeping a mirror: 16 "
            "channels from 0.47-micron blue to 13.3-micron infrared, 0.5-km "
            "visible resolution, 2-km infrared. Infrared brightness "
            "temperature converts radiance via the inverse Planck function; "
            "cloud-top height follows from matching that temperature to a "
            "sounding. Atmospheric motion vectors track cloud and water-"
            "vapor features between images to infer winds where no "
            "balloons fly - the tropics' main wind source. Microwave "
            "sounders exploit the 60-GHz oxygen band: weighting functions "
            "at different frequencies peak at different pressures, "
            "retrieving the temperature profile through cloud. Data "
            "assimilation ingests millions of these radiances per cycle, "
            "with bias correction against models - the quiet revolution "
            "behind modern forecast skill."
        ),
        "key_points": [
            "Geostationary (35,786 km): continuous hemispheric watch, 10-min full disk, lightning mapping.",
            "Polar orbiters (~850 km): sharper global coverage twice daily, microwave sounding through clouds.",
            "IR window channel: cloud-top temperature = storm height, day and night.",
            "Water-vapor channels reveal mid-upper moisture, jet streams, and dry intrusions.",
            "Satellite radiances are the majority of data initializing modern forecast models.",
        ],
        "requirements": [
            "Derive the geostationary altitude from Kepler's third law.",
            "Name the key spectral channels and what each reveals.",
            "Explain how microwave sounders retrieve temperature profiles through cloud.",
        ],
        "standards": [
            "Satellite channels follow standard WMO nomenclature (VIS, IR window, WV).",
            "Brightness temperature is the standard reported quantity for infrared channels.",
        ],
        "citations": [CIT_KIDDER, CIT_WALLACE],
        "sig_lens": (
            "Signature edition: satellites as his Signature high watch, "
            "every photon of Earthlight read from orbit."
        ),
        "demo_kind": "satellites",
    },
    {
        "key": "numerical_weather_prediction",
        "name": "Numerical Weather Prediction",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Numerical weather prediction is the atmosphere computed: the "
            "primitive equations - momentum, mass, energy, moisture - "
            "discretized on a three-dimensional grid and stepped forward "
            "in time from today's observed state. The workflow has three "
            "acts. Data assimilation blends millions of observations "
            "(satellites, balloons, aircraft, surface stations) with a "
            "short forecast to produce the best estimate of the current "
            "state. The model integrates forward: global models at ~9-km "
            "grid spacing resolve cyclones but parameterize convection; "
            "convection-allowing models at ~3 km resolve individual "
            "storms. Ensembles run dozens of slightly perturbed forecasts "
            "to map uncertainty - the spread is the forecast's honest "
            "error bar. Skill has marched steadily: today's 5-day forecast "
            "is as accurate as the 3-day forecast of twenty years ago, "
            "and the theoretical predictability limit of ~2 weeks stands "
            "as chaos theory's boundary."
        ),
        "how_it_works": (
            "Discretization turns derivatives into grid differences; the "
            "Courant-Friedrichs-Lewy condition, c dt/dx <= 1, caps the "
            "time step - no signal may cross a grid box per step, so finer "
            "grids cost cubically (finer in x, y, and time). Processes "
            "smaller than the grid - turbulence, convection, cloud "
            "microphysics, radiation - are parameterized: represented by "
            "their statistical effect on the grid scale, the largest "
            "error source in models. Data assimilation (4D-Var or ensemble "
            "Kalman filters) solves a giant optimization: minimize the "
            "misfit to observations plus the misfit to the background "
            "forecast, weighted by their error covariances. Ensembles "
            "perturb initial conditions and physics; the ensemble mean "
            "beats any single run, and the spread calibrates probability "
            "- a 70 percent chance of rain means 7 of 10 members rained. "
            "Chaos sets the wall: Lorenz showed errors double every ~2 "
            "days in the mid-latitudes, so initial errors of any size "
            "saturate by about two weeks - the predictability horizon."
        ),
        "key_points": [
            "NWP = primitive equations on a grid, stepped forward from an assimilated initial state.",
            "Data assimilation optimally blends millions of observations with a short forecast background.",
            "The CFL condition (c dt/dx <= 1) caps time steps; finer grids cost cubically.",
            "Sub-grid processes (convection, turbulence, microphysics) are parameterized - the main error source.",
            "Ensembles map uncertainty; chaos doubles errors ~every 2 days, setting the ~2-week predictability limit.",
        ],
        "requirements": [
            "Name the three acts: assimilation, integration, ensembles.",
            "Apply the CFL condition to relate grid spacing and time step.",
            "Explain why ensembles beat single runs and what spread means.",
        ],
        "standards": [
            "Global model grids and output follow WMO GRIB standards for exchange.",
            "Forecast verification uses standard metrics (anomaly correlation, RMSE) against analyses.",
        ],
        "citations": [CIT_HOLTON, CIT_BLUESTEIN],
        "sig_lens": (
            "Signature edition: forecasting as his Signature computation, "
            "the whole sky stepped forward one grid box at a time."
        ),
        "demo_kind": "nwp",
    },
    {
        "key": "gaussian_plume",
        "name": "Atmospheric Dispersion: The Gaussian Plume",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "When a smokestack emits, where does the plume go? The "
            "Gaussian plume model answers with elegant statistics: "
            "turbulent eddies jostle the pollutant randomly, and the "
            "central limit theorem shapes the crosswind concentration "
            "into a bell curve. Downwind concentration falls as one over "
            "wind speed (faster wind dilutes more) and spreads with the "
            "dispersion sigmas, which grow with distance and depend on "
            "stability class - from A (very unstable, looping plumes) to "
            "F (very stable, fanning plumes that barely mix down). The "
            "effective stack height adds plume rise: hot buoyant exhaust "
            "climbs tens to hundreds of meters above the stack top before "
            "leveling, per the Briggs formulas. Ground-level concentration "
            "peaks some distance downwind where the plume first touches "
            "earth - the design point for every air-quality permit. "
            "Regulatory models (AERMOD and its kin) are Gaussian-plume "
            "descendants with terrain, building downwash, and deposition "
            "added; Lagrangian puff models handle the cases - calm winds, "
            "complex terrain - where steady plumes fail."
        ),
        "how_it_works": (
            "The steady-state solution for a continuous source in uniform "
            "wind u: C(x,y,z) = Q/(2 pi u sigma_y sigma_z) exp(-y^2/2 "
            "sigma_y^2) [exp(-(z-H)^2/2 sigma_z^2) + exp(-(z+H)^2/2 "
            "sigma_z^2)], with Q the emission rate, H the effective stack "
            "height, and the second vertical term the ground reflection. "
            "The sigmas come from Pasquill-Gifford curves: at 1 km "
            "downwind, sigma_y ~ 100 m in unstable air but ~30 m in "
            "stable air. Plume rise follows Briggs: delta-h proportional "
            "to (buoyancy flux)^1/3 x^2/3 / u for buoyant rise, bending "
            "over in strong wind. Stability classes A-F are set by wind "
            "speed, insolation, and cloud cover - a sunny light-wind "
            "afternoon is class A-B (vigorous mixing, low ground impact), "
            "a clear calm night is F (plume stays aloft, then fumigation "
            "at sunrise as the mixed layer grows into it). Deposition "
            "adds a sink: particles settle and gases absorb at the "
            "surface, parameterized by deposition velocities."
        ),
        "key_points": [
            "Turbulent diffusion shapes the plume cross-section into a Gaussian bell curve.",
            "Centerline concentration ~ Q/(u sigma_y sigma_z): faster wind dilutes, stability sets the sigmas.",
            "Pasquill-Gifford classes A (unstable) to F (stable) control how fast the plume spreads.",
            "Briggs plume rise: hot exhaust climbs above the stack before leveling off.",
            "Ground impact peaks downwind where the plume first touches earth - the permit design point.",
        ],
        "requirements": [
            "Write the Gaussian plume equation and name every term.",
            "Look up sigma_y/sigma_z for a stability class and distance.",
            "Explain plume rise and the fumigation trap at sunrise.",
        ],
        "standards": [
            "Stability classes follow the Pasquill-Gifford A-F scheme from standard meteorological inputs.",
            "Regulatory modeling follows EPA guideline models (AERMOD family).",
        ],
        "citations": [CIT_STULL, CIT_SEINFELD],
        "sig_lens": (
            "Signature edition: dispersion as his Signature bell-curve law, "
            "every plume's spread tallied downwind."
        ),
        "demo_kind": "plume",
    },
    {
        "key": "tropical_cyclones",
        "name": "Tropical Cyclones: Structure and Energetics",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A tropical cyclone is a Carnot heat engine built from ocean "
            "and air: heat flows in at the warm sea surface (~28 C+), "
            "work comes out as the furious winds, and waste heat exhausts "
            "at the cold tropopause. The structure is iconic - a calm "
            "eye 20-60 km wide where air sinks gently, ringed by the "
            "eyewall where the most violent updrafts and winds live, with "
            "spiral rainbands feeding moisture inward. Surface inflow "
            "spirals in, conserving angular momentum as it contracts, "
            "which is why winds peak at the eyewall's radius of maximum "
            "wind. The storm needs six ingredients: sea surface above "
            "~26.5 C, deep warm water, moist mid-troposphere, low vertical "
            "wind shear, a pre-existing disturbance, and enough latitude "
            "(~5 degrees) for Coriolis to organize rotation. Eyewall "
            "replacement cycles - an outer eyewall choking off the inner - "
            "cause the characteristic intensity wobbles of major "
            "hurricanes."
        ),
        "how_it_works": (
            "Emanuel's potential-intensity theory treats the cyclone as a "
            "Carnot cycle: maximum wind V_max^2 = (C_k/C_D) (T_s - T_o)/"
            "T_o (k_s - k_a), where the thermodynamic efficiency (T_s - "
            "T_o)/T_o uses sea-surface and outflow temperatures and (k_s "
            "- k_a) is the air-sea enthalpy contrast - typically yielding "
            "70-90 m/s for warm-pool conditions. The WISHE feedback "
            "closes the loop: surface fluxes grow with wind speed, so "
            "stronger winds evaporate more fuel. Angular momentum "
            "conservation, M = r v + f r^2/2, forces the inflow to spin "
            "faster as r shrinks - the figure-skater effect writ across "
            "500 kilometers. The secondary circulation (in, up, out) is "
            "driven by the radial gradient of heating; the warm core "
            "(5-10 C warmer than the environment at 300 hPa) hydrostatically "
            "demands the surface pressure fall. Storm surge - the deadliest "
            "hazard - is wind stress piling water against the coast plus "
            "the inverted-barometer lift of low pressure."
        ),
        "key_points": [
            "A tropical cyclone is a Carnot engine: ocean heat in, wind work out, tropopause exhaust.",
            "Potential intensity V_max^2 ~ efficiency x air-sea enthalpy contrast - typically 70-90 m/s.",
            "Angular momentum conservation spins inflow up as it contracts - winds peak at the eyewall.",
            "Six ingredients: warm deep ocean, moist mid-levels, low shear, a seed disturbance, latitude for Coriolis.",
            "Eyewall replacement cycles drive intensity wobbles; storm surge is the deadliest hazard.",
        ],
        "requirements": [
            "Explain the Carnot-cycle analogy and the potential-intensity formula's terms.",
            "Use angular-momentum conservation to explain the wind maximum at the eyewall.",
            "Name the six genesis ingredients and the two main hazards (wind, surge, plus rain).",
        ],
        "standards": [
            "Intensity follows the Saffir-Simpson scale by maximum sustained 1-minute wind.",
            "Minimum central pressure in hPa is the standard intensity metric alongside wind.",
        ],
        "citations": [CIT_EMANUEL, CIT_WALLACE],
        "sig_lens": (
            "Signature edition: the hurricane as his Signature heat engine, "
            "ocean warmth converted to wind by his thermodynamic law."
        ),
        "demo_kind": "tropical_cyclone",
    },
]

# Re-export for the build script
__all__ = ["ENTRIES", "SIG_TAIL"]
