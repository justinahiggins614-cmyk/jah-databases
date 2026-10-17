(function(){'use strict';
/* JAH The Hausa to English Signature Database generator — jahdb-language-hausa-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LHAUS-";
var FIELDS=["Foundations","Core Vocabulary","Grammar Essentials","Everyday Themes","Grammar in Action","Stories and Idioms","Conversation and Registers","Mastery Reference"];
var TOPICS={
 "Foundations": [
  "Hausa Language Overview (Signature Edition) - Foundations",
  "The Hausa Writing System (Signature Edition) - Foundations",
  "Hausa Pronunciation and Phonology (Signature Edition) - Foundations"
 ],
 "Core Vocabulary": [
  "Core Hausa Nouns I (Signature Edition) - Core Vocabulary",
  "Core Hausa Verbs I (Signature Edition) - Core Vocabulary",
  "Hausa Adjectives and Adverbs (Signature Edition) - Core Vocabulary",
  "Hausa Pronouns (Signature Edition) - Core Vocabulary",
  "Hausa Numbers and Time (Signature Edition) - Core Vocabulary",
  "Hausa Greetings and Everyday Phrases (Signature Edition) - Core Vocabulary"
 ],
 "Grammar Essentials": [
  "Hausa Grammar Essentials (Signature Edition) - Grammar Essentials"
 ],
 "Everyday Themes": [
  "Hausa Home and Family Sentences (Signature Edition) - Everyday Themes",
  "Hausa Food and Cooking Sentences (Signature Edition) - Everyday Themes",
  "Hausa Travel and Directions Sentences (Signature Edition) - Everyday Themes",
  "Hausa Work and School Sentences (Signature Edition) - Everyday Themes",
  "Hausa Health and Body Sentences (Signature Edition) - Everyday Themes",
  "Hausa Emotions and Feelings Sentences (Signature Edition) - Everyday Themes",
  "Hausa Nature and Weather Sentences (Signature Edition) - Everyday Themes",
  "Hausa Shopping and Money Sentences (Signature Edition) - Everyday Themes",
  "Hausa Friendship and Social Life Sentences (Signature Edition) - Everyday Themes",
  "Hausa Technology and Communication Sentences (Signature Edition) - Everyday Themes"
 ],
 "Grammar in Action": [
  "Hausa Verb Tenses in Sentences (Signature Edition) - Grammar in Action",
  "Hausa Questions and Answers (Signature Edition) - Grammar in Action",
  "Hausa Commands and Requests (Signature Edition) - Grammar in Action",
  "Hausa Descriptions of People and Places (Signature Edition) - Grammar in Action"
 ],
 "Stories and Idioms": [
  "Hausa Short Story I: A Simple Day (Signature Edition) - Stories and Idioms",
  "Hausa Short Story II: A Journey in the Past (Signature Edition) - Stories and Idioms",
  "Hausa Short Story III: Plans for Tomorrow (Signature Edition) - Stories and Idioms",
  "Hausa Idioms and Proverbs (Signature Edition) - Stories and Idioms"
 ],
 "Conversation and Registers": [
  "Hausa Formal and Polite Registers (Signature Edition) - Conversation and Registers",
  "Hausa Compound and Complex Sentences (Signature Edition) - Conversation and Registers",
  "Hausa Conversation: At the Market (Signature Edition) - Conversation and Registers",
  "Hausa Conversation: Meeting a Friend (Signature Edition) - Conversation and Registers",
  "Hausa Conversation: Solving a Problem (Signature Edition) - Conversation and Registers"
 ],
 "Mastery Reference": [
  "Hausa Mastery Review and Full Reference (Signature Edition) - Mastery Reference"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hausa Language Study — "+safe+"\n"
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
    demo:{kind:"hausa-language-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-hausa-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-hausa-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
