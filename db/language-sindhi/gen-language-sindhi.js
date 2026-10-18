(function(){'use strict';
/* JAH The Sindhi to English Database generator — jahdb-language-sindhi-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LSND-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Sindhi Language Overview - Foundations",
  "Sindhi Writing System and Alphabet - Foundations",
  "Sindhi Pronunciation and Phonology - Foundations",
  "Sindhi Core Nouns I - Foundations",
  "Sindhi Core Verbs I - Foundations",
  "Sindhi Adjectives and Adverbs - Foundations",
  "Sindhi Pronouns - Foundations",
  "Sindhi Numbers and Time - Foundations",
  "Sindhi Greetings and Everyday Phrases - Foundations",
  "Sindhi Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Sindhi at Home and with Family - Compounded",
  "Sindhi Food and Cooking - Compounded",
  "Sindhi Travel and Directions - Compounded",
  "Sindhi Work and School - Compounded",
  "Sindhi Health and the Body - Compounded",
  "Sindhi Emotions and Feelings - Compounded",
  "Sindhi Nature and Weather - Compounded",
  "Sindhi Shopping and Money - Compounded",
  "Sindhi Friendship and Social Life - Compounded",
  "Sindhi Technology and Communication - Compounded",
  "Sindhi Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Sindhi Questions and Answers - Advanced",
  "Sindhi Commands and Requests - Advanced",
  "Sindhi Descriptions of People and Places - Advanced",
  "Sindhi Story I: The Clever Herd Boy - Advanced",
  "Sindhi Story II: The Lost Key - Advanced",
  "Sindhi Story III: The New School - Advanced",
  "Sindhi Idioms and Proverbs - Advanced",
  "Sindhi Formal and Polite Registers - Advanced",
  "Sindhi Compound and Complex Sentences - Advanced",
  "Sindhi Conversation: At the Market - Advanced",
  "Sindhi Conversation: Meeting a Friend - Advanced",
  "Sindhi Conversation: Solving a Problem - Advanced",
  "Sindhi Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Sindhi Study — "+safe+"\n"
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
    demo:{kind:"sindhi-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-sindhi-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-sindhi',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
