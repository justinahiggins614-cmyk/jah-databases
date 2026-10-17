(function(){'use strict';
/* JAH The Language Arts Quiz Signature Database generator — jahdb-quiz-language-arts-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-QZLAS-";
var FIELDS=["Vocabulary","Grammar","Spelling and Punctuation","Literature","Wordplay and Puzzles","Reading and Rhetoric","Poetry and Prosody"];
var TOPICS={
 "Vocabulary": [
  "Easy Synonyms Quiz (Signature Edition) - Vocabulary",
  "Easy Antonyms Quiz (Signature Edition) - Vocabulary",
  "Common Prefixes Quiz (Signature Edition) - Vocabulary",
  "Commonly Confused Words Quiz (Signature Edition) - Vocabulary",
  "Suffixes and Word Endings Quiz (Signature Edition) - Vocabulary",
  "Advanced Synonyms Quiz (Signature Edition) - Vocabulary",
  "Graduate-Level Vocabulary Quiz (Signature Edition) - Vocabulary"
 ],
 "Grammar": [
  "Parts of Speech Basics Quiz (Signature Edition) - Grammar",
  "Simple and Compound Sentences Quiz (Signature Edition) - Grammar",
  "Subject-Verb Agreement Basics Quiz (Signature Edition) - Grammar",
  "Pronoun Agreement Quiz (Signature Edition) - Grammar",
  "Verb Tenses Quiz (Signature Edition) - Grammar",
  "Dangling and Misplaced Modifiers Quiz (Signature Edition) - Grammar",
  "Subjunctive Mood and Parallel Structure Quiz (Signature Edition) - Grammar"
 ],
 "Spelling and Punctuation": [
  "Basic Spelling Quiz (Signature Edition) - Spelling and Punctuation",
  "Plurals Quiz (Signature Edition) - Spelling and Punctuation",
  "Apostrophes Quiz (Signature Edition) - Spelling and Punctuation",
  "Commas Quiz (Signature Edition) - Spelling and Punctuation",
  "Tricky Spellings Quiz (Signature Edition) - Spelling and Punctuation"
 ],
 "Literature": [
  "Classic Childrens Literature Quiz (Signature Edition) - Literature",
  "Literary Terms Basics Quiz (Signature Edition) - Literature",
  "Famous Opening Lines Quiz (Signature Edition) - Literature",
  "American Classics Quiz (Signature Edition) - Literature",
  "Shakespeare Quiz (Signature Edition) - Literature",
  "Literary Movements Quiz (Signature Edition) - Literature"
 ],
 "Wordplay and Puzzles": [
  "Anagrams Quiz (Signature Edition) - Wordplay and Puzzles",
  "Palindromes and Word Patterns Quiz (Signature Edition) - Wordplay and Puzzles",
  "Riddles and Word Riddles Quiz (Signature Edition) - Wordplay and Puzzles",
  "Cryptic-Style Wordplay Quiz (Signature Edition) - Wordplay and Puzzles"
 ],
 "Reading and Rhetoric": [
  "Figurative Language Quiz (Signature Edition) - Reading and Rhetoric",
  "Rhetorical Devices Quiz (Signature Edition) - Reading and Rhetoric",
  "Reading Inference Quiz (Signature Edition) - Reading and Rhetoric"
 ],
 "Poetry and Prosody": [
  "Poetry Forms Quiz (Signature Edition) - Poetry and Prosody",
  "Meter and Sound Devices Quiz (Signature Edition) - Poetry and Prosody"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Quiz Study — "+safe+"\n"
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
    name:topic+' — quiz record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A quiz record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"quiz-runner",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-quiz-language-arts-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('quiz-language-arts-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
