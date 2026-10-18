(function(){'use strict';
/* JAH The Quechua Language Database generator — jahdb-language-quechua-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LQUE-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Quechua Language Overview - Foundations",
  "Quechua Writing System and Alphabet - Foundations",
  "Quechua Pronunciation and Phonology - Foundations",
  "Quechua Core Nouns I - Foundations",
  "Quechua Core Verbs I - Foundations",
  "Quechua Adjectives and Adverbs - Foundations",
  "Quechua Pronouns - Foundations",
  "Quechua Numbers and Time - Foundations",
  "Quechua Greetings and Everyday Phrases - Foundations",
  "Quechua Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Quechua At Home and with Family - Compounded",
  "Quechua Food and Cooking - Compounded",
  "Quechua Travel and Directions - Compounded",
  "Quechua Work and School - Compounded",
  "Quechua Health and the Body - Compounded",
  "Quechua Emotions and Feelings - Compounded",
  "Quechua Nature and Weather - Compounded",
  "Quechua Shopping and Money - Compounded",
  "Quechua Friendship and Social Life - Compounded",
  "Quechua Technology and Communication - Compounded",
  "Quechua Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Quechua Questions and Answers - Advanced",
  "Quechua Commands and Requests - Advanced",
  "Quechua Descriptions of People and Places - Advanced",
  "Quechua Story I: Irqiwan Allquwan - Advanced",
  "Quechua Story II: Chakramayu - Advanced",
  "Quechua Story III: Musuq Yachaywasi - Advanced",
  "Quechua Idioms and Proverbs - Advanced",
  "Quechua Formal and Polite Registers - Advanced",
  "Quechua Compound and Complex Sentences - Advanced",
  "Quechua Conversation: Qhatupi - Advanced",
  "Quechua Conversation: Masiwan Tupay - Advanced",
  "Quechua Conversation: Sasachakuyta Allichay - Advanced",
  "Quechua Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Quechua Study — "+safe+"\n"
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
    demo:{kind:"language-quechua-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-quechua-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-quechua',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
