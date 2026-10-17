(function(){'use strict';
/* JAH Wu Chinese Language Signature Database generator — jahdb-language-wu-chinese-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LWUUS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Wu Chinese Language Overview (Signature Edition) - Foundations",
  "Wu Chinese Writing System (Signature Edition) - Foundations",
  "Wu Chinese Pronunciation and Phonology (Signature Edition) - Foundations",
  "Wu Chinese Core Nouns I (Signature Edition) - Foundations",
  "Wu Chinese Core Verbs I (Signature Edition) - Foundations",
  "Wu Chinese Adjectives and Adverbs (Signature Edition) - Foundations",
  "Wu Chinese Pronouns (Signature Edition) - Foundations",
  "Wu Chinese Numbers and Time (Signature Edition) - Foundations",
  "Wu Chinese Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Wu Chinese Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Wu Chinese Home and Family Sentences (Signature Edition) - Compounded",
  "Wu Chinese Food and Cooking Sentences (Signature Edition) - Compounded",
  "Wu Chinese Travel and Directions Sentences (Signature Edition) - Compounded",
  "Wu Chinese Work and School Sentences (Signature Edition) - Compounded",
  "Wu Chinese Health and Body Sentences (Signature Edition) - Compounded",
  "Wu Chinese Emotions and Feelings Sentences (Signature Edition) - Compounded",
  "Wu Chinese Nature and Weather Sentences (Signature Edition) - Compounded",
  "Wu Chinese Shopping and Money Sentences (Signature Edition) - Compounded",
  "Wu Chinese Friendship and Social Life Sentences (Signature Edition) - Compounded",
  "Wu Chinese Technology and Communication Sentences (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Wu Chinese Verb Tenses in Sentences (Signature Edition) - Advanced",
  "Wu Chinese Questions and Answers (Signature Edition) - Advanced",
  "Wu Chinese Commands and Requests (Signature Edition) - Advanced",
  "Wu Chinese Descriptions of People and Places (Signature Edition) - Advanced",
  "Wu Chinese Story I: A Morning at the Market (Signature Edition) - Advanced",
  "Wu Chinese Story II: A Trip to Suzhou (Signature Edition) - Advanced",
  "Wu Chinese Story III: Plans for Tomorrow (Signature Edition) - Advanced",
  "Wu Chinese Idioms and Proverbs (Signature Edition) - Advanced",
  "Wu Chinese Formal and Polite Registers (Signature Edition) - Advanced",
  "Wu Chinese Compound and Complex Sentences (Signature Edition) - Advanced",
  "Wu Chinese Conversation: At the Market (Signature Edition) - Advanced",
  "Wu Chinese Conversation: Meeting a Friend (Signature Edition) - Advanced",
  "Wu Chinese Conversation: Solving a Problem (Signature Edition) - Advanced",
  "Wu Chinese Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Wu Chinese Study — "+safe+"\n"
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
    demo:{kind:"wu-chinese-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-wu-chinese-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-wu-chinese-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
