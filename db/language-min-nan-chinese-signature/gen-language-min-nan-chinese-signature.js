(function(){'use strict';
/* JAH Min Nan Chinese Language Signature Database generator — jahdb-language-min-nan-chinese-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LNANS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Min Nan Chinese Language Overview (Signature Edition) - Foundations",
  "Min Nan Chinese Writing System (Signature Edition) - Foundations",
  "Min Nan Chinese Pronunciation and Phonology (Signature Edition) - Foundations",
  "Min Nan Chinese Core Nouns I (Signature Edition) - Foundations",
  "Min Nan Chinese Core Verbs I (Signature Edition) - Foundations",
  "Min Nan Chinese Adjectives and Adverbs (Signature Edition) - Foundations",
  "Min Nan Chinese Pronouns (Signature Edition) - Foundations",
  "Min Nan Chinese Numbers and Time (Signature Edition) - Foundations",
  "Min Nan Chinese Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Min Nan Chinese Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Min Nan Chinese Home and Family Sentences (Signature Edition) - Compounded",
  "Min Nan Chinese Food and Cooking Sentences (Signature Edition) - Compounded",
  "Min Nan Chinese Travel and Directions Sentences (Signature Edition) - Compounded",
  "Min Nan Chinese Work and School Sentences (Signature Edition) - Compounded",
  "Min Nan Chinese Health and Body Sentences (Signature Edition) - Compounded",
  "Min Nan Chinese Emotions and Feelings Sentences (Signature Edition) - Compounded",
  "Min Nan Chinese Nature and Weather Sentences (Signature Edition) - Compounded",
  "Min Nan Chinese Shopping and Money Sentences (Signature Edition) - Compounded",
  "Min Nan Chinese Friendship and Social Life Sentences (Signature Edition) - Compounded",
  "Min Nan Chinese Technology and Communication Sentences (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Min Nan Chinese Verb Tenses in Sentences (Signature Edition) - Advanced",
  "Min Nan Chinese Questions and Answers (Signature Edition) - Advanced",
  "Min Nan Chinese Commands and Requests (Signature Edition) - Advanced",
  "Min Nan Chinese Descriptions of People and Places (Signature Edition) - Advanced",
  "Min Nan Chinese Story I: A Morning at the Market (Signature Edition) - Advanced",
  "Min Nan Chinese Story II: A Trip to Lukang (Signature Edition) - Advanced",
  "Min Nan Chinese Story III: Plans for Tomorrow (Signature Edition) - Advanced",
  "Min Nan Chinese Idioms and Proverbs (Signature Edition) - Advanced",
  "Min Nan Chinese Formal and Polite Registers (Signature Edition) - Advanced",
  "Min Nan Chinese Compound and Complex Sentences (Signature Edition) - Advanced",
  "Min Nan Chinese Conversation: At the Market (Signature Edition) - Advanced",
  "Min Nan Chinese Conversation: Meeting a Friend (Signature Edition) - Advanced",
  "Min Nan Chinese Conversation: Solving a Problem (Signature Edition) - Advanced",
  "Min Nan Chinese Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Min Nan Chinese Study — "+safe+"\n"
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
    demo:{kind:"min-nan-chinese-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-min-nan-chinese-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-min-nan-chinese-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
