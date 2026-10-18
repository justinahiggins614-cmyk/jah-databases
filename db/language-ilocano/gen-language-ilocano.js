(function(){'use strict';
/* JAH The Ilocano Language Database generator — jahdb-language-ilocano-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LILO-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Ilocano Language Overview - Foundations",
  "Ilocano Writing System and Alphabet - Foundations",
  "Ilocano Pronunciation and Phonology - Foundations",
  "Ilocano Core Nouns I - Foundations",
  "Ilocano Core Verbs I - Foundations",
  "Ilocano Adjectives and Adverbs - Foundations",
  "Ilocano Pronouns - Foundations",
  "Ilocano Numbers and Time - Foundations",
  "Ilocano Greetings and Everyday Phrases - Foundations",
  "Ilocano Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Ilocano At Home and with Family - Compounded",
  "Ilocano Food and Cooking - Compounded",
  "Ilocano Travel and Directions - Compounded",
  "Ilocano Work and School - Compounded",
  "Ilocano Health and the Body - Compounded",
  "Ilocano Emotions and Feelings - Compounded",
  "Ilocano Nature and Weather - Compounded",
  "Ilocano Shopping and Money - Compounded",
  "Ilocano Friendship and Social Life - Compounded",
  "Ilocano Technology and Communication - Compounded",
  "Ilocano Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Ilocano Questions and Answers - Advanced",
  "Ilocano Commands and Requests - Advanced",
  "Ilocano Descriptions of People and Places - Advanced",
  "Ilocano Story I: Ti Ubing ken ti Aso - Advanced",
  "Ilocano Story II: Ti Mannalon - Advanced",
  "Ilocano Story III: Ti Baro nga Eskwela - Advanced",
  "Ilocano Idioms and Proverbs - Advanced",
  "Ilocano Formal and Polite Registers - Advanced",
  "Ilocano Compound and Complex Sentences - Advanced",
  "Ilocano Conversation: At the Market - Advanced",
  "Ilocano Conversation: Meeting a Friend - Advanced",
  "Ilocano Conversation: Solving a Problem - Advanced",
  "Ilocano Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Ilocano Study — "+safe+"\n"
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
    demo:{kind:"language-ilocano-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-ilocano-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-ilocano',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
