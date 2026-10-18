(function(){'use strict';
/* JAH The Bulgarian Language Signature Database generator — jahdb-language-bulgarian-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LBULS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Bulgarian Language Overview (Signature Edition) - Foundations",
  "Bulgarian Writing System and Alphabet (Signature Edition) - Foundations",
  "Bulgarian Pronunciation and Phonology (Signature Edition) - Foundations",
  "Bulgarian Core Nouns I (Signature Edition) - Foundations",
  "Bulgarian Core Verbs I (Signature Edition) - Foundations",
  "Bulgarian Adjectives and Adverbs (Signature Edition) - Foundations",
  "Bulgarian Pronouns (Signature Edition) - Foundations",
  "Bulgarian Numbers and Time (Signature Edition) - Foundations",
  "Bulgarian Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Bulgarian Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Bulgarian At Home and with Family (Signature Edition) - Compounded",
  "Bulgarian Food and Cooking (Signature Edition) - Compounded",
  "Bulgarian Travel and Directions (Signature Edition) - Compounded",
  "Bulgarian Work and School (Signature Edition) - Compounded",
  "Bulgarian Health and the Body (Signature Edition) - Compounded",
  "Bulgarian Emotions and Feelings (Signature Edition) - Compounded",
  "Bulgarian Nature and Weather (Signature Edition) - Compounded",
  "Bulgarian Shopping and Money (Signature Edition) - Compounded",
  "Bulgarian Friendship and Social Life (Signature Edition) - Compounded",
  "Bulgarian Technology and Communication (Signature Edition) - Compounded",
  "Bulgarian Verb Tenses in Sentences (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Bulgarian Questions and Answers (Signature Edition) - Advanced",
  "Bulgarian Commands and Requests (Signature Edition) - Advanced",
  "Bulgarian Descriptions of People and Places (Signature Edition) - Advanced",
  "Bulgarian Story I: \u041c\u043e\u043c\u0447\u0435\u0442\u043e \u0438 \u043a\u0443\u0447\u0435\u0442\u043e (Signature Edition) - Advanced",
  "Bulgarian Story II: \u0424\u0435\u0440\u043c\u0435\u0440\u044a\u0442 (Signature Edition) - Advanced",
  "Bulgarian Story III: \u041d\u043e\u0432\u043e\u0442\u043e \u0443\u0447\u0438\u043b\u0438\u0449\u0435 (Signature Edition) - Advanced",
  "Bulgarian Idioms and Proverbs (Signature Edition) - Advanced",
  "Bulgarian Formal and Polite Registers (Signature Edition) - Advanced",
  "Bulgarian Compound and Complex Sentences (Signature Edition) - Advanced",
  "Bulgarian Conversation: \u041d\u0430 \u043f\u0430\u0437\u0430\u0440\u0430 (Signature Edition) - Advanced",
  "Bulgarian Conversation: \u0421\u0440\u0435\u0449\u0430 \u0441 \u043f\u0440\u0438\u044f\u0442\u0435\u043b (Signature Edition) - Advanced",
  "Bulgarian Conversation: \u0420\u0435\u0448\u0430\u0432\u0430\u043d\u0435 \u043d\u0430 \u043f\u0440\u043e\u0431\u043b\u0435\u043c (Signature Edition) - Advanced",
  "Bulgarian Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Bulgarian Study — "+safe+"\n"
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
    demo:{kind:"language-bulgarian-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-bulgarian-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-bulgarian-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
