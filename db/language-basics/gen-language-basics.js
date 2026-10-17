(function(){'use strict';
/* JAH The Language Basics Database generator — jahdb-language-basics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LANB-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Language - Foundations",
  "The English Alphabet: 26 Letters - Foundations",
  "Letter Sounds and Phonics: Consonants - Foundations",
  "Vowel Sounds: The Open Doors of Speech - Foundations",
  "Syllables: Breaking Words Apart - Foundations",
  "Blending Sounds Into Words - Foundations",
  "Reading Basics: Direction and Tracking - Foundations",
  "Words: The Building Blocks of Meaning - Foundations",
  "What Is a Noun - Foundations",
  "What Is a Verb - Foundations",
  "What Is an Adjective - Foundations",
  "What Is an Adverb - Foundations",
  "Pronouns: Standing In for Nouns - Foundations"
 ],
 "Compounded": [
  "Articles: A, An, and The - Compounded",
  "Prepositions: Words of Place and Time - Compounded",
  "Conjunctions: Joining Words Together - Compounded",
  "Interjections: Words of Feeling - Compounded",
  "Building a Sentence: Subject and Predicate - Compounded",
  "Sentence Types: Statements, Questions, Commands, Exclamations - Compounded",
  "Capitalization Rules - Compounded",
  "Ending Punctuation: Period, Question Mark, Exclamation Point - Compounded",
  "The Comma: Pauses That Organize - Compounded",
  "Quotation Marks and Dialogue - Compounded",
  "Apostrophes: Possession and Contractions - Compounded",
  "Singular and Plural Nouns - Compounded",
  "Verb Tenses: Past, Present, Future - Compounded"
 ],
 "Advanced": [
  "Subject-Verb Agreement - Advanced",
  "Paragraphs: Building Ideas in Order - Advanced",
  "Compound and Complex Sentences - Advanced",
  "Prefixes and Suffixes: Word Parts - Advanced",
  "Homophones and Commonly Confused Words - Advanced",
  "Reading Fluency and Comprehension Strategies - Advanced",
  "Proofreading and Editing Your Writing - Advanced",
  "From Basics to Mastery: The Language Learning Path - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Basics Study — "+safe+"\n"
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
    name:topic+' — language basics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A language basics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"language-basics-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-basics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-basics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
