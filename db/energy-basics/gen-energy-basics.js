(function(){'use strict';
/* Energy Basics Database generator — jahdb-energy-basics-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-ENERGY-BAS-';
var TOPICS=[["Kinetic Energy", "The energy of motion, from a rolling ball to flowing water."], ["Potential Energy", "Stored energy, such as water held behind a dam."], ["Thermal Energy", "Heat energy from the movement of particles."], ["Chemical Energy", "Energy stored in the bonds of molecules, released in reactions."], ["Electrical Energy", "Energy carried by moving electric charges."], ["Nuclear Energy", "Energy from atomic nuclei, released in fission and fusion."], ["Solar Energy", "Power from sunlight, captured by panels and plants alike."], ["Wind Energy", "Power from moving air, harvested by wind turbines."], ["Hydroelectric Power", "Electricity from falling or flowing water."], ["Geothermal Energy", "Heat from inside the Earth used for power and warmth."], ["Biomass Energy", "Energy from wood, crops, and other organic matter."], ["Fossil Fuels", "Coal, oil, and natural gas formed from ancient organic matter."], ["Conservation of Energy", "The principle that energy is never created or destroyed, only changed."], ["Renewable Energy", "Sources that replenish naturally, like sun and wind."], ["Nonrenewable Energy", "Sources used up faster than nature replaces them."], ["Energy Efficiency", "Getting more useful work from less energy."], ["Power vs. Energy", "Power is the rate of using energy; energy is the total amount."], ["The Watt", "The unit of power, named for James Watt."], ["Photosynthesis", "How plants convert sunlight into chemical energy."], ["Food Energy", "The chemical energy in food that powers living bodies."], ["Batteries", "Devices storing chemical energy and releasing it as electricity."], ["The Electric Grid", "The network delivering electricity from plants to homes."], ["Energy Storage", "Ways of saving energy for later, from dams to batteries."], ["Insulation", "Materials that slow heat loss and save energy in buildings."], ["Transportation Energy", "The fuels and electricity that move people and goods."], ["Energy Audits", "Checking a home or business for wasted energy."], ["Peak Demand", "The times when electricity use is highest."], ["The Future of Energy", "The shift toward cleaner and more efficient energy systems."]];
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
    type:'energy basics record', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
    demo:null, src:'public', _seed:seed
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('energy-basics',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();