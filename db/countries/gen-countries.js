(function(){'use strict';
/* Countries Database generator — jahdb-countries-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-COUNTRY-';
var TOPICS=[["France", "Western European country; capital Paris."], ["Japan", "Island nation in East Asia; capital Tokyo."], ["Brazil", "Largest country in South America; capital Brasilia."], ["Canada", "North American country known for vast wilderness; capital Ottawa."], ["Australia", "Island continent and country; capital Canberra."], ["Egypt", "Northeastern African country of the Nile and pyramids; capital Cairo."], ["India", "South Asian country, the world's most populous; capital New Delhi."], ["Italy", "Southern European peninsula nation; capital Rome."], ["Spain", "Iberian peninsula country; capital Madrid."], ["Germany", "Central European country; capital Berlin."], ["Mexico", "North American country south of the United States; capital Mexico City."], ["Argentina", "Southern South American country; capital Buenos Aires."], ["South Africa", "Country at the southern tip of Africa; administrative capital Pretoria."], ["China", "Large East Asian country; capital Beijing."], ["Russia", "The world's largest country by area, spanning Europe and Asia; capital Moscow."], ["United Kingdom", "Island nation off northwestern Europe; capital London."], ["United States", "North American country of fifty states; capital Washington, D.C."], ["Nigeria", "Populous West African country; capital Abuja."], ["Kenya", "East African country known for savannas and wildlife; capital Nairobi."], ["Thailand", "Southeast Asian country; capital Bangkok."], ["Greece", "Southern European country, cradle of democracy; capital Athens."], ["Portugal", "Western Iberian country; capital Lisbon."], ["Norway", "Scandinavian country of fjords; capital Oslo."], ["Sweden", "Scandinavian country; capital Stockholm."], ["Netherlands", "Low-lying Western European country; capital Amsterdam."], ["Switzerland", "Alpine Central European country; capital Bern."], ["Peru", "Western South American country of the Andes and Machu Picchu; capital Lima."], ["Chile", "Long narrow country along South America's west coast; capital Santiago."], ["Morocco", "Northwestern African country; capital Rabat."], ["Vietnam", "Southeast Asian country; capital Hanoi."]];
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
    type:'countries record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('countries',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();