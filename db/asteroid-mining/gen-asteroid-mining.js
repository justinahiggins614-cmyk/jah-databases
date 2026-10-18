(function(){'use strict';
/* Signature Asteroid Mining Database generator — jahdb-asteroid-mining-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-AST-MINE-';
var TOPICS=[["Target Asteroids", "Best rocks to mine."], ["Water Mining", "Propellant from space ice."], ["Platinum-Group Metals", "Precious asteroid ores."], ["Iron and Nickel", "Structural metals."], ["Rare Earths", "Tech-metal bonanzas."], ["Mining Spacecraft", "Prospector designs."], ["Extraction Methods", "Digging in zero-g."], ["Processing in Space", "Refining off-Earth."], ["Returning Resources", "Bringing riches home."], ["Orbital Refineries", "Space-based smelters."], ["Mining Economics", "Trillion-dollar rocks."], ["Legal Framework", "Who owns asteroids."], ["Prospecting Telescopes", "Finding rich rocks."], ["Sample Return Missions", "Scout missions."], ["Robot Miners", "Autonomous diggers."], ["Human Missions", "Crewed mining outposts."], ["Asteroid Redirect", "Bringing rocks to Earth orbit."], ["Space Debris Risks", "Mining safely."], ["Environmental Wins", "Off-Earth mining benefits."], ["Company Players", "Who's in the race."], ["Mining Timelines", "When it begins."], ["Asteroid Bases", "Living on rocks."], ["Fuel Depots", "Gas stations in space."], ["Market Effects", "What cheap metals change."], ["The Trillion-Dollar Future", "Space resource economy."], ["16 Psyche: The Metal World", "16 Psyche is a 220-kilometer asteroid believed to be the exposed iron-nickel core of a shattered protoplanet, making it the most famous mining target in the solar system."], ["Ryugu and Bennu: The Sample Return Pioneers", "Japan's Hayabusa2 and NASA's OSIRIS-REx returned samples from asteroids Ryugu and Bennu, proving that precision mining operations on small bodies are possible."], ["Water: The First Asteroid Commodity", "Water is the most valuable near-term asteroid commodity, not for drinking but for splitting into hydrogen and oxygen rocket propellant."], ["Platinum-Group Metals: The Long Game", "M-type asteroids are enriched in platinum-group metals like platinum, palladium, and iridium at concentrations that make terrestrial mines look barren."], ["Anchoring on Rubble Piles", "Many asteroids are rubble piles, loose collections of boulders held together by microgravity, which makes anchoring mining equipment a novel engineering challenge."], ["Optical Mining: Sunlight as a Drill", "Optical mining uses concentrated sunlight to fracture and extract volatiles from asteroid rock, avoiding the need for heavy drilling equipment."], ["The Legal Frontier: Who Owns an Asteroid", "The 2015 US Commercial Space Launch Competitiveness Act and Luxembourg's 2017 space resources law grant companies rights to resources they extract, but no nation can claim the asteroid itself."], ["Prospecting: Finding the Good Rocks", "Asteroid prospecting starts with spectroscopy from Earth, classifying asteroids into C, S, and M types that hint at water, silicates, or metals."], ["Regolith Processing in Microgravity", "Processing crushed asteroid rock in microgravity breaks most terrestrial mining methods, which rely on gravity for separation."], ["The Mass Driver: Throwing Rocks Home", "A mass driver, an electromagnetic catapult, could launch processed asteroid material toward Earth or to construction sites without rockets."], ["Crew Safety Beyond the Magnetosphere", "Human mining crews beyond Earth's magnetosphere face radiation levels that make long stays dangerous without heavy shielding."], ["The Economics of Returning Metals", "Returning platinum or gold to Earth only makes sense if the delivery cost per kilogram stays below the metal's market price, a bar that current launch costs barely clear."], ["Trojan Asteroids: The Jupiter Cache", "Jupiter's Trojan asteroids, two vast swarms sharing the giant's orbit, may hold more accessible material than the entire main belt."], ["Planetary Defense as a Mining Side Effect", "The same spacecraft that prospect asteroids for mining also characterize their orbits and compositions, directly serving planetary defense."], ["The First Trillion-Dollar Rock", "Industry folklore speaks of the first trillion-dollar rock, the asteroid whose extraction will prove the entire business case and trigger a rush."]];
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
    type:'asteroid mining creation', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('asteroid-mining',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();