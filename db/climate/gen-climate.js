(function(){'use strict';
/* Climate Database generator — jahdb-climate-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-CLIM-';
var TOPICS=[["Weather vs. Climate", "Weather is short-term conditions; climate is the long-term pattern."], ["Tropical Climate", "Hot, humid zones near the equator with abundant rainfall."], ["Arid Climate", "Dry zones with very little rainfall, including true deserts."], ["Temperate Climate", "Moderate zones with distinct seasons between the tropics and poles."], ["Continental Climate", "Interior zones with hot summers and cold winters."], ["Polar Climate", "Freezing zones around the poles with ice and tundra."], ["The Greenhouse Effect", "The natural warming of Earth by gases that trap heat in the atmosphere."], ["Seasons", "The yearly cycle caused by Earth's tilted axis as it orbits the Sun."], ["El Nino", "The Pacific warming pattern that shifts weather around the world."], ["La Nina", "The Pacific cooling pattern with opposite effects to El Nino."], ["Monsoons", "Seasonal wind shifts bringing heavy rains to South and Southeast Asia."], ["Mediterranean Climate", "Mild, wet winters and hot, dry summers around the Mediterranean and similar coasts."], ["Rainforests", "Lush, rainy forests of the tropics with immense biodiversity."], ["Tundra", "Treeless Arctic plains with frozen subsoil called permafrost."], ["Permafrost", "Permanently frozen ground beneath the Arctic surface."], ["Ocean Currents", "The great flows of seawater that move heat around the planet."], ["Altitude and Climate", "How elevation cools the air and changes local climate."], ["Desert Climates", "Extreme dryness with hot days and often cold nights."], ["Savanna Climate", "Tropical grasslands with distinct wet and dry seasons."], ["Maritime Climate", "Mild, moist climates moderated by nearby oceans."], ["Microclimates", "Small-scale climate differences, such as a sheltered valley."], ["Climate Zones", "The broad bands of climate from equator to poles."], ["Prevailing Winds", "The dominant wind patterns, like the trade winds and westerlies."], ["The Water Cycle", "The endless movement of water between oceans, air, and land."], ["Cloud Formation", "How rising moist air cools and condenses into clouds."], ["Climate Records", "Ice cores, tree rings, and other archives of past climate."], ["Urban Heat Islands", "How cities run warmer than the surrounding countryside."], ["Climate Adaptation", "Adjusting societies and infrastructure to changing climate conditions."]];
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
    type:'climate record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('climate',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();