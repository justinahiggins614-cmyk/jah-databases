(function(){'use strict';
/* Explorers Database generator — jahdb-explorers-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-EXPLOR-';
var TOPICS=[["Marco Polo", "The Venetian traveler whose account of Asia amazed Europe."], ["Christopher Columbus", "The navigator whose 1492 voyage opened the Americas to European contact."], ["Vasco da Gama", "The Portuguese captain who sailed around Africa to India."], ["Ferdinand Magellan", "Leader of the first expedition to circle the globe."], ["Captain James Cook", "The British navigator who charted the Pacific."], ["Lewis and Clark", "The leaders of the American expedition across the continent to the Pacific."], ["Ernest Shackleton", "The Antarctic explorer famed for saving his stranded crew."], ["Roald Amundsen", "The Norwegian first to reach the South Pole."], ["Edmund Hillary", "With Tenzing Norgay, among the first confirmed to summit Mount Everest."], ["Amelia Earhart", "The pioneering aviator who vanished on a round-the-world flight."], ["Ibn Battuta", "The Moroccan scholar who traveled across the medieval Islamic world."], ["Zheng He", "The Chinese admiral of the great treasure fleets."], ["Leif Erikson", "The Norse explorer who reached North America centuries before Columbus."], ["Sacagawea", "The Shoshone guide of the Lewis and Clark expedition."], ["John Cabot", "The Venetian sailing for England who reached North America."], ["Hernan Cortes", "The Spanish conquistador of the Aztec Empire."], ["Francisco Pizarro", "The Spanish conquistador of the Inca Empire."], ["Henry Hudson", "The explorer of the North American waters that bear his name."], ["David Livingstone", "The missionary-explorer of central Africa."], ["Robert Peary", "The American explorer credited with reaching the North Pole."], ["Sacred Expeditions", "The pilgrimages and religious journeys of history."], ["The Silk Road", "The ancient trade routes linking China to the Mediterranean."], ["Age of Exploration", "The era when European ships mapped the world's oceans."], ["Navigation Tools", "Compass, astrolabe, and charts that made long voyages possible."], ["Mapping the World", "How explorers' charts grew into modern maps."], ["Indigenous Guides", "The local knowledge that made expeditions possible."], ["Exploration Costs", "The dangers, from scurvy to shipwreck, that explorers faced."], ["Modern Explorers", "Today's explorers of deep oceans, caves, and space."]];
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
    type:'explorers record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('explorers',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();