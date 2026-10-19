(function(){'use strict';
/* Signature Mars City Database generator — jahdb-mars-city-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-MARS-CITY-';
var TOPICS=[["City Site Selection", "Where to build."], ["Dome Designs", "Pressurized habitats."], ["Underground Cities", "Lava-tube metropolises."], ["Radiation Shielding", "Regolith roofs."], ["Water Mining", "Polar ice extraction."], ["Greenhouse Districts", "Feeding a city."], ["Power Grids", "Nuclear plus solar."], ["Transport Networks", "Pressurized rovers and tubes."], ["City Governance", "Martian charters."], ["Martian Economy", "What cities produce."], ["Construction Robots", "Builder bot fleets."], ["3D-Printed Habitats", "Regolith printing."], ["Atmosphere Factories", "Making air and fuel."], ["City Districts", "Zoning on Mars."], ["Martian Culture", "Art of the red city."], ["Sports on Mars", "Low-gravity games."], ["Education", "Schools under domes."], ["Healthcare", "Medicine far from Earth."], ["Tourism", "Visiting the red city."], ["City Expansion", "Growing to millions."], ["Terraforming Links", "Long-term planet plans."], ["Earth Relations", "Trade and politics."], ["City Timelines", "When millions live there."], ["Mars City Art", "Visualizing metropolises."], ["The Martian Century", "Humanity's second home."], ["The Lava Tube Metropolis", "A moon city design housed in lava tubes: natural tunnels offering radiation shielding and stable temperatures."], ["The Polar Ice Mine City", "A moon city design at the lunar south pole, mining water ice from permanently shadowed craters."], ["The Regolith 3D-Printed Habitat", "A moon city design using regolith 3D printing: robots sinter lunar soil into habitat shells."], ["The Inflatable Greenhouse District", "A moon city design centered on inflatable greenhouses: food grown under transparent domes in lunar gravity."], ["The Mass Driver Launch City", "A moon city design built around an electromagnetic mass driver: the city's export is launch services."], ["The Far Side Radio Observatory Town", "A moon city design on the far side, built to service the radio-quiet observatory shielded from Earth's noise."], ["The Subsurface Transit Network", "A moon city design connected by subsurface transit: pressurized tunnels linking habitats, mines, and ports."], ["The Helium-3 Mining Camp", "A moon city design for helium-3 mining: harvesting the fusion fuel implanted by the solar wind."], ["The Lunar University", "A moon city design as a university: low gravity and vacuum enable research impossible on Earth."], ["The Crater Rim Resort", "A moon city design as a resort: low-gravity sports, Earth-view dining, and the ultimate destination."], ["The Manufacturing District", "A moon city design for manufacturing: vacuum, low gravity, and abundant solar power enable novel processes."], ["The Water Bank", "A moon city design as a water bank: storing and trading lunar water for the cislunar economy."], ["The Seismic Research Station", "A moon city design for seismology: the moon's quiet interior is a window into planetary formation."], ["The Lunar Farm Belt", "A moon city design with an agricultural belt: stacked farms feeding a growing population."], ["The Gateway Port", "A moon city design as a port: the interface between surface and orbit, Earth and deep space."], ["The Canyon City: Valles Marineris", "A Mars colony design in Valles Marineris: the canyon's walls offer shielding and its depth offers pressure."], ["The Polar Cap Water City", "A Mars colony design at the poles, mining water ice from the caps."], ["The Lava Tube Network", "A Mars colony design in lava tubes: natural shielding from radiation and dust storms."], ["The Domed Agricultural Plain", "A Mars colony design of agricultural domes: feeding the colony under transparent pressure domes."], ["The Methane Fuel Depot", "A Mars colony design around ISRU fuel production: making methane and oxygen from air and ice."], ["The Subsurface Ocean Outpost", "A Mars colony design targeting subsurface water: drilling to the deep aquifers."], ["The Terraforming Research Station", "A Mars colony design dedicated to terraforming research: the long project begins with experiments."], ["The University of Mars", "A Mars colony design as a university: the planet as laboratory."], ["The Industrial Crater", "A Mars colony design in a crater optimized for industry: mining, manufacturing, and launch."], ["The Garden Habitat", "A Mars colony design prioritizing green space: parks and farms as the city's heart."], ["The Phobos Elevator Port", "A Mars colony design linked to Phobos: the moon as a space elevator anchor and port."], ["The Dust Storm Shelter Network", "A Mars colony design for dust storms: a network of hardened shelters connected by tunnels."], ["The Art Colony", "A Mars colony design for artists: the ultimate residency, where the landscape is the muse."], ["The Children's Mars", "A Mars colony design for families: schools, playgrounds, and a genuine childhood on another world."], ["The Capital of Mars", "A Mars colony design as a capital: the political center of a Martian civilization."],
 ["The Lunar Night Survival City", "The lunar night survival city solves the Moon's cruelest problem: 14 Earth days of darkness at minus 173 degrees. The design buries habitats under 3 meters o..."],
 ["The Far Side Quiet City", "The far side quiet city exploits the Moon's greatest scientific asset: the far side is the quietest radio environment in the inner solar system, shielded fro..."],
 ["The Rimview Grand Hotel", "The Rimview Grand Hotel is the Moon's first tourist city: 300 guests at a time in a ring habitat on Shackleton's rim, with Earth hanging permanently in the b..."],
 ["The Regolith Print District", "The regolith print district is a construction zone that never imports a brick: 12 giant printers sinter lunar soil into habitat shells, landing pads, and roa..."],
 ["The Underground Harvest Belt", "The Underground Harvest Belt feeds the Moon from the Moon: 20 hectares of underground greenhouses growing potatoes, soy, and greens under LED suns, producing..."],
 ["The Helium-3 Port", "The helium-3 port is the Moon's first export economy: robotic harvesters scrape the top 3 meters of regolith across 100 square kilometers, extracting the hel..."],
 ["The Seismic Listening City", "The seismic listening city is built around the Moon's heartbeat: 100 seismometers across 50 kilometers listen to moonquakes, mapping the interior in 3D, whil..."],
 ["The Gateway Market", "The gateway market is the Moon's commercial airlock: a pressurized bazaar at the transit hub where 5,000 travelers a month buy lunar souvenirs, eat Earth-imp..."],
 ["The Polar Ice Mine", "The polar ice mine works Shackleton's permanently shadowed floor, where water ice has waited a billion years at minus 233 degrees: the mine's 150 robots exca..."],
 ["The Tycho Academy", "The Tycho Academy enrolls 3,000 students in the most extreme campus in history: 6 colleges in lava tubes, teaching everything from regolith engineering to lo..."],
 ["The Canyon University", "The canyon university sits on the rim of Valles Marineris, the 4,000-kilometer canyon, enrolling 5,000 students who study Mars by living inside its greatest ..."],
 ["The Dust Storm Bunker Network", "The dust storm bunker network keeps Mars alive through the months-long global storms: 50 hardened shelters connected by subsurface tunnels, each stocked for ..."],
 ["The Phobos Elevator Anchor", "The Phobos elevator anchor is Mars's stairway to orbit: a tether from Phobos down toward the Martian surface, with climbers carrying 20-ton payloads, cutting..."],
 ["The Terraforming Test Garden", "The terraforming test garden is a 10-hectare dome where Mars practices becoming Earth: engineered mosses and lichens colonize raw regolith, and the dome's at..."],
 ["The Subsurface Ocean Port", "The subsurface ocean port taps Mars's buried seas: radar found liquid water 1.5 kilometers down, and the port's 8 wells bring up 1,000 tons a day, the colony..."],
 ["The Industrial Crater Foundry", "The industrial crater foundry turns a 20-kilometer impact crater into Mars's factory floor: solar furnaces on the rim smelt regolith into steel and glass, pr..."],
 ["The Garden Habitat Ring", "The garden habitat ring is a 2-kilometer torus where 10,000 colonists live among trees: the ring rotates for 0.38 g, Mars gravity, and its inner surface is a..."],
 ["The Methane Farm Collective", "The methane farm collective makes rocket fuel from air and ice: 100 Sabatier reactors combine Martian CO2 with hydrogen from water, producing 1,000 tons of m..."],
 ["The Art Colony of Elysium", "The art colony of Elysium houses 500 artists in Mars's cultural capital: studios in lava tubes, galleries in crater galleries, and the famous dust-sculpture ..."],
 ["The Children's Mars Revisited", "The children's Mars revisited is the second-generation family colony: 3,000 kids growing up under the dome, attending the 12 schools, playing in the 0.38-g p..."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1];
  var content=topic[0]+' \u2014 '+topic[1];
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'mars city creation', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
    demo:null, src:'signature', _seed:seed
  };
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<50)errs.push('content too short');
  return {ok:errs.length===0, errors:errs};
}
function driftCheck(rec,sample){
  // Simple: check for exact title duplicates in sample
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('mars-city',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();