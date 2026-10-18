(function(){'use strict';
/* JAH The Catalan Language Database generator — jahdb-language-catalan-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LCAT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Catalan Language Overview - Foundations",
  "Catalan Writing System and Alphabet - Foundations",
  "Catalan Pronunciation and Phonology - Foundations",
  "Catalan Core Nouns I - Foundations",
  "Catalan Core Verbs I - Foundations",
  "Catalan Adjectives and Adverbs - Foundations",
  "Catalan Pronouns - Foundations",
  "Catalan Numbers and Time - Foundations",
  "Catalan Greetings and Everyday Phrases - Foundations",
  "Catalan Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Catalan at Home and with Family - Compounded",
  "Catalan Food and Cooking - Compounded",
  "Catalan Travel and Directions - Compounded",
  "Catalan Work and School - Compounded",
  "Catalan Health and the Body - Compounded",
  "Catalan Emotions and Feelings - Compounded",
  "Catalan Nature and Weather - Compounded",
  "Catalan Shopping and Money - Compounded",
  "Catalan Friendship and Social Life - Compounded",
  "Catalan Technology and Communication - Compounded",
  "Catalan Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Catalan Questions and Answers - Advanced",
  "Catalan Commands and Requests - Advanced",
  "Catalan Descriptions of People and Places - Advanced",
  "Catalan Story I: The Lost Key - Advanced",
  "Catalan Story II: The Little Bird - Advanced",
  "Catalan Story III: The Market Day - Advanced",
  "Catalan Idioms and Proverbs - Advanced",
  "Catalan Formal and Polite Registers - Advanced",
  "Catalan Compound and Complex Sentences - Advanced",
  "Catalan Conversation: At the Market - Advanced",
  "Catalan Conversation: Meeting a Friend - Advanced",
  "Catalan Conversation: Solving a Problem - Advanced",
  "Catalan Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Catalan Study — "+safe+"\n"
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
    demo:{kind:"catalan-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-catalan-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-catalan',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
