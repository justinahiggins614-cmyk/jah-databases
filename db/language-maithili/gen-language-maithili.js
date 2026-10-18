(function(){'use strict';
/* JAH The Maithili Language Database generator — jahdb-language-maithili-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LMAI-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Maithili Language Overview - Foundations",
  "Maithili Writing System and Alphabet - Foundations",
  "Maithili Pronunciation and Phonology - Foundations",
  "Maithili Core Nouns I - Foundations",
  "Maithili Core Verbs I - Foundations",
  "Maithili Adjectives and Adverbs - Foundations",
  "Maithili Pronouns - Foundations",
  "Maithili Numbers and Time - Foundations",
  "Maithili Greetings and Everyday Phrases - Foundations",
  "Maithili Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Maithili at Home and with Family - Compounded",
  "Maithili Food and Cooking - Compounded",
  "Maithili Travel and Directions - Compounded",
  "Maithili Work and School - Compounded",
  "Maithili Health and the Body - Compounded",
  "Maithili Emotions and Feelings - Compounded",
  "Maithili Nature and Weather - Compounded",
  "Maithili Shopping and Money - Compounded",
  "Maithili Friendship and Social Life - Compounded",
  "Maithili Technology and Communication - Compounded",
  "Maithili Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Maithili Questions and Answers - Advanced",
  "Maithili Commands and Requests - Advanced",
  "Maithili Descriptions of People and Places - Advanced",
  "Maithili Story I: The Lost Key - Advanced",
  "Maithili Story II: The Little Bird - Advanced",
  "Maithili Story III: The Market Day - Advanced",
  "Maithili Idioms and Proverbs - Advanced",
  "Maithili Formal and Polite Registers - Advanced",
  "Maithili Compound and Complex Sentences - Advanced",
  "Maithili Conversation: At the Market - Advanced",
  "Maithili Conversation: Meeting a Friend - Advanced",
  "Maithili Conversation: Solving a Problem - Advanced",
  "Maithili Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Maithili Study — "+safe+"\n"
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
    demo:{kind:"maithili-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-maithili-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-maithili',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
