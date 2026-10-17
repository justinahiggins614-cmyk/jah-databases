(function(){'use strict';
/* JAH The Bengali to English Signature Database generator — jahdb-language-bengali-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LBENS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Bengali Language Overview (Signature Edition) - Foundations",
  "Bengali Writing System (Signature Edition) - Foundations",
  "Bengali Pronunciation and Phonology (Signature Edition) - Foundations",
  "Bengali Core Nouns I (Signature Edition) - Foundations",
  "Bengali Core Verbs I (Signature Edition) - Foundations",
  "Bengali Adjectives and Adverbs (Signature Edition) - Foundations",
  "Bengali Pronouns (Signature Edition) - Foundations",
  "Bengali Numbers and Time (Signature Edition) - Foundations",
  "Bengali Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Bengali Grammar Essentials (Signature Edition) - Foundations",
  "Bengali Home and Family Sentences (Signature Edition) - Foundations",
  "Bengali Food and Cooking Sentences (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Bengali Travel and Directions Sentences (Signature Edition) - Compounded",
  "Bengali Work and School Sentences (Signature Edition) - Compounded",
  "Bengali Health and Body Sentences (Signature Edition) - Compounded",
  "Bengali Emotions and Feelings Sentences (Signature Edition) - Compounded",
  "Bengali Nature and Weather Sentences (Signature Edition) - Compounded",
  "Bengali Shopping and Money Sentences (Signature Edition) - Compounded",
  "Bengali Friendship and Social Life Sentences (Signature Edition) - Compounded",
  "Bengali Technology and Communication Sentences (Signature Edition) - Compounded",
  "Bengali Verb Tenses in Sentences (Signature Edition) - Compounded",
  "Bengali Questions and Answers (Signature Edition) - Compounded",
  "Bengali Commands and Requests (Signature Edition) - Compounded",
  "Bengali Descriptions of People and Places (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Bengali Story I: A Day in the Village (Signature Edition) - Advanced",
  "Bengali Story II: The River Journey (Signature Edition) - Advanced",
  "Bengali Story III: The Dream Shop (Signature Edition) - Advanced",
  "Bengali Idioms and Proverbs (Signature Edition) - Advanced",
  "Bengali Formal and Polite Registers (Signature Edition) - Advanced",
  "Bengali Compound and Complex Sentences (Signature Edition) - Advanced",
  "Bengali Conversation: At the Market (Signature Edition) - Advanced",
  "Bengali Conversation: Meeting a Friend (Signature Edition) - Advanced",
  "Bengali Conversation: Solving a Problem (Signature Edition) - Advanced",
  "Bengali Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Lesson — "+safe+"\n"
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
    demo:{kind:"language-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-bengali-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-bengali-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
