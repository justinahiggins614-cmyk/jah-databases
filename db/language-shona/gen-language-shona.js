(function(){'use strict';
/* JAH The Shona Language Database generator — jahdb-language-shona-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LSNA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Shona Language Overview - Foundations",
  "Shona Writing System and Alphabet - Foundations",
  "Shona Pronunciation and Phonology - Foundations",
  "Shona Core Nouns I - Foundations",
  "Shona Core Verbs I - Foundations",
  "Shona Adjectives and Adverbs - Foundations",
  "Shona Pronouns - Foundations",
  "Shona Numbers and Time - Foundations",
  "Shona Greetings and Everyday Phrases - Foundations",
  "Shona Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Shona at Home and with Family - Compounded",
  "Shona Food and Cooking - Compounded",
  "Shona Travel and Directions - Compounded",
  "Shona Work and School - Compounded",
  "Shona Health and the Body - Compounded",
  "Shona Emotions and Feelings - Compounded",
  "Shona Nature and Weather - Compounded",
  "Shona Shopping and Money - Compounded",
  "Shona Friendship and Social Life - Compounded",
  "Shona Technology and Communication - Compounded",
  "Shona Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Shona Questions and Answers - Advanced",
  "Shona Commands and Requests - Advanced",
  "Shona Descriptions of People and Places - Advanced",
  "Shona Story I: Tsuro and the Elephant - Advanced",
  "Shona Story II: Tsuro and the Clever Answer - Advanced",
  "Shona Story III: The New School in Harare - Advanced",
  "Shona Idioms and Proverbs - Advanced",
  "Shona Formal and Polite Registers - Advanced",
  "Shona Compound and Complex Sentences - Advanced",
  "Shona Conversation: At the Market - Advanced",
  "Shona Conversation: Meeting a Friend - Advanced",
  "Shona Conversation: Solving a Problem - Advanced",
  "Shona Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Shona Study — "+safe+"\n"
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
    demo:{kind:"shona-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-shona-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-shona',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
