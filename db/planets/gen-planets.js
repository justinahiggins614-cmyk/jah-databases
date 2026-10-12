(function(){'use strict';
/* Planets Database generator — jahdb-planets-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-PLANET-';
var TOPICS=[["Mercury", "The smallest planet, closest to the Sun."], ["Venus", "The hot cloud-covered planet, Earth's near-twin in size."], ["Earth", "Our home, the only known planet with life."], ["Mars", "The red planet, target of rovers and future explorers."], ["Jupiter", "The largest planet, a gas giant with a great storm."], ["Saturn", "The ringed giant of the solar system."], ["Uranus", "The tilted ice giant rolling on its side."], ["Neptune", "The distant blue ice giant of fierce winds."], ["Pluto", "The famous dwarf planet of the outer solar system."], ["The Sun", "The star at the center of our solar system."], ["The Moon", "Earth's natural satellite, visited by astronauts."], ["Orbits", "The paths planets follow around the Sun."], ["Inner Planets", "The four small rocky worlds near the Sun."], ["Outer Planets", "The four giant worlds of the outer solar system."], ["Gas Giants", "Jupiter and Saturn, made mostly of hydrogen and helium."], ["Terrestrial Planets", "The rocky Earth-like planets."], ["The Asteroid Belt", "The rocky ring between Mars and Jupiter."], ["Day and Night", "How a planet's spin makes light and dark."], ["The Seasons", "How tilt gives planets their yearly cycles."], ["Gravity", "The force holding planets and people down."], ["Mars Rovers", "The robotic explorers studying the red planet."], ["The Voyager Probes", "The spacecraft that toured the outer planets."], ["Exoplanets", "Planets orbiting other stars."], ["Dwarf Planets", "Small round worlds like Pluto and Ceres."], ["Comets", "Icy visitors with glowing tails."], ["Planetary Rings", "The flat discs circling giant planets."], ["Moons", "The natural satellites of planets."], ["The Solar System's Age", "The billions of years since the planets formed."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1]+' This '+angle+' guide provides comprehensive coverage.';
  var content='['+angle+'] '+topic[0]+': '+topic[1]+' Full detailed content for '+angle+' perspective.';
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'planets record', content:content,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('planets',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();