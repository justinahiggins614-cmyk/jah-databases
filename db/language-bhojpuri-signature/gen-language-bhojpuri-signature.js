(function(){'use strict';
/* JAH The Bhojpuri to English Signature Database generator — jahdb-language-bhojpuri-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LBHOS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Bhojpuri Language Overview (Signature Edition) - overview",
  "Bhojpuri Writing System (Devanagari and Kaithi) (Signature Edition) - script",
  "Bhojpuri Pronunciation and Phonology (Signature Edition) - sounds",
  "Bhojpuri Core Nouns I (Signature Edition) - words",
  "Bhojpuri Core Verbs I (Signature Edition) - words",
  "Bhojpuri Adjectives and Adverbs (Signature Edition) - words",
  "Bhojpuri Pronouns (Signature Edition) - words",
  "Bhojpuri Numbers and Time (Signature Edition) - words",
  "Bhojpuri Greetings and Everyday Phrases (Signature Edition) - phrases"
 ],
 "Compounded": [
  "Bhojpuri Grammar Essentials (Signature Edition) - grammar",
  "Bhojpuri Home and Family Sentences (Signature Edition) - sentences",
  "Bhojpuri Food and Cooking Sentences (Signature Edition) - sentences",
  "Bhojpuri Travel and Directions Sentences (Signature Edition) - sentences",
  "Bhojpuri Work and School Sentences (Signature Edition) - sentences",
  "Bhojpuri Health and Body Sentences (Signature Edition) - sentences",
  "Bhojpuri Emotions and Feelings Sentences (Signature Edition) - sentences",
  "Bhojpuri Nature and Weather Sentences (Signature Edition) - sentences",
  "Bhojpuri Shopping and Money Sentences (Signature Edition) - sentences",
  "Bhojpuri Friendship and Social Life Sentences (Signature Edition) - sentences",
  "Bhojpuri Technology and Communication Sentences (Signature Edition) - sentences"
 ],
 "Advanced": [
  "Bhojpuri Verb Tenses in Sentences (Signature Edition) - grammar",
  "Bhojpuri Questions and Answers (Signature Edition) - sentences",
  "Bhojpuri Commands and Requests (Signature Edition) - sentences",
  "Bhojpuri Descriptions of People and Places (Signature Edition) - sentences",
  "Bhojpuri Story I: The Farmer and the River (Signature Edition) - stories",
  "Bhojpuri Story II: The Market Day (Signature Edition) - stories",
  "Bhojpuri Story III: The Journey Ahead (Signature Edition) - stories",
  "Bhojpuri Idioms and Proverbs (Signature Edition) - idioms",
  "Bhojpuri Formal and Polite Registers (Signature Edition) - registers",
  "Bhojpuri Compound and Complex Sentences (Signature Edition) - sentences",
  "Bhojpuri Conversation: At the Market (Signature Edition) - dialogue",
  "Bhojpuri Conversation: Meeting a Friend (Signature Edition) - dialogue",
  "Bhojpuri Conversation: Solving a Problem (Signature Edition) - dialogue",
  "Bhojpuri Mastery Review and Full Reference (Signature Edition) - reference"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Bhojpuri Language Study — "+safe+"\n"
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
    demo:{kind:"bhojpuri-language-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-bhojpuri-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-bhojpuri-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
