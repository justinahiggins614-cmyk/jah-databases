(function(){'use strict';
/* JAH The Swahili to English Database generator — jahdb-language-swahili-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LSWA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Swahili Language Overview - Foundations",
  "Swahili Writing System and Alphabet - Foundations",
  "Swahili Pronunciation and Phonology - Foundations",
  "Swahili Core Nouns I - Foundations",
  "Swahili Core Verbs I - Foundations",
  "Swahili Adjectives and Adverbs - Foundations",
  "Swahili Pronouns - Foundations",
  "Swahili Numbers and Time - Foundations",
  "Swahili Greetings and Everyday Phrases - Foundations",
  "Swahili Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Swahili at Home and with Family - Compounded",
  "Swahili Food and Cooking - Compounded",
  "Swahili Travel and Directions - Compounded",
  "Swahili Work and School - Compounded",
  "Swahili Health and the Body - Compounded",
  "Swahili Emotions and Feelings - Compounded",
  "Swahili Nature and Weather - Compounded",
  "Swahili Shopping and Money - Compounded",
  "Swahili Friendship and Social Life - Compounded",
  "Swahili Technology and Communication - Compounded",
  "Swahili Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Swahili Questions and Answers - Advanced",
  "Swahili Commands and Requests - Advanced",
  "Swahili Descriptions of People and Places - Advanced",
  "Swahili Story I: The Clever Herd Boy - Advanced",
  "Swahili Story II: The Lost Key - Advanced",
  "Swahili Story III: The New School - Advanced",
  "Swahili Idioms and Proverbs - Advanced",
  "Swahili Formal and Polite Registers - Advanced",
  "Swahili Compound and Complex Sentences - Advanced",
  "Swahili Conversation: At the Market - Advanced",
  "Swahili Conversation: Meeting a Friend - Advanced",
  "Swahili Conversation: Solving a Problem - Advanced",
  "Swahili Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Swahili Study — "+safe+"\n"
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
    demo:{kind:"swahili-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-swahili-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-swahili',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
