(function(){'use strict';
/* JAH The Spanish to English Signature Database generator — jahdb-language-spanish-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LSPAS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Spanish Language Overview (Signature Edition) - Foundations",
  "Spanish Writing System and Alphabet (Signature Edition) - Foundations",
  "Spanish Pronunciation and Phonology (Signature Edition) - Foundations",
  "Spanish Core Nouns I (Signature Edition) - Foundations",
  "Spanish Core Verbs I (Signature Edition) - Foundations",
  "Spanish Adjectives and Adverbs (Signature Edition) - Foundations",
  "Spanish Pronouns (Signature Edition) - Foundations",
  "Spanish Numbers and Time (Signature Edition) - Foundations",
  "Spanish Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Spanish Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Spanish Home and Family Sentences (Signature Edition) - Compounded",
  "Spanish Food and Cooking Sentences (Signature Edition) - Compounded",
  "Spanish Travel and Directions Sentences (Signature Edition) - Compounded",
  "Spanish Work and School Sentences (Signature Edition) - Compounded",
  "Spanish Health and Body Sentences (Signature Edition) - Compounded",
  "Spanish Emotions and Feelings Sentences (Signature Edition) - Compounded",
  "Spanish Nature and Weather Sentences (Signature Edition) - Compounded",
  "Spanish Shopping and Money Sentences (Signature Edition) - Compounded",
  "Spanish Friendship and Social Life Sentences (Signature Edition) - Compounded",
  "Spanish Technology and Communication Sentences (Signature Edition) - Compounded",
  "Spanish Verb Tenses in Sentences (Signature Edition) - Compounded",
  "Spanish Questions and Answers (Signature Edition) - Compounded",
  "Spanish Commands and Requests (Signature Edition) - Compounded",
  "Spanish Descriptions of People and Places (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Spanish Story I: A Simple Day (Signature Edition) - Advanced",
  "Spanish Story II: Yesterday (Signature Edition) - Advanced",
  "Spanish Story III: Tomorrow (Signature Edition) - Advanced",
  "Spanish Idioms and Proverbs (Signature Edition) - Advanced",
  "Spanish Formal and Polite Registers (Signature Edition) - Advanced",
  "Spanish Compound and Complex Sentences (Signature Edition) - Advanced",
  "Spanish Conversation: At the Market (Signature Edition) - Advanced",
  "Spanish Conversation: Meeting a Friend (Signature Edition) - Advanced",
  "Spanish Conversation: Solving a Problem (Signature Edition) - Advanced",
  "Spanish Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Spanish Language Study — "+safe+"\n"
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
    demo:{kind:"spanish-language-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-spanish-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-spanish-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
