(function(){'use strict';
/* JAH The English to English Signature Database generator — jahdb-language-english-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LENGS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Language Overview: English (Signature Edition) - Foundations",
  "The English Writing System (Signature Edition) - Foundations",
  "English Pronunciation and Phonology (Signature Edition) - Foundations",
  "Core Nouns I: People, Places, and Things (Signature Edition) - Foundations",
  "Core Verbs I: Essential Action Words (Signature Edition) - Foundations",
  "Adjectives and Adverbs (Signature Edition) - Foundations",
  "Pronouns (Signature Edition) - Foundations",
  "Numbers and Time (Signature Edition) - Foundations",
  "Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Home and Family Sentences (Signature Edition) - Compounded",
  "Food and Cooking Sentences (Signature Edition) - Compounded",
  "Travel and Directions Sentences (Signature Edition) - Compounded",
  "Work and School Sentences (Signature Edition) - Compounded",
  "Health and Body Sentences (Signature Edition) - Compounded",
  "Emotions and Feelings Sentences (Signature Edition) - Compounded",
  "Nature and Weather Sentences (Signature Edition) - Compounded",
  "Shopping and Money Sentences (Signature Edition) - Compounded",
  "Friendship and Social Life Sentences (Signature Edition) - Compounded",
  "Technology and Communication Sentences (Signature Edition) - Compounded",
  "Verb Tenses in Sentences (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Questions and Answers (Signature Edition) - Advanced",
  "Commands and Requests (Signature Edition) - Advanced",
  "Descriptions of People and Places (Signature Edition) - Advanced",
  "Short Story I: A Simple Day (Signature Edition) - Advanced",
  "Short Story II: The Trip Last Summer (Signature Edition) - Advanced",
  "Short Story III: Plans for Tomorrow (Signature Edition) - Advanced",
  "Idioms and Proverbs (Signature Edition) - Advanced",
  "Formal and Polite Registers (Signature Edition) - Advanced",
  "Compound and Complex Sentences (Signature Edition) - Advanced",
  "Conversation: At the Market (Signature Edition) - Advanced",
  "Conversation: Meeting a Friend (Signature Edition) - Advanced",
  "Conversation: Solving a Problem (Signature Edition) - Advanced",
  "Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# English Lesson — "+safe+"\n"
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
    demo:{kind:"english-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-english-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-english-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
