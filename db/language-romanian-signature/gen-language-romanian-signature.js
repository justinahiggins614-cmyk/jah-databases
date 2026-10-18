(function(){'use strict';
/* JAH The Romanian to English Signature Database generator — jahdb-language-romanian-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LRONS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Romanian Language Overview (Signature Edition) - Foundations",
  "Romanian Writing System and Alphabet (Signature Edition) - Foundations",
  "Romanian Pronunciation and Phonology (Signature Edition) - Foundations",
  "Romanian Core Nouns I (Signature Edition) - Foundations",
  "Romanian Core Verbs I (Signature Edition) - Foundations",
  "Romanian Adjectives and Adverbs (Signature Edition) - Foundations",
  "Romanian Pronouns (Signature Edition) - Foundations",
  "Romanian Numbers and Time (Signature Edition) - Foundations",
  "Romanian Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Romanian Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Romanian at Home and with Family (Signature Edition) - Compounded",
  "Romanian Food and Cooking (Signature Edition) - Compounded",
  "Romanian Travel and Directions (Signature Edition) - Compounded",
  "Romanian Work and School (Signature Edition) - Compounded",
  "Romanian Health and the Body (Signature Edition) - Compounded",
  "Romanian Emotions and Feelings (Signature Edition) - Compounded",
  "Romanian Nature and Weather (Signature Edition) - Compounded",
  "Romanian Shopping and Money (Signature Edition) - Compounded",
  "Romanian Friendship and Social Life (Signature Edition) - Compounded",
  "Romanian Technology and Communication (Signature Edition) - Compounded",
  "Romanian Verb Tenses in Sentences (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Romanian Questions and Answers (Signature Edition) - Advanced",
  "Romanian Commands and Requests (Signature Edition) - Advanced",
  "Romanian Descriptions of People and Places (Signature Edition) - Advanced",
  "Romanian Story I: The Clever Shepherd (Signature Edition) - Advanced",
  "Romanian Story II: The Lost Key (Signature Edition) - Advanced",
  "Romanian Story III: The New School (Signature Edition) - Advanced",
  "Romanian Idioms and Proverbs (Signature Edition) - Advanced",
  "Romanian Formal and Polite Registers (Signature Edition) - Advanced",
  "Romanian Compound and Complex Sentences (Signature Edition) - Advanced",
  "Romanian Conversation: At the Market (Signature Edition) - Advanced",
  "Romanian Conversation: Meeting a Friend (Signature Edition) - Advanced",
  "Romanian Conversation: Solving a Problem (Signature Edition) - Advanced",
  "Romanian Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Romanian Study — "+safe+"\n"
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
    demo:{kind:"romanian-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-romanian-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-romanian-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
