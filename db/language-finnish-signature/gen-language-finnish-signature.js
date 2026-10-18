(function(){'use strict';
/* JAH The Finnish Language Signature Database generator — jahdb-language-finnish-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LFINS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Finnish Language Overview (Signature Edition) - Foundations",
  "Finnish Writing System and Alphabet (Signature Edition) - Foundations",
  "Finnish Pronunciation and Phonology (Signature Edition) - Foundations",
  "Finnish Core Nouns I (Signature Edition) - Foundations",
  "Finnish Core Verbs I (Signature Edition) - Foundations",
  "Finnish Adjectives and Adverbs (Signature Edition) - Foundations",
  "Finnish Pronouns (Signature Edition) - Foundations",
  "Finnish Numbers and Time (Signature Edition) - Foundations",
  "Finnish Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Finnish Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Finnish At Home and with Family (Signature Edition) - Compounded",
  "Finnish Food and Cooking (Signature Edition) - Compounded",
  "Finnish Travel and Directions (Signature Edition) - Compounded",
  "Finnish Work and School (Signature Edition) - Compounded",
  "Finnish Health and the Body (Signature Edition) - Compounded",
  "Finnish Emotions and Feelings (Signature Edition) - Compounded",
  "Finnish Nature and Weather (Signature Edition) - Compounded",
  "Finnish Shopping and Money (Signature Edition) - Compounded",
  "Finnish Friendship and Social Life (Signature Edition) - Compounded",
  "Finnish Technology and Communication (Signature Edition) - Compounded",
  "Finnish Verb Tenses in Sentences (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Finnish Questions and Answers (Signature Edition) - Advanced",
  "Finnish Commands and Requests (Signature Edition) - Advanced",
  "Finnish Descriptions of People and Places (Signature Edition) - Advanced",
  "Finnish Story I: Poika ja koira (Signature Edition) - Advanced",
  "Finnish Story II: Maanviljelij\u00e4 (Signature Edition) - Advanced",
  "Finnish Story III: Uusi koulu (Signature Edition) - Advanced",
  "Finnish Idioms and Proverbs (Signature Edition) - Advanced",
  "Finnish Formal and Polite Registers (Signature Edition) - Advanced",
  "Finnish Compound and Complex Sentences (Signature Edition) - Advanced",
  "Finnish Conversation: Torilla (Signature Edition) - Advanced",
  "Finnish Conversation: Yst\u00e4v\u00e4n tapaaminen (Signature Edition) - Advanced",
  "Finnish Conversation: Ongelman ratkaisu (Signature Edition) - Advanced",
  "Finnish Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Finnish Study — "+safe+"\n"
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
    demo:{kind:"language-finnish-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-finnish-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-finnish-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
