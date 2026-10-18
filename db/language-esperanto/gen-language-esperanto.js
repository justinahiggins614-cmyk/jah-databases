(function(){'use strict';
/* JAH The Esperanto to English Database generator — jahdb-language-esperanto-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LESP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Esperanto Language Overview - Foundations",
  "Esperanto Writing System and Alphabet - Foundations",
  "Esperanto Pronunciation and Phonology - Foundations",
  "Esperanto Core Nouns I - Foundations",
  "Esperanto Core Verbs I - Foundations",
  "Esperanto Adjectives and Adverbs - Foundations",
  "Esperanto Pronouns - Foundations",
  "Esperanto Numbers and Time - Foundations",
  "Esperanto Greetings and Everyday Phrases - Foundations",
  "Esperanto Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Esperanto at Home and with Family - Compounded",
  "Esperanto Food and Cooking - Compounded",
  "Esperanto Travel and Directions - Compounded",
  "Esperanto Work and School - Compounded",
  "Esperanto Health and the Body - Compounded",
  "Esperanto Emotions and Feelings - Compounded",
  "Esperanto Nature and Weather - Compounded",
  "Esperanto Shopping and Money - Compounded",
  "Esperanto Friendship and Social Life - Compounded",
  "Esperanto Technology and Communication - Compounded",
  "Esperanto Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Esperanto Questions and Answers - Advanced",
  "Esperanto Commands and Requests - Advanced",
  "Esperanto Descriptions of People and Places - Advanced",
  "Esperanto Story I: The Clever Shepherd - Advanced",
  "Esperanto Story II: The Lost Key - Advanced",
  "Esperanto Story III: The New School - Advanced",
  "Esperanto Idioms and Proverbs - Advanced",
  "Esperanto Formal and Polite Registers - Advanced",
  "Esperanto Compound and Complex Sentences - Advanced",
  "Esperanto Conversation: At the Market - Advanced",
  "Esperanto Conversation: Meeting a Friend - Advanced",
  "Esperanto Conversation: Solving a Problem - Advanced",
  "Esperanto Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Esperanto Study — "+safe+"\n"
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
    demo:{kind:"esperanto-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-esperanto-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-esperanto',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
