(function(){'use strict';
/* JAH The Hebrew Language Signature Database generator — jahdb-language-hebrew-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LHEBS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Hebrew Language Overview (Signature Edition) - Foundations",
  "Hebrew Writing System and Alphabet (Signature Edition) - Foundations",
  "Hebrew Pronunciation and Phonology (Signature Edition) - Foundations",
  "Hebrew Core Nouns I (Signature Edition) - Foundations",
  "Hebrew Core Verbs I (Signature Edition) - Foundations",
  "Hebrew Adjectives and Adverbs (Signature Edition) - Foundations",
  "Hebrew Pronouns (Signature Edition) - Foundations",
  "Hebrew Numbers and Time (Signature Edition) - Foundations",
  "Hebrew Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Hebrew Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Hebrew At Home and with Family (Signature Edition) - Compounded",
  "Hebrew Food and Cooking (Signature Edition) - Compounded",
  "Hebrew Travel and Directions (Signature Edition) - Compounded",
  "Hebrew Work and School (Signature Edition) - Compounded",
  "Hebrew Health and the Body (Signature Edition) - Compounded",
  "Hebrew Emotions and Feelings (Signature Edition) - Compounded",
  "Hebrew Nature and Weather (Signature Edition) - Compounded",
  "Hebrew Shopping and Money (Signature Edition) - Compounded",
  "Hebrew Friendship and Social Life (Signature Edition) - Compounded",
  "Hebrew Technology and Communication (Signature Edition) - Compounded",
  "Hebrew Verb Tenses in Sentences (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Hebrew Questions and Answers (Signature Edition) - Advanced",
  "Hebrew Commands and Requests (Signature Edition) - Advanced",
  "Hebrew Descriptions of People and Places (Signature Edition) - Advanced",
  "Hebrew Story I: \u05d4\u05d9\u05dc\u05d3 \u05d5\u05d4\u05db\u05dc\u05d1 (Signature Edition) - Advanced",
  "Hebrew Story II: \u05d4\u05d0\u05d9\u05db\u05e8 (Signature Edition) - Advanced",
  "Hebrew Story III: \u05d1\u05d9\u05ea \u05d4\u05e1\u05e4\u05e8 \u05d4\u05d7\u05d3\u05e9 (Signature Edition) - Advanced",
  "Hebrew Idioms and Proverbs (Signature Edition) - Advanced",
  "Hebrew Formal and Polite Registers (Signature Edition) - Advanced",
  "Hebrew Compound and Complex Sentences (Signature Edition) - Advanced",
  "Hebrew Conversation: \u05d1\u05e9\u05d5\u05e7 (Signature Edition) - Advanced",
  "Hebrew Conversation: \u05e4\u05d2\u05d9\u05e9\u05d4 \u05e2\u05dd \u05d7\u05d1\u05e8 (Signature Edition) - Advanced",
  "Hebrew Conversation: \u05e4\u05ea\u05e8\u05d5\u05df \u05d1\u05e2\u05d9\u05d4 (Signature Edition) - Advanced",
  "Hebrew Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Hebrew Study — "+safe+"\n"
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
    demo:{kind:"language-hebrew-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-hebrew-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-hebrew-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
