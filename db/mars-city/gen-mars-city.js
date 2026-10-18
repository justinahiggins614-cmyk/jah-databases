(function(){'use strict';
/* Signature Mars City Database generator — jahdb-mars-city-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-MARS-CITY-';
var TOPICS=[["City Site Selection", "Where to build."], ["Dome Designs", "Pressurized habitats."], ["Underground Cities", "Lava-tube metropolises."], ["Radiation Shielding", "Regolith roofs."], ["Water Mining", "Polar ice extraction."], ["Greenhouse Districts", "Feeding a city."], ["Power Grids", "Nuclear plus solar."], ["Transport Networks", "Pressurized rovers and tubes."], ["City Governance", "Martian charters."], ["Martian Economy", "What cities produce."], ["Construction Robots", "Builder bot fleets."], ["3D-Printed Habitats", "Regolith printing."], ["Atmosphere Factories", "Making air and fuel."], ["City Districts", "Zoning on Mars."], ["Martian Culture", "Art of the red city."], ["Sports on Mars", "Low-gravity games."], ["Education", "Schools under domes."], ["Healthcare", "Medicine far from Earth."], ["Tourism", "Visiting the red city."], ["City Expansion", "Growing to millions."], ["Terraforming Links", "Long-term planet plans."], ["Earth Relations", "Trade and politics."], ["City Timelines", "When millions live there."], ["Mars City Art", "Visualizing metropolises."], ["The Martian Century", "Humanity's second home."], ["The Lava Tube Metropolis", "A moon city design housed in lava tubes: natural tunnels offering radiation shielding and stable temperatures."], ["The Polar Ice Mine City", "A moon city design at the lunar south pole, mining water ice from permanently shadowed craters."], ["The Regolith 3D-Printed Habitat", "A moon city design using regolith 3D printing: robots sinter lunar soil into habitat shells."], ["The Inflatable Greenhouse District", "A moon city design centered on inflatable greenhouses: food grown under transparent domes in lunar gravity."], ["The Mass Driver Launch City", "A moon city design built around an electromagnetic mass driver: the city's export is launch services."], ["The Far Side Radio Observatory Town", "A moon city design on the far side, built to service the radio-quiet observatory shielded from Earth's noise."], ["The Subsurface Transit Network", "A moon city design connected by subsurface transit: pressurized tunnels linking habitats, mines, and ports."], ["The Helium-3 Mining Camp", "A moon city design for helium-3 mining: harvesting the fusion fuel implanted by the solar wind."], ["The Lunar University", "A moon city design as a university: low gravity and vacuum enable research impossible on Earth."], ["The Crater Rim Resort", "A moon city design as a resort: low-gravity sports, Earth-view dining, and the ultimate destination."], ["The Manufacturing District", "A moon city design for manufacturing: vacuum, low gravity, and abundant solar power enable novel processes."], ["The Water Bank", "A moon city design as a water bank: storing and trading lunar water for the cislunar economy."], ["The Seismic Research Station", "A moon city design for seismology: the moon's quiet interior is a window into planetary formation."], ["The Lunar Farm Belt", "A moon city design with an agricultural belt: stacked farms feeding a growing population."], ["The Gateway Port", "A moon city design as a port: the interface between surface and orbit, Earth and deep space."], ["The Canyon City: Valles Marineris", "A Mars colony design in Valles Marineris: the canyon's walls offer shielding and its depth offers pressure."], ["The Polar Cap Water City", "A Mars colony design at the poles, mining water ice from the caps."], ["The Lava Tube Network", "A Mars colony design in lava tubes: natural shielding from radiation and dust storms."], ["The Domed Agricultural Plain", "A Mars colony design of agricultural domes: feeding the colony under transparent pressure domes."], ["The Methane Fuel Depot", "A Mars colony design around ISRU fuel production: making methane and oxygen from air and ice."], ["The Subsurface Ocean Outpost", "A Mars colony design targeting subsurface water: drilling to the deep aquifers."], ["The Terraforming Research Station", "A Mars colony design dedicated to terraforming research: the long project begins with experiments."], ["The University of Mars", "A Mars colony design as a university: the planet as laboratory."], ["The Industrial Crater", "A Mars colony design in a crater optimized for industry: mining, manufacturing, and launch."], ["The Garden Habitat", "A Mars colony design prioritizing green space: parks and farms as the city's heart."], ["The Phobos Elevator Port", "A Mars colony design linked to Phobos: the moon as a space elevator anchor and port."], ["The Dust Storm Shelter Network", "A Mars colony design for dust storms: a network of hardened shelters connected by tunnels."], ["The Art Colony", "A Mars colony design for artists: the ultimate residency, where the landscape is the muse."], ["The Children's Mars", "A Mars colony design for families: schools, playgrounds, and a genuine childhood on another world."], ["The Capital of Mars", "A Mars colony design as a capital: the political center of a Martian civilization."]];
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