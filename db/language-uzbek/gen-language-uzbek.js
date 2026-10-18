(function(){'use strict';
/* JAH The Uzbek to English Database generator — jahdb-language-uzbek-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LUZB-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Uzbek Language Overview - Foundations",
  "Uzbek Writing System and Alphabet - Foundations",
  "Uzbek Pronunciation and Phonology - Foundations",
  "Uzbek Core Nouns I - Foundations",
  "Uzbek Core Verbs I - Foundations",
  "Uzbek Adjectives and Adverbs - Foundations",
  "Uzbek Pronouns - Foundations",
  "Uzbek Numbers and Time - Foundations",
  "Uzbek Greetings and Everyday Phrases - Foundations",
  "Uzbek Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Uzbek at Home and with Family - Compounded",
  "Uzbek Food and Cooking - Compounded",
  "Uzbek Travel and Directions - Compounded",
  "Uzbek Work and School - Compounded",
  "Uzbek Health and the Body - Compounded",
  "Uzbek Emotions and Feelings - Compounded",
  "Uzbek Nature and Weather - Compounded",
  "Uzbek Shopping and Money - Compounded",
  "Uzbek Friendship and Social Life - Compounded",
  "Uzbek Technology and Communication - Compounded",
  "Uzbek Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Uzbek Questions and Answers - Advanced",
  "Uzbek Commands and Requests - Advanced",
  "Uzbek Descriptions of People and Places - Advanced",
  "Uzbek Story I: The Clever Shepherd - Advanced",
  "Uzbek Story II: The Lost Key - Advanced",
  "Uzbek Story III: The New School - Advanced",
  "Uzbek Idioms and Proverbs - Advanced",
  "Uzbek Formal and Polite Registers - Advanced",
  "Uzbek Compound and Complex Sentences - Advanced",
  "Uzbek Conversation: At the Market - Advanced",
  "Uzbek Conversation: Meeting a Friend - Advanced",
  "Uzbek Conversation: Solving a Problem - Advanced",
  "Uzbek Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Uzbek Study — "+safe+"\n"
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
    demo:{kind:"uzbek-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-uzbek-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-uzbek',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
