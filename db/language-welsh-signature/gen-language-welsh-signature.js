(function(){'use strict';
/* JAH The Welsh to English Signature Database generator — jahdb-language-welsh-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LWELS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Welsh Language Overview (Signature Edition) - Foundations",
  "Welsh Writing System and Alphabet (Signature Edition) - Foundations",
  "Welsh Pronunciation and Phonology (Signature Edition) - Foundations",
  "Welsh Core Nouns I (Signature Edition) - Foundations",
  "Welsh Core Verbs I (Signature Edition) - Foundations",
  "Welsh Adjectives and Adverbs (Signature Edition) - Foundations",
  "Welsh Pronouns (Signature Edition) - Foundations",
  "Welsh Numbers and Time (Signature Edition) - Foundations",
  "Welsh Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Welsh Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Welsh at Home and with Family (Signature Edition) - Compounded",
  "Welsh Food and Cooking (Signature Edition) - Compounded",
  "Welsh Travel and Directions (Signature Edition) - Compounded",
  "Welsh Work and School (Signature Edition) - Compounded",
  "Welsh Health and the Body (Signature Edition) - Compounded",
  "Welsh Emotions and Feelings (Signature Edition) - Compounded",
  "Welsh Nature and Weather (Signature Edition) - Compounded",
  "Welsh Shopping and Money (Signature Edition) - Compounded",
  "Welsh Friendship and Social Life (Signature Edition) - Compounded",
  "Welsh Technology and Communication (Signature Edition) - Compounded",
  "Welsh Verb Tenses in Sentences (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Welsh Questions and Answers (Signature Edition) - Advanced",
  "Welsh Commands and Requests (Signature Edition) - Advanced",
  "Welsh Descriptions of People and Places (Signature Edition) - Advanced",
  "Welsh Story I: The Clever Shepherd (Signature Edition) - Advanced",
  "Welsh Story II: The Lost Key (Signature Edition) - Advanced",
  "Welsh Story III: The New School (Signature Edition) - Advanced",
  "Welsh Idioms and Proverbs (Signature Edition) - Advanced",
  "Welsh Formal and Polite Registers (Signature Edition) - Advanced",
  "Welsh Compound and Complex Sentences (Signature Edition) - Advanced",
  "Welsh Conversation: At the Market (Signature Edition) - Advanced",
  "Welsh Conversation: Meeting a Friend (Signature Edition) - Advanced",
  "Welsh Conversation: Solving a Problem (Signature Edition) - Advanced",
  "Welsh Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Welsh Study — "+safe+"\n"
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
    demo:{kind:"welsh-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-welsh-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-welsh-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
