(function(){'use strict';
/* JAH The Slovak Language Signature Database generator — jahdb-language-slovak-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LSLKS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Slovak Language Overview (Signature Edition) - Foundations",
  "Slovak Writing System and Alphabet (Signature Edition) - Foundations",
  "Slovak Pronunciation and Phonology (Signature Edition) - Foundations",
  "Slovak Core Nouns I (Signature Edition) - Foundations",
  "Slovak Core Verbs I (Signature Edition) - Foundations",
  "Slovak Adjectives and Adverbs (Signature Edition) - Foundations",
  "Slovak Pronouns (Signature Edition) - Foundations",
  "Slovak Numbers and Time (Signature Edition) - Foundations",
  "Slovak Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Slovak Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Slovak At Home and with Family (Signature Edition) - Compounded",
  "Slovak Food and Cooking (Signature Edition) - Compounded",
  "Slovak Travel and Directions (Signature Edition) - Compounded",
  "Slovak Work and School (Signature Edition) - Compounded",
  "Slovak Health and the Body (Signature Edition) - Compounded",
  "Slovak Emotions and Feelings (Signature Edition) - Compounded",
  "Slovak Nature and Weather (Signature Edition) - Compounded",
  "Slovak Shopping and Money (Signature Edition) - Compounded",
  "Slovak Friendship and Social Life (Signature Edition) - Compounded",
  "Slovak Technology and Communication (Signature Edition) - Compounded",
  "Slovak Verb Tenses in Sentences (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Slovak Questions and Answers (Signature Edition) - Advanced",
  "Slovak Commands and Requests (Signature Edition) - Advanced",
  "Slovak Descriptions of People and Places (Signature Edition) - Advanced",
  "Slovak Story I: Chlapec a pes (Signature Edition) - Advanced",
  "Slovak Story II: Ro\u013en\u00edk (Signature Edition) - Advanced",
  "Slovak Story III: Nov\u00e1 \u0161kola (Signature Edition) - Advanced",
  "Slovak Idioms and Proverbs (Signature Edition) - Advanced",
  "Slovak Formal and Polite Registers (Signature Edition) - Advanced",
  "Slovak Compound and Complex Sentences (Signature Edition) - Advanced",
  "Slovak Conversation: Na trhu (Signature Edition) - Advanced",
  "Slovak Conversation: Stretnutie s priate\u013eom (Signature Edition) - Advanced",
  "Slovak Conversation: Rie\u0161enie probl\u00e9mu (Signature Edition) - Advanced",
  "Slovak Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Slovak Study — "+safe+"\n"
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
    demo:{kind:"language-slovak-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-slovak-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-slovak-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
