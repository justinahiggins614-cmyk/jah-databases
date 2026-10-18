(function(){'use strict';
/* JAH The Indonesian to English Database generator — jahdb-language-indonesian-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LIND-";
var FIELDS=["Foundations","Core Vocabulary","Grammar Essentials","Everyday Themes","Grammar in Action","Stories and Idioms","Conversation and Registers","Mastery Reference"];
var TOPICS={
 "Foundations": [
  "Indonesian Language Overview - Foundations",
  "The Indonesian Writing System - Foundations",
  "Indonesian Pronunciation and Phonology - Foundations"
 ],
 "Core Vocabulary": [
  "Core Nouns I - 25 Essential Nouns - Core Vocabulary",
  "Core Verbs I - 25 Essential Verbs - Core Vocabulary",
  "Adjectives and Adverbs - 25 Plus 15 - Core Vocabulary",
  "Pronouns - Full Paradigms - Core Vocabulary",
  "Numbers and Time - 1 to 100 and Beyond - Core Vocabulary",
  "Greetings and Everyday Phrases - 30 Phrases - Core Vocabulary"
 ],
 "Grammar Essentials": [
  "Grammar Essentials - Ten Load-Bearing Rules - Grammar Essentials"
 ],
 "Everyday Themes": [
  "Home and Family - 20 Sentences - Everyday Themes",
  "Food and Cooking - 20 Sentences - Everyday Themes",
  "Travel and Directions - 20 Sentences - Everyday Themes",
  "Work and School - 20 Sentences - Everyday Themes",
  "Health and Body - 20 Sentences - Everyday Themes",
  "Emotions and Feelings - 20 Sentences - Everyday Themes",
  "Nature and Weather - 20 Sentences - Everyday Themes",
  "Shopping and Money - 20 Sentences - Everyday Themes",
  "Friendship and Social Life - 20 Sentences - Everyday Themes",
  "Technology and Communication - 20 Sentences - Everyday Themes"
 ],
 "Grammar in Action": [
  "Verb Tenses in Sentences - Past, Present, Future - Grammar in Action",
  "Questions and Answers - 20 Pairs - Grammar in Action",
  "Commands and Requests - 20 Sentences - Grammar in Action",
  "Descriptions - 20 Sentences on People and Places - Grammar in Action"
 ],
 "Stories and Idioms": [
  "Story I - A Simple Ten-Sentence Story - Stories and Idioms",
  "Story II - A Ten-Sentence Story in the Past - Stories and Idioms",
  "Story III - A Ten-Sentence Story in the Future - Stories and Idioms",
  "Idioms and Proverbs - 20 Sayings - Stories and Idioms"
 ],
 "Conversation and Registers": [
  "Formal and Polite Registers - 15 Pairs - Conversation and Registers",
  "Compound and Complex Sentences - 15 Parsed - Conversation and Registers",
  "Conversation - At the Market (20 Lines) - Conversation and Registers",
  "Conversation - Meeting a Friend (20 Lines) - Conversation and Registers",
  "Conversation - Solving a Problem (20 Lines) - Conversation and Registers"
 ],
 "Mastery Reference": [
  "Mastery Review - The Whole Database in One Reference - Mastery Reference"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Indonesian Language Study — "+safe+"\n"
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
    demo:{kind:"indonesian-language-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-indonesian-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-indonesian',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
