(function(){'use strict';
/* JAH The Somali Language Database generator — jahdb-language-somali-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LSOM-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Somali Language Overview - Foundations",
  "Somali Writing System and Alphabet - Foundations",
  "Somali Pronunciation and Phonology - Foundations",
  "Somali Core Nouns I - Foundations",
  "Somali Core Verbs I - Foundations",
  "Somali Adjectives and Adverbs - Foundations",
  "Somali Pronouns - Foundations",
  "Somali Numbers and Time - Foundations",
  "Somali Greetings and Everyday Phrases - Foundations",
  "Somali Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Somali at Home and with Family - Compounded",
  "Somali Food and Cooking - Compounded",
  "Somali Travel and Directions - Compounded",
  "Somali Work and School - Compounded",
  "Somali Health and the Body - Compounded",
  "Somali Emotions and Feelings - Compounded",
  "Somali Nature and Weather - Compounded",
  "Somali Shopping and Money - Compounded",
  "Somali Friendship and Social Life - Compounded",
  "Somali Technology and Communication - Compounded",
  "Somali Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Somali Questions and Answers - Advanced",
  "Somali Commands and Requests - Advanced",
  "Somali Descriptions of People and Places - Advanced",
  "Somali Story I: Wiil Waal and the Chief - Advanced",
  "Somali Story II: The Clever Camel Herder - Advanced",
  "Somali Story III: The New School in Hargeysa - Advanced",
  "Somali Idioms and Proverbs - Advanced",
  "Somali Formal and Polite Registers - Advanced",
  "Somali Compound and Complex Sentences - Advanced",
  "Somali Conversation: At the Market - Advanced",
  "Somali Conversation: Meeting a Friend - Advanced",
  "Somali Conversation: Solving a Problem - Advanced",
  "Somali Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Somali Study — "+safe+"\n"
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
    demo:{kind:"somali-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-somali-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-somali',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
