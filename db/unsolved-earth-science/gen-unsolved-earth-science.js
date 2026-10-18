(function(){'use strict';
/* JAH The Unsolved Earth Science Database generator — jahdb-unsolved-earth-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Topics mirror the archive's 34
   seeded records; generated records are labeled samples, never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USES-";
var FIELDS=["Seismology", "Volcanology", "Climate", "Paleoclimate", "Oceans", "Geomagnetism", "Geodynamics", "Geochemistry", "Planetary Formation", "Deep Earth"];
var TOPICS=[
 ["Can Earthquakes Be Predicted?", "Seismology", "No reliable method exists today for predicting the time, place, and magnitude of a damaging earthquake with the precision that would let a city evacuate."],
 ["Can Volcanic Eruptions Be Forecast Reliably?", "Volcanology", "Most episodes of volcanic unrest never lead to eruption, and some eruptions arrive with little warning, so reliably forecasting which restless volcano will erupt - and when - remains unsolved."],
 ["How High and How Fast Will Sea Level Rise?", "Climate", "The exact amount and rate of sea-level rise through 2100 and beyond is unknown, because the future of the Greenland and Antarctic ice sheets - the biggest wildcards - is deeply uncertain."],
 ["Where Are Earth's Climate Tipping Points?", "Climate", "Nobody knows how close the climate system is to tipping points - thresholds where ice sheets, ocean circulation, or rainforests shift abruptly and irreversibly on human timescales."],
 ["Why Did Earth's Climate Flip Abruptly in the Past?", "Paleoclimate", "Greenland ice cores prove the climate has lurched by many degrees within decades during the last ice age, but the exact trigger and mechanism of these abrupt flips is still debated."],
 ["What Makes El Nino Irregular, and Can It Be Forecast Years Ahead?", "Oceans", "El Nino events arrive every 2 to 7 years with wildly varying strength, and forecasts lose skill after about 6 to 9 months - nobody knows whether the irregularity is chaos, noise, or predictable physics we have not captured."],
 ["How Much Carbon Will Thawing Permafrost Release?", "Climate", "Permafrost soils hold roughly twice the carbon in the atmosphere, and nobody knows how much of it will escape as the Arctic thaws - or how much will come out as methane, which warms far more per ton."],
 ["Is the Atlantic Overturning Circulation Heading for Collapse?", "Oceans", "The Atlantic overturning circulation may be weakening, and some analyses claim early-warning signals of collapse - but the evidence is contested, the observations are short, and the stakes are enormous."],
 ["Why Does Earths Magnetic Field Reverse, and When Is Next?", "Geomagnetism", "Earth's magnetic field has reversed hundreds of times, the last full reversal was 780,000 years ago, and the field is weakening now - but nobody knows what triggers reversals or whether one is coming."],
 ["What Causes Deep-Focus Earthquakes?", "Seismology", "Earthquakes occur as deep as 700 kilometers, inside hot high-pressure mantle where rock should flow rather than fracture - and the mechanism that lets them happen is still not settled."],
 ["What Drives Slow Earthquakes and Tremor?", "Seismology", "Faults can slip slowly over weeks, releasing the energy of a large earthquake with no shaking - and the physics that decides between silent creep, slow slip, and violent rupture is not fully understood."],
 ["How and When Did Plate Tectonics Begin?", "Geodynamics", "Earth is the only known planet with plate tectonics, and geologists cannot agree when it started - estimates span from over 4 billion years ago to under 1 billion."],
 ["How Did the Continents Grow?", "Geodynamics", "Continents grew in dramatic pulses billions of years ago, but how much was brand-new crust from the mantle versus recycled older crust is still disputed - so the true growth curve of the continents is unknown."],
 ["How Much Life Is in the Deep Biosphere?", "Geochemistry", "Microbes live kilometers beneath the surface in rock with no sunlight, but the total size of this deep biosphere - possibly Earth's largest ecosystem - is uncertain by orders of magnitude."],
 ["How Much Water Is Hidden Inside the Mantle?", "Geochemistry", "Mantle minerals can lock up water in their crystal structures, possibly holding several oceans' worth - but whether the mantle is wet or dry, and where the water sits, is fiercely debated."],
 ["Where Did Earths Oceans Come From?", "Planetary Formation", "Earth's water could have arrived late on asteroids, or been baked into the planet from the start - and isotope evidence currently supports both stories at once."],
 ["How Does Carbon Move Through the Deep Earth?", "Geochemistry", "Subduction zones drag carbon into the mantle, volcanoes return some of it, but the fluxes in both directions are uncertain by an order of magnitude - so the deep carbon budget does not close."],
 ["What Are the Giant Blobs at the Base of the Mantle?", "Deep Earth", "Two continent-sized slow regions sit at the base of the mantle, and seismologists cannot agree whether they are hot rising rock, dense primordial piles, or graveyards of sunken tectonic plates."],
 ["What Drives Mantle Plumes?", "Geodynamics", "Hotspot volcanoes like Hawaii are blamed on plumes rising from the deep mantle, but whether plumes are narrow deep jets or shallow plate-tectonic artifacts is still contested."],
 ["What Is the Core-Mantle Boundary Really Like?", "Deep Earth", "At 2,900 kilometers depth, the rocky mantle meets the liquid iron core across a boundary with mountain-scale topography, strange slow patches, and unknown chemistry - and our maps of it are still crude."],
 ["What Powers Earths Magnetic Field?", "Geomagnetism", "The geodynamo needs a continuous power supply to sustain the magnetic field for billions of years, but how much comes from cooling, from inner-core growth, and from chemical separation is not settled."],
 ["How Old Is the Solid Inner Core?", "Deep Earth", "The inner core - a moon-sized ball of solid iron at Earth's center - could have begun freezing anywhere from half a billion to over two billion years ago, and the estimates refuse to converge."],
 ["Why Is the Inner Core Seismically Anisotropic?", "Deep Earth", "Seismic waves travel through the inner core faster pole-to-pole than around the equator, by about 3% - and after forty years, the cause of this anisotropy is still debated."],
 ["Does the Inner Core Spin Faster Than the Rest of Earth?", "Deep Earth", "Measurements have variously claimed the inner core spins faster than the mantle, spins slower, or oscillates - and the field cannot agree which is real."],
 ["How Exactly Did the Moon Form?", "Planetary Formation", "The giant-impact hypothesis explains the Moon's existence but not why Earth and Moon are nearly identical in isotopes - and no impact model yet fits all the evidence at once."],
 ["How Did Earth Escape Snowball Glaciations?", "Paleoclimate", "Twice in the deep past the planet froze over almost entirely, and the mechanism that broke the ice - and its timescale - is still only approximately understood."],
 ["Why Was the Young Earth Warm Under a Faint Young Sun?", "Paleoclimate", "Four billion years ago the Sun shone about 25% dimmer, yet Earth had liquid water and early life - and the greenhouse recipe that kept it warm is still not agreed upon."],
 ["What Caused the Great Oxidation Event?", "Geochemistry", "Oxygen-producing photosynthesis existed long before oxygen accumulated in the atmosphere 2.4 billion years ago - and what finally tipped the balance is one of geochemistry's great unsolved whys."],
 ["What Killed Almost Everything at the End of the Permian?", "Paleoclimate", "252 million years ago about 90% of marine species vanished in the largest extinction ever, triggered by Siberian volcanism - but the exact kill mechanism, or sequence of mechanisms, is still disputed."],
 ["Where Does Earths Missing Heat Come From?", "Geodynamics", "Earth radiates about 47 terawatts of heat, but radioactive decay accounts for only around 20 - and the source and distribution of the rest is one of geophysics' longest-running puzzles."],
 ["Where Does Deep Nitrogen Go?", "Geochemistry", "Nitrogen subducts into the mantle with oceanic plates, but how much stays down there - possibly more than in the entire atmosphere - is barely measured."],
 ["How Strong Is the Oceans Biological Carbon Pump?", "Oceans", "Ocean life exports carbon to the deep sea, but the efficiency of this biological carbon pump - and how it will change as the ocean warms - is uncertain enough to matter for the global carbon budget."],
 ["How Long Does Deep Water Stay in the Deep Ocean?", "Oceans", "Water in the deep Pacific last touched the surface over a thousand years ago, but exactly how the deep ocean ventilates - and how that changed in ice ages - remains poorly quantified."],
 ["What Is Earths Complete Volatile Budget?", "Planetary Formation", "Nobody has closed the books on Earth's water, carbon, and nitrogen - delivered, lost, and stored - from formation to today, and the imbalance is where the next discoveries hide."]
];
function topicFor(seed){
  return TOPICS[((seed-1)%TOPICS.length+TOPICS.length)%TOPICS.length];
}
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}"+ "\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts){
  opts=opts||{};
  var rnd=prng(seed);
  var t=topicFor(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:t[1];
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:t[0]+' — unsolved problem record (sample)',
    title:t[0],
    description:'SAMPLE RECORD (generated — structural sample). '+t[2]+' Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'unsolved-demo',language:'python',program:demoProgram(t[0],field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-unsolved-earth-science-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("unsolved-earth-science",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
