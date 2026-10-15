(function(){'use strict';
/* Public Textbook Database generator — jahdb-textbook-public-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-TEXT-PUB-';
var TOPICS=[["Public Domain Textbooks", "Free classic textbooks, full text in file."], ["OpenStax and OER", "Modern open textbooks for college courses."], ["Mathematics Textbooks", "Public texts from arithmetic to calculus."], ["Science Textbooks", "Open science texts across the disciplines."], ["History Textbooks", "Public histories of nations and eras."], ["Literature Anthologies", "Collected public domain readings."], ["Grammar References", "Classic guides to English grammar."], ["Economics Primers", "Foundational economics texts."], ["Psychology Introductions", "Classic and open psychology texts."], ["Philosophy Texts", "Primary sources free for study."], ["Language Learning Books", "Historic and open language courses."], ["Computer Science Texts", "Open CS textbooks and references."], ["Engineering Handbooks", "Public engineering references."], ["Law Textbooks", "Public legal education materials."], ["Art History Surveys", "Open surveys of art through the ages."], ["Music Theory Books", "Public domain theory and harmony texts."], ["Study Guides", "How to study from any textbook."], ["How Textbooks Are Written", "The authoring and review process."], ["Evaluating Textbook Quality", "What makes a textbook trustworthy."], ["Digital vs Print", "Choosing formats for learning."], ["Textbook Affordability", "The open movement against high prices."], ["Open Licensing (CC)", "Creative Commons licenses explained."], ["Using Textbooks Effectively", "Active reading and problem strategies."], ["Supplementary Materials", "Workbooks, slides, and question banks."], ["Teacher Editions", "Guides for instructors using open texts."], ["Building a Home Library", "Curating your own reference shelf."], ["Finding Free Textbooks", "Where to look for open educational resources."], ["Classic Reference Works", "Dictionaries, encyclopedias, and companions."]];
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
    type:'public textbook record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('textbook-public',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();