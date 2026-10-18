(function(){'use strict';
/* JAH The Serbian Language Signature Database generator — jahdb-language-serbian-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LSRPS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Serbian Language Overview (Signature Edition) - Foundations",
  "Serbian Writing System and Alphabet (Signature Edition) - Foundations",
  "Serbian Pronunciation and Phonology (Signature Edition) - Foundations",
  "Serbian Core Nouns I (Signature Edition) - Foundations",
  "Serbian Core Verbs I (Signature Edition) - Foundations",
  "Serbian Adjectives and Adverbs (Signature Edition) - Foundations",
  "Serbian Pronouns (Signature Edition) - Foundations",
  "Serbian Numbers and Time (Signature Edition) - Foundations",
  "Serbian Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Serbian Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Serbian at Home and with Family (Signature Edition) - Compounded",
  "Serbian Food and Cooking (Signature Edition) - Compounded",
  "Serbian Travel and Directions (Signature Edition) - Compounded",
  "Serbian Work and School (Signature Edition) - Compounded",
  "Serbian Health and the Body (Signature Edition) - Compounded",
  "Serbian Emotions and Feelings (Signature Edition) - Compounded",
  "Serbian Nature and Weather (Signature Edition) - Compounded",
  "Serbian Shopping and Money (Signature Edition) - Compounded",
  "Serbian Friendship and Social Life (Signature Edition) - Compounded",
  "Serbian Technology and Communication (Signature Edition) - Compounded",
  "Serbian Verb Tenses in Sentences (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Serbian Questions and Answers (Signature Edition) - Advanced",
  "Serbian Commands and Requests (Signature Edition) - Advanced",
  "Serbian Descriptions of People and Places (Signature Edition) - Advanced",
  "Serbian Story I: The Lost Key (Signature Edition) - Advanced",
  "Serbian Story II: The Little Bird (Signature Edition) - Advanced",
  "Serbian Story III: The Market Day (Signature Edition) - Advanced",
  "Serbian Idioms and Proverbs (Signature Edition) - Advanced",
  "Serbian Formal and Polite Registers (Signature Edition) - Advanced",
  "Serbian Compound and Complex Sentences (Signature Edition) - Advanced",
  "Serbian Conversation: At the Market (Signature Edition) - Advanced",
  "Serbian Conversation: Meeting a Friend (Signature Edition) - Advanced",
  "Serbian Conversation: Solving a Problem (Signature Edition) - Advanced",
  "Serbian Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Serbian Study — "+safe+"\n"
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
    demo:{kind:"serbian-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-serbian-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-serbian-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
