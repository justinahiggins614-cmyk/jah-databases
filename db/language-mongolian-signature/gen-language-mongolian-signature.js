(function(){'use strict';
/* JAH The Mongolian Language Signature Database generator — jahdb-language-mongolian-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LMONS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Mongolian Language Overview (Signature Edition) - Foundations",
  "Mongolian Writing System and Alphabet (Signature Edition) - Foundations",
  "Mongolian Pronunciation and Phonology (Signature Edition) - Foundations",
  "Mongolian Core Nouns I (Signature Edition) - Foundations",
  "Mongolian Core Verbs I (Signature Edition) - Foundations",
  "Mongolian Adjectives and Adverbs (Signature Edition) - Foundations",
  "Mongolian Pronouns (Signature Edition) - Foundations",
  "Mongolian Numbers and Time (Signature Edition) - Foundations",
  "Mongolian Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Mongolian Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Mongolian At Home and with Family (Signature Edition) - Compounded",
  "Mongolian Food and Cooking (Signature Edition) - Compounded",
  "Mongolian Travel and Directions (Signature Edition) - Compounded",
  "Mongolian Work and School (Signature Edition) - Compounded",
  "Mongolian Health and the Body (Signature Edition) - Compounded",
  "Mongolian Emotions and Feelings (Signature Edition) - Compounded",
  "Mongolian Nature and Weather (Signature Edition) - Compounded",
  "Mongolian Shopping and Money (Signature Edition) - Compounded",
  "Mongolian Friendship and Social Life (Signature Edition) - Compounded",
  "Mongolian Technology and Communication (Signature Edition) - Compounded",
  "Mongolian Verb Tenses in Sentences (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Mongolian Questions and Answers (Signature Edition) - Advanced",
  "Mongolian Commands and Requests (Signature Edition) - Advanced",
  "Mongolian Descriptions of People and Places (Signature Edition) - Advanced",
  "Mongolian Story I: \u0425\u04af\u04af\u0445\u044d\u0434 \u0431\u0430 \u043d\u043e\u0445\u043e\u0439 (Signature Edition) - Advanced",
  "Mongolian Story II: \u041c\u0430\u043b\u0447\u0438\u043d (Signature Edition) - Advanced",
  "Mongolian Story III: \u0428\u0438\u043d\u044d \u0441\u0443\u0440\u0433\u0443\u0443\u043b\u044c (Signature Edition) - Advanced",
  "Mongolian Idioms and Proverbs (Signature Edition) - Advanced",
  "Mongolian Formal and Polite Registers (Signature Edition) - Advanced",
  "Mongolian Compound and Complex Sentences (Signature Edition) - Advanced",
  "Mongolian Conversation: \u0417\u0430\u0445\u0430\u0434 (Signature Edition) - Advanced",
  "Mongolian Conversation: \u041d\u0430\u0439\u0437\u0442\u0430\u0439\u0433\u0430\u0430 \u0443\u0443\u043b\u0437\u0430\u0445 (Signature Edition) - Advanced",
  "Mongolian Conversation: \u0410\u0441\u0443\u0443\u0434\u043b\u044b\u0433 \u0448\u0438\u0439\u0434\u044d\u0445 (Signature Edition) - Advanced",
  "Mongolian Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Mongolian Study — "+safe+"\n"
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
    demo:{kind:"language-mongolian-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-mongolian-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-mongolian-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
