(function(){'use strict';
/* JAH The Zulu Language Database generator — jahdb-language-zulu-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LZUL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Zulu Language Overview - Foundations",
  "Zulu Writing System and Alphabet - Foundations",
  "Zulu Pronunciation and Phonology - Foundations",
  "Zulu Core Nouns I - Foundations",
  "Zulu Core Verbs I - Foundations",
  "Zulu Adjectives and Adverbs - Foundations",
  "Zulu Pronouns - Foundations",
  "Zulu Numbers and Time - Foundations",
  "Zulu Greetings and Everyday Phrases - Foundations",
  "Zulu Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Zulu at Home and with Family - Compounded",
  "Zulu Food and Cooking - Compounded",
  "Zulu Travel and Directions - Compounded",
  "Zulu Work and School - Compounded",
  "Zulu Health and the Body - Compounded",
  "Zulu Emotions and Feelings - Compounded",
  "Zulu Nature and Weather - Compounded",
  "Zulu Shopping and Money - Compounded",
  "Zulu Friendship and Social Life - Compounded",
  "Zulu Technology and Communication - Compounded",
  "Zulu Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Zulu Questions and Answers - Advanced",
  "Zulu Commands and Requests - Advanced",
  "Zulu Descriptions of People and Places - Advanced",
  "Zulu Story I: uHlakanyana and the Giant - Advanced",
  "Zulu Story II: uHlakanyana and the Clever Plan - Advanced",
  "Zulu Story III: The New School in Durban - Advanced",
  "Zulu Idioms and Proverbs - Advanced",
  "Zulu Formal and Polite Registers - Advanced",
  "Zulu Compound and Complex Sentences - Advanced",
  "Zulu Conversation: At the Market - Advanced",
  "Zulu Conversation: Meeting a Friend - Advanced",
  "Zulu Conversation: Solving a Problem - Advanced",
  "Zulu Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Zulu Study — "+safe+"\n"
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
    demo:{kind:"zulu-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-zulu-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-zulu',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
