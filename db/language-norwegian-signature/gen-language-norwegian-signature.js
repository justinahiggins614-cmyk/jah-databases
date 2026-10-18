(function(){'use strict';
/* JAH The Norwegian Language Signature Database generator — jahdb-language-norwegian-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LNORS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Norwegian Language Overview (Signature Edition) - Foundations",
  "Norwegian Writing System and Alphabet (Signature Edition) - Foundations",
  "Norwegian Pronunciation and Phonology (Signature Edition) - Foundations",
  "Norwegian Core Nouns I (Signature Edition) - Foundations",
  "Norwegian Core Verbs I (Signature Edition) - Foundations",
  "Norwegian Adjectives and Adverbs (Signature Edition) - Foundations",
  "Norwegian Pronouns (Signature Edition) - Foundations",
  "Norwegian Numbers and Time (Signature Edition) - Foundations",
  "Norwegian Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Norwegian Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Norwegian At Home and with Family (Signature Edition) - Compounded",
  "Norwegian Food and Cooking (Signature Edition) - Compounded",
  "Norwegian Travel and Directions (Signature Edition) - Compounded",
  "Norwegian Work and School (Signature Edition) - Compounded",
  "Norwegian Health and the Body (Signature Edition) - Compounded",
  "Norwegian Emotions and Feelings (Signature Edition) - Compounded",
  "Norwegian Nature and Weather (Signature Edition) - Compounded",
  "Norwegian Shopping and Money (Signature Edition) - Compounded",
  "Norwegian Friendship and Social Life (Signature Edition) - Compounded",
  "Norwegian Technology and Communication (Signature Edition) - Compounded",
  "Norwegian Verb Tenses in Sentences (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Norwegian Questions and Answers (Signature Edition) - Advanced",
  "Norwegian Commands and Requests (Signature Edition) - Advanced",
  "Norwegian Descriptions of People and Places (Signature Edition) - Advanced",
  "Norwegian Story I: Gutten og hunden (Signature Edition) - Advanced",
  "Norwegian Story II: Bonden (Signature Edition) - Advanced",
  "Norwegian Story III: Den nye skolen (Signature Edition) - Advanced",
  "Norwegian Idioms and Proverbs (Signature Edition) - Advanced",
  "Norwegian Formal and Polite Registers (Signature Edition) - Advanced",
  "Norwegian Compound and Complex Sentences (Signature Edition) - Advanced",
  "Norwegian Conversation: P\u00e5 markedet (Signature Edition) - Advanced",
  "Norwegian Conversation: M\u00f8te en venn (Signature Edition) - Advanced",
  "Norwegian Conversation: L\u00f8se et problem (Signature Edition) - Advanced",
  "Norwegian Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Norwegian Study — "+safe+"\n"
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
    demo:{kind:"language-norwegian-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-norwegian-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-norwegian-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
