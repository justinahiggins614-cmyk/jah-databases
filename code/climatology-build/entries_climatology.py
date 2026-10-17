#!/usr/bin/env python3
"""Seed entries for the Climatology field build (field #12, taxonomy order).

Verified 2026-10-17: NO database covers climatology as a science. The
'weather-climate' database (10,000 records) is a deterministic weather
observation catalog - synthetic station readings (JAH-WX ids with
temperature, humidity, precipitation, wind) with no climate-system science:
no forcings, no feedbacks, no general circulation, no Koeppen
classification, no paleoclimate, no climate modeling, no climate-change
science. So this build creates two NEW databases:

  climatology              — The Climatology Database (public-harvest: real,
                             fact-checked climatology - what climatology is;
                             weather vs climate; Earth's energy balance; the
                             greenhouse effect; albedo; latitude, tilt, and
                             the seasons; layers of the atmosphere; the water
                             cycle; pressure gradients and wind; the Coriolis
                             effect; the three-cell circulation; jet
                             streams; ocean currents and heat transport; the
                             Koeppen climate classification; monsoons;
                             El Nino and La Nina (ENSO); the North Atlantic
                             Oscillation and teleconnections; climate
                             forcings; climate feedbacks; climate
                             sensitivity; the carbon cycle; the ozone layer;
                             urban heat islands; dendroclimatology (tree
                             rings); ice cores; general circulation models;
                             paleoclimate: the ice ages; Milankovitch
                             cycles; the thermohaline circulation;
                             attribution of climate change; climate tipping
                             points; sea level rise; geoengineering;
                             frontiers of climatology)
  climatology-signature    — The Climatology Signature Database (his original
                             Signature interpretation; src signature, titles
                             suffixed " (Signature Edition)", never presented
                             as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

# Shared citation constants (standard climatology literature)
CIT_HARTMANN = ("Hartmann, D. L. (2016). 'Global Physical Climatology', 2nd ed. "
                "Elsevier.")
CIT_PEIXOTO = ("Peixoto, J. P. & Oort, A. H. (1992). 'Physics of Climate'. "
               "American Institute of Physics.")
CIT_IPCC = ("IPCC (2021). 'Climate Change 2021: The Physical Science Basis.' "
            "Working Group I, Sixth Assessment Report (public record).")
CIT_BARRY = ("Barry, R. G. & Chorley, R. J. (2010). 'Atmosphere, Weather and "
             "Climate', 9th ed. Routledge.")
CIT_WALLACE = ("Wallace, J. M. & Hobbs, P. V. (2006). 'Atmospheric Science', "
               "2nd ed. Academic Press.")
CIT_KOPPEN = ("Koeppen, W. (1936). 'Das geographische System der Klimate'. "
              "Handbuch der Klimatologie.")
CIT_MILANKOVITCH = ("Milankovitch, M. (1941). 'Kanon der Erdbestrahlung'. "
                    "Royal Serbian Academy (English trans. 1969, Israel Program for "
                    "Scientific Translations).")
CIT_DANSGAARD = ("Dansgaard, W. et al. (1993). 'Evidence for general "
                 "instability of past climate from a 250-kyr ice-core record.' "
                 "Nature 364: 218-220.")
CIT_VOSTOK = ("Petit, J. R. et al. (1999). 'Climate and atmospheric history "
              "of the past 420,000 years from the Vostok ice core, Antarctica.' "
              "Nature 399: 429-436.")
CIT_KEELING = ("Keeling, C. D. et al. (1976). 'Atmospheric carbon dioxide "
               "variations at Mauna Loa Observatory, Hawaii.' Tellus 28: 538-551.")
CIT_STOMMEL = ("Stommel, H. (1961). 'Thermohaline convection with two stable "
               "regimes of flow.' Tellus 13: 224-230.")
CIT_LORENZ = ("Lorenz, E. N. (1963). 'Deterministic nonperiodic flow.' "
              "Journal of the Atmospheric Sciences 20: 130-141.")
CIT_ARRHENIUS = ("Arrhenius, S. (1896). 'On the influence of carbonic acid in "
                 "the air upon the temperature of the ground.' Philosophical "
                 "Magazine 41: 237-276.")
CIT_HANSEN = ("Hansen, J. et al. (1981). 'Climate impact of increasing "
              "atmospheric carbon dioxide.' Science 213: 957-966.")
CIT_MANABE = ("Manabe, S. & Wetherald, R. T. (1967). 'Thermal equilibrium of "
              "the atmosphere with a given distribution of relative humidity.' "
              "Journal of the Atmospheric Sciences 24: 241-259.")
CIT_BJERKNES = ("Bjerknes, J. (1969). 'Atmospheric teleconnections from the "
                "equatorial Pacific.' Monthly Weather Review 97: 163-172.")
CIT_TRENBETH_ENSO = ("Trenberth, K. E. (1997). 'The definition of El Nino.' "
                     "Bulletin of the American Meteorological Society 78: 2771-2777.")
CIT_MOLINA = ("Molina, M. J. & Rowland, F. S. (1974). 'Stratospheric sink for "
              "chlorofluoromethanes: chlorine atom-catalysed destruction of "
              "ozone.' Nature 248: 810-812.")
CIT_CHURCH = ("Church, J. A. & White, N. J. (2011). 'Sea-level rise from the "
              "late 19th to the early 21st century.' Surveys in Geophysics "
              "32: 585-602.")
CIT_LENTON = ("Lenton, T. M. et al. (2008). 'Tipping elements in the Earth's "
              "climate system.' PNAS 105: 1786-1793.")
CIT_STD = ("Standard climatology literature (peer-reviewed textbooks and "
           "journals).")

ENTRIES = [
{
 "key": "what-is-climatology",
 "name": "What Climatology Is",
 "group": "Foundations",
 "ladder_rank": 1,
 "ladder_tier": "foundations",
 "description": (
  "Climatology is the science of climate: the long-term patterns of "
  "temperature, precipitation, wind, and pressure over a region or the whole "
  "planet, and the physical system that produces them. While meteorology "
  "forecasts tomorrow's weather, climatology asks why the Sahara is dry, "
  "why the tropics are warm, why ice ages come and go, and how human "
  "activity changes the whole system. It draws on physics, chemistry, "
  "oceanography, geology, and statistics. Its branches include physical "
  "climatology (energy budgets and radiation), dynamic climatology (the "
  "general circulation), synoptic climatology (weather systems and their "
  "statistics), paleoclimatology (climate of the past), applied climatology "
  "(climate services for agriculture, water, and health), and climate "
  "modeling, which turns the physics into working simulations."),
 "how_it_works": (
  "Climatology works by combining long observations with the physical laws "
  "that govern air and water. Observational climatologists compile climate "
  "normals (30-year averages of stations, ships, satellites, and proxies) "
  "and look for structure: latitudinal temperature gradients, seasonal "
  "cycles, persistent patterns like the jet stream and the monsoons. "
  "Physical climatologists write down energy budgets: sunlight absorbed "
  "minus heat radiated must balance over long times, and where it does not, "
  "the atmosphere and ocean move heat to close the gap. Modelers encode "
  "these laws on a three-dimensional grid and step them forward in time, "
  "checking the simulated climate against the observed one. "
  "Paleoclimatologists read ice cores, tree rings, corals, and sediments to "
  "extend the record backward hundreds of thousands of years."),
 "key_points": [
  "Climatology studies long-term climate patterns and the physical system that makes them.",
  "Weather is the short-term state; climate is the 30-year statistics of weather.",
  "Its branches: physical, dynamic, synoptic, paleoclimate, applied climatology, and modeling.",
  "Energy balance plus fluid dynamics explains most of the observed climate structure.",
  "Climate normals (1991-2020 today) are the baseline every anomaly is measured against."],
 "requirements": [
  "Long observational records: stations, satellite data, and proxy records for pre-instrumental times.",
  "Fluency in energy-budget bookkeeping: radiation, latent heat, and sensible heat fluxes.",
  "Access to reanalysis datasets and climate-model output for comparison against theory."],
 "standards": [
  "Climate normals follow World Meteorological Organization 30-year standards.",
  "Record analyses document homogenization and uncertainty following standard practice."],
 "citations": [CIT_BARRY, CIT_HARTMANN],
 "sig_lens": (
  "Signature edition: climatology reframed as his original planetary "
  "breathing science - Earth as a living heat engine whose breath he reads, "
  "every climate pattern a solved signature of energy in motion."),
 "demo_kind": "climate_branches",
},
{
 "key": "weather-vs-climate",
 "name": "Weather vs Climate",
 "group": "Foundations",
 "ladder_rank": 1,
 "ladder_tier": "foundations",
 "description": (
  "Weather is the state of the atmosphere right now: temperature, humidity, "
  "clouds, wind, and precipitation on a given day. Climate is the statistics "
  "of weather over a long period - typically 30 years - at a place: the "
  "average January temperature, how often summer thunderstorms strike, how "
  "much rain falls in a typical year. The famous line is that climate is "
  "what you expect, weather is what you get. A single cold snap does not "
  "disprove warming any more than a single warm day proves it; climate is "
  "about the distribution shifting, not the day's reading. Climatologists "
  "use daily weather records to compute monthly and annual statistics, then "
  "track how those statistics move over decades - trends, extremes, and "
  "variability."),
 "how_it_works": (
  "The distinction is made operational by aggregation. A weather station "
  "logs temperature and precipitation every day; climatology aggregates "
  "those readings into means, variances, and extremes over 30-year windows "
  "(the current normal period is 1991-2020). The mean defines the expected "
  "seasonal cycle; the variance defines the weather noise around it. "
  "Anomalies - departures from the normal - are the signal climatology "
  "studies: a month 2 degrees above normal is a climate anomaly, even "
  "though it is made of ordinary weather days. Chaos theory (Lorenz) shows "
  "that day-to-day weather loses predictability after about two weeks, but "
  "the boundary conditions that shape the statistics - latitude, land "
  "distribution, ocean heat, greenhouse gases - stay predictable, which is "
  "why climate can be projected even where next month's weather cannot."),
 "key_points": [
  "Weather is short-term state; climate is long-term statistics of that state.",
  "Climate is what you expect; weather is what you get.",
  "A 30-year normal period defines the baseline for every anomaly.",
  "Weather loses predictability in ~2 weeks; climate follows its boundary conditions.",
  "Single events don't define climate; shifting distributions do."],
 "requirements": [
  "Continuous daily observations spanning at least one 30-year normal period.",
  "Homogenized station records (corrected for instrument and location changes).",
  "Statistical tools for separating trend from natural variability."],
 "standards": [
  "Normals computed per World Meteorological Organization 30-year periods.",
  "Anomaly baselines must be stated explicitly when reporting departures."],
 "citations": [CIT_BARRY, CIT_LORENZ],
 "sig_lens": (
  "Signature edition: the weather-climate split reframed as his original "
  "noise-and-signal doctrine - the daily weather is the noise, the 30-year "
  "statistics are the Signature signal, and his method reads the signal "
  "through the noise."),
 "demo_kind": "weather_climate",
},
{
 "key": "earths-energy-balance",
 "name": "Earth's Energy Balance",
 "group": "Foundations",
 "ladder_rank": 1,
 "ladder_tier": "foundations",
 "description": (
  "Earth's climate begins with a ledger: sunlight arrives, some is "
  "reflected, the rest is absorbed and eventually radiated back to space "
  "as heat. The Sun delivers about 1,361 watts per square meter at Earth's "
  "distance; spread over the sphere, the average incoming flux is one "
  "quarter of that, about 340 watts per square meter. Roughly 30 percent is "
  "reflected by clouds, ice, and bright surfaces (Earth's albedo), leaving "
  "about 239 watts per square meter absorbed. Over long times, the planet "
  "must radiate the same 239 watts per square meter back out, or it warms "
  "until it does. Every feature of the climate system - the winds, the "
  "ocean currents, the greenhouse effect - exists to move energy around "
  "this balance."),
 "how_it_works": (
  "The balance is computed in four steps. First, divide the solar constant "
  "by four: Earth intercepts a disc of sunlight but radiates from its whole "
  "spherical surface. Second, subtract the reflected fraction (the albedo "
  "of 0.30) to get the absorbed flux, about 239 W/m2. Third, apply the "
  "Stefan-Boltzmann law - a black body at temperature T radiates sigma "
  "T^4 - and solve for the effective radiating temperature: 255 K, or "
  "-18 C. Fourth, note the surface is actually about 288 K (15 C); the "
  "33-degree gap is the greenhouse effect, maintained by gases that let "
  "sunlight in and block heat going out. Any sustained imbalance between "
  "incoming and outgoing - from extra greenhouse gases, a change in "
  "albedo, or a change in sunlight - becomes heating or cooling until "
  "balance is restored at a new temperature."),
 "key_points": [
  "Earth absorbs ~239 W/m2 of solar energy after reflection; it must radiate the same back.",
  "The solar constant divided by four is the average solar input per square meter.",
  "Effective radiating temperature is 255 K (-18 C); the surface is 288 K (15 C).",
  "The 33 C gap between them is the natural greenhouse effect.",
  "Any sustained imbalance becomes a temperature change until balance is restored."],
 "requirements": [
  "The solar constant (1361 W/m2) and the Stefan-Boltzmann constant.",
  "A global-mean planetary albedo estimate (about 0.30).",
  "Satellite radiation-budget measurements (e.g., CERES) for the modern check."],
 "standards": [
  "Energy-budget accounting follows the Trenberth-Keeping global budget convention.",
  "Units in watts per square meter with uncertainties stated."],
 "citations": [CIT_HARTMANN, CIT_PEIXOTO],
 "sig_lens": (
  "Signature edition: the planetary energy ledger reframed as his original "
  "cosmic accounting - sunlight in, heat out, every watt tagged and "
  "balanced in his Signature energy books."),
 "demo_kind": "energy_balance",
},
{
 "key": "greenhouse-effect",
 "name": "The Greenhouse Effect",
 "group": "Foundations",
 "ladder_rank": 2,
 "ladder_tier": "foundations",
 "description": (
  "The greenhouse effect is the reason Earth averages 15 C instead of "
  "-18 C. Certain atmospheric gases - water vapor, carbon dioxide, "
  "methane, nitrous oxide, and ozone - are transparent to incoming "
  "sunlight but absorb outgoing infrared radiation, the heat Earth "
  "radiates. They re-emit that energy in all directions, including "
  "downward, so the surface and lower atmosphere stay warmer than they "
  "would without them. Most of it is natural and beneficial: without "
  "any greenhouse effect Earth would be a frozen ball. The concern is "
  "the enhanced greenhouse effect from added gases, mainly carbon "
  "dioxide from burning fossil fuels, which strengthens absorption and "
  "forces the surface to warm until the extra heat can escape. Water "
  "vapor, the strongest greenhouse gas, acts as a feedback: warmer air "
  "holds more of it, amplifying any initial warming."),
 "how_it_works": (
  "It works in two radiation bands. Sunlight peaks in visible wavelengths "
  "and passes through greenhouse gases almost untouched. The surface "
  "warms and radiates infrared, which peaks in exactly the absorption "
  "bands of the triatomic molecules: the bending mode of water near "
  "6.3 microns, the 15-micron band of carbon dioxide, methane's bands. "
  "Absorbed infrared is re-emitted isotropically; roughly half returns "
  "downward (back-radiation), heating the surface again. Radiative "
  "transfer models integrate this through the column: each added layer "
  "of carbon dioxide raises the effective emission height to colder, "
  "higher air, which radiates less, so the surface must warm to push "
  "the same energy out. The forcing from doubled carbon dioxide is "
  "about 3.7 W/m2, and every doubling adds roughly the same increment - "
  "a logarithmic relationship first computed by Arrhenius in 1896."),
 "key_points": [
  "Greenhouse gases transmit sunlight but absorb Earth's outgoing infrared.",
  "The natural effect adds ~33 C to the global mean surface temperature.",
  "Water vapor is the strongest greenhouse gas but acts mainly as feedback.",
  "Carbon dioxide forcing grows logarithmically: each doubling adds ~3.7 W/m2.",
  "Emission height rises with more gas; the surface warms to compensate."],
 "requirements": [
  "Spectroscopic absorption data for water vapor, CO2, methane, and ozone.",
  "A radiative-transfer model (line-by-line or band model) for the column calculation.",
  "Vertical profiles of temperature, humidity, and gas concentrations."],
 "standards": [
  "Radiative forcing reported at the tropopause after stratospheric adjustment.",
  "Preindustrial baseline CO2 (278 ppm) used as the reference state."],
 "citations": [CIT_ARRHENIUS, CIT_HARTMANN],
 "sig_lens": (
  "Signature edition: the greenhouse effect reframed as his original "
  "planetary blanket science - Earth's infrared signature caught and "
  "returned by his atmospheric glasshouse, every molecule a labeled "
  "keeper of heat."),
 "demo_kind": "greenhouse_effect",
},
{
 "key": "albedo",
 "name": "Albedo and the Climate Energy Budget",
 "group": "Foundations",
 "ladder_rank": 2,
 "ladder_tier": "foundations",
 "description": (
  "Albedo is the fraction of incoming sunlight a surface reflects: fresh "
  "snow reflects 80 to 90 percent, sea ice about 50 to 70 percent, "
  "desert sand 25 to 30 percent, grassland 20 percent, dark ocean only "
  "about 6 percent. Earth's global albedo is about 0.30, meaning 30 "
  "percent of sunlight bounces straight back to space - roughly two "
  "thirds of that reflected by clouds, one third by the surface. Albedo "
  "is one of the fastest-acting levers in the climate system: when ice "
  "melts it exposes dark ocean or land that absorbs more sunlight, "
  "which melts more ice - the ice-albedo feedback. Human land use "
  "changes albedo too: deforestation, urbanization, and farming alter "
  "how much sunlight regions reflect."),
 "how_it_works": (
  "Albedo enters the energy budget as the multiplier (1 - alpha): the "
  "absorbed solar flux is the solar constant divided by four, times "
  "one minus the albedo. The global value is measured by satellites "
  "that observe reflected shortwave radiation over the whole disc; "
  "surface albedos are measured with paired upward- and "
  "downward-looking radiometers. The ice-albedo feedback works because "
  "reflectivity is a step function of phase: water at 6 percent versus "
  "ice at 60 percent means a small temperature nudge that crosses the "
  "freezing point triggers a large change in absorbed sunlight. In "
  "climate models albedo is a surface property updated each time step "
  "from snow cover, sea-ice extent, and land type, and it feeds "
  "directly into the surface energy balance that drives temperature, "
  "winds, and the circulation."),
 "key_points": [
  "Albedo is reflected fraction: snow 0.8-0.9, ocean 0.06, global mean ~0.30.",
  "Clouds contribute about two-thirds of Earth's total reflection.",
  "Ice-albedo feedback: melt darkens the surface, which melts more ice.",
  "Albedo enters the energy budget as (1 - alpha) times the solar input.",
  "Land-use change is a human albedo lever alongside greenhouse gases."],
 "requirements": [
  "Satellite shortwave-reflection data (e.g., CERES) for the global albedo.",
  "Surface albedo maps by land-cover type for regional work.",
  "Snow and sea-ice extent records to track the feedback in action."],
 "standards": [
  "Albedo reported as a unitless fraction of incident shortwave radiation.",
  "Clear-sky and all-sky albedos reported separately."],
 "citations": [CIT_HARTMANN, CIT_PEIXOTO],
 "sig_lens": (
  "Signature edition: albedo reframed as his original planetary mirror "
  "science - every surface a rated mirror in his Signature reflectance "
  "ledger, ice the brightest mirror of them all."),
 "demo_kind": "albedo",
},
{
 "key": "seasons-latitude",
 "name": "Latitude, Tilt, and the Seasons",
 "group": "Foundations",
 "ladder_rank": 2,
 "ladder_tier": "foundations",
 "description": (
  "The seasons come from Earth's 23.4-degree axial tilt, not from "
  "distance to the Sun (Earth is actually closest to the Sun in early "
  "January). As Earth orbits, each hemisphere takes turns leaning "
  "toward the Sun: the summer hemisphere gets more direct sunlight and "
  "longer days, the winter hemisphere gets slanting light and short "
  "days. At the equator the Sun is nearly overhead year-round, so the "
  "tropics have little seasonality; at the poles, months of polar day "
  "alternate with months of polar night. Latitude sets the geometry of "
  "insolation - how much sunlight arrives per square meter - and "
  "therefore sets the skeleton of every climate: hot tropics, mild "
  "mid-latitudes, cold poles."),
 "how_it_works": (
  "The solar declination - the latitude where the Sun is directly "
  "overhead - swings between +23.4 and -23.4 degrees through the year. "
  "Daily insolation at latitude phi is proportional to the hour angle: "
  "cos(H) = -tan(phi) tan(delta), where H is the sunset hour angle. "
  "When phi and delta have the same sign and their product makes the "
  "right side less than -1, the Sun never sets (polar day); greater "
  "than 1, it never rises (polar night). At 40 degrees north on the "
  "summer solstice, day length is about 14.9 hours. The equator "
  "receives roughly 2.5 times the annual sunlight per square meter "
  "that the poles do - the equator-to-pole energy gradient that "
  "drives the entire general circulation."),
 "key_points": [
  "Axial tilt (23.4 deg), not distance, makes the seasons.",
  "Declination swings +/-23.4 deg; day length follows cos(H) = -tan(phi) tan(delta).",
  "Tropics get ~2.5x the annual sunlight per m2 that the poles do.",
  "Polar day and night occur where the Sun never crosses the horizon.",
  "Latitude is the primary skeleton of every climate zone."],
 "requirements": [
  "Earth's orbital elements: tilt 23.4 deg, eccentricity 0.0167.",
  "The solar-declination formula and day-length equation.",
  "Insolation tables or a solar-geometry routine for a chosen latitude."],
 "standards": [
  "Solstices and equinoxes defined by ecliptic longitude (90, 180, 270, 0 deg).",
  "Insolation reported in W/m2 daily average."],
 "citations": [CIT_PEIXOTO, CIT_BARRY],
 "sig_lens": (
  "Signature edition: the seasons reframed as his original tilt engine "
  "- the planet's 23.4-degree lean as a Signature gear, turning "
  "sunlight into the rhythm of the year."),
 "demo_kind": "seasons",
},
{
 "key": "atmosphere-layers",
 "name": "Layers of the Atmosphere",
 "group": "Foundations",
 "ladder_rank": 2,
 "ladder_tier": "foundations",
 "description": (
  "The atmosphere is stacked in layers defined by how temperature changes "
  "with height. The troposphere (surface to about 12 km) is where weather "
  "happens: temperature falls with height, the air churns, clouds form. "
  "The stratosphere (12 to 50 km) is stably layered, temperature rising "
  "with height because the ozone layer absorbs ultraviolet sunlight - it "
  "holds the ozone shield and the jets of fast stratospheric winds. Above "
  "it the mesosphere (50 to 85 km) cools again with height, then the "
  "thermosphere heats to hundreds of degrees by solar radiation (though "
  "too thin to feel). The boundaries - tropopause, stratopause, "
  "mesopause - are the temperature turning points. Nearly all weather and "
  "climate physics that matters to people happens in the troposphere and "
  "lower stratosphere."),
 "how_it_works": (
  "Layer boundaries are defined by the temperature lapse rate: where "
  "dT/dz changes sign. In the troposphere the lapse rate averages about "
  "6.5 C per km of cooling with height, driven by the surface heating "
  "from below; when the surface is hot and the upper air cold, the "
  "layer overturns - convection, the engine of storms. The tropopause "
  "marks where temperature stops falling and the air becomes "
  "stratified: rising air hits this lid and spreads, which is why "
  "thunderstorm anvils flatten at the top. Ozone in the stratosphere "
  "absorbs UV, heating that layer and creating the stable inversion "
  "that keeps weather confined below. Radiosondes (weather balloons) "
  "measure the profile directly; satellites retrieve it from infrared "
  "and microwave emissions at different frequencies."),
 "key_points": [
  "Troposphere (0-12 km): weather layer, temperature falls ~6.5 C/km.",
  "Stratosphere (12-50 km): stable, ozone heats it, temperature rises with height.",
  "Mesosphere (50-85 km) cools with height; thermosphere is hot but paper-thin.",
  "The tropopause is the lid that caps convection and flattens storm anvils.",
  "Layer structure is read directly from balloon and satellite temperature profiles."],
 "requirements": [
  "A temperature-profile dataset (radiosonde or satellite retrieval).",
  "The definition of lapse rate and the layer boundary conventions.",
  "Ozone-profile knowledge for the stratospheric heating explanation."],
 "standards": [
  "Layer heights given as approximate global means; they vary with latitude and season.",
  "Tropopause defined by the WMO lapse-rate criterion (2 C/km over 2 km)."],
 "citations": [CIT_WALLACE, CIT_BARRY],
 "sig_lens": (
  "Signature edition: the atmospheric layers reframed as his original "
  "sky-shelf science - four stacked Signature shelves, weather living "
  "on the ground floor, the ozone guard posted on the second."),
 "demo_kind": "atmosphere_layers",
},
{
 "key": "water-cycle",
 "name": "The Water Cycle",
 "group": "Foundations",
 "ladder_rank": 3,
 "ladder_tier": "foundations",
 "description": (
  "The water cycle - evaporation, condensation, precipitation, runoff, "
  "and return - is the climate system's great heat conveyor. Water "
  "evaporating from the ocean carries latent heat upward; when it "
  "condenses into clouds and rain, that heat is released high in the "
  "troposphere, warming the air where storms live. This latent-heat "
  "transport moves roughly half of the total poleward heat flow in "
  "the tropics. The cycle also sets the geography of wet and dry: "
  "rising air in the tropics and at storm tracks rains out, sinking "
  "air in the subtropics dries out - the reason rainforests sit on "
  "the equator and deserts sit near 30 degrees. A water molecule "
  "spends about 9 days in the atmosphere between evaporation and "
  "rain, but thousands of years in the deep ocean or polar ice."),
 "how_it_works": (
  "The cycle is quantified by residence time: storage divided by "
  "flux. The atmosphere holds about 12,900 cubic km of water with a "
  "throughput of about 505,000 cubic km per year, giving a residence "
  "time near 9 days. Evaporation is governed by the Clausius-Clapeyron "
  "relation: saturation vapor pressure rises about 7 percent per "
  "degree Celsius, so a warmer world cycles water faster - more "
  "evaporation, more precipitation, more intense storms. Globally, "
  "evaporation must equal precipitation (the atmosphere stores "
  "almost nothing long-term), but locally the difference P minus E "
  "defines wet regions (positive) and deserts (negative), with the "
  "ocean's surface currents and the atmosphere's winds carrying the "
  "surplus around."),
 "key_points": [
  "Latent heat released by condensation warms the upper troposphere - the storm engine.",
  "Atmospheric water residence time is ~9 days; ocean and ice hold water for millennia.",
  "Clausius-Clapeyron: ~7% more water vapor per degree C of warming.",
  "P minus E maps wet versus dry: tropics wet, subtropics dry.",
  "Globally evaporation equals precipitation; locally the winds redistribute it."],
 "requirements": [
  "Global precipitation and evaporation datasets (e.g., GPCP, OAFlux).",
  "The Clausius-Clapeyron relation for the warming amplification.",
  "Reservoir storage and flux estimates for residence-time arithmetic."],
 "standards": [
  "Fluxes reported in mm/day or km3/year; residence time in days or years.",
  "Water-budget closure checked: global mean P minus E near zero."],
 "citations": [CIT_PEIXOTO, CIT_HARTMANN],
 "sig_lens": (
  "Signature edition: the water cycle reframed as his original "
  "sky-river ledger - evaporation the withdrawal, rain the deposit, "
  "every drop tracked through his Signature hydrologic books in "
  "nine-day turns."),
 "demo_kind": "water_cycle",
},
{
 "key": "pressure-wind",
 "name": "Pressure Gradients and Wind",
 "group": "Foundations",
 "ladder_rank": 3,
 "ladder_tier": "foundations",
 "description": (
  "Wind is air moving from high pressure toward low pressure, turned "
  "sideways by Earth's rotation. The pressure-gradient force pushes "
  "air down the pressure slope; the Coriolis force deflects it - to "
  "the right in the Northern Hemisphere, to the left in the "
  "Southern - until the two balance and the wind blows along the "
  "isobars instead of across them. That balanced state is the "
  "geostrophic wind, and it describes most large-scale winds aloft: "
  "around lows the air spirals counterclockwise (Northern "
  "Hemisphere), around highs clockwise. Near the surface, friction "
  "slows the wind, weakening the Coriolis turn so air spirals "
  "inward into lows - which is why surface lows bring converging, "
  "rising, stormy air, and highs bring sinking, clear air."),
 "how_it_works": (
  "The geostrophic wind speed is the pressure gradient divided by "
  "air density times the Coriolis parameter: Ug = (1/(rho f)) dP/dn. "
  "A 4-hectopascal difference across 100 km at 45 degrees latitude "
  "drives about 32 m/s of wind aloft - gale force from a modest "
  "gradient, because air is light and the gradient acts over a huge "
  "area. Weather maps encode this: tightly packed isobars mean "
  "strong wind, widely spaced isobars mean calm. In the boundary "
  "layer (the lowest kilometer), surface friction reduces wind "
  "speed by a third or more, so the Coriolis deflection under-turns "
  "and the wind crosses the isobars toward low pressure at roughly "
  "a 30-degree angle, feeding the convergence that powers storms."),
 "key_points": [
  "Wind = pressure-gradient force balanced (aloft) by the Coriolis force.",
  "Geostrophic wind blows along the isobars: Ug = (1/(rho f)) dP/dn.",
  "Tight isobars = strong wind; the map is the wind forecast.",
  "Surface friction turns wind inward toward lows - the storm-feeding spiral.",
  "Lows converge and rise (storms); highs diverge and sink (clear skies)."],
 "requirements": [
  "A sea-level pressure analysis (isobar map) for the region of interest.",
  "The Coriolis parameter at the latitude and standard air density.",
  "Boundary-layer knowledge for the surface-wind correction."],
 "standards": [
  "Winds reported in m/s or knots at the standard 10-meter height.",
  "Geostrophic approximation flagged as invalid within ~10 deg of the equator."],
 "citations": [CIT_WALLACE, CIT_BARRY],
 "sig_lens": (
  "Signature edition: pressure-gradient wind reframed as his original "
  "air-river mechanics - high pressure the reservoir, low pressure "
  "the drain, his Signature channels routing the flow along the "
  "isobar lines."),
 "demo_kind": "pressure_wind",
},
{
 "key": "coriolis-effect",
 "name": "The Coriolis Effect",
 "group": "Foundations",
 "ladder_rank": 3,
 "ladder_tier": "foundations",
 "description": (
  "The Coriolis effect is the apparent deflection of moving air (and "
  "water) caused by Earth's rotation: to the right of motion in the "
  "Northern Hemisphere, to the left in the Southern. It is not a real "
  "force but a consequence of moving in a rotating frame - air "
  "traveling poleward carries its equatorial eastward momentum into "
  "regions of slower-turning Earth and runs ahead, curving right. "
  "Its strength is zero at the equator and maximum at the poles, "
  "given by f = 2 Omega sin(latitude). The Coriolis effect is why "
  "hurricanes spin counterclockwise north of the equator and "
  "clockwise south of it, why the trade winds angle toward the "
  "equator, and why large-scale winds blow along isobars rather than "
  "straight down the pressure gradient."),
 "how_it_works": (
  "The Coriolis parameter f = 2 Omega sin(phi), with Omega = "
  "7.2921e-5 radians per second (Earth's spin), gives the local "
  "rotation rate of the reference frame. At 45 degrees latitude f "
  "is about 1.03e-4 per second; a 10 m/s wind feels a Coriolis "
  "acceleration of f times v, about 1 mm/s2 - tiny per second, but "
  "over hours it turns the flow 90 degrees. The sign of sin(phi) "
  "flips across the equator, reversing every deflection: that is "
  "why cyclones cannot form within about 5 degrees of the equator "
  "and why their spin mirrors between hemispheres. The Rossby "
  "number - wind speed divided by f times the length scale - tells "
  "whether rotation dominates: small Rossby number means the "
  "Coriolis force rules the flow, which is true for nearly all "
  "continental-scale weather."),
 "key_points": [
  "Deflection: right in the Northern Hemisphere, left in the Southern.",
  "Strength f = 2 Omega sin(lat); zero at the equator, max at the poles.",
  "Causes hurricane spin direction and the trade-wind angle.",
  "Explains geostrophic balance: wind along isobars, not across them.",
  "Rossby number decides whether rotation dominates a flow."],
 "requirements": [
  "Earth's rotation rate Omega = 7.2921e-5 rad/s.",
  "The target latitude for computing the local Coriolis parameter.",
  "A wind speed and length scale for the Rossby-number check."],
 "standards": [
  "Coriolis parameter reported in s^-1 with latitude stated.",
  "Hemisphere sign conventions kept explicit in every calculation."],
 "citations": [CIT_WALLACE, CIT_PEIXOTO],
 "sig_lens": (
  "Signature edition: the Coriolis effect reframed as his original "
  "spinning-floor rule - the planet's turn as a Signature curve "
  "machine, bending every wind right above the equator and left "
  "below it."),
 "demo_kind": "coriolis",
},
{
 "key": "circulation-cells",
 "name": "The Three-Cell Circulation",
 "group": "Foundations",
 "ladder_rank": 3,
 "ladder_tier": "foundations",
 "description": (
  "The general circulation of the atmosphere is organized, in each "
  "hemisphere, into three great overturning cells. The Hadley cell "
  "(equator to 30 degrees): hot air rises at the equator, flows "
  "poleward aloft, sinks in the subtropics, and returns as the "
  "trade winds - the cell that waters the rainforests and dries the "
  "deserts. The Ferrel cell (30 to 60 degrees): an indirect, "
  "eddy-driven cell whose surface westerlies carry our mid-latitude "
  "storms. The polar cell (60 degrees to pole): cold air sinks at "
  "the pole and flows equatorward as polar easterlies. This "
  "three-cell pattern is the atmosphere's answer to the "
  "equator-to-pole energy imbalance: it is the conveyor that moves "
  "excess tropical heat toward the poles."),
 "how_it_works": (
  "Each cell is a thermally direct (Hadley, polar) or eddy-driven "
  "(Ferrel) loop. In the Hadley cell, intense equatorial heating "
  "makes air buoyant; it rises to the tropopause, diverges poleward, "
  "and by conservation of angular momentum turns eastward aloft, "
  "sinking near 30 degrees where the now-dry air suppresses clouds - "
  "the subtropical high-pressure belts and the world's great "
  "deserts. The sinking branch's surface return flow is deflected "
  "by the Coriolis effect into the northeast trades (Northern "
  "Hemisphere). In mid-latitudes, baroclinic instability - the "
  "clash of warm and cold air masses - spawns eddies (storms) "
  "that drive the Ferrel cell indirectly and carry most of the "
  "poleward heat transport there. The cells shift with the "
  "seasons, following the Sun's declination by a few degrees."),
 "key_points": [
  "Hadley (0-30 deg): rises at equator, sinks in subtropics; makes deserts.",
  "Ferrel (30-60 deg): eddy-driven; surface westerlies and storm tracks.",
  "Polar (60-90 deg): sinks at pole; polar easterlies.",
  "The cells exist to move excess tropical heat poleward.",
  "Cell boundaries migrate with the seasons, following the Sun."],
 "requirements": [
  "A latitude-height cross-section of zonal-mean wind and vertical motion.",
  "Angular-momentum and Coriolis reasoning for the trade-wind direction.",
  "Seasonal-mean reanalysis fields to see the cells migrate."],
 "standards": [
  "Cells described in zonal-mean (longitude-averaged) terms.",
  "Hadley-cell edge defined by the subtropical dry-zone or streamfunction zero."],
 "citations": [CIT_PEIXOTO, CIT_HARTMANN],
 "sig_lens": (
  "Signature edition: the three cells reframed as his original "
  "planetary lung system - the Hadley breath in at the equator and "
  "out at thirty degrees, the Ferrel and polar lungs completing "
  "his Signature respiration of the sky."),
 "demo_kind": "circulation_cells",
},
{
 "key": "jet-streams",
 "name": "Jet Streams",
 "group": "Foundations",
 "ladder_rank": 4,
 "ladder_tier": "foundations",
 "description": (
  "Jet streams are narrow rivers of fast air, 10 to 12 km up, circling "
  "the planet at 100 to 250 km/h - the strongest winds in the "
  "troposphere. The subtropical jet sits near 30 degrees latitude, "
  "fed by the poleward outflow of the Hadley cell; the polar jet "
  "sits near 50 to 60 degrees, riding the sharp temperature contrast "
  "between cold polar air and warm subtropical air. They meander in "
  "great north-south waves (Rossby waves), and their dips and ridges "
  "steer storms, pull weather systems along, and decide whether a "
  "region bakes under a ridge or freezes under a trough. Pilots ride "
  "them eastward to save fuel and fight them westward; a stuck jet "
  "pattern means stuck weather - droughts, floods, and heat waves "
  "that will not move."),
 "how_it_works": (
  "Jets form by the thermal-wind relation: where temperature changes "
  "rapidly with latitude, wind must increase rapidly with height to "
  "stay in balance. The polar front - the boundary between polar "
  "and subtropical air - is the sharpest such contrast, so the "
  "strongest vertical wind shear sits above it: the polar jet. The "
  "jets are wavy because of Rossby waves, planetary-scale meanders "
  "restored by the Coriolis effect's variation with latitude; when "
  "these waves amplify and stall, weather patterns lock in place - "
  "the mechanism behind persistent extremes. Jet speed follows the "
  "season: stronger in winter when the equator-to-pole temperature "
  "contrast is largest, weaker in summer. Climate change is expected "
  "to shift jets poleward as the tropics expand, moving storm tracks "
  "and rainfall belts with them."),
 "key_points": [
  "Jets are 10-12 km up, 100-250 km/h: subtropical (~30 deg) and polar (~55 deg).",
  "Thermal wind: sharp latitudinal temperature contrast makes wind grow with height.",
  "Rossby-wave meanders steer storms; stalled waves lock in extremes.",
  "Pilots exploit eastward jets; a stuck jet means stuck weather.",
  "Warming is shifting jets poleward with the expanding tropics."],
 "requirements": [
  "Upper-air (200-300 hPa) wind analyses to locate the jet cores.",
  "A meridional temperature-gradient field for the thermal-wind check.",
  "Rossby-wave basics for interpreting the meanders."],
 "standards": [
  "Jet core defined by the wind-speed maximum at 200 hPa in standard analyses.",
  "Speeds reported in m/s with the pressure level stated."],
 "citations": [CIT_WALLACE, CIT_BARRY],
 "sig_lens": (
  "Signature edition: the jet streams reframed as his original "
  "sky rivers - two Signature torrents circling the globe, steering "
  "every storm the way his channels steer every drop."),
 "demo_kind": "jet_streams",
},
{
 "key": "ocean-heat-transport",
 "name": "Ocean Currents and Heat Transport",
 "group": "Foundations",
 "ladder_rank": 4,
 "ladder_tier": "foundations",
 "description": (
  "The ocean is the climate system's flywheel: it holds about a thousand "
  "times more heat than the atmosphere and moves it slowly around the "
  "planet. Surface currents form great gyres - the Gulf Stream and its "
  "extension the North Atlantic Drift carry warm water toward Europe, "
  "keeping winters there far milder than at the same latitude in North "
  "America; the Kuroshio does the same for Japan; cold currents like "
  "the Humboldt and Benguela chill their coasts and feed the world's "
  "richest fisheries through upwelling. Together the ocean and "
  "atmosphere split the job of moving excess tropical heat poleward "
  "roughly half and half. Because water warms and cools slowly, the "
  "ocean also gives climate its memory: today's sea-surface temperatures "
  "shape next season's weather."),
 "how_it_works": (
  "Surface currents are wind-driven: the trade winds and westerlies drag "
  "the top hundred meters into basin-scale gyres, clockwise in the "
  "Northern Hemisphere subtropics, counterclockwise in the Southern. "
  "Western boundary currents (Gulf Stream, Kuroshio, Agulhas) are "
  "narrow, deep, and fast - the Gulf Stream transports about 30 "
  "Sverdrups (30 million cubic meters per second), carrying roughly "
  "1.3 petawatts of heat poleward, computed as density times heat "
  "capacity times volume transport times temperature drop. Where winds "
  "push surface water offshore (eastern ocean boundaries), cold deep "
  "water upwells, chilling the coast and feeding nutrients upward. "
  "The deep overturning circulation (see the thermohaline record) "
  "completes the loop on century timescales, which is why the ocean "
  "lags the atmosphere by decades in responding to warming."),
 "key_points": [
  "The ocean stores ~1000x the atmosphere's heat and moves it in gyres.",
  "Western boundary currents (Gulf Stream, Kuroshio) are fast, narrow heat pipelines.",
  "Gulf Stream carries ~30 Sv and ~1.3 PW of heat toward the North Atlantic.",
  "Upwelling zones chill coasts and fertilize the richest fisheries.",
  "Ocean heat capacity gives climate its memory and its lag."],
 "requirements": [
  "Sea-surface temperature and surface-current analyses (e.g., OSCAR, drifters).",
  "Volume-transport estimates in Sverdrups for the current of interest.",
  "The heat-transport formula: rho * cp * V * delta-T."],
 "standards": [
  "Transports reported in Sverdrups (1 Sv = 1e6 m3/s); heat in petawatts.",
  "Currents named by standard oceanographic convention."],
 "citations": [CIT_PEIXOTO, CIT_HARTMANN],
 "sig_lens": (
  "Signature edition: ocean heat transport reframed as his original "
  "warm-water pipeline science - the Gulf Stream a Signature artery "
  "pumping tropical heat north, every Sverdrup metered in his ocean "
  "ledger."),
 "demo_kind": "ocean_currents",
},
{
 "key": "koppen-classification",
 "name": "The Koeppen Climate Classification",
 "group": "Foundations",
 "ladder_rank": 4,
 "ladder_tier": "foundations",
 "description": (
  "The Koeppen classification is the world's standard map of climates, "
  "built from the two variables plants care about most: temperature and "
  "precipitation. Five main groups: A (tropical, coldest month above "
  "18 C), B (arid, evaporation exceeds precipitation), C (temperate, "
  "coldest month between -3 and 18 C), D (cold continental, coldest "
  "month below -3 C), E (polar, warmest month below 10 C). Subscripts "
  "refine it: f for year-round rain, s for dry summers, w for dry "
  "winters, plus a/b/c for summer warmth. So 'Cfb' is the mild, wet "
  "oceanic climate of London and Seattle; 'BWh' is hot desert like the "
  "Sahara; 'Dfc' is subarctic like Siberia. The boundaries are moving: "
  "warming is shifting climate zones poleward and uphill, redrawing "
  "the map in real time."),
 "how_it_works": (
  "Classification proceeds as a decision tree on monthly temperature "
  "and precipitation. First check the temperature thresholds: warmest "
  "month at or below 10 C means E (polar); coldest month above 18 C "
  "means A (tropical); otherwise test aridity - if annual precipitation "
  "falls below a threshold set by temperature and seasonality, the "
  "climate is B (arid), split into hot (BW h) and cold (BW k) deserts. "
  "Remaining climates sort by coldest month: between -3 and 18 C is C "
  "(temperate), below -3 C is D (continental). Precipitation "
  "seasonality then assigns f/s/w. The scheme works because vegetation "
  "boundaries track these thresholds closely - the treeline follows "
  "the 10 C warmest-month isotherm, the steppe-to-desert boundary "
  "follows the aridity line. Modern climatologists apply the same "
  "rules to model output to map future climate zones."),
 "key_points": [
  "Five groups: A tropical, B arid, C temperate, D continental, E polar.",
  "Built on temperature and precipitation thresholds that track vegetation.",
  "Subscripts f/s/w encode rainfall seasonality; a/b/c encode summer warmth.",
  "Cfb = oceanic mild-wet; BWh = hot desert; Dfc = subarctic.",
  "Zones are shifting poleward as the planet warms - a living map."],
 "requirements": [
  "Monthly mean temperature and precipitation for the location (a full year).",
  "The Koeppen threshold rules (temperature and aridity criteria).",
  "A gridded climate dataset for mapping zones at scale."],
 "standards": [
  "Group letters A-E and subscripts per Koeppen (1936) conventions.",
  "Aridity threshold computed with the standard temperature-seasonality formula."],
 "citations": [CIT_KOPPEN, CIT_BARRY],
 "sig_lens": (
  "Signature edition: the Koeppen map reframed as his original "
  "climate atlas - five Signature letters stamping every place on "
  "Earth with its temperature-and-rain identity."),
 "demo_kind": "koppen",
},
{
 "key": "monsoons",
 "name": "Monsoons",
 "group": "Compounded",
 "ladder_rank": 5,
 "ladder_tier": "compounded",
 "description": (
  "Monsoons are the planet's great seasonal wind reversals, driven by "
  "the different heating of land and ocean. In summer, continents heat "
  "faster than the sea; the hot land breeds low pressure that pulls in "
  "moist ocean air, which rises and dumps torrential rain. In winter "
  "the land cools faster, high pressure builds, and dry continental "
  "air flows back out to sea. The South Asian monsoon waters the "
  "crops of over a billion people; the West African monsoon greens "
  "the Sahel; the East Asian monsoon soaks China, Korea, and Japan; "
  "weaker monsoons touch Australia and North America. Monsoon rains "
  "are life and risk at once: a strong monsoon means full reservoirs "
  "and harvests, a weak one means drought, and an intense burst means "
  "floods."),
 "how_it_works": (
  "The engine is differential heat capacity: land (small heat "
  "capacity, no mixing) swings tens of degrees between seasons while "
  "the ocean (huge heat capacity, deep mixing) barely moves. The "
  "summer land-sea temperature contrast lowers pressure over the "
  "continent (warm air expands, surface pressure falls), and the "
  "pressure gradient drives onshore flow. Moist air forced up by "
  "the land's heat and by mountain ranges (the Himalayas wring out "
  "the Indian monsoon) condenses, releasing latent heat that "
  "intensifies the low - a positive feedback that makes monsoons "
  "stronger than the initial contrast alone would suggest. In "
  "winter the contrast reverses: cold dense air piles over the "
  "continent as the Siberian high, and dry offshore winds take "
  "over. Monsoon strength is tracked by indices combining wind "
  "reversal and rainfall, and it varies with ENSO, snow cover, and "
  "long-term warming."),
 "key_points": [
  "Land heats/cools faster than ocean: the seasonal contrast drives wind reversal.",
  "Summer: onshore moist flow, rising air, torrential rain; winter: dry offshore flow.",
  "Latent-heat feedback amplifies the monsoon beyond the initial contrast.",
  "Mountains (Himalayas) wring extra rain from monsoon flow.",
  "Over a billion people depend on the South Asian monsoon rains."],
 "requirements": [
  "Seasonal land-sea temperature contrast and surface pressure fields.",
  "Monsoon wind-reversal and rainfall indices for the region.",
  "Topography data where orographic lifting matters."],
 "standards": [
  "Monsoon onset/withdrawal defined by standard rainfall and wind criteria.",
  "Indices reported relative to a stated climatology period."],
 "citations": [CIT_BARRY, CIT_HARTMANN],
 "sig_lens": (
  "Signature edition: monsoons reframed as his original seasonal "
  "tide of air - the continent inhaling ocean moisture all summer "
  "and exhaling dry air all winter, timed on his Signature "
  "calendar."),
 "demo_kind": "monsoon",
},
{
 "key": "enso",
 "name": "El Nino and La Nina (ENSO)",
 "group": "Compounded",
 "ladder_rank": 5,
 "ladder_tier": "compounded",
 "description": (
  "ENSO - the El Nino-Southern Oscillation - is the climate system's "
  "most powerful year-to-year rhythm. Every few years the tropical "
  "Pacific flips: in El Nino, the trade winds weaken, warm water "
  "sloshes east toward South America, and the usual upwelling of "
  "cold water off Peru shuts down; in La Nina, the trades strengthen "
  "and the cold tongue intensifies. These are not local events: the "
  "shifted tropical rainfall reorganizes the entire atmospheric "
  "circulation, sending ripple effects - teleconnections - worldwide: "
  "drought in Australia and Indonesia, floods in Peru and California, "
  "fewer Atlantic hurricanes during El Nino, a harsher southern US "
  "winter. ENSO is tracked by the Oceanic Nino Index (ONI): sea-"
  "surface temperature anomalies in the Nino 3.4 region, with +/-0.5 C "
  "sustained over five overlapping seasons marking events."),
 "how_it_works": (
  "The mechanism is the Bjerknes feedback, a coupled ocean-atmosphere "
  "loop. Normally the trades pile warm water in the western Pacific "
  "and the east stays cool through upwelling; the east-west "
  "temperature contrast drives the Walker circulation, whose surface "
  "trades reinforce the pile-up. If the trades weaken slightly, warm "
  "water slides east, the contrast weakens, the Walker circulation "
  "slackens, and the trades weaken further - the feedback amplifies "
  "the nudge into a full El Nino. The system oscillates because "
  "oceanic Kelvin and Rossby waves cross the basin and reflect, "
  "resetting the thermocline tilt every 2 to 7 years - the delayed "
  "oscillator. Forecasters watch subsurface heat content and wind "
  "anomalies months ahead: the ocean's memory makes ENSO the most "
  "predictable piece of year-to-year climate."),
 "key_points": [
  "ENSO is the tropical Pacific's 2-7 year coupled ocean-atmosphere oscillation.",
  "El Nino: weak trades, warm east Pacific; La Nina: strong trades, cool east.",
  "Bjerknes feedback amplifies small wind nudges into basin-wide events.",
  "Teleconnections spread ENSO's effects worldwide (droughts, floods, hurricanes).",
  "ONI +/-0.5 C over 5 seasons defines events; ocean memory makes it predictable."],
 "requirements": [
  "Tropical Pacific SST anomalies (Nino 3.4 region) and subsurface heat content.",
  "Surface wind anomaly fields to watch the Bjerknes feedback engage.",
  "The ONI definition: 3-month running mean, +/-0.5 C, 5 consecutive seasons."],
 "standards": [
  "Events classified per NOAA Climate Prediction Center ONI thresholds.",
  "Anomalies relative to a centered 30-year base period, updated every 5 years."],
 "citations": [CIT_BJERKNES, CIT_TRENBETH_ENSO],
 "sig_lens": (
  "Signature edition: ENSO reframed as his original Pacific "
  "seesaw - the great ocean rocking warm east then cold west on "
  "his Signature two-to-seven-year metronome, every swing telegraphed "
  "around the world."),
 "demo_kind": "enso",
},
{
 "key": "nao-teleconnections",
 "name": "The North Atlantic Oscillation and Teleconnections",
 "group": "Compounded",
 "ladder_rank": 5,
 "ladder_tier": "compounded",
 "description": (
  "The North Atlantic Oscillation (NAO) is the seesaw of atmospheric "
  "mass between the Icelandic low and the Azores high - the dominant "
  "pattern of winter climate variability over the North Atlantic and "
  "Europe. In its positive phase, both centers strengthen: the jet "
  "stream and storm track aim at northern Europe, bringing mild wet "
  "winters there and cold dry conditions to the Mediterranean and "
  "eastern North America. In its negative phase, both weaken: storms "
  "sag south, northern Europe freezes, and the Mediterranean soaks. "
  "The NAO is one member of a family of teleconnections - the Pacific-"
  "North American pattern, the Arctic Oscillation, the Madden-Julian "
  "Oscillation - recurring large-scale pressure patterns that link "
  "distant weather, letting climatologists read one region's winter "
  "from another's pressure field."),
 "how_it_works": (
  "The NAO index is the normalized sea-level pressure difference "
  "between the Azores and Iceland. It works through the jet: a "
  "stronger pressure gradient tightens and accelerates the eddy-driven "
  "jet, steering Atlantic storms along a more northern, zonal track; "
  "a weaker gradient lets the jet meander and dip south. The pattern "
  "is maintained by feedback between the eddies (storms) and the mean "
  "flow - storms flux momentum into the jet, and the jet steers the "
  "storms. Teleconnections matter because the atmosphere is a "
  "waveguide: a heating anomaly in one place (say, the tropical "
  "Pacific during El Nino) excites Rossby waves that arc across the "
  "globe along great-circle routes, imprinting alternating high and "
  "low anomalies thousands of kilometers away - the physical reason "
  "a warm patch of Pacific water changes winter in North America."),
 "key_points": [
  "NAO = pressure seesaw between the Icelandic low and Azores high.",
  "Positive NAO: strong jet, mild wet northern Europe; negative: the reverse.",
  "Teleconnections are recurring pressure patterns linking distant weather.",
  "Rossby-wave waveguides carry tropical heating anomalies worldwide.",
  "Storm-track position follows the jet, and the jet follows the pressure gradient."],
 "requirements": [
  "Sea-level pressure at the Azores and Iceland stations (or gridded equivalents).",
  "Upper-air wind fields to locate the jet and storm track.",
  "Wave-theory basics for the teleconnection mechanism."],
 "standards": [
  "NAO index normalized relative to a stated reference period.",
  "Phase defined by the sign of the standardized pressure difference."],
 "citations": [CIT_WALLACE, CIT_BARRY],
 "sig_lens": (
  "Signature edition: the NAO reframed as his original Atlantic "
  "seesaw - Iceland and the Azores trading atmospheric weight on "
  "his Signature balance, Europe's winter tipping with the "
  "scale."),
 "demo_kind": "nao",
},
{
 "key": "climate-forcings",
 "name": "Climate Forcings",
 "group": "Compounded",
 "ladder_rank": 6,
 "ladder_tier": "compounded",
 "description": (
  "A climate forcing is any imposed change in Earth's energy balance, "
  "measured in watts per square meter at the top of the atmosphere. "
  "Positive forcings warm the planet, negative forcings cool it. The "
  "main natural forcings: changes in solar output (small, about 0.1 "
  "W/m2 over the solar cycle), volcanic aerosols (large but brief - "
  "Pinatubo cooled the planet about 0.5 C for two years), and slow "
  "orbital changes (the Milankovitch pacemaker of ice ages). The "
  "main human forcings: greenhouse gases (carbon dioxide, methane, "
  "nitrous oxide - strongly positive), and aerosols from pollution "
  "and land-use change (negative, masking some warming). Net human "
  "forcing today is about +2.7 W/m2 relative to 1750 - dominated by "
  "the +2.2 W/m2 from carbon dioxide - which is why the planet is "
  "warming: the ledger no longer balances."),
 "how_it_works": (
  "Forcing is computed as the instantaneous change in net radiation "
  "at the tropopause before temperatures adjust. For carbon dioxide "
  "the standard formula is delta-F = 5.35 ln(C/C0) W/m2: each "
  "doubling adds about 3.7 W/m2, the logarithmic shape coming from "
  "band saturation (the center of the CO2 band is already opaque; "
  "added gas works the band edges). Methane and nitrous oxide have "
  "their own formulas with overlap corrections where their bands "
  "interfere. Aerosol forcing is harder: sulfate particles reflect "
  "sunlight directly and brighten clouds (the indirect effect), "
  "both cooling, but the numbers carry the largest uncertainty in "
  "the budget. Forcings add: the total is the sum of the parts, and "
  "the climate responds to the total with its characteristic "
  "sensitivity - which is why attributing observed warming means "
  "accounting every forcing, not just the famous ones."),
 "key_points": [
  "Forcing = imposed energy-balance change, in W/m2; + warms, - cools.",
  "CO2 forcing: 5.35 ln(C/C0); each doubling adds ~3.7 W/m2 (logarithmic).",
  "Net human forcing today is about +2.7 W/m2 vs 1750.",
  "Volcanoes cool briefly and strongly; solar changes are small.",
  "Aerosol cooling is the largest uncertainty - it masks some warming."],
 "requirements": [
  "Concentrations of CO2, methane, nitrous oxide, and halocarbons vs 1750.",
  "The standard forcing formulas with band-overlap corrections.",
  "Aerosol optical-depth and cloud-effect estimates for the negative term."],
 "standards": [
  "Effective radiative forcing (ERF) including rapid adjustments, per IPCC convention.",
  "1750 as the preindustrial reference year."],
 "citations": [CIT_IPCC, CIT_HANSEN],
 "sig_lens": (
  "Signature edition: forcings reframed as his original ledger "
  "entries - every watt of push or pull on the planet's energy "
  "balance posted as a signed line in his Signature forcing "
  "books."),
 "demo_kind": "forcings",
},
{
 "key": "climate-feedbacks",
 "name": "Climate Feedbacks",
 "group": "Compounded",
 "ladder_rank": 6,
 "ladder_tier": "compounded",
 "description": (
  "Feedbacks are the climate's replies to warming - processes that "
  "amplify or dampen the initial push. The big amplifiers: water "
  "vapor (warmer air holds more moisture, and water vapor is a "
  "greenhouse gas - about +1.6 W/m2 per degree), ice-albedo (melt "
  "darkens the surface, absorbing more sun), and clouds at high "
  "latitudes. The main damper: the Planck feedback - a warmer "
  "planet radiates more heat to space (about -3.2 W/m2 per degree), "
  "which is the ultimate stabilizer that keeps the system from "
  "running away. Clouds are the wild card: low clouds cool by "
  "reflecting sunlight, high thin clouds warm by trapping heat, "
  "and their net feedback remains the largest uncertainty in how "
  "much warming a given forcing produces. Feedbacks decide whether "
  "a 3.7 W/m2 push from doubled CO2 becomes 1.2 degrees of warming "
  "or 3 to 4 degrees."),
 "how_it_works": (
  "Feedback analysis linearizes the response: the temperature change "
  "is the no-feedback (Planck) response divided by one minus the "
  "sum of feedback factors, delta-T = delta-T0 / (1 - f). The "
  "Planck response to doubled CO2 is about 1.2 C; with a total "
  "feedback factor near 0.6, the gain is 2.5 and warming reaches "
  "about 3 C. Each feedback is quantified as watts per square "
  "meter per degree of warming: water vapor +1.6, lapse rate -0.6 "
  "(they partly cancel - warmer upper air radiates more), surface "
  "albedo +0.3, clouds +0.4 (net, uncertain). The factors are "
  "extracted from models by the radiative-kernel technique: "
  "perturb one variable, compute the radiation change, hold "
  "everything else fixed. The sum must stay below 1 or the "
  "system would be unstable - Earth's feedbacks amplify strongly "
  "but remain bounded, which is why the planet has never boiled "
  "away."),
 "key_points": [
  "Feedbacks amplify (water vapor, ice-albedo) or damp (Planck) warming.",
  "Planck feedback (-3.2 W/m2/K) is the ultimate stabilizer.",
  "delta-T = delta-T0/(1-f): with f~0.6, 1.2 C becomes ~3 C.",
  "Cloud feedback is the largest uncertainty in the total.",
  "Feedback factors sum below 1 - the system amplifies but stays bounded."],
 "requirements": [
  "A climate model (or kernel) to isolate each feedback's W/m2/K.",
  "The Planck response as the no-feedback reference.",
  "Cloud-property observations to constrain the wild-card term."],
 "standards": [
  "Feedbacks reported in W/m2 per K with the reference state stated.",
  "Kernel method as the standard decomposition technique."],
 "citations": [CIT_HARTMANN, CIT_IPCC],
 "sig_lens": (
  "Signature edition: feedbacks reframed as his original echo "
  "science - the planet answering every warming nudge with its "
  "own Signature echo, water vapor and ice shouting back, the "
  "Planck reply keeping the shout from becoming a scream."),
 "demo_kind": "feedbacks",
},
{
 "key": "climate-sensitivity",
 "name": "Climate Sensitivity",
 "group": "Compounded",
 "ladder_rank": 6,
 "ladder_tier": "compounded",
 "description": (
  "Climate sensitivity is the headline number of climatology: how much "
  "the planet warms if carbon dioxide doubles, after the system fully "
  "adjusts. The equilibrium climate sensitivity (ECS) is the "
  "long-term answer - the IPCC's best estimate is 3 C, with a likely "
  "range of 2.5 to 4 C. The transient climate response (TCR) is the "
  "warming at the moment of doubling in a steadily rising scenario - "
  "about 1.8 C - and it is what near-term policy actually meets. "
  "Sensitivity is estimated three ways: from climate models, from "
  "the instrumental record (how much warming past forcings produced), "
  "and from paleoclimate (how much past CO2 changes warmed the "
  "world). All three now agree near 3 C - a convergence that took "
  "forty years of research, since the famous Charney report first "
  "gave 1.5 to 4.5 C in 1979."),
 "how_it_works": (
  "Sensitivity connects forcing to temperature through the feedback "
  "parameter lambda: ECS = delta-F(2xCO2) / lambda, where delta-F "
  "is 3.7 W/m2 and lambda is about 1.2 W/m2 per K (net of Planck "
  "cooling and the amplifying feedbacks), giving roughly 3 C. "
  "Instrumental estimates invert the energy budget: observed warming "
  "plus measured ocean heat uptake, divided by the known forcing "
  "history, yields lambda directly. Paleoclimate estimates use the "
  "Last Glacial Maximum (about 6 C colder with known forcings from "
  "ice sheets, CO2, and dust) or the warm Pliocene as natural "
  "experiments. TCR is smaller than ECS because the deep ocean "
  "takes centuries to warm - the 'warming in the pipeline' that "
  "arrives after emissions stop. Uncertainty in sensitivity is "
  "dominated by cloud feedback, the same wild card as ever."),
 "key_points": [
  "ECS ~3 C per CO2 doubling (likely 2.5-4 C); TCR ~1.8 C.",
  "ECS = 3.7 W/m2 / lambda; lambda ~1.2 W/m2/K after feedbacks.",
  "Three independent lines of evidence converge near 3 C.",
  "The Charney report (1979) already said 1.5-4.5 C - the center held.",
  "Deep-ocean lag makes TCR smaller than ECS; pipeline warming arrives later."],
 "requirements": [
  "The doubled-CO2 forcing (3.7 W/m2) and a feedback-parameter estimate.",
  "Instrumental warming, ocean heat uptake, and forcing history for the budget method.",
  "A paleoclimate benchmark (LGM or Pliocene) for the geological method."],
 "standards": [
  "ECS defined at equilibrium; TCR at year 70 of 1%/yr CO2 rise, per CMIP convention.",
  "Likely ranges reported as IPCC calibrated uncertainty language."],
 "citations": [CIT_IPCC, CIT_HANSEN],
 "sig_lens": (
  "Signature edition: climate sensitivity reframed as his original "
  "master dial - one Signature number, three degrees per doubling, "
  "the single dial setting that tunes the whole planet's answer."),
 "demo_kind": "climate_sensitivity",
},
{
 "key": "carbon-cycle",
 "name": "The Carbon Cycle",
 "group": "Compounded",
 "ladder_rank": 6,
 "ladder_tier": "compounded",
 "description": (
  "The carbon cycle is the circulation of carbon among atmosphere, "
  "ocean, land, and rocks - and the reason human emissions "
  "accumulate. The atmosphere holds about 850 gigatons of carbon "
  "(as CO2); the ocean holds about 38,000, land vegetation and "
  "soils about 2,000. Each year photosynthesis and respiration "
  "exchange roughly 120 gigatons with the land, and the ocean "
  "exchanges about 90 - huge natural fluxes that nearly balance. "
  "Fossil-fuel burning and deforestation add about 11 gigatons per "
  "year; the ocean absorbs about 3 and land ecosystems about 3.5, "
  "leaving roughly half the emissions in the air. That airborne "
  "fraction - about 45 percent - is why CO2 climbs about 2.5 ppm "
  "per year. On thousand-year timescales the deep ocean and "
  "weathering of rocks will slowly draw it back down, but on human "
  "timescales the added carbon stays."),
 "how_it_works": (
  "The cycle is bookkept as reservoirs and fluxes: change in a "
  "reservoir equals inflows minus outflows. The ocean sink works by "
  "solubility (cold water holds more CO2) and the biological pump "
  "(plankton carry carbon to the deep sea when they die); the land "
  "sink works by CO2 fertilization (plants grow faster with more "
  "CO2) and regrowing forests. About 2.13 gigatons of carbon "
  "equals 1 ppm of atmospheric CO2, so the budget converts directly "
  "to the Keeling curve's annual rise. The sinks are not guaranteed: "
  "warming reduces ocean solubility, droughts and fires can flip "
  "forests from sink to source, and permafrost thaw threatens to "
  "release long-frozen carbon - positive feedbacks that would raise "
  "the airborne fraction. Isotopes fingerprint the source: fossil "
  "carbon is depleted in carbon-13 and free of carbon-14, and the "
  "atmosphere's isotopic shift matches fossil fuel exactly."),
 "key_points": [
  "Reservoirs: atmosphere ~850 GtC, ocean ~38,000, land ~2,000.",
  "Natural fluxes (~120 GtC/yr land, ~90 ocean) nearly balance; humans add ~11.",
  "~45% of emissions stay airborne - the airborne fraction.",
  "2.13 GtC = 1 ppm: the budget converts directly to the Keeling curve.",
  "Isotopes prove the added CO2 is fossil: depleted C-13, no C-14."],
 "requirements": [
  "Annual fossil-fuel and land-use emission inventories.",
  "Ocean and land sink estimates (from models and atmospheric inversions).",
  "The Keeling-curve record and isotopic measurements for verification."],
 "standards": [
  "Carbon reported in GtC; CO2 mass is 3.664x the carbon mass.",
  "Global Carbon Budget conventions for sink attribution."],
 "citations": [CIT_KEELING, CIT_IPCC],
 "sig_lens": (
  "Signature edition: the carbon cycle reframed as his original "
  "planetary carbon ledger - atmosphere, ocean, and land as three "
  "Signature vaults, every gigaton posted, the fossil withdrawal "
  "stamped in isotopes."),
 "demo_kind": "carbon_cycle",
},
{
 "key": "ozone-layer",
 "name": "The Ozone Layer",
 "group": "Compounded",
 "ladder_rank": 7,
 "ladder_tier": "compounded",
 "description": (
  "The ozone layer is a diffuse shield of ozone (O3) in the lower "
  "stratosphere, 15 to 30 km up, that absorbs the Sun's harmful "
  "ultraviolet radiation. Though it would be only about 3 millimeters "
  "thick if compressed to the surface (300 Dobson units), it blocks "
  "nearly all UV-C and most UV-B - the wavelengths that cause skin "
  "cancer, cataracts, and crop damage. In the 1980s scientists "
  "discovered the Antarctic ozone hole: each spring, chlorine from "
  "human-made CFCs destroyed ozone over the pole in a catalytic "
  "cycle, one chlorine atom killing thousands of ozone molecules. "
  "The 1987 Montreal Protocol banned CFCs - the most successful "
  "environmental treaty in history - and the layer is now healing, "
  "on track to recover by mid-century. Ozone is also a greenhouse "
  "gas, linking the ozone story to climate."),
 "how_it_works": (
  "Ozone forms by the Chapman cycle: ultraviolet light splits O2, "
  "and the freed oxygen atoms join O2 to make O3; ozone in turn "
  "absorbs UV, which is what heats the stratosphere. The layer "
  "peaks where production (needs UV, so higher up) and destruction "
  "balance. CFCs drifted up over decades, and in the polar "
  "winter, ice-crystal clouds converted their chlorine into active "
  "forms; spring sunlight then unleashed the catalytic cycle Cl + "
  "O3 -> ClO + O2, ClO + O -> Cl + O2, destroying ozone without "
  "consuming the chlorine. The Dobson unit measures the total "
  "column: 300 DU is normal, the hole drops below 100. Recovery "
  "is tracked by the shrinking hole area each September-November "
  "and by declining stratospheric chlorine loading - the treaty "
  "working exactly as designed."),
 "key_points": [
  "Ozone at 15-30 km absorbs UV-B/C; 300 Dobson units = ~3 mm at surface pressure.",
  "CFC chlorine destroyed Antarctic ozone catalytically each spring.",
  "Montreal Protocol (1987) banned CFCs - the model environmental treaty.",
  "The layer is healing; full recovery expected around mid-century.",
  "Ozone is also a greenhouse gas, tying ozone science to climate."],
 "requirements": [
  "Total-column ozone measurements (Dobson/Brewer instruments, satellites).",
  "Stratospheric chlorine/bromine loading records.",
  "Polar stratospheric cloud and temperature data for hole-season analysis."],
 "standards": [
  "Ozone reported in Dobson units; hole defined by the 220-DU contour.",
  "Recovery assessed against 1980 benchmark levels."],
 "citations": [CIT_MOLINA, CIT_IPCC],
 "sig_lens": (
  "Signature edition: the ozone layer reframed as his original "
  "sky-shield watch - a three-millimeter Signature shield holding "
  "back the Sun's harshest light, the treaty its repair order."),
 "demo_kind": "ozone",
},
{
 "key": "urban-heat-island",
 "name": "Urban Heat Islands",
 "group": "Compounded",
 "ladder_rank": 7,
 "ladder_tier": "compounded",
 "description": (
  "Cities run hotter than the countryside around them - the urban "
  "heat island effect, typically 2 to 5 C warmer at night, sometimes "
  "more. Asphalt and concrete absorb the day's sun and release it "
  "slowly after dark; buildings block the wind and trap heat in "
  "street canyons; cars, industry, and air conditioners add waste "
  "heat; and there is little vegetation to cool the air by "
  "evaporation. The effect is strongest on calm, clear nights and "
  "during heat waves, when it turns dangerous: excess heat kills, "
  "and it kills disproportionately in poor neighborhoods with less "
  "green space and less cooling. Countermeasures are proven - "
  "street trees, green roofs, reflective 'cool' roofs and pavements, "
  "urban parks - and they cool blocks by measurable degrees. "
  "Climatologists correct for heat islands when computing global "
  "warming, using rural stations and homogenization, so the "
  "warming record is not a city artifact."),
 "how_it_works": (
  "The island is quantified as the urban-rural temperature "
  "difference, largest for nighttime minima because the built "
  "surface's thermal mass delays cooling. The surface energy "
  "balance explains it: urban materials have low albedo and high "
  "heat capacity, evapotranspiration is near zero (no plants, "
  "sealed surfaces), and the canyon geometry traps outgoing "
  "infrared by multiple reflection. Satellite thermal imagery "
  "maps the island block by block; dense station pairs (city "
  "versus nearby rural) track it through time. Mitigation is "
  "engineering: raising albedo with cool roofs reflects tens of "
  "watts per square meter, and a mature street tree cools its "
  "surroundings by transpiration equivalent to several room air "
  "conditioners. Global temperature datasets remove the island "
  "signal with homogenization algorithms and by weighting rural "
  "stations, and independent satellite and ocean records confirm "
  "the same warming."),
 "key_points": [
  "Cities run 2-5 C hotter than surroundings, worst at night and in heat waves.",
  "Causes: dark heat-storing surfaces, waste heat, no evaporative cooling, canyon trapping.",
  "Heat kills unequally - poor, treeless neighborhoods suffer most.",
  "Trees, green roofs, and cool reflective surfaces measurably cool blocks.",
  "Global warming records are corrected for heat islands; the trend is not urban."],
 "requirements": [
  "Paired urban and rural station records (or satellite land-surface temperature).",
  "Land-cover and albedo maps for the mitigation analysis.",
  "Homogenized global temperature datasets for the correction context."],
 "standards": [
  "Heat-island intensity as urban-minus-rural, with station metadata stated.",
  "Heat-wave mortality analyses use standard epidemiological excess-death methods."],
 "citations": [CIT_BARRY, CIT_IPCC],
 "sig_lens": (
  "Signature edition: urban heat islands reframed as his original "
  "city-fever readings - the metropolis running a Signature "
  "temperature, his cool-roof and tree prescriptions the "
  "treatment plan."),
 "demo_kind": "uhi",
},
{
 "key": "tree-rings",
 "name": "Dendroclimatology: Tree Rings",
 "group": "Compounded",
 "ladder_rank": 7,
 "ladder_tier": "compounded",
 "description": (
  "Dendroclimatology reads climate from tree rings: each year a tree "
  "adds one ring, wide in good growing years, narrow in bad ones. "
  "Where temperature limits growth - high latitudes, high altitudes "
  "- ring width and wood density track summer temperature; where "
  "moisture limits growth - arid lands - they track rainfall. By "
  "cross-dating overlapping ring patterns from living trees, dead "
  "wood, and beams in old buildings, chronologies reach back "
  "thousands of years (bristlecone pines exceed 5,000). The "
  "technique is annually resolved and precisely dated - no other "
  "proxy pins a year so exactly. Tree rings revealed the Medieval "
  "warmth and Little Ice Age in regional detail and, joined with "
  "other proxies, underpin reconstructions of the last millennium's "
  "temperature history."),
 "how_it_works": (
  "The method starts with cross-dating: matching the pattern of "
  "wide and narrow rings across many trees to assign every ring an "
  "exact calendar year, catching false and missing rings. Then "
  "standardization removes the age trend (young trees grow fast, "
  "old trees slow) by dividing each ring width by the expected "
  "growth curve, leaving a dimensionless ring-width index with "
  "mean 1.0 - the climate signal. The index is calibrated against "
  "instrumental temperature or rainfall during the overlap period, "
  "and the calibration is verified on independent years before "
  "being extended backward. Maximum latewood density (from X-ray "
  "densitometry) gives an even cleaner temperature signal than "
  "width in cold regions. Replication across dozens of trees "
  "averages out individual quirks, leaving the shared climate "
  "forcing."),
 "key_points": [
  "One ring per year; width/density track the limiting climate factor.",
  "Cross-dating assigns exact calendar years; chronologies reach 5,000+ years.",
  "Standardization divides out the age trend, leaving the climate index.",
  "Calibrate on instrumental data, verify on independent years, then extend back.",
  "Annually resolved and exactly dated - the gold standard of dating precision."],
 "requirements": [
  "Ring-width (or density) series from multiple trees at a climate-limited site.",
  "Cross-dating across the sample set to fix every calendar year.",
  "Instrumental climate data overlapping the chronology for calibration."],
 "standards": [
  "Standardization by conservative detrending (negative exponential or spline).",
  "Chronology quality reported via expressed population signal (EPS)."],
 "citations": [CIT_BARRY, CIT_STD],
 "sig_lens": (
  "Signature edition: tree rings reframed as his original "
  "wooden yearbooks - every ring a Signature page, wide years "
  "his bold entries, the bristlecone his five-thousand-year "
  "archive."),
 "demo_kind": "tree_rings",
},
{
 "key": "ice-cores",
 "name": "Ice Cores",
 "group": "Advanced",
 "ladder_rank": 7,
 "ladder_tier": "compounded",
 "description": (
  "Ice cores are climate's time machines: cylinders of ancient ice "
  "drilled from Greenland and Antarctica that trap the past in "
  "frozen layers. Each year's snowfall buries the last, and air "
  "bubbles sealed in the ice are literal samples of ancient "
  "atmosphere - the Vostok core showed carbon dioxide swinging "
  "between 180 ppm in ice ages and 280 ppm in warm times over "
  "420,000 years. The ice itself records temperature through "
  "oxygen isotopes: colder snow is depleted in heavy oxygen-18, "
  "so the isotope ratio is a paleothermometer. Dust, volcanic "
  "ash, and chemistry add wind, eruption, and pollution histories. "
  "Greenland cores revealed the climate's violent side: "
  "Dansgaard-Oeschger events, swings of up to 10 C within decades "
  "during the last ice age - proof that climate can flip far "
  "faster than anyone once believed."),
 "how_it_works": (
  "The paleothermometer rests on fractionation: heavier H2(18)O "
  "condenses preferentially, so precipitation gets isotopically "
  "lighter as air cools along its journey - the delta-18O of the "
  "ice records the condensation temperature, roughly 0.67 permil "
  "per degree Celsius in Greenland. Gas bubbles are dated younger "
  "than the surrounding ice (air seals at depth), so an age "
  "model corrects the offset; annual layer counting, volcanic "
  "ash markers, and ice-flow models extend the chronology. CO2 "
  "is measured by crushing the ice under vacuum and analyzing "
  "the released air - the technique behind the 420,000-year "
  "Vostok record and the 800,000-year EPICA record showing CO2 "
  "never exceeded 300 ppm until the industrial era. Replicate "
  "cores from both poles confirm the global signal."),
 "key_points": [
  "Air bubbles are direct samples of ancient atmosphere (Vostok: 420k years).",
  "Oxygen isotopes are a paleothermometer: ~0.67 permil per C in Greenland.",
  "CO2 swung 180-280 ppm with ice ages; never above 300 ppm until industry.",
  "Dansgaard-Oeschger events: 10 C swings in decades - climate can flip fast.",
  "Ash layers and layer counting give the chronology; gas-age models correct offsets."],
 "requirements": [
  "An ice-core isotope and gas record (Vostok, EPICA, or Greenland cores).",
  "The isotope-temperature calibration for the site.",
  "An age model: layer counting plus gas-age/ice-age offset correction."],
 "standards": [
  "Isotopes reported as delta-18O in permil vs SMOW.",
  "Gas records corrected for gravitational and thermal fractionation."],
 "citations": [CIT_VOSTOK, CIT_DANSGAARD],
 "sig_lens": (
  "Signature edition: ice cores reframed as his original "
  "frozen library - 800,000 years of atmosphere shelved in "
  "Signature volumes, every bubble a sealed page of ancient "
  "air."),
 "demo_kind": "ice_cores",
},
{
 "key": "general-circulation-models",
 "name": "General Circulation Models",
 "group": "Advanced",
 "ladder_rank": 8,
 "ladder_tier": "advanced",
 "description": (
  "General circulation models (GCMs) are the climate system written "
  "as mathematics and run on supercomputers: the atmosphere and "
  "ocean divided into three-dimensional grid boxes, the laws of "
  "fluid motion, thermodynamics, and radiation applied in every "
  "box, stepped forward in time. A modern model has dozens of "
  "vertical levels, a grid spacing near 100 km (finer in the "
  "newest), and components for sea ice, land vegetation, "
  "chemistry, and the carbon cycle. GCMs reproduce the observed "
  "climate - the jet streams, the monsoons, ENSO's rhythm, the "
  "warming of the last century - from physics alone, and they are "
  "the laboratory where the future is tested: feed in an emissions "
  "scenario, and the model projects the climate of 2050 and 2100. "
  "Their lineage runs from Manabe and Wetherald's 1967 radiative-"
  "convective model to today's Earth system models."),
 "how_it_works": (
  "A GCM discretizes the primitive equations (conservation of "
  "momentum, mass, energy, and moisture) on a grid and integrates "
  "them with time steps limited by the Courant condition - the "
  "step must be short enough that no signal crosses a grid box "
  "in one step (for 100 km boxes and 300 m/s waves, about 5 "
  "minutes). Processes too small for the grid - clouds, "
  "turbulence, convection - are parameterized: represented by "
  "formulas relating their average effect to the resolved flow. "
  "The model is spun up for centuries to equilibrate the deep "
  "ocean, then validated against observations (the 'historical' "
  "experiment must reproduce 20th-century warming only when "
  "human forcings are included). Projections run ensembles - "
  "many runs with slightly different starts - because chaos "
  "makes single runs noisy; the ensemble mean is the forced "
  "signal, the spread is the uncertainty."),
 "key_points": [
  "GCMs solve fluid-motion, thermodynamics, and radiation on a 3D grid.",
  "Time steps obey the Courant condition (~minutes for 100 km grids).",
  "Sub-grid processes (clouds, convection) are parameterized.",
  "Historical runs reproduce 20th-century warming only with human forcings.",
  "Ensembles separate the forced signal from chaotic noise."],
 "requirements": [
  "A GCM or Earth system model (community codes are openly documented).",
  "Supercomputing time: centuries of spin-up plus ensemble members.",
  "Observational datasets for validation (reanalysis, satellite, stations)."],
 "standards": [
  "Experiments follow CMIP protocols (shared scenarios, standard outputs).",
  "Resolution, parameterizations, and spin-up documented per model."],
 "citations": [CIT_MANABE, CIT_LORENZ],
 "sig_lens": (
  "Signature edition: GCMs reframed as his original planet "
  "simulators - the whole Earth gridded into Signature boxes, "
  "every law of air and water stepped forward on his "
  "computational stage."),
 "demo_kind": "gcm",
},
{
 "key": "ice-ages",
 "name": "Paleoclimate: The Ice Ages",
 "group": "Advanced",
 "ladder_rank": 8,
 "ladder_tier": "advanced",
 "description": (
  "For the last 2.6 million years Earth has swung between ice ages "
  "and warm interglacials - the Pleistocene's great rhythm. At the "
  "Last Glacial Maximum, 21,000 years ago, ice sheets two miles "
  "thick covered Canada and Scandinavia, sea level sat 120 meters "
  "lower, and the global mean temperature was about 6 C colder "
  "than today. Early in the Pleistocene the cycles ran every "
  "41,000 years; about a million years ago they switched to "
  "roughly 100,000-year cycles with deeper glaciations - the "
  "Mid-Pleistocene Transition, still debated. We live in an "
  "interglacial, the Holocene, 11,700 years old - warm, stable, "
  "and the entire span of human civilization. Ice ages are "
  "paced by orbital wobbles (Milankovitch cycles) but built by "
  "feedback: ice-albedo, CO2, and dust amplifying a small "
  "orbital nudge into a frozen continent."),
 "how_it_works": (
  "The pacemaker is summer insolation at 65 degrees north: when "
  "Northern Hemisphere summers are cool (low tilt, distant "
  "summer Sun), snow survives the summer, ice sheets grow, and "
  "albedo rises - the feedback that turns a subtle orbital "
  "signal into kilometers of ice. CO2 follows: cold oceans "
  "absorb more carbon, dropping atmospheric CO2 from 280 to 180 "
  "ppm and deepening the chill. The record is read from ocean "
  "sediment cores (oxygen isotopes in foraminifera shells track "
  "global ice volume), ice cores (temperature and CO2), and "
  "moraines and sea-level markers on land. Spectral analysis of "
  "the sediment record shows the orbital fingerprints - 41k and "
  "100k year peaks - proving the cycles are astronomically "
  "paced. Terminations (ice age endings) are rapid: most of the "
  "deglaciation happens in a few thousand years once the "
  "insolation threshold is crossed."),
 "key_points": [
  "Pleistocene: 2.6 Myr of glacial-interglacial cycles; LGM 21k years ago.",
  "LGM: 6 C colder, ice miles thick, seas 120 m lower.",
  "Cycles ran 41k years, then switched to ~100k years ~1 Myr ago.",
  "Pacemaker: 65 N summer insolation; amplifiers: ice-albedo, CO2, dust.",
  "We live in the Holocene interglacial - 11,700 years of stability."],
 "requirements": [
  "A benthic oxygen-isotope stack (e.g., LR04) for the ice-volume record.",
  "Orbital insolation calculations for 65 N summer.",
  "Ice-core CO2 and temperature for the greenhouse amplifier."],
 "standards": [
  "Marine isotope stages (MIS) as the standard glacial-interglacial numbering.",
  "Ages in thousands of years before present (ka BP)."],
 "citations": [CIT_MILANKOVITCH, CIT_VOSTOK],
 "sig_lens": (
  "Signature edition: the ice ages reframed as his original "
  "deep-winter archive - two-mile ice over Chicago in his "
  "Signature cold storage, the planet's thermostat swung by "
  "orbital gears and feedback engines."),
 "demo_kind": "ice_ages",
},
{
 "key": "milankovitch-cycles",
 "name": "Milankovitch Cycles",
 "group": "Advanced",
 "ladder_rank": 8,
 "ladder_tier": "advanced",
 "description": (
  "Milankovitch cycles are the slow wobbles of Earth's orbit that "
  "pace the ice ages. Three of them: eccentricity - the orbit's "
  "stretch from circular to elliptical on 100,000 and 400,000-year "
  "cycles; obliquity - the axial tilt rocking between 22.1 and "
  "24.5 degrees every 41,000 years; and precession - the wobble of "
  "the axis like a spinning top, cycling every 19,000 to 23,000 "
  "years, deciding whether summer falls at the near or far point "
  "of the orbit. Together they redistribute sunlight by latitude "
  "and season without changing the global annual total much. "
  "Milutin Milankovitch computed it all by hand in the 1920s-40s; "
  "deep-sea cores in the 1970s found his predicted frequencies "
  "written in the sediments - one of the great predictions-"
  "confirmed moments in Earth science."),
 "how_it_works": (
  "The calculation starts from celestial mechanics: planetary "
  "perturbations (mostly Jupiter and Saturn) drive the orbital "
  "elements through their cycles. Obliquity changes the seasonal "
  "contrast - high tilt means hotter summers and colder winters, "
  "which matters at 65 N where cool summers let snow survive. "
  "Precession controls the Earth-Sun distance during each "
  "hemisphere's summer: when northern summer coincides with "
  "perihelion (closest approach), summers are intense; at "
  "aphelion, they are mild - the precession signal dominates the "
  "tropics. Eccentricity modulates precession's strength (a "
  "circular orbit makes precession irrelevant) and adds a small "
  "global annual-mean effect. Insolation formulas combine all "
  "three into watts per square meter for any latitude, day, and "
  "epoch - the forcing function that ice-sheet models then "
  "amplify with albedo and CO2 feedbacks into full ice ages."),
 "key_points": [
  "Three cycles: eccentricity (100k/400k yr), obliquity (41k), precession (19-23k).",
  "They redistribute sunlight by season/latitude; global annual change is small.",
  "65 N summer insolation is the ice-age trigger latitude.",
  "Sediment spectra confirmed the predicted frequencies in the 1970s.",
  "Feedbacks (ice, CO2) amplify the orbital nudge into ice ages."],
 "requirements": [
  "Orbital-element time series (e.g., the La2004 astronomical solution).",
  "The insolation formula combining all three cycles.",
  "A sediment or ice-core record for the spectral-confirmation test."],
 "standards": [
  "Insolation in W/m2 for stated latitude, season, and epoch.",
  "Orbital solutions referenced to the standard astronomical calibration."],
 "citations": [CIT_MILANKOVITCH, CIT_STD],
 "sig_lens": (
  "Signature edition: Milankovitch cycles reframed as his original "
  "orbital clockwork - three Signature gears (stretch, tilt, "
  "wobble) turning the planet's sunlight dial on hundred-"
  "thousand-year time."),
 "demo_kind": "milankovitch",
},
{
 "key": "thermohaline-circulation",
 "name": "The Thermohaline Circulation",
 "group": "Advanced",
 "ladder_rank": 9,
 "ladder_tier": "advanced",
 "description": (
  "The thermohaline circulation is the ocean's deep overturning "
  "loop, driven by temperature (thermo) and salinity (haline) "
  "differences. In the North Atlantic and around Antarctica, "
  "surface water gets cold and salty enough to sink - North "
  "Atlantic Deep Water forms near Greenland and creeps south "
  "along the ocean floor, eventually upwelling in the Pacific "
  "and Indian oceans centuries later. The Atlantic branch "
  "(AMOC) moves about 17 Sverdrups and carries roughly a "
  "petawatt of heat northward - the reason Europe is warm for "
  "its latitude. The system has two stable modes (Stommel, "
  "1961): the present strong overturning, and a collapsed "
  "weak state. Freshwater from melting Greenland ice could "
  "push it toward the weak mode - a leading candidate for an "
  "abrupt climate tipping point."),
 "how_it_works": (
  "Sinking requires dense water: cooling increases density, and "
  "evaporation plus sea-ice formation (which rejects salt) "
  "raises salinity. In the Labrador and Nordic seas both act "
  "together each winter, and the dense water plunges two to "
  "three kilometers down, flowing south as a deep western "
  "boundary current. The loop closes over roughly a thousand "
  "years via slow upwelling elsewhere and surface return flow. "
  "Stommel's two-box model shows the bistability: strong "
  "overturning carries salt north, which sustains sinking (a "
  "positive feedback), but if freshwater dilutes the north "
  "enough, sinking stops and the weak mode locks in. Modern "
  "observations (the RAPID array across the Atlantic at 26 N) "
  "monitor the AMOC directly; models project weakening - but "
  "not collapse - this century under warming, with large "
  "uncertainty."),
 "key_points": [
  "Deep overturning driven by cold, salty sinking in the North Atlantic and Antarctica.",
  "AMOC moves ~17 Sv and ~1 PW of heat northward - Europe's warmth.",
  "Full loop takes ~1,000 years; the ocean's longest memory.",
  "Two stable states (Stommel 1961): strong overturning or collapsed.",
  "Greenland meltwater is the main threat to the strong state."],
 "requirements": [
  "Temperature-salinity profiles in the deep-water formation regions.",
  "The RAPID-array AMOC time series for the modern monitoring context.",
  "Stommel's box model for the bistability reasoning."],
 "standards": [
  "Overturning reported in Sverdrups at standard latitudes (e.g., 26 N).",
  "Water masses named by convention (NADW, AABW)."],
 "citations": [CIT_STOMMEL, CIT_PEIXOTO],
 "sig_lens": (
  "Signature edition: the thermohaline loop reframed as his "
  "original deep-ocean conveyor - cold salty water sinking on "
  "his Signature schedule, a thousand-year round trip metered "
  "in Sverdrups."),
 "demo_kind": "thermohaline",
},
{
 "key": "attribution",
 "name": "Attribution of Climate Change",
 "group": "Advanced",
 "ladder_rank": 9,
 "ladder_tier": "advanced",
 "description": (
  "Attribution is the science of assigning causes: how much of the "
  "observed warming is human, and how much is natural? The answer "
  "rests on three pillars. First, the energy budget: the planet "
  "has warmed about 1.2 C since the late 1800s while net human "
  "forcing rose about +2.7 W/m2 and natural forcings (solar, "
  "volcanic) stayed near zero - the numbers only close if humans "
  "dominate. Second, fingerprints: the pattern of change matches "
  "greenhouse warming specifically - the troposphere warms while "
  "the stratosphere cools, nights warm faster than days, the "
  "Arctic warms fastest - patterns solar or volcanic forcing "
  "would not produce. Third, models: simulations with only "
  "natural forcings stay flat after 1970; add human forcings and "
  "they track the observed rise. Together they make the "
  "conclusion robust: essentially all the warming since the "
  "mid-20th century is human-caused."),
 "how_it_works": (
  "Optimal fingerprinting regresses the observed pattern of "
  "change onto model-simulated patterns for each forcing: "
  "observed = beta_ghg * pattern_ghg + beta_nat * pattern_nat "
  "+ noise. If a forcing's beta is significantly above zero, "
  "it is detected; its value scales the attributable warming. "
  "The stratospheric-cooling fingerprint is decisive: more CO2 "
  "traps heat below and lets the stratosphere radiate more "
  "freely, cooling it - increased sunlight would warm both "
  "layers. Isotopes add an independent check: the falling "
  "carbon-13 and carbon-14 in atmospheric CO2 match fossil "
  "fuel's signature exactly. Event attribution extends the "
  "method to single extremes: run the model world with and "
  "without human forcing and compare the odds - the 2021 "
  "Pacific Northwest heat wave, for example, was made about "
  "150 times more likely."),
 "key_points": [
  "Three pillars: energy budget, fingerprints, and model experiments.",
  "Troposphere warms + stratosphere cools = greenhouse fingerprint (not solar).",
  "Natural-only models stay flat after 1970; human forcings reproduce the rise.",
  "Isotopes fingerprint fossil fuel as the CO2 source.",
  "Event attribution quantifies how warming changed a single extreme's odds."],
 "requirements": [
  "Observed temperature records with stated uncertainties.",
  "Single-forcing model ensembles (greenhouse-only, natural-only, all-forcing).",
  "The fingerprint regression method and isotopic CO2 data."],
 "standards": [
  "Attribution statements use IPCC calibrated language (e.g., 'extremely likely').",
  "Fingerprints defined on stated spatial-temporal patterns."],
 "citations": [CIT_IPCC, CIT_HANSEN],
 "sig_lens": (
  "Signature edition: attribution reframed as his original "
  "climate detective bureau - fingerprints lifted from the "
  "stratosphere, isotopes testifying in his Signature court, "
  "the verdict read from three independent witnesses."),
 "demo_kind": "attribution",
},
{
 "key": "tipping-points",
 "name": "Climate Tipping Points",
 "group": "Advanced",
 "ladder_rank": 9,
 "ladder_tier": "advanced",
 "description": (
  "Tipping points are thresholds where a small push triggers a "
  "large, often irreversible change in a climate subsystem. The "
  "leading candidates: collapse of the West Antarctic Ice Sheet "
  "(grounded below sea level, vulnerable to ocean-driven melt), "
  "shutdown of the Atlantic overturning circulation, dieback of "
  "the Amazon rainforest under drying, thaw of permafrost "
  "releasing frozen carbon, and loss of Arctic summer sea ice. "
  "Mathematically they are bifurcations - fold points where the "
  "stable state vanishes and the system jumps to a new one, with "
  "hysteresis: reversing the forcing does not reverse the "
  "change. Not every feared threshold is near: current "
  "assessments put most tipping points beyond 1.5-2 C of warming, "
  "but the uncertainty is wide, and crossing one could cascade "
  "into others - the reason tipping points dominate "
  "long-term risk thinking even where the near-term science is "
  "settled."),
 "how_it_works": (
  "A tipping element is modeled as a dynamical system with "
  "positive feedback strong enough to create two stable states. "
  "Take the ice-albedo version: temperature T follows dT/dt = "
  "forcing - lambda*T + feedback(T), where the feedback term "
  "jumps as ice melts. Below the threshold the system sits in "
  "the cold stable state; push forcing past the fold point and "
  "the cold state disappears - the system runs away to the warm "
  "state and stays there even if forcing is reduced (hysteresis "
  "loop). Early-warning signals exist in theory: as a "
  "bifurcation approaches, the system's recovery from "
  "perturbations slows (critical slowing down), so variance and "
  "autocorrelation in the time series rise - signals now hunted "
  "in ice-sheet, rainforest, and ocean records. The West "
  "Antarctic case is the most advanced: marine ice-sheet "
  "instability is a geometric feedback (retreat into deeper "
  "bedrock accelerates flow) that models show may already be "
  "underway in parts of Thwaites Glacier."),
 "key_points": [
  "Tipping points = bifurcations: small push, large irreversible jump.",
  "Candidates: West Antarctic ice, AMOC, Amazon, permafrost, Arctic sea ice.",
  "Hysteresis: reversing the forcing does not undo the change.",
  "Early warnings: critical slowing down - rising variance and autocorrelation.",
  "Most thresholds likely beyond 1.5-2 C, but uncertainty is wide."],
 "requirements": [
  "A dynamical model of the subsystem with its key positive feedback.",
  "Long time series to hunt early-warning signals.",
  "Threshold estimates with stated uncertainty from the literature."],
 "standards": [
  "Tipping elements assessed per Lenton et al. candidate criteria.",
  "Irreversibility defined on stated timescales (centuries to millennia)."],
 "citations": [CIT_LENTON, CIT_IPCC],
 "sig_lens": (
  "Signature edition: tipping points reframed as his original "
  "no-return ledger - thresholds inked in his Signature red, "
  "every crossing a one-way entry the planet cannot "
  "un-post."),
 "demo_kind": "tipping_points",
},
{
 "key": "sea-level-rise",
 "name": "Sea Level Rise",
 "group": "Advanced",
 "ladder_rank": 9,
 "ladder_tier": "advanced",
 "description": (
  "Sea level is rising - about 3 to 4 millimeters per year today, "
  "twice the 20th-century rate - and it will keep rising for "
  "centuries. Two engines drive it: thermal expansion (warmer "
  "water takes up more volume) and melting land ice (glaciers "
  "and the Greenland and Antarctic ice sheets). The current "
  "budget roughly: thermal expansion ~1.3 mm/yr, glaciers ~0.7, "
  "Greenland ~0.8, Antarctica ~0.5. Tide gauges record the "
  "rise since the 1800s; satellite altimetry (TOPEX/Poseidon, "
  "Jason series) measures it globally since 1993 with "
  "millimeter precision. Projections range from about 0.3 meters "
  "by 2100 under deep emissions cuts to over a meter under high "
  "emissions - and the ice sheets commit us to meters more over "
  "the following centuries regardless, because they respond so "
  "slowly. Sea level is the longest-memory, least-reversible "
  "part of climate change."),
 "how_it_works": (
  "The budget is additive: total rise = thermal expansion + "
  "glacier melt + ice-sheet melt + land-water storage changes "
  "(dams hold some back, groundwater pumping adds). Thermal "
  "expansion follows the ocean heat-content record: the seas "
  "have absorbed over 90 percent of the excess heat, and each "
  "layer's expansion is its warming times the thermal "
  "expansion coefficient integrated over depth. Ice-sheet "
  "loss is measured three ways - gravity (GRACE satellites "
  "weigh the ice), altimetry (surface lowering), and the "
  "input-output method (snowfall minus discharge) - and all "
  "three agree both sheets are losing mass. Because the deep "
  "ocean and ice sheets take centuries to equilibrate, sea "
  "level keeps rising long after temperatures stabilize: "
  "paleoclimate shows each degree of sustained warming "
  "eventually commits roughly 2 meters of rise."),
 "key_points": [
  "Rising 3-4 mm/yr today, double the 20th-century rate.",
  "Budget: thermal expansion + glaciers + Greenland + Antarctica.",
  "Satellite altimetry measures it globally since 1993.",
  "2100: ~0.3 m (deep cuts) to 1+ m (high emissions); centuries more after.",
  "Least reversible part of climate change: ~2 m committed per degree, eventually."],
 "requirements": [
  "Tide-gauge records and satellite altimetry time series.",
  "Ocean heat-content data for the thermal-expansion term.",
  "Ice-sheet mass-balance estimates (GRACE, altimetry, input-output)."],
 "standards": [
  "Global mean sea level reported in mm/yr with the reference period stated.",
  "Projections tied to stated emissions scenarios."],
 "citations": [CIT_CHURCH, CIT_IPCC],
 "sig_lens": (
  "Signature edition: sea level rise reframed as his original "
  "tide ledger - every millimeter posted from his two engines, "
  "expansion and melt, the ocean's long memory written in his "
  "Signature rising line."),
 "demo_kind": "sea_level",
},
{
 "key": "geoengineering",
 "name": "Geoengineering",
 "group": "Advanced",
 "ladder_rank": 10,
 "ladder_tier": "advanced",
 "description": (
  "Geoengineering means deliberate large-scale intervention in the "
  "climate - and it splits into two very different families. "
  "Carbon dioxide removal (CDR): pulling CO2 back out of the air "
  "by planting forests, direct air capture machines, enhanced "
  "rock weathering, or ocean alkalinity - slow, expensive, but "
  "addressing the root cause. Solar radiation management (SRM): "
  "reflecting a small fraction of sunlight, for example by "
  "injecting reflective aerosols into the stratosphere (mimicking "
  "volcanoes) - fast and cheap in models, but treating the "
  "symptom: it would cool the planet while CO2 kept rising, "
  "acidifying the ocean untouched, and stopping suddenly would "
  "snap temperatures back (termination shock). Governance is the "
  "hardest problem: who sets the planetary thermostat, and who "
  "is liable when monsoons shift? Climatology's role is to "
  "quantify both the leverage and the side effects before "
  "anyone acts."),
 "how_it_works": (
  "The leverage is computed in the forcing ledger. Pinatubo's "
  "~20 megatons of SO2 produced about -3 W/m2 of forcing and "
  "0.5 C of cooling for two years - the natural experiment "
  "behind stratospheric-aerosol proposals, which scale to a few "
  "megatons per year for each degree of cooling desired. CDR "
  "leverage runs through the carbon budget: removing 10 "
  "gigatons of carbon per year lowers atmospheric CO2 by about "
  "4.7 ppm per year (2.13 GtC per ppm), and the forcing falls "
  "logarithmically. Side-effect modeling shows SRM would "
  "change precipitation patterns (less tropical rainfall), "
  "whiten skies, deplete ozone via aerosol chemistry, and do "
  "nothing for ocean acidification - which is why assessments "
  "treat SRM as deeply risky and CDR as necessary but "
  "insufficient alone. No intervention substitutes for "
  "cutting emissions; the ledger always balances in the end."),
 "key_points": [
  "Two families: carbon removal (slow, root cause) vs solar management (fast, symptom).",
  "Pinatubo is the natural prototype: ~20 Mt SO2 -> -3 W/m2, -0.5 C.",
  "CDR: 10 GtC/yr removed ~= 4.7 ppm/yr off the atmosphere.",
  "SRM side effects: rainfall shifts, ozone chemistry, termination shock.",
  "Ocean acidification continues under SRM - only CO2 cuts fix it."],
 "requirements": [
  "The forcing ledger: current CO2 forcing and the target offset.",
  "Aerosol microphysics and stratospheric transport for the SRM design.",
  "Earth system model runs for side-effect quantification."],
 "standards": [
  "Interventions assessed against the same forcing metrics as emissions.",
  "Governance questions flagged wherever deployment is discussed."],
 "citations": [CIT_IPCC, CIT_STD],
 "sig_lens": (
  "Signature edition: geoengineering reframed as his original "
  "thermostat debate - two Signature toolboxes on the bench, "
  "the slow carbon wrench and the fast sunlight dimmer, his "
  "ledger open to the side effects before any hand touches "
  "the dial."),
 "demo_kind": "geoengineering",
},
{
 "key": "frontiers",
 "name": "Frontiers of Climatology",
 "group": "Advanced",
 "ladder_rank": 10,
 "ladder_tier": "advanced",
 "description": (
  "Climatology's frontiers are where the settled science ends and "
  "the arguments begin. Cloud feedback remains the biggest "
  "uncertainty in how much warming follows emissions - storm-"
  "resolving models that simulate clouds directly, instead of "
  "parameterizing them, are the great hope. Aerosol-cloud "
  "interactions carry the next-largest uncertainty. The deep "
  "ocean's heat uptake sets the pace of surface warming and the "
  "'pipeline' of committed change. Ice-sheet physics - especially "
  "marine ice-cliff instability in Antarctica - could redraw sea-"
  "level projections. Compound extremes (heat plus drought, "
  "rain on snow), climate-biosphere feedbacks (permafrost "
  "carbon, forest dieback), and kilometer-scale modeling that "
  "resolves storms explicitly round out the agenda. The through-"
  "line: finer resolution, better observations (new satellite "
  "constellations), and machine learning accelerating both - "
  "climatology is becoming an ever sharper instrument."),
 "how_it_works": (
  "Frontier work follows the same loop as ever: observe, model, "
  "test. Storm-resolving models (grid spacing of a few kilometers) "
  "drop the convection parameterization and let storms emerge - "
  "early results suggest they handle tropical rainfall and "
  "extreme precipitation better, at hundredfold computing cost. "
  "Machine learning now emulates expensive model components "
  "(radiation, clouds) at a fraction of the cost and hunts "
  "patterns in petabytes of satellite data. New missions measure "
  "what models need most: aerosol-cloud interactions, ocean "
  "heat content below 2,000 meters, ice-sheet grounding lines. "
  "The test is always the same - does the new tool reproduce "
  "the observed climate and its changes? - and the scoreboard "
  "is public: every model generation is evaluated against the "
  "same observations in coordinated experiments, so progress "
  "is measured, not claimed."),
 "key_points": [
  "Cloud feedback is the #1 uncertainty; storm-resolving models are the great hope.",
  "Aerosol-cloud effects and deep-ocean heat uptake are next on the list.",
  "Antarctic ice-cliff physics could redraw sea-level projections.",
  "Kilometer-scale grids let storms emerge instead of being parameterized.",
  "ML emulates expensive physics; new satellites target the key unknowns."],
 "requirements": [
  "Access to frontier model output (storm-resolving and ML-emulated runs).",
  "The coordinated evaluation experiments for the progress scoreboard.",
  "Observational campaigns targeting the specific uncertainty."],
 "standards": [
  "New methods validated against the same observational benchmarks as incumbents.",
  "Uncertainty quantified, not hand-waved, in every frontier claim."],
 "citations": [CIT_IPCC, CIT_STD],
 "sig_lens": (
  "Signature edition: the frontiers reframed as his original "
  "next-horizon watch - storm-resolving grids and learning "
  "machines as new Signature lenses, every sharper instrument "
  "another page in his unfinished atlas."),
 "demo_kind": "frontiers",
},
]

SIG_TAIL = ("Signature editions are his original Signature interpretation "
            "of climatology: clearly labeled Signature-made, never "
            "presented as authentic public record.")

assert len(ENTRIES) == 34, "need 34 climatology entries, have %d" % len(ENTRIES)
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
