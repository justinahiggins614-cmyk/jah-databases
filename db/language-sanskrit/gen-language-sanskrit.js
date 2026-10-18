(function(){'use strict';
/* JAH The Sanskrit to English Database generator — jahdb-language-sanskrit-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LSAN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Sanskrit Language Overview - Foundations",
  "Sanskrit Writing System and Alphabet - Foundations",
  "Sanskrit Pronunciation and Phonology - Foundations",
  "Sanskrit Core Nouns I - Foundations",
  "Sanskrit Core Verbs I - Foundations",
  "Sanskrit Adjectives and Adverbs - Foundations",
  "Sanskrit Pronouns - Foundations",
  "Sanskrit Numbers and Time - Foundations",
  "Sanskrit Greetings and Everyday Phrases - Foundations",
  "Sanskrit Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Sanskrit at Home and with Family - Compounded",
  "Sanskrit Food and Cooking - Compounded",
  "Sanskrit Travel and Directions - Compounded",
  "Sanskrit Work and School - Compounded",
  "Sanskrit Health and the Body - Compounded",
  "Sanskrit Emotions and Feelings - Compounded",
  "Sanskrit Nature and Weather - Compounded",
  "Sanskrit Shopping and Money - Compounded",
  "Sanskrit Friendship and Social Life - Compounded",
  "Sanskrit Technology and Communication - Compounded",
  "Sanskrit Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Sanskrit Questions and Answers - Advanced",
  "Sanskrit Commands and Requests - Advanced",
  "Sanskrit Descriptions of People and Places - Advanced",
  "Sanskrit Story I: The Clever Monkey - Advanced",
  "Sanskrit Story II: The Talkative Tortoise - Advanced",
  "Sanskrit Story III: The Golden Geese - Advanced",
  "Sanskrit Idioms and Proverbs - Advanced",
  "Sanskrit Formal and Polite Registers - Advanced",
  "Sanskrit Compound and Complex Sentences - Advanced",
  "Sanskrit Conversation: At the Market - Advanced",
  "Sanskrit Conversation: Meeting a Friend - Advanced",
  "Sanskrit Conversation: Solving a Problem - Advanced",
  "Sanskrit Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Sanskrit Study — "+safe+"\n"
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
    demo:{kind:"sanskrit-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-sanskrit-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-sanskrit',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
