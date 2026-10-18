(function(){'use strict';
/* JAH The Awadhi Language Database generator — jahdb-language-awadhi-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LAWA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Awadhi Language Overview - Foundations",
  "Awadhi Writing System and Alphabet - Foundations",
  "Awadhi Pronunciation and Phonology - Foundations",
  "Awadhi Core Nouns I - Foundations",
  "Awadhi Core Verbs I - Foundations",
  "Awadhi Adjectives and Adverbs - Foundations",
  "Awadhi Pronouns - Foundations",
  "Awadhi Numbers and Time - Foundations",
  "Awadhi Greetings and Everyday Phrases - Foundations",
  "Awadhi Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Awadhi at Home and with Family - Compounded",
  "Awadhi Food and Cooking - Compounded",
  "Awadhi Travel and Directions - Compounded",
  "Awadhi Work and School - Compounded",
  "Awadhi Health and the Body - Compounded",
  "Awadhi Emotions and Feelings - Compounded",
  "Awadhi Nature and Weather - Compounded",
  "Awadhi Shopping and Money - Compounded",
  "Awadhi Friendship and Social Life - Compounded",
  "Awadhi Technology and Communication - Compounded",
  "Awadhi Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Awadhi Questions and Answers - Advanced",
  "Awadhi Commands and Requests - Advanced",
  "Awadhi Descriptions of People and Places - Advanced",
  "Awadhi Story I: The Lost Key - Advanced",
  "Awadhi Story II: The Little Bird - Advanced",
  "Awadhi Story III: The Market Day - Advanced",
  "Awadhi Idioms and Proverbs - Advanced",
  "Awadhi Formal and Polite Registers - Advanced",
  "Awadhi Compound and Complex Sentences - Advanced",
  "Awadhi Conversation: At the Market - Advanced",
  "Awadhi Conversation: Meeting a Friend - Advanced",
  "Awadhi Conversation: Solving a Problem - Advanced",
  "Awadhi Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Awadhi Study — "+safe+"\n"
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
    demo:{kind:"awadhi-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-awadhi-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-awadhi',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
