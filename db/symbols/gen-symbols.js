(function(){'use strict';
/* Symbols Database generator — jahdb-symbols-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-SYMBOL-';
var TOPICS=[["The Ampersand", "The & sign meaning 'and'."], ["The At Sign", "The @ connecting names and email addresses."], ["The Hashtag", "The # marking topics on social media."], ["Copyright Symbol", "The (c) marking creative ownership."], ["Trademark Symbol", "The marks showing brand claims."], ["The Dollar Sign", "The $ of dollars and pesos."], ["The Euro Sign", "The currency symbol of the euro."], ["The Yen Sign", "The currency mark of Japan and China."], ["Plus and Minus", "The + and - of mathematics."], ["The Equals Sign", "The = showing equivalence."], ["Infinity", "The endless loop of the infinite."], ["Pi", "The Greek letter for the circle constant."], ["The Percent Sign", "The % of parts per hundred."], ["The Degree Symbol", "The mark for angles and temperature."], ["The Peace Symbol", "The circle-and-lines emblem of peace."], ["The Recycling Symbol", "The chasing arrows of recycling."], ["The Heart", "The universal shape of love."], ["Skull and Crossbones", "The warning of poison and danger."], ["The Radiation Symbol", "The trefoil warning of radioactivity."], ["The Biohazard Symbol", "The warning for biological hazards."], ["The Ankh", "The Egyptian symbol of life."], ["Yin and Yang", "The Taoist symbol of balanced opposites."], ["The Cross", "The central symbol of Christianity."], ["The Crescent", "The symbol associated with Islam."], ["The Om", "The sacred syllable of Hinduism."], ["The Rod of Asclepius", "The serpent staff of medicine."], ["The Olympic Rings", "The five interlocking rings of the Games."], ["The Power Symbol", "The circle-and-line of on and off."]];
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
    type:'symbols record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('symbols',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();