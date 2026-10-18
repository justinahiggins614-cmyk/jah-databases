(function(){'use strict';
/* JAH The Tigrinya Language Database generator — jahdb-language-tigrinya-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LTIR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Tigrinya Language Overview - Foundations",
  "Tigrinya Writing System and Alphabet - Foundations",
  "Tigrinya Pronunciation and Phonology - Foundations",
  "Tigrinya Core Nouns I - Foundations",
  "Tigrinya Core Verbs I - Foundations",
  "Tigrinya Adjectives and Adverbs - Foundations",
  "Tigrinya Pronouns - Foundations",
  "Tigrinya Numbers and Time - Foundations",
  "Tigrinya Greetings and Everyday Phrases - Foundations",
  "Tigrinya Grammar Essentials - Foundations",
 ],
 "Compounded": [
  "Tigrinya at Home and Family - Compounded",
  "Tigrinya Food and Cooking - Compounded",
  "Tigrinya Travel and Directions - Compounded",
  "Tigrinya Work and School - Compounded",
  "Tigrinya Health and the Body - Compounded",
  "Tigrinya Emotions and Feelings - Compounded",
  "Tigrinya Nature and Weather - Compounded",
  "Tigrinya Shopping and Money - Compounded",
  "Tigrinya Friendship and Social Life - Compounded",
  "Tigrinya Technology and Communication - Compounded",
  "Tigrinya Verb Tenses in Sentences - Compounded",
 ],
 "Advanced": [
  "Tigrinya Questions and Answers - Advanced",
  "Tigrinya Commands and Requests - Advanced",
  "Tigrinya Descriptions of People and Places - Advanced",
  "Tigrinya Story I: The Boy and the Lamb - Advanced",
  "Tigrinya Story II: The Rainy Day - Advanced",
  "Tigrinya Story III: The Market Trip - Advanced",
  "Tigrinya Idioms and Proverbs - Advanced",
  "Tigrinya Formal and Polite Registers - Advanced",
  "Tigrinya Compound and Complex Sentences - Advanced",
  "Tigrinya Conversation: At the Market - Advanced",
  "Tigrinya Conversation: Meeting a Friend - Advanced",
  "Tigrinya Conversation: Solving a Problem - Advanced",
  "Tigrinya Mastery Review and Full Reference - Advanced",
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Tigrinya Study — "+safe+"\n"
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
    demo:{kind:"tigrinya-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-tigrinya-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-tigrinya',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
