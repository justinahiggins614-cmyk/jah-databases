(function(){'use strict';
/* Planet Colonization Database generator — jahdb-planet-colonization-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-PLANETCOL-';
var TOPICS=[["Mars: Olympus Base", "The first great Martian city beneath Olympus Mons."], ["Venus Cloud Cities", "Floating habitats in the temperate Venusian cloud deck."], ["Mercury Polar Shades", "Settlements in Mercury's permanently shadowed polar craters."], ["Europa Outpost", "A station on Jupiter's ice moon above a hidden ocean."], ["Titan Domes", "Habitats on Saturn's hazy moon with its methane lakes."], ["Miranda Station", "An outpost on Uranus's fractured moon."], ["Triton Base", "Neptune's captured moon: geysers and nitrogen ice."], ["Mars Terraforming Concepts", "Long-term ideas for warming the Red Planet."], ["Asteroid Belt Habitats", "Spinning stations hollowed from asteroids."], ["Ceres Station", "The dwarf planet as a belt-trade hub."], ["Interplanetary Transport Network", "Cycler ships and fuel depots linking colonies."], ["Gravity Solutions", "Spin gravity, exoskeletons, and medical adaptation."], ["Radiation Shielding", "Protecting colonists from cosmic and solar radiation."], ["Closed-Loop Life Support", "Air, water, and food recycled indefinitely."], ["Off-World Agriculture", "Farming in regolith under artificial suns."], ["Planetary Governments", "Charters and councils for new worlds."], ["First Colonist Training", "Selecting and preparing the first settlers."], ["Deep-Space Supply Chains", "Keeping colonies supplied across millions of miles."], ["Exoplanet Survey Program", "Scouting worlds around other stars."], ["Generation Ships", "Multi-century vessels carrying colonists to the stars."], ["Cryosleep Concepts", "Suspended animation for long transits."], ["Planetary Defense", "Protecting colonies from impacts and debris."], ["Alien Microbe Protocols", "Planetary protection in both directions."], ["Off-World Economies", "What colonies make, mine, and trade."], ["Colonial Charters", "Founding documents for new settlements."], ["Multi-Planet Internet", "Communications across light-minute delays."], ["Emergency Evacuation Plans", "Getting colonists home when things fail."], ["Centennial Colonization Roadmap", "A hundred-year plan for settling the solar system."]];
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
    type:'planet colonization plan', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('planet-colonization',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}

/* Group-0 expansion: 10 new topics. */
TOPICS.push(
["Designing a Tidally-Locked Ocean World","One side eternal day, one side eternal night: colonizing the twilight band of a red-dwarf ocean planet."],
["The Low-Gravity Greenhouse Dome","Farming on a world with a third of Earth’s gravity: taller plants, stranger water, and domes that practically lift themselves."],
["Mars: The Canyon City","Why the first Martian city belongs in a canyon: radiation shielding, water ice, and a sky you can pressurize."],
["The Ice Moon Harbor","A colony beneath the ice of an ocean moon: melting down to a black sea that has waited a billion years."],
["Venus Cloud Cities","Fifty kilometers above Venus’s hellish surface, the air is Earthlike: floating cities in the most Earth-like place off Earth."],
["The Desert World Water Plan","Colonizing a dune planet: every drop accounted for, from atmospheric condensers to deep fossil aquifers."],
["A Colony on a Super-Earth","Twice the gravity, endless horizons: designing for a world where everything weighs double and the air is thick."],
["The Generation Ship’s Destination","Choosing where a century-long voyage ends: the survey criteria for a world worth a hundred years of travel."],
["Terraforming in Stages","The thousand-year project: how a dead world becomes a living one, one engineered stage at a time."],
["The First Hundred Days on a New World","Landing to living: the critical first hundred days when a colony either takes root or dies trying."]
);
})();