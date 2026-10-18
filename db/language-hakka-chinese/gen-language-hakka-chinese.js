(function(){'use strict';
/* JAH The Hakka Chinese to English Database generator — jahdb-language-hakka-chinese-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LHAK-";
var FIELDS=["Foundations","Core Vocabulary","Grammar Essentials","Everyday Themes","Grammar in Action","Stories and Idioms","Conversation and Registers","Mastery Reference"];
var TOPICS={
 "Foundations": [
  "Hakka Chinese Language Overview - Foundations",
  "Hakka Chinese Writing System - Foundations",
  "Hakka Chinese Pronunciation and Tones - Foundations"
 ],
 "Core Vocabulary": [
  "Hakka Chinese Core Nouns I - Core Vocabulary",
  "Hakka Chinese Core Verbs I - Core Vocabulary",
  "Hakka Chinese Adjectives and Adverbs - Core Vocabulary",
  "Hakka Chinese Pronouns - Core Vocabulary",
  "Hakka Chinese Numbers and Time - Core Vocabulary",
  "Hakka Chinese Greetings and Everyday Phrases - Core Vocabulary"
 ],
 "Grammar Essentials": [
  "Hakka Chinese Grammar Essentials - Grammar Essentials"
 ],
 "Everyday Themes": [
  "Hakka Chinese Home and Family Sentences - Everyday Themes",
  "Hakka Chinese Food and Cooking Sentences - Everyday Themes",
  "Hakka Chinese Travel and Directions Sentences - Everyday Themes",
  "Hakka Chinese Work and School Sentences - Everyday Themes",
  "Hakka Chinese Health and Body Sentences - Everyday Themes",
  "Hakka Chinese Emotions and Feelings Sentences - Everyday Themes",
  "Hakka Chinese Nature and Weather Sentences - Everyday Themes",
  "Hakka Chinese Shopping and Money Sentences - Everyday Themes",
  "Hakka Chinese Friendship and Social Life Sentences - Everyday Themes",
  "Hakka Chinese Technology and Communication Sentences - Everyday Themes"
 ],
 "Grammar in Action": [
  "Hakka Chinese Verb Tenses in Sentences - Grammar in Action",
  "Hakka Chinese Questions and Answers - Grammar in Action",
  "Hakka Chinese Commands and Requests - Grammar in Action",
  "Hakka Chinese Descriptions of People and Places - Grammar in Action"
 ],
 "Stories and Idioms": [
  "Hakka Chinese Story I - All People Are Born Free - Stories and Idioms",
  "Hakka Chinese Story II - The Guest Family's Journey - Stories and Idioms",
  "Hakka Chinese Story III - Tomorrow's Hakka - Stories and Idioms",
  "Hakka Chinese Idioms and Proverbs - Stories and Idioms"
 ],
 "Conversation and Registers": [
  "Hakka Chinese Formal and Polite Registers - Conversation and Registers",
  "Hakka Chinese Compound and Complex Sentences - Conversation and Registers",
  "Hakka Chinese Conversation - At the Market - Conversation and Registers",
  "Hakka Chinese Conversation - Meeting a Friend - Conversation and Registers",
  "Hakka Chinese Conversation - Solving a Problem - Conversation and Registers"
 ],
 "Mastery Reference": [
  "Hakka Chinese Mastery Review and Full Reference - Mastery Reference"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hakka Chinese Language Study — "+safe+"\n"
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
    demo:{kind:"hakka-chinese-language-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-hakka-chinese-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-hakka-chinese',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
