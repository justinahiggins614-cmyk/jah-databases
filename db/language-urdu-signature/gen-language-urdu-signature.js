(function(){'use strict';
/* JAH The Urdu to English Signature Database generator — jahdb-language-urdu-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LURDS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Urdu Language Overview (Signature Edition) - Foundations",
  "Urdu Writing System: Perso-Arabic Script (Signature Edition) - Foundations",
  "Urdu Pronunciation and Phonology (Signature Edition) - Foundations",
  "Urdu Core Nouns I: People, Places, Things (Signature Edition) - Foundations",
  "Urdu Core Verbs I: Essential Actions (Signature Edition) - Foundations",
  "Urdu Adjectives and Adverbs (Signature Edition) - Foundations",
  "Urdu Pronouns: Full Paradigms (Signature Edition) - Foundations",
  "Urdu Numbers, Time, Days, and Dates (Signature Edition) - Foundations",
  "Urdu Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Urdu Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Urdu Sentences: Home and Family (Signature Edition) - Compounded",
  "Urdu Sentences: Food and Cooking (Signature Edition) - Compounded",
  "Urdu Sentences: Travel and Directions (Signature Edition) - Compounded",
  "Urdu Sentences: Work and School (Signature Edition) - Compounded",
  "Urdu Sentences: Health and the Body (Signature Edition) - Compounded",
  "Urdu Sentences: Emotions and Feelings (Signature Edition) - Compounded",
  "Urdu Sentences: Nature and Weather (Signature Edition) - Compounded",
  "Urdu Sentences: Shopping and Money (Signature Edition) - Compounded",
  "Urdu Sentences: Friendship and Social Life (Signature Edition) - Compounded",
  "Urdu Sentences: Technology and Communication (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Urdu Verb Tenses in Sentences (Signature Edition) - Advanced",
  "Urdu Questions and Answers (Signature Edition) - Advanced",
  "Urdu Commands and Polite Requests (Signature Edition) - Advanced",
  "Urdu Descriptions: People and Places (Signature Edition) - Advanced",
  "Urdu Story I: A Simple Story (Signature Edition) - Advanced",
  "Urdu Story II: A Story in the Past Tense (Signature Edition) - Advanced",
  "Urdu Story III: A Story in Future and Conditional (Signature Edition) - Advanced",
  "Urdu Idioms and Proverbs (Signature Edition) - Advanced",
  "Urdu Formal and Polite Registers (Signature Edition) - Advanced",
  "Urdu Compound and Complex Sentences (Signature Edition) - Advanced",
  "Urdu Conversation: At the Market (Signature Edition) - Advanced",
  "Urdu Conversation: Meeting a Friend (Signature Edition) - Advanced",
  "Urdu Conversation: Solving a Problem (Signature Edition) - Advanced",
  "Urdu Mastery Review and Full Reference (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Urdu Lesson — "+safe+"\n"
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
    demo:{kind:"urdu-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-urdu-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-urdu-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
