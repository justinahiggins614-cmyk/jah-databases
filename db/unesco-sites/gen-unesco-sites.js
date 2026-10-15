(function(){'use strict';
/* UNESCO Sites Database generator — jahdb-unesco-sites-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-UNESCO-';
var TOPICS=[["The Great Wall of China", "The vast fortifications, a World Heritage site."], ["The Taj Mahal", "The marble mausoleum on the World Heritage list."], ["Machu Picchu", "The Inca citadel protected as World Heritage."], ["The Acropolis of Athens", "The ancient citadel, a World Heritage site."], ["Historic Rome", "The ancient center listed for its monuments."], ["Angkor Wat", "The Cambodian temple complex of world renown."], ["Petra", "The Jordanian rock city on the Heritage list."], ["The Grand Canyon", "The natural wonder listed for geology."], ["The Great Barrier Reef", "The reef system listed for marine life."], ["The Serengeti", "The Tanzanian park listed for wildlife."], ["The Galapagos Islands", "The evolutionary laboratory on the list."], ["Yellowstone", "The American park recognized for nature."], ["Venice", "The canal city and its lagoon on the list."], ["Historic Kyoto", "The temples and shrines of old Kyoto."], ["Mont-Saint-Michel", "The tidal abbey island of Normandy."], ["The Alhambra", "The Moorish palace of Granada."], ["Stonehenge", "The prehistoric monument on the list."], ["Istanbul's Historic Areas", "The mosques and palaces of old Istanbul."], ["Old Havana", "The colonial center of Cuba's capital."], ["Chichen Itza", "The Mayan city of the great pyramid."], ["Tikal", "The Mayan ruins in the Guatemalan jungle."], ["Rapa Nui", "Easter Island and its moai statues."], ["Uluru", "The great Australian rock of cultural significance."], ["What Is UNESCO", "The United Nations agency for culture and heritage."], ["The World Heritage List", "The register of protected cultural and natural sites."], ["Cultural vs. Natural", "The two categories of Heritage sites."], ["The In-Danger List", "Sites threatened and needing urgent help."], ["How Sites Are Chosen", "The nomination and evaluation process."]];
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
    type:'unesco sites record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('unesco-sites',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();