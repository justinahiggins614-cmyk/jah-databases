(function(){'use strict';
/* JAH The Fula Language Database generator — jahdb-language-fula-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LFUL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Fula Language Overview - Foundations",
  "Fula Writing System and Alphabet - Foundations",
  "Fula Pronunciation and Phonology - Foundations",
  "Fula Core Nouns I - Foundations",
  "Fula Core Verbs I - Foundations",
  "Fula Adjectives and Adverbs - Foundations",
  "Fula Pronouns - Foundations",
  "Fula Numbers and Time - Foundations",
  "Fula Greetings and Everyday Phrases - Foundations",
  "Fula Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Fula at Home and with Family - Compounded",
  "Fula Food and Cooking - Compounded",
  "Fula Travel and Directions - Compounded",
  "Fula Work and School - Compounded",
  "Fula Health and the Body - Compounded",
  "Fula Emotions and Feelings - Compounded",
  "Fula Nature and Weather - Compounded",
  "Fula Shopping and Money - Compounded",
  "Fula Friendship and Social Life - Compounded",
  "Fula Technology and Communication - Compounded",
  "Fula Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Fula Questions and Answers - Advanced",
  "Fula Commands and Requests - Advanced",
  "Fula Descriptions of People and Places - Advanced",
  "Fula Story I: The Lost Key - Advanced",
  "Fula Story II: The Little Bird - Advanced",
  "Fula Story III: The Market Day - Advanced",
  "Fula Idioms and Proverbs - Advanced",
  "Fula Formal and Polite Registers - Advanced",
  "Fula Compound and Complex Sentences - Advanced",
  "Fula Conversation: At the Market - Advanced",
  "Fula Conversation: Meeting a Friend - Advanced",
  "Fula Conversation: Solving a Problem - Advanced",
  "Fula Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Fula Study — "+safe+"\n"
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
    demo:{kind:"fula-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-fula-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-fula',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
