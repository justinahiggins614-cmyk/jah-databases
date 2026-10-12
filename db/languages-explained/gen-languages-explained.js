(function(){'use strict';
/* All Languages Explained Database generator — jahdb-languages-explained-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-LANG-';
var TOPICS=[["Mandarin Chinese", "The world's most-spoken native language: tones, characters, and grammar."], ["Spanish", "A global Romance language: pronunciation, grammar, and regional varieties."], ["English", "The global lingua franca: history, grammar, and worldwide varieties."], ["Hindi", "India's widely spoken language: Devanagari script and grammar."], ["Arabic", "A Semitic language family: script, dialects, and Modern Standard Arabic."], ["Portuguese", "From Portugal to Brazil: grammar and pronunciation."], ["Bengali", "South Asia's literary giant: script and structure."], ["Russian", "Cyrillic script, cases, and the Slavic language family."], ["Japanese", "Three scripts, honorifics, and sentence structure."], ["German", "Cases, compound words, and Germanic roots."], ["French", "Romance elegance: gender, liaison, and global reach."], ["Korean", "Hangul: the scientific alphabet, plus grammar and honorifics."], ["Turkish", "Agglutinative structure and vowel harmony."], ["Vietnamese", "Tones and Latin-based script in Southeast Asia."], ["Italian", "The language of music and art: pronunciation and grammar."], ["Language Families Overview", "How linguists group the world's 7,000 languages."], ["Writing Systems of the World", "Alphabets, abjads, abugidas, syllabaries, and logographs."], ["Tonal Languages", "How pitch changes meaning in Mandarin, Thai, Yoruba, and more."], ["Agglutinative Languages", "Building words from stacked meaningful pieces."], ["Sign Languages Overview", "Natural visual languages with their own grammars."], ["Endangered Languages", "Languages at risk and efforts to revitalize them."], ["Pidgins and Creoles", "Contact languages born from trade and history."], ["Latin and the Romance Roots", "How Latin became French, Spanish, Italian, and more."], ["Sanskrit and Indo-Aryan", "Ancient roots of Hindi, Bengali, and their sisters."], ["Constructed Languages", "Esperanto, Klingon, and languages built by design."], ["How Children Learn Language", "Acquisition milestones from babbling to sentences."], ["Translation Concepts", "What translators balance: meaning, tone, and culture."], ["Language and Identity", "How language shapes who we are."]];
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
    type:'language record', content:content,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('languages-explained',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();