(function(){'use strict';
/* JAH The Madurese Language Database generator — jahdb-language-madurese-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LMAD-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Madurese Language Overview - Foundations",
  "Madurese Writing System and Alphabet - Foundations",
  "Madurese Pronunciation and Phonology - Foundations",
  "Madurese Core Nouns I - Foundations",
  "Madurese Core Verbs I - Foundations",
  "Madurese Adjectives and Adverbs - Foundations",
  "Madurese Pronouns - Foundations",
  "Madurese Numbers and Time - Foundations",
  "Madurese Greetings and Everyday Phrases - Foundations",
  "Madurese Grammar Essentials - Foundations",
 ],
 "Compounded": [
  "Madurese at Home and Family - Compounded",
  "Madurese Food and Cooking - Compounded",
  "Madurese Travel and Directions - Compounded",
  "Madurese Work and School - Compounded",
  "Madurese Health and the Body - Compounded",
  "Madurese Emotions and Feelings - Compounded",
  "Madurese Nature and Weather - Compounded",
  "Madurese Shopping and Money - Compounded",
  "Madurese Friendship and Social Life - Compounded",
  "Madurese Technology and Communication - Compounded",
  "Madurese Verb Tenses in Sentences - Compounded",
 ],
 "Advanced": [
  "Madurese Questions and Answers - Advanced",
  "Madurese Commands and Requests - Advanced",
  "Madurese Descriptions of People and Places - Advanced",
  "Madurese Story I: The Boy and the Goat - Advanced",
  "Madurese Story II: The Rainy Day - Advanced",
  "Madurese Story III: The Market Trip - Advanced",
  "Madurese Idioms and Proverbs - Advanced",
  "Madurese Formal and Polite Registers - Advanced",
  "Madurese Compound and Complex Sentences - Advanced",
  "Madurese Conversation: At the Market - Advanced",
  "Madurese Conversation: Meeting a Friend - Advanced",
  "Madurese Conversation: Solving a Problem - Advanced",
  "Madurese Mastery Review and Full Reference - Advanced",
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Madurese Study — "+safe+"\n"
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
    demo:{kind:"madurese-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-madurese-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-madurese',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
