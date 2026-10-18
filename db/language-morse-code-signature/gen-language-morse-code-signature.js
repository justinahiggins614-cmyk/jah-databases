(function(){'use strict';
/* JAH The Morse Code to English Signature Database generator — jahdb-language-morse-code-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LMORS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Morse Code Language Overview (Signature Edition) - Foundations",
  "Morse Code Writing System and Alphabet (Signature Edition) - Foundations",
  "Morse Code Pronunciation and Phonology (Signature Edition) - Foundations",
  "Morse Code Core Nouns I (Signature Edition) - Foundations",
  "Morse Code Core Verbs I (Signature Edition) - Foundations",
  "Morse Code Adjectives and Adverbs (Signature Edition) - Foundations",
  "Morse Code Pronouns (Signature Edition) - Foundations",
  "Morse Code Numbers and Time (Signature Edition) - Foundations",
  "Morse Code Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Morse Code Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Morse Code at Home and with Family (Signature Edition) - Compounded",
  "Morse Code Food and Cooking (Signature Edition) - Compounded",
  "Morse Code Travel and Directions (Signature Edition) - Compounded",
  "Morse Code Work and School (Signature Edition) - Compounded",
  "Morse Code Health and the Body (Signature Edition) - Compounded",
  "Morse Code Emotions and Feelings (Signature Edition) - Compounded",
  "Morse Code Nature and Weather (Signature Edition) - Compounded",
  "Morse Code Shopping and Money (Signature Edition) - Compounded",
  "Morse Code Friendship and Social Life (Signature Edition) - Compounded",
  "Morse Code Technology and Communication (Signature Edition) - Compounded",
  "Morse Code Verb Tenses in Sentences (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Morse Code Questions and Answers (Signature Edition) - Advanced",
  "Morse Code Commands and Requests (Signature Edition) - Advanced",
  "Morse Code Descriptions of People and Places (Signature Edition) - Advanced",
  "Morse Code Story I: What Hath God Wrought (Signature Edition) - Advanced",
  "Morse Code Story II: The Titanic Calls (Signature Edition) - Advanced",
  "Morse Code Story III: The New Operator (Signature Edition) - Advanced",
  "Morse Code Idioms and Proverbs (Signature Edition) - Advanced",
  "Morse Code Formal and Polite Registers (Signature Edition) - Advanced",
  "Morse Code Compound and Complex Sentences (Signature Edition) - Advanced",
  "Morse Code Conversation: At the Market (Signature Edition) - Advanced",
  "Morse Code Conversation: Meeting a Friend (Signature Edition) - Advanced",
  "Morse Code Conversation: Solving a Problem (Signature Edition) - Advanced",
  "Morse Code Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Morse_Code Study — "+safe+"\n"
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
    demo:{kind:"morse_code-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-morse-code-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-morse-code-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
