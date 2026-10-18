(function(){'use strict';
/* JAH The Croatian Language Signature Database generator — jahdb-language-croatian-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LHRVS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Croatian Language Overview (Signature Edition) - Foundations",
  "Croatian Writing System and Alphabet (Signature Edition) - Foundations",
  "Croatian Pronunciation and Phonology (Signature Edition) - Foundations",
  "Croatian Core Nouns I (Signature Edition) - Foundations",
  "Croatian Core Verbs I (Signature Edition) - Foundations",
  "Croatian Adjectives and Adverbs (Signature Edition) - Foundations",
  "Croatian Pronouns (Signature Edition) - Foundations",
  "Croatian Numbers and Time (Signature Edition) - Foundations",
  "Croatian Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Croatian Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Croatian At Home and with Family (Signature Edition) - Compounded",
  "Croatian Food and Cooking (Signature Edition) - Compounded",
  "Croatian Travel and Directions (Signature Edition) - Compounded",
  "Croatian Work and School (Signature Edition) - Compounded",
  "Croatian Health and the Body (Signature Edition) - Compounded",
  "Croatian Emotions and Feelings (Signature Edition) - Compounded",
  "Croatian Nature and Weather (Signature Edition) - Compounded",
  "Croatian Shopping and Money (Signature Edition) - Compounded",
  "Croatian Friendship and Social Life (Signature Edition) - Compounded",
  "Croatian Technology and Communication (Signature Edition) - Compounded",
  "Croatian Verb Tenses in Sentences (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Croatian Questions and Answers (Signature Edition) - Advanced",
  "Croatian Commands and Requests (Signature Edition) - Advanced",
  "Croatian Descriptions of People and Places (Signature Edition) - Advanced",
  "Croatian Story I: Dje\u010dak i pas (Signature Edition) - Advanced",
  "Croatian Story II: Seljak (Signature Edition) - Advanced",
  "Croatian Story III: Nova \u0161kola (Signature Edition) - Advanced",
  "Croatian Idioms and Proverbs (Signature Edition) - Advanced",
  "Croatian Formal and Polite Registers (Signature Edition) - Advanced",
  "Croatian Compound and Complex Sentences (Signature Edition) - Advanced",
  "Croatian Conversation: Na tr\u017enici (Signature Edition) - Advanced",
  "Croatian Conversation: Susret s prijateljem (Signature Edition) - Advanced",
  "Croatian Conversation: Rje\u0161avanje problema (Signature Edition) - Advanced",
  "Croatian Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Croatian Study — "+safe+"\n"
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
    demo:{kind:"language-croatian-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-croatian-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-croatian-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
