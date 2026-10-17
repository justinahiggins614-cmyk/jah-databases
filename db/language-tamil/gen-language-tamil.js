(function(){'use strict';
/* JAH Tamil Language Database generator — jahdb-language-tamil-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LTAM-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Tamil Language Overview - Foundations",
  "Tamil Script and Writing System - Foundations",
  "Tamil Pronunciation and Phonology - Foundations",
  "Tamil Core Nouns I - Foundations",
  "Tamil Core Verbs I - Foundations",
  "Tamil Adjectives and Adverbs - Foundations",
  "Tamil Pronouns - Foundations",
  "Tamil Numbers and Time - Foundations",
  "Tamil Greetings and Everyday Phrases - Foundations",
  "Tamil Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Tamil Home and Family Sentences - Compounded",
  "Tamil Food and Cooking Sentences - Compounded",
  "Tamil Travel and Directions Sentences - Compounded",
  "Tamil Work and School Sentences - Compounded",
  "Tamil Health and Body Sentences - Compounded",
  "Tamil Emotions and Feelings Sentences - Compounded",
  "Tamil Nature and Weather Sentences - Compounded",
  "Tamil Shopping and Money Sentences - Compounded",
  "Tamil Friendship and Social Life Sentences - Compounded",
  "Tamil Technology and Communication Sentences - Compounded",
  "Tamil Verb Tenses in Sentences - Compounded",
  "Tamil Questions and Answers - Compounded",
  "Tamil Commands and Requests - Compounded",
  "Tamil Descriptions of People and Places - Compounded"
 ],
 "Advanced": [
  "Tamil Story: A Simple Day - Advanced",
  "Tamil Story: A Journey in the Past - Advanced",
  "Tamil Story: Dreams of Tomorrow - Advanced",
  "Tamil Idioms and Proverbs - Advanced",
  "Tamil Formal and Polite Registers - Advanced",
  "Tamil Compound and Complex Sentences - Advanced",
  "Tamil Conversation: At the Market - Advanced",
  "Tamil Conversation: Meeting a Friend - Advanced",
  "Tamil Conversation: Solving a Problem - Advanced",
  "Tamil Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Tamil Language Study — "+safe+"\n"
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
    demo:{kind:"tamil-language-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-tamil-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-tamil',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
