(function(){'use strict';
/* JAH The Yoruba to English Database generator — jahdb-language-yoruba-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LYOR-";
var FIELDS=["Foundations","Core Vocabulary","Grammar Essentials","Everyday Themes","Grammar in Action","Stories and Idioms","Conversation and Registers","Mastery Reference"];
var TOPICS={
 "Foundations": [
  "Yoruba Language Overview - Foundations",
  "The Yoruba Writing System - Foundations",
  "Yoruba Pronunciation and Phonology - Foundations"
 ],
 "Core Vocabulary": [
  "Core Yoruba Nouns I - Core Vocabulary",
  "Core Yoruba Verbs I - Core Vocabulary",
  "Yoruba Adjectives and Adverbs - Core Vocabulary",
  "Yoruba Pronouns - Core Vocabulary",
  "Yoruba Numbers and Time - Core Vocabulary",
  "Yoruba Greetings and Everyday Phrases - Core Vocabulary"
 ],
 "Grammar Essentials": [
  "Yoruba Grammar Essentials - Grammar Essentials"
 ],
 "Everyday Themes": [
  "Home and Family Sentences - Everyday Themes",
  "Food and Cooking Sentences - Everyday Themes",
  "Travel and Directions Sentences - Everyday Themes",
  "Work and School Sentences - Everyday Themes",
  "Health and Body Sentences - Everyday Themes",
  "Emotions and Feelings Sentences - Everyday Themes",
  "Nature and Weather Sentences - Everyday Themes",
  "Shopping and Money Sentences - Everyday Themes",
  "Friendship and Social Life Sentences - Everyday Themes",
  "Technology and Communication Sentences - Everyday Themes"
 ],
 "Grammar in Action": [
  "Yoruba Verb Tenses in Sentences - Grammar in Action",
  "Yoruba Questions and Answers - Grammar in Action",
  "Yoruba Commands and Requests - Grammar in Action",
  "Describing People and Places - Grammar in Action"
 ],
 "Stories and Idioms": [
  "Story I: The Market Day - Stories and Idioms",
  "Story II: The Lost Goat - Stories and Idioms",
  "Story III: The Journey Tomorrow - Stories and Idioms",
  "Yoruba Idioms and Proverbs - Stories and Idioms"
 ],
 "Conversation and Registers": [
  "Formal and Polite Registers - Conversation and Registers",
  "Compound and Complex Sentences - Conversation and Registers",
  "Conversation: At the Market - Conversation and Registers",
  "Conversation: Meeting a Friend - Conversation and Registers",
  "Conversation: Solving a Problem - Conversation and Registers"
 ],
 "Mastery Reference": [
  "Yoruba Mastery Review and Full Reference - Mastery Reference"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Yoruba Language Study — "+safe+"\n"
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
    demo:{kind:"yoruba-language-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-yoruba-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-yoruba',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
