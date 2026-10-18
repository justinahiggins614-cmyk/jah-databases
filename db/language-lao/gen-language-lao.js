(function(){'use strict';
/* JAH The Lao Language Database generator — jahdb-language-lao-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LLAO-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Lao Language Overview - Foundations",
  "Lao Writing System and Alphabet - Foundations",
  "Lao Pronunciation and Phonology - Foundations",
  "Lao Core Nouns I - Foundations",
  "Lao Core Verbs I - Foundations",
  "Lao Adjectives and Adverbs - Foundations",
  "Lao Pronouns - Foundations",
  "Lao Numbers and Time - Foundations",
  "Lao Greetings and Everyday Phrases - Foundations",
  "Lao Grammar Essentials - Foundations",
 ],
 "Compounded": [
  "Lao at Home and Family - Compounded",
  "Lao Food and Cooking - Compounded",
  "Lao Travel and Directions - Compounded",
  "Lao Work and School - Compounded",
  "Lao Health and the Body - Compounded",
  "Lao Emotions and Feelings - Compounded",
  "Lao Nature and Weather - Compounded",
  "Lao Shopping and Money - Compounded",
  "Lao Friendship and Social Life - Compounded",
  "Lao Technology and Communication - Compounded",
  "Lao Verb Tenses in Sentences - Compounded",
 ],
 "Advanced": [
  "Lao Questions and Answers - Advanced",
  "Lao Commands and Requests - Advanced",
  "Lao Descriptions of People and Places - Advanced",
  "Lao Story I: The Boy and the Goat - Advanced",
  "Lao Story II: The Rainy Day - Advanced",
  "Lao Story III: The Market Trip - Advanced",
  "Lao Idioms and Proverbs - Advanced",
  "Lao Formal and Polite Registers - Advanced",
  "Lao Compound and Complex Sentences - Advanced",
  "Lao Conversation: At the Market - Advanced",
  "Lao Conversation: Meeting a Friend - Advanced",
  "Lao Conversation: Solving a Problem - Advanced",
  "Lao Mastery Review and Full Reference - Advanced",
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Lao Study — "+safe+"\n"
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
    demo:{kind:"lao-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-lao-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-lao',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
