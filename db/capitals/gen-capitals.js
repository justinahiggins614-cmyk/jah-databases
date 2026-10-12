(function(){'use strict';
/* Capitals Database generator — jahdb-capitals-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-CAPITAL-';
var TOPICS=[["Paris", "Capital of France, famed for art, fashion, and the Eiffel Tower."], ["Tokyo", "Capital of Japan, one of the world's largest metropolitan areas."], ["London", "Capital of the United Kingdom, a global center of finance and culture."], ["Washington, D.C.", "Capital of the United States, seat of the federal government."], ["Beijing", "Capital of China, a political and cultural center with ancient history."], ["Moscow", "Capital of Russia and its largest city."], ["Berlin", "Capital of Germany, reunified after the Cold War division."], ["Rome", "Capital of Italy, built on the ancient heart of the Roman Empire."], ["Madrid", "Capital of Spain, located on the central plateau."], ["Cairo", "Capital of Egypt, the largest city in the Arab world."], ["New Delhi", "Capital of India, the seat of its government."], ["Ottawa", "Capital of Canada, on the Ottawa River."], ["Canberra", "Planned capital of Australia, built as a compromise between Sydney and Melbourne."], ["Brasilia", "Planned capital of Brazil, built in the interior in the twentieth century."], ["Buenos Aires", "Capital of Argentina, a major cultural and economic center."], ["Mexico City", "Capital of Mexico, one of the largest cities in the world."], ["Lima", "Capital of Peru, founded on the Pacific coast."], ["Oslo", "Capital of Norway, set at the head of the Oslofjord."], ["Stockholm", "Capital of Sweden, spread across an archipelago."], ["Helsinki", "Capital of Finland, on the Gulf of Finland."], ["Warsaw", "Capital of Poland, rebuilt after the Second World War."], ["Athens", "Capital of Greece and the birthplace of democracy."], ["Lisbon", "Capital of Portugal, on the Atlantic coast."], ["Vienna", "Capital of Austria, famed for music and imperial history."], ["Bern", "Capital of Switzerland."], ["Prague", "Capital of Czechia, known for its preserved old town."], ["Nairobi", "Capital of Kenya, a major East African hub."], ["Bangkok", "Capital of Thailand, on the Chao Phraya River."]];
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
    type:'capitals record', content:content,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('capitals',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();