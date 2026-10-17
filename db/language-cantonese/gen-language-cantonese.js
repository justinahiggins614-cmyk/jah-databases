(function(){'use strict';
/* JAH The Cantonese Language Database generator — jahdb-language-cantonese-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LYUE-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Cantonese Language Overview - Foundations",
  "Cantonese Writing System - Foundations",
  "Cantonese Pronunciation and Tones - Foundations",
  "Cantonese Core Nouns I - Foundations",
  "Cantonese Core Verbs I - Foundations",
  "Cantonese Adjectives and Adverbs - Foundations",
  "Cantonese Pronouns - Foundations",
  "Cantonese Numbers and Time - Foundations",
  "Cantonese Greetings and Everyday Phrases - Foundations",
  "Cantonese Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Cantonese Home and Family Sentences - Compounded",
  "Cantonese Food and Cooking Sentences - Compounded",
  "Cantonese Travel and Directions Sentences - Compounded",
  "Cantonese Work and School Sentences - Compounded",
  "Cantonese Health and Body Sentences - Compounded",
  "Cantonese Emotions and Feelings Sentences - Compounded",
  "Cantonese Nature and Weather Sentences - Compounded",
  "Cantonese Shopping and Money Sentences - Compounded",
  "Cantonese Friendship and Social Life Sentences - Compounded",
  "Cantonese Technology and Communication Sentences - Compounded",
  "Cantonese Verb Aspects in Sentences - Compounded"
 ],
 "Advanced": [
  "Cantonese Questions and Answers - Advanced",
  "Cantonese Commands and Requests - Advanced",
  "Cantonese Descriptions of People and Places - Advanced",
  "Cantonese Story I: A Day at Home - Advanced",
  "Cantonese Story II: The Trip to the Market - Advanced",
  "Cantonese Story III: The Plan for Tomorrow - Advanced",
  "Cantonese Idioms and Proverbs - Advanced",
  "Cantonese Formal and Polite Registers - Advanced",
  "Cantonese Compound and Complex Sentences - Advanced",
  "Cantonese Conversation: At the Market - Advanced",
  "Cantonese Conversation: Meeting a Friend - Advanced",
  "Cantonese Conversation: Solving a Problem - Advanced",
  "Cantonese Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Lesson — "+safe+"\n"
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
    demo:{kind:"language-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-cantonese-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-cantonese',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
