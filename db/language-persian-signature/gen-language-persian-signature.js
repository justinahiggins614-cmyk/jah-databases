(function(){'use strict';
/* JAH Persian Language Signature Database generator — jahdb-language-persian-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LFASS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Persian Language Overview (Signature Edition) - Language overview",
  "Persian Writing System (Signature Edition) - Language overview",
  "Persian Pronunciation and Phonology (Signature Edition) - Language overview",
  "Persian Core Nouns (Signature Edition) - Core vocabulary",
  "Persian Core Verbs (Signature Edition) - Core vocabulary",
  "Persian Adjectives and Adverbs (Signature Edition) - Core vocabulary",
  "Persian Pronouns (Signature Edition) - Grammar basics",
  "Persian Numbers and Time (Signature Edition) - Grammar basics",
  "Persian Greetings and Everyday Phrases (Signature Edition) - Grammar basics",
  "Persian Grammar Essentials (Signature Edition) - Grammar basics"
 ],
 "Compounded": [
  "Persian Home and Family Sentences (Signature Edition) - Everyday sentences",
  "Persian Food and Cooking Sentences (Signature Edition) - Everyday sentences",
  "Persian Travel and Directions Sentences (Signature Edition) - Everyday sentences",
  "Persian Work and School Sentences (Signature Edition) - Everyday sentences",
  "Persian Health and Body Sentences (Signature Edition) - Everyday sentences",
  "Persian Emotions and Feelings Sentences (Signature Edition) - Everyday sentences",
  "Persian Nature and Weather Sentences (Signature Edition) - Everyday sentences",
  "Persian Shopping and Money Sentences (Signature Edition) - Everyday sentences",
  "Persian Friendship and Social Life Sentences (Signature Edition) - Everyday sentences",
  "Persian Technology and Communication Sentences (Signature Edition) - Everyday sentences",
  "Persian Verb Tenses in Sentences (Signature Edition) - Grammar in use",
  "Persian Questions and Answers (Signature Edition) - Grammar in use",
  "Persian Commands and Requests (Signature Edition) - Grammar in use",
  "Persian Descriptions of People and Places (Signature Edition) - Grammar in use"
 ],
 "Advanced": [
  "Persian Short Story One (Signature Edition) - Stories",
  "Persian Short Story Two (Signature Edition) - Stories",
  "Persian Short Story Three (Signature Edition) - Stories",
  "Persian Idioms and Proverbs (Signature Edition) - Mastery",
  "Persian Formal and Polite Registers (Signature Edition) - Mastery",
  "Persian Compound and Complex Sentences (Signature Edition) - Mastery",
  "Persian Conversation at the Market (Signature Edition) - Conversations",
  "Persian Conversation Meeting a Friend (Signature Edition) - Conversations",
  "Persian Conversation Solving a Problem (Signature Edition) - Conversations",
  "Persian Mastery Review and Full Reference (Signature Edition) - Mastery"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Persian Lesson — "+safe+"\n"
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
    demo:{kind:"persian-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-persian-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-persian-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
