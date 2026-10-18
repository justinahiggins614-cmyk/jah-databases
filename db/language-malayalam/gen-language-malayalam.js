(function(){'use strict';
/* JAH The Malayalam to English Database generator — jahdb-language-malayalam-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LMAL-";
var FIELDS=["Foundations","Core Vocabulary","Grammar Essentials","Everyday Themes","Grammar in Action","Stories and Idioms","Conversation and Registers","Mastery Reference"];
var TOPICS={
 "Foundations": [
  "Malayalam Language Overview - Foundations",
  "The Malayalam Writing System - Foundations",
  "Malayalam Pronunciation and Phonology - Foundations"
 ],
 "Core Vocabulary": [
  "Malayalam Core Nouns I - Core Vocabulary",
  "Malayalam Core Verbs I - Core Vocabulary",
  "Malayalam Adjectives and Adverbs - Core Vocabulary",
  "Malayalam Pronouns - Core Vocabulary",
  "Malayalam Numbers and Time - Core Vocabulary",
  "Malayalam Greetings and Everyday Phrases - Core Vocabulary"
 ],
 "Grammar Essentials": [
  "Malayalam Grammar Essentials - Grammar Essentials"
 ],
 "Everyday Themes": [
  "Malayalam Home and Family Sentences - Everyday Themes",
  "Malayalam Food and Cooking Sentences - Everyday Themes",
  "Malayalam Travel and Directions Sentences - Everyday Themes",
  "Malayalam Work and School Sentences - Everyday Themes",
  "Malayalam Health and Body Sentences - Everyday Themes",
  "Malayalam Emotions and Feelings Sentences - Everyday Themes",
  "Malayalam Nature and Weather Sentences - Everyday Themes",
  "Malayalam Shopping and Money Sentences - Everyday Themes",
  "Malayalam Friendship and Social Sentences - Everyday Themes",
  "Malayalam Technology and Communication Sentences - Everyday Themes"
 ],
 "Grammar in Action": [
  "Malayalam Verb Tenses in Sentences - Grammar in Action",
  "Malayalam Questions and Answers - Grammar in Action",
  "Malayalam Commands and Requests - Grammar in Action",
  "Malayalam Descriptions of People and Places - Grammar in Action"
 ],
 "Stories and Idioms": [
  "Malayalam Short Story I: A Simple Day - Stories and Idioms",
  "Malayalam Short Story II: The Journey - Stories and Idioms",
  "Malayalam Short Story III: Plans for Tomorrow - Stories and Idioms",
  "Malayalam Idioms and Proverbs - Stories and Idioms"
 ],
 "Conversation and Registers": [
  "Malayalam Formal and Polite Registers - Conversation and Registers",
  "Malayalam Compound and Complex Sentences - Conversation and Registers",
  "Malayalam Conversation: At the Market - Conversation and Registers",
  "Malayalam Conversation: Meeting a Friend - Conversation and Registers",
  "Malayalam Conversation: Solving a Problem - Conversation and Registers"
 ],
 "Mastery Reference": [
  "Malayalam Mastery Review and Full Reference - Mastery Reference"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Malayalam Language Study — "+safe+"\n"
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
    demo:{kind:"malayalam-language-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-malayalam-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-malayalam',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
