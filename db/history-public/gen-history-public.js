(function(){'use strict';
/* Public History Database generator — jahdb-history-public-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-HIST-PUB-';
var TOPICS=[["Ancient Civilizations", "Mesopotamia, Egypt, and the first cities and writing."], ["Classical Greece", "City-states, democracy, philosophy, and the Persian Wars."], ["The Roman Empire", "From republic to empire; law, roads, and legacy."], ["The Middle Ages", "Feudalism, the Church, and medieval kingdoms."], ["The Renaissance", "Rebirth of art, science, and learning in Europe."], ["The Reformation", "Religious upheaval and the split of Western Christianity."], ["The Age of Exploration", "Ocean voyages connecting continents."], ["The Scientific Revolution", "Copernicus to Newton: the new science."], ["The Enlightenment", "Reason, rights, and the ideas behind revolutions."], ["The American Revolution", "Independence, the Constitution, and the republic."], ["The French Revolution", "Liberty, terror, and Napoleon's rise."], ["The Industrial Revolution", "Steam, factories, and transformed societies."], ["The Civil War", "America's conflict over union and slavery."], ["World War I", "The Great War: causes, trenches, and aftermath."], ["World War II", "Global conflict, the Holocaust, and the atomic age."], ["The Cold War", "Superpower rivalry, proxy wars, and the space race."], ["Decolonization", "Independence movements across Africa and Asia."], ["Civil Rights Movement", "The struggle for racial equality in America."], ["Ancient China", "Dynasties, Confucianism, and Chinese inventions."], ["The Ottoman Empire", "Six centuries of empire at the crossroads."], ["Latin American History", "Conquest, independence, and modern republics."], ["African Kingdoms", "Mali, Songhai, Great Zimbabwe, and more."], ["The Silk Road", "Trade routes linking East and West."], ["Historiography", "How historians interpret and debate the past."], ["Primary Sources", "Reading letters, diaries, and documents as evidence."]];
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
    type:'history knowledge record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('history-public',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();