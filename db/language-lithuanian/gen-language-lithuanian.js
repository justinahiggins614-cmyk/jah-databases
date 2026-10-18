(function(){'use strict';
/* JAH The Lithuanian Language Database generator — jahdb-language-lithuanian-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LLIT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Lithuanian Language Overview - Foundations",
  "Lithuanian Writing System and Alphabet - Foundations",
  "Lithuanian Pronunciation and Phonology - Foundations",
  "Lithuanian Core Nouns I - Foundations",
  "Lithuanian Core Verbs I - Foundations",
  "Lithuanian Adjectives and Adverbs - Foundations",
  "Lithuanian Pronouns - Foundations",
  "Lithuanian Numbers and Time - Foundations",
  "Lithuanian Greetings and Everyday Phrases - Foundations",
  "Lithuanian Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Lithuanian at Home and with Family - Compounded",
  "Lithuanian Food and Cooking - Compounded",
  "Lithuanian Travel and Directions - Compounded",
  "Lithuanian Work and School - Compounded",
  "Lithuanian Health and the Body - Compounded",
  "Lithuanian Emotions and Feelings - Compounded",
  "Lithuanian Nature and Weather - Compounded",
  "Lithuanian Shopping and Money - Compounded",
  "Lithuanian Friendship and Social Life - Compounded",
  "Lithuanian Technology and Communication - Compounded",
  "Lithuanian Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Lithuanian Questions and Answers - Advanced",
  "Lithuanian Commands and Requests - Advanced",
  "Lithuanian Descriptions of People and Places - Advanced",
  "Lithuanian Story I: The Lost Key - Advanced",
  "Lithuanian Story II: The Little Bird - Advanced",
  "Lithuanian Story III: The Market Day - Advanced",
  "Lithuanian Idioms and Proverbs - Advanced",
  "Lithuanian Formal and Polite Registers - Advanced",
  "Lithuanian Compound and Complex Sentences - Advanced",
  "Lithuanian Conversation: At the Market - Advanced",
  "Lithuanian Conversation: Meeting a Friend - Advanced",
  "Lithuanian Conversation: Solving a Problem - Advanced",
  "Lithuanian Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Lithuanian Study — "+safe+"\n"
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
    demo:{kind:"lithuanian-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-lithuanian-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-lithuanian',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
