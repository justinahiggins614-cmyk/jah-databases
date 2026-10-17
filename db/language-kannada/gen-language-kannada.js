(function(){'use strict';
/* JAH Kannada Language Database generator — jahdb-language-kannada-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LKAN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Kannada Language Overview - Foundations",
  "Kannada Writing System: The Kannada Script - Foundations",
  "Kannada Pronunciation and Phonology - Foundations",
  "Core Kannada Nouns I - Foundations",
  "Core Kannada Verbs I - Foundations",
  "Kannada Adjectives and Adverbs - Foundations",
  "Kannada Pronouns - Foundations",
  "Kannada Numbers and Time - Foundations",
  "Kannada Greetings and Everyday Phrases - Foundations",
  "Kannada Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Home and Family in Kannada - Compounded",
  "Food and Cooking in Kannada - Compounded",
  "Travel and Directions in Kannada - Compounded",
  "Work and School in Kannada - Compounded",
  "Health and the Body in Kannada - Compounded",
  "Emotions and Feelings in Kannada - Compounded",
  "Nature and Weather in Kannada - Compounded",
  "Shopping and Money in Kannada - Compounded",
  "Friendship and Social Life in Kannada - Compounded",
  "Technology and Communication in Kannada - Compounded"
 ],
 "Advanced": [
  "Kannada Verb Tenses in Sentences - Advanced",
  "Kannada Questions and Answers - Advanced",
  "Kannada Commands and Requests - Advanced",
  "Describing People and Places in Kannada - Advanced",
  "Kannada Story I: A Simple Day - Advanced",
  "Kannada Story II: A Past Journey - Advanced",
  "Kannada Story III: A Future Plan - Advanced",
  "Kannada Idioms and Proverbs - Advanced",
  "Formal and Polite Kannada - Advanced",
  "Compound and Complex Kannada Sentences - Advanced",
  "Conversation in Kannada: At the Market - Advanced",
  "Conversation in Kannada: Meeting a Friend - Advanced",
  "Conversation in Kannada: Solving a Problem - Advanced",
  "Kannada Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Kannada Lesson — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — language learning record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A language learning record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"kannada-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-language-kannada-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-kannada',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
