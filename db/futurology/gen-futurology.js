/* JAH Future Studies Database generator — jahdb-futurology-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: seed -> full future scenario. 1,000,000 address space (seed % 1M).
   Records are either sourced (real, verifiable trends/technologies), projected (labeled forecasts),
   or signature-generated speculative scenarios \u2014 never presented as fact. The `record_status`
   field always says which: 'historical trend' | 'projection' | 'speculative scenario'. */
(function () {
'use strict';
function prng(seed) { var a = (seed >>> 0) || 1; return function () { a |= 0; a = (a + 0x6D2B79F5) | 0; var t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
function pick(a, r) { return a[(r() * a.length) | 0]; }
function ri(r, a, b) { return a + ((r() * (b - a + 1)) | 0); }
function shuffle(a, r) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = (r() * (i + 1)) | 0; var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
function interleave(lists) { var out = [], i = 0, more = true; while (more) { more = false; for (var k = 0; k < lists.length; k++) { if (i < lists[k].length) { out.push(lists[k][i]); more = true; } } i++; } return out; }

var SLUG = 'futurology';
var PREFIX = 'JAH-FUT-';
var VERSION = 'jahdb-futurology-1.0';
var RECORD_KIND = 'future scenario';
var CATS = ['future-scenario', 'trend', 'forecast', 'emerging-tech'];

/* ================= REAL (sourced) data ================= */
/* Trends: [title, description] — verifiable historical trends, worded without dubious statistics */
var REAL_TRENDS = [
['The falling cost of solar power', 'Over the past decade and a half, the cost of solar photovoltaic electricity has fallen dramatically, making solar the cheapest source of new electricity in many regions. The learning curve of manufacturing scale continues to push prices down.'],
['Wind power scaling up', 'Turbines have grown taller and more powerful, and offshore wind farms now deliver utility-scale power. Wind has become one of the fastest-growing sources of electricity worldwide.'],
['Battery costs declining', 'Lithium-ion battery pack prices have fallen steeply since 2010, driven by electric vehicles and grid storage demand. Cheaper storage makes renewables dispatchable.'],
['Electric vehicle adoption rising', 'EVs have moved from niche to mainstream in many markets, with dozens of models available and charging networks expanding yearly. Automakers worldwide have announced electrified lineups.'],
['Global internet connectivity growth', 'Billions more people have come online since 2000, first through mobile phones and now through expanding broadband and satellite constellations. The offline population keeps shrinking.'],
['Urbanization continuing', 'For the first time in history a majority of humanity lives in cities, and the urban share keeps rising \u2014 concentrating both opportunity and infrastructure strain.'],
['Population aging in many countries', 'Falling birth rates and longer lives are aging populations across East Asia, Europe, and increasingly the Americas, reshaping workforces and healthcare demand.'],
['UN world population projections', 'The United Nations projects world population approaching 10 billion around mid-century before stabilizing \u2014 a projection, not a certainty, sensitive to fertility trends.'],
['Renewable electricity share growing', 'Wind and solar together now supply a substantial and growing share of global electricity, with records for new installations set repeatedly in recent years.'],
['The Transformer and large language models', 'The 2017 \u201cAttention Is All You Need\u201d paper introduced the Transformer architecture, which underlies today\u2019s large language models and a wave of AI capability gains.'],
['CRISPR gene editing', 'CRISPR-Cas9, described in 2012 by Doudna and Charpentier (Nobel Prize 2020), made precise gene editing cheap and fast, opening therapeutic trials for genetic diseases.'],
['Falling genome sequencing cost', 'Sequencing a human genome has fallen from billions of dollars to roughly the cost of routine medical tests, enabling population-scale genomics.'],
['mRNA vaccine platforms', 'The COVID-19 pandemic proved mRNA vaccines could be designed, tested, and manufactured in months \u2014 a platform now aimed at flu, RSV, and cancers.'],
['Reusable rockets', 'SpaceX\u2019s Falcon 9 achieved routine first-stage landings from 2015 onward, cutting launch costs and raising global launch cadence to historic highs.'],
['Artemis lunar program', 'NASA\u2019s Artemis program aims to return astronauts to the Moon and build a sustained presence \u2014 a stated plan in progress, with timelines that have already shifted.'],
['Fusion ignition milestone', 'In December 2022 the National Ignition Facility reported net energy gain from a fusion reaction \u2014 scientific breakeven, still far from a power plant.'],
['Quantum computing milestones', 'Quantum processors have demonstrated calculations intractable for classical supercomputers on narrow problems; fault-tolerant machines remain years away.'],
['5G network rollout', 'Fifth-generation mobile networks have rolled out across much of the world, bringing higher bandwidth and lower latency to phones and industry.'],
['Autonomous vehicle testing', 'Robotaxi services operate in several cities with safety drivers removed, while full autonomy in all conditions remains unsolved.'],
['Vertical farming growth', 'Indoor farms growing leafy greens under LEDs have multiplied, trading energy cost for water savings and local production.'],
['Lab-grown meat progress', 'Cultivated meat has won regulatory approval in several countries, though cost and scale still block mass markets.'],
['Global warming trend', 'NASA and NOAA records show a clear multi-decade warming trend in global surface temperatures, with recent years among the warmest observed.'],
['Decline of extreme poverty', 'The share of humanity living in extreme poverty has fallen dramatically since 1990, even as hundreds of millions remain poor.'],
['Rising life expectancy (with setbacks)', 'Global life expectancy rose for decades before pandemic setbacks; the long trend reflects vaccines, sanitation, and nutrition.'],
['The attention economy', 'Advertising-funded platforms turned human attention into the core commodity of the internet economy, reshaping media and politics.'],
['Remote work normalization', 'The pandemic made remote and hybrid work normal in knowledge industries, reshaping cities, offices, and management.'],
['E-commerce share of retail', 'Online shopping has taken a steadily growing share of retail sales for two decades, accelerated by the pandemic.'],
['Streaming displacing broadcast', 'Subscription streaming has overtaken traditional broadcast and cable viewing in many markets.'],
['Renewable hydrogen pilots', 'Green hydrogen \u2014 made with renewable electricity \u2014 is being piloted for steel, shipping, and heavy transport where batteries struggle.'],
['Small modular reactors', 'Small modular nuclear reactor designs are moving through licensing in several countries, promising factory-built nuclear power.'],
['Direct air capture pilots', 'Plants that pull CO2 directly from the air now operate at pilot scale; costs must fall orders of magnitude to matter.'],
['Brain-computer interfaces', 'Implanted BCIs have let paralyzed patients control cursors and robotic arms; non-invasive approaches lag far behind.'],
['Solid-state batteries', 'Solid-state battery prototypes promise higher energy density and safety; mass production timelines keep slipping.'],
['LEO satellite internet', 'Thousands of low-Earth-orbit satellites now provide broadband to remote areas, creating both connectivity and orbital-debris concerns.'],
['Precision fermentation', 'Engineered microbes now brew proteins, fats, and flavors \u2014 from insulin to egg whites \u2014 without animals or fields.'],
['The creator economy', 'Millions earn income directly from audiences via platforms, shifting cultural production from studios to individuals.'],
['Aging grids and electrification', 'Electrifying heat and transport is straining grids built for a fossil era, driving a historic infrastructure buildout.'],
['Water stress spreading', 'Groundwater depletion and shifting rainfall are stressing water supplies from the American West to South Asia.'],
['Antibiotic resistance rising', 'Drug-resistant infections are a growing global health threat, driving stewardship and new-drug incentives.']
];
/* Emerging tech: [title, what_it_is, state_of_play] */
var REAL_TECH = [
['Solid-state batteries', 'Lithium batteries with solid electrolytes instead of flammable liquid', 'Prototypes exist from major automakers and startups; mass production remains the hurdle.'],
['Small modular reactors', 'Factory-built nuclear reactors under 300 MW', 'Designs in licensing in the US, Canada, and Europe; first deployments targeted late this decade.'],
['Green hydrogen', 'Hydrogen made by electrolyzing water with renewable electricity', 'Pilot plants operating; cost must fall sharply to compete in steel and shipping.'],
['Direct air capture', 'Machines that extract CO2 from ambient air', 'Pilot plants capture thousands of tons yearly; megaton scale needs massive cost cuts.'],
['Fusion power plants', 'Power from fusing light atomic nuclei', 'NIF achieved scientific breakeven in 2022; private startups target pilot plants in the 2030s.'],
['Brain-computer interfaces', 'Devices translating neural signals into computer control', 'Implants restore communication for paralyzed patients; consumer uses are distant.'],
['Quantum computers', 'Computers using qubits and quantum effects', 'Hundreds of noisy qubits today; fault tolerance needs thousands to millions.'],
['CRISPR therapies', 'Medicines that edit a patient\u2019s genes', 'Approved therapies exist for sickle cell disease; delivery to organs beyond blood is the frontier.'],
['mRNA medicines', 'Drugs and vaccines using messenger RNA', 'Proven in COVID vaccines; cancer and rare-disease trials underway.'],
['Cultivated meat', 'Meat grown from animal cells without slaughter', 'Approved in Singapore and the US; price and scale are the barriers.'],
['Precision fermentation', 'Microbes brewed to make proteins and fats', 'Commercial for insulin, rennet, and egg-white protein; expanding fast.'],
['Vertical farms', 'Crops grown in stacked indoor layers under LEDs', 'Economic for leafy greens near cities; energy cost limits staples.'],
['Autonomous trucks', 'Self-driving long-haul freight', 'Hub-to-hub highway autonomy in testing; drivers still handle the last mile.'],
['Robotaxis', 'Driverless ride-hailing cars', 'Operating commercially in several cities with expanding service areas.'],
['eVTOL air taxis', 'Electric vertical-takeoff aircraft for short hops', 'Certified prototypes flying; commercial service targeted this decade.'],
['LEO broadband constellations', 'Thousands of satellites beaming internet down', 'Operational globally; astronomers and debris trackers raise concerns.'],
['6G research', 'The generation after 5G wireless', 'Standards work underway; deployment expected around 2030.'],
['Neuromorphic chips', 'Processors mimicking brain architecture', 'Research chips show efficiency gains; commercial niches emerging.'],
['Photonic computing', 'Computation with light instead of electrons', 'Startups demo accelerators; integration with silicon is the challenge.'],
['DNA data storage', 'Archiving digital data in synthetic DNA', 'Lab demos store megabytes; read/write speed and cost limit use to cold archives.'],
['De-extinction projects', 'Using gene editing to revive extinct species\u2019 traits', 'Mammoth-trait elephants and dire-wolf pups announced; ecological questions abound.'],
['Ocean alkalinity enhancement', 'Adding alkaline minerals to seawater to absorb CO2', 'Field trials beginning; measurement and governance are open questions.'],
['Space-based solar power', 'Collecting sunlight in orbit and beaming it down', 'Demonstrator missions flown; economics unproven at scale.'],
['Asteroid mining ventures', 'Extracting water and metals from near-Earth asteroids', 'Prospecting missions flown; commercial mining remains speculative.'],
['Digital twins of cities', 'Live virtual models of urban systems', 'Deployed in Singapore and several European cities for planning.'],
['AI drug discovery', 'Machine learning designing new medicines', 'AI-designed molecules now in clinical trials.'],
['Protein folding solved-ish', 'AlphaFold predicting protein structures', 'AlphaFold\u2019s database covers hundreds of millions of structures, accelerating biology.'],
['Long-duration energy storage', 'Storing renewable power for days to seasons', 'Iron-air, compressed air, and thermal pilots compete beyond lithium\u2019s hours.'],
['Perovskite solar cells', 'High-efficiency thin-film photovoltaics', 'Lab efficiencies rival silicon; durability is the commercial hurdle.']
];
/* Forecasts: [title, forecast_text] — always labeled projection */
var REAL_FORECASTS = [
['UN population projection to 2100', 'PROJECTION: The UN\u2019s medium variant sees world population peaking this century near 10\u201311 billion, then stabilizing \u2014 highly sensitive to fertility assumptions.'],
['Energy transition pace', 'PROJECTION: Major energy outlooks project wind and solar becoming the largest sources of new electricity through 2050, though the speed of fossil decline varies widely by scenario.'],
['EV market share outlook', 'PROJECTION: Analysts project electric vehicles taking a majority of new car sales in leading markets during the 2030s, contingent on battery costs and policy.'],
['AI capability trajectory', 'PROJECTION: Extrapolating compute and algorithmic trends suggests continued rapid AI capability gains, but the timing of transformative systems is deeply uncertain and disputed.'],
['Climate warming scenarios', 'PROJECTION: IPCC scenarios span roughly 1.5\u00b0C to 4\u00b0C+ of warming by 2100 depending on emissions \u2014 policy choices, not physics alone, decide the path.'],
['Fusion timeline forecasts', 'PROJECTION: Private fusion companies target pilot plants in the 2030s; expert surveys remain skeptical of grid power before 2040. Treat company timelines as aspirations.'],
['Quantum advantage timeline', 'PROJECTION: Useful fault-tolerant quantum computers are widely projected for the 2030s at earliest; near-term value will come from noisy hybrid algorithms.'],
['Moon base timelines', 'PROJECTION: NASA\u2019s Artemis aims for a sustained lunar presence in the 2030s; historical space timelines suggest expecting delays.'],
['Mars mission forecasts', 'PROJECTION: Robotic Mars sample return is in development; credible crewed Mars timelines cluster in the late 2030s\u20132040s at earliest.'],
['Aging-workforce projections', 'PROJECTION: Demographers project old-age dependency ratios doubling in many countries by 2050, pressuring pensions and healthcare.'],
['Urbanization to 2050', 'PROJECTION: The UN projects nearly 70% of humanity urban by 2050, with almost all growth in Asia and Africa.'],
['Food demand outlook', 'PROJECTION: The FAO projects food production must rise substantially by 2050 to feed a wealthier, larger population \u2014 yield growth, not just land, must deliver it.'],
['Water demand projections', 'PROJECTION: Global water demand is projected to outstrip sustainable supply in many basins by 2050 without efficiency gains and reuse.'],
['Renewable hydrogen cost curve', 'PROJECTION: Analysts project green hydrogen costs falling with electrolyzer scale, potentially competitive in heavy industry by the 2030s.'],
['Autonomous vehicle adoption curve', 'PROJECTION: Adoption forecasts range from rapid robotaxi expansion to decades of edge cases; regulation and liability are the binding constraints.']
];

/* ================= Signature-generation pools (all speculative, labeled) ================= */
var HORIZONS = ['2030', '2035', '2040', '2050', '2075', '2100'];
var DOMAINS = ['cities', 'energy', 'transport', 'medicine', 'work', 'education', 'oceans', 'space', 'food', 'climate', 'AI and robotics', 'materials'];
var SCEN_A = ['A coastal metropolis', 'A landlocked megacity', 'A network of small towns', 'An island nation', 'A desert settlement', 'A mountain region', 'A river delta community', 'A high-latitude city'];
var SCEN_B = [
'retrofits every rooftop for solar and gardens, and the grid becomes a neighborhood marketplace',
'replaces car lanes with autonomous shuttles and greenways, and childhood asthma rates fall',
'moves its port operations to floating platforms as sea levels rise',
'rebuilds around a 15-minute neighborhood model where daily needs sit within a short walk',
'powers itself on a microgrid of solar, batteries, and green hydrogen through storm season',
'treats its wastewater to drinking standards and cuts imports to near zero',
'grows a vertical farming district that supplies half its fresh produce',
'deploys a digital twin that reroutes traffic and energy in real time'
];
var SCEN_C = [
'The transition is uneven: wealthy districts adapt first, and policy scrambles to keep the benefits shared.',
'Costs fall faster than expected, but the workforce retraining lags a decade behind the technology.',
'The change proves popular once the first neighborhood demonstrates it, and adoption cascades.',
'Regulation becomes the bottleneck: the technology works, the permits do not.',
'A surprise breakthrough halves the cost, and planners rewrite every forecast in a year.',
'Public opinion swings after one dramatic season, and the political will finally matches the engineering.'
];
var TECH_SPEC = [
['Self-healing concrete districts', 'energy', 'Concrete infused with limestone-producing bacteria repairs its own cracks, extending infrastructure life for decades.'],
['Atmospheric water districts', 'climate', 'Neighborhood-scale condensers pull drinking water from humid air, buffering droughts.'],
['Algae facade buildings', 'cities', 'Living algae panels on towers absorb CO2 and yield biofuel while shading interiors.'],
['Silent electric shipping corridors', 'transport', 'Wind-assisted, battery-hybrid cargo ships run scheduled quiet corridors that let whale populations recover.'],
['Personal health twins', 'medicine', 'Continuous wearable data feeds a personal physiological model that predicts illness before symptoms.'],
['Four-day work regions', 'work', 'Whole regions coordinate on shorter weeks, trading some output for wellbeing and local spending.'],
['Ocean thermal cities', 'oceans', 'Floating districts draw power from the temperature difference between surface and deep water.'],
['Lunar construction crews', 'space', 'Robotic crews sinter lunar regolith into landing pads and habitats before astronauts arrive.'],
['Perennial grain belts', 'food', 'Deep-rooted perennial grains cut fertilizer and erosion while yielding annual harvests.'],
['Direct-air-capture parks', 'climate', 'Solar-powered capture arrays paired with mineralization turn a district carbon-negative.'],
['Care robot cooperatives', 'AI and robotics', 'Municipal cooperatives own care robots that assist the elderly at home, keeping independence longer.'],
['Programmable matter workshops', 'materials', 'Neighborhood fab-labs print tools and parts from recyclable smart materials on demand.'],
['Heat-resilient school design', 'education', 'Schools built as cooling centers double as community refuges during heat waves.'],
['Migratory workforce visas', 'work', 'Climate-linked labor agreements let workers follow harvest and rebuilding seasons legally.'],
['Rewilded transit corridors', 'cities', 'Rail and trail corridors double as wildlife passages, reconnecting fragmented habitats.'],
['Fusion pilot towns', 'energy', 'The first fusion pilot plants anchor company towns built around abundant clean heat.']
];
var TREND_SPEC = [
['The longevity economy', 'Longer healthy lives reshape retirement, education, and housing into multi-stage life design.'],
['The attention restoration movement', 'A cultural backlash against infinite feeds drives demand for quiet tech and slow media.'],
['Climate migration compacts', 'Regions negotiate planned relocation frameworks before disasters force chaotic movement.'],
['The repair renaissance', 'Right-to-repair laws and modular design make fixing things normal again.'],
['Synthetic media literacy', 'Schools teach verification as a core skill as generated video floods the internet.'],
['The 15-minute countryside', 'Remote work revives small towns built around walkable cores and fast rail links.'],
['Water markets mature', 'Tradable water rights with ecological floors bring efficiency \u2014 and equity fights.'],
['The care economy boom', 'Aging populations make caregiving the largest employer, professionalized and tech-assisted.'],
['Degrowth experiments', 'Cities test wellbeing budgets that target health and time over GDP growth.'],
['The orbital economy', 'In-space manufacturing of fiber optics and pharmaceuticals becomes a real industry.']
];
function realTrend(e, id, seed) {
  var secs = [
    { heading: 'The trend (historical)', body: e[0] + '. ' + e[1] },
    { heading: 'What to watch', body: 'Track whether the cost curves and adoption rates behind this trend hold through the next cycle: watch deployment numbers, not announcements.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: e[0], category: 'trend', record_kind: RECORD_KIND, origin: 'sourced', record_status: 'historical trend', summary: e[1], details: {}, sections: secs, record_text: text, source_note: 'Sourced: verifiable historical trend; figures deliberately qualitative \u2014 check primary sources for numbers.', related: [], _seed: seed };
}
function realTech(e, id, seed) {
  var secs = [
    { heading: 'The technology', body: e[0] + ': ' + e[1] + '.' },
    { heading: 'State of play', body: e[2] + ' Treat company timelines as aspirations until demonstrated at scale.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: e[0], category: 'emerging-tech', record_kind: RECORD_KIND, origin: 'sourced', record_status: 'historical trend', summary: e[1] + '. ' + e[2], details: {}, sections: secs, record_text: text, source_note: 'Sourced: publicly reported technology status; not a forecast.', related: [], _seed: seed };
}
function realForecast(e, id, seed) {
  var secs = [
    { heading: 'The forecast (projection \u2014 not fact)', body: e[0] + '. ' + e[1] },
    { heading: 'How to use it', body: 'Use projections to bound planning, never as predictions: track which scenario the world is actually following and update.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: e[0], category: 'forecast', record_kind: RECORD_KIND, origin: 'sourced', record_status: 'projection', summary: e[1], details: {}, sections: secs, record_text: text, source_note: 'Sourced: labeled projection from cited outlooks; projections are not facts.', related: [], _seed: seed };
}
function sigScenario(r, id, seed) {
  var h = pick(HORIZONS, r), dom = pick(DOMAINS, r);
  var title = pick(SCEN_A, r) + ' in ' + h + ': ' + pick(SCEN_B, r).split(',')[0];
  var secs = [
    { heading: 'SPECULATIVE SCENARIO \u2014 not a prediction', body: 'Horizon ' + h + ' \u00b7 Domain: ' + dom + '. ' + pick(SCEN_A, r) + ' ' + pick(SCEN_B, r) + '.' },
    { heading: 'How it could unfold', body: pick(SCEN_C, r) + ' Early signals to watch: pilot projects scaling, cost curves bending, and one jurisdiction proving the model.' },
    { heading: 'What would falsify it', body: 'This scenario fails if the core cost or adoption assumption breaks: track the leading indicators yearly and retire the scenario if they stall for a full cycle.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: title, category: 'future-scenario', record_kind: RECORD_KIND, origin: 'signature-generated', record_status: 'speculative scenario', summary: 'A speculative ' + h + ' scenario for ' + dom + ' \u2014 exploratory fiction, not a forecast.', details: { horizon: h, domain: dom }, sections: secs, record_text: text, source_note: 'Signature-generated speculative scenario. Not a fact, not a forecast \u2014 an exploratory story.', related: [], _seed: seed };
}
function sigTrend(r, id, seed) {
  var t = pick(TREND_SPEC, r);
  var secs = [
    { heading: 'SPECULATIVE TREND SKETCH \u2014 not established fact', body: t[0] + '. ' + t[1] },
    { heading: 'Signals vs noise', body: 'Treat this as a hypothesis: look for three independent real-world signals before upgrading it to a watched trend.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: t[0] + ' \u2014 speculative sketch', category: 'trend', record_kind: RECORD_KIND, origin: 'signature-generated', record_status: 'speculative scenario', summary: t[1], details: {}, sections: secs, record_text: text, source_note: 'Signature-generated speculative sketch, not an established trend.', related: [], _seed: seed };
}
function sigTech(r, id, seed) {
  var t = pick(TECH_SPEC, r);
  var secs = [
    { heading: 'SPECULATIVE TECHNOLOGY CONCEPT \u2014 not a real product', body: t[0] + ' (' + t[1] + '). ' + t[2] },
    { heading: 'Path to reality', body: 'For this concept to matter, three gates must fall: a lab demo, a pilot at meaningful scale, and a cost curve that bends toward affordability. None have fallen yet.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: t[0] + ' \u2014 speculative concept', category: 'emerging-tech', record_kind: RECORD_KIND, origin: 'signature-generated', record_status: 'speculative scenario', summary: t[2], details: { domain: t[1] }, sections: secs, record_text: text, source_note: 'Signature-generated speculative concept, not a real technology.', related: [], _seed: seed };
}
function sigForecast(r, id, seed) {
  var h = pick(HORIZONS, r), dom = pick(DOMAINS, r);
  var secs = [
    { heading: 'SCENARIO FORECAST \u2014 a structured guess, not a fact', body: 'Horizon ' + h + ' \u00b7 ' + dom + '. Under current trends extended, ' + pick(SCEN_A, r).toLowerCase() + ' ' + pick(SCEN_B, r) + '.' },
    { heading: 'Confidence and caveats', body: 'Confidence: low. ' + pick(SCEN_C, r) }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: 'Scenario forecast: ' + dom + ' by ' + h, category: 'forecast', record_kind: RECORD_KIND, origin: 'signature-generated', record_status: 'speculative scenario', summary: 'A structured speculative guess for ' + dom + ' by ' + h + ' \u2014 not a prediction.', details: { horizon: h, domain: dom }, sections: secs, record_text: text, source_note: 'Signature-generated scenario forecast. Not a fact.', related: [], _seed: seed };
}
var REAL = interleave([
  REAL_TRENDS.map(function (e) { return { k: 't', e: e }; }),
  REAL_TECH.map(function (e) { return { k: 'e', e: e }; }),
  REAL_FORECASTS.map(function (e) { return { k: 'f', e: e }; })
]);
var CATMAP = { t: 'trend', e: 'emerging-tech', f: 'forecast' };
function generate(seed, opts, rnd) {
  opts = opts || {}; rnd = rnd || prng(seed);
  var idx = ((seed % 1000000) + 1000000) % 1000000;
  var id = PREFIX + String(idx + 1).padStart(7, '0');
  if (idx < REAL.length) {
    var re = REAL[idx];
    if (!opts.category || CATMAP[re.k] === opts.category) {
      if (re.k === 't') return realTrend(re.e, id, seed);
      if (re.k === 'e') return realTech(re.e, id, seed);
      return realForecast(re.e, id, seed);
    }
  }
  var cat = opts.category || pick(CATS, rnd);
  if (cat === 'future-scenario') return sigScenario(rnd, id, seed);
  if (cat === 'trend') return sigTrend(rnd, id, seed);
  if (cat === 'emerging-tech') return sigTech(rnd, id, seed);
  return sigForecast(rnd, id, seed);
}
var REQUIRED = ['id', 'title', 'category', 'record_kind', 'origin', 'record_status', 'summary', 'details', 'sections', 'record_text', 'source_note'];
function validate(rec) {
  var errors = [];
  if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
  REQUIRED.forEach(function (k) { if (rec[k] === undefined || rec[k] === null || rec[k] === '') errors.push('missing ' + k); });
  if (rec.id && !/^JAH-FUT-\d{7}$/.test(rec.id)) errors.push('bad id format');
  if (rec.category && CATS.indexOf(rec.category) < 0) errors.push('bad category');
  if (rec.origin && ['sourced', 'signature-generated'].indexOf(rec.origin) < 0) errors.push('bad origin');
  if (rec.record_status && ['historical trend', 'projection', 'speculative scenario'].indexOf(rec.record_status) < 0) errors.push('bad record_status');
  if (rec.sections && (!Array.isArray(rec.sections) || !rec.sections.length)) errors.push('sections empty');
  if (rec.record_text && rec.record_text.length < 120) errors.push('record_text too short');
  if (rec.origin === 'signature-generated' && /not a fact|speculative|projection/i.test(rec.record_text) === false) errors.push('speculative label missing');
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
