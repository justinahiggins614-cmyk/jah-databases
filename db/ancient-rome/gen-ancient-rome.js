(function(){'use strict';
/* Ancient Rome Database generator — jahdb-ancient-rome-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-ROME-';
var TOPICS=[["The City of Rome", "The capital founded on the Tiber River that grew into a vast empire."], ["Julius Caesar", "The general and statesman whose assassination ended the Roman Republic's crisis years."], ["Augustus", "The first Roman emperor, who began two centuries of relative peace."], ["The Colosseum", "The great amphitheater in Rome built for gladiatorial contests and spectacles."], ["The Roman Senate", "The advisory council of elders that governed alongside Rome's magistrates."], ["Roman Legions", "The disciplined heavy infantry that was the backbone of Rome's armies."], ["Aqueducts", "The arched water channels that supplied Rome and other cities with fresh water."], ["Latin", "The language of Rome that became the ancestor of the Romance languages."], ["Roman Law", "The legal system whose principles still underlie many modern legal codes."], ["Pompeii", "The city buried by the eruption of Mount Vesuvius, preserved as an archaeological site."], ["Pax Romana", "The long period of relative peace across the empire under the early emperors."], ["Gladiators", "The fighters who battled in arenas for public entertainment."], ["The Pantheon", "The domed temple in Rome, a masterpiece of Roman engineering."], ["Roman Roads", "The paved highway network that connected the empire and carried armies and trade."], ["Roman Numerals", "The letter-based number system (I, V, X, L, C, D, M) used across the empire."], ["The Republic", "The five centuries of Roman government before the emperors."], ["The Empire", "The imperial system that ruled the Mediterranean world for centuries."], ["Roman Baths", "The great public bathhouses that were centers of social life."], ["The Forum", "The central plaza of Rome for politics, business, and public life."], ["Villas", "The country estates of wealthy Romans."], ["Roman Coins", "The standardized currency, from copper asses to gold aurei, used across the empire."], ["The Fall of Rome", "The decline of the Western Empire in the fifth century of the common era."], ["Byzantium", "The eastern half of the empire that continued for a thousand years after Rome's fall."], ["Cicero", "The orator and statesman whose speeches and letters defined Latin prose."], ["Virgil", "The poet of the Aeneid, Rome's great national epic."], ["Hadrian's Wall", "The defensive wall built across northern Britain."], ["Roman Concrete", "The durable building material that let Romans raise domes and harbors."], ["Circus Maximus", "The huge stadium for chariot races in Rome."]];
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
    type:'ancient rome record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('ancient-rome',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();