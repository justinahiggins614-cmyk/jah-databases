(function(){'use strict';
/* JAH Korean Language Database generator — jahdb-language-korean-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LKOR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Korean Language Overview - Foundations",
  "Hangul: The Korean Writing System - Foundations",
  "Korean Pronunciation and Phonology - Foundations",
  "Core Korean Nouns I: People, Places, Things - Foundations",
  "Core Korean Verbs I: Essential Actions - Foundations",
  "Korean Adjectives and Adverbs - Foundations",
  "Korean Pronouns and Demonstratives - Foundations",
  "Korean Numbers, Dates, and Time - Foundations",
  "Korean Greetings and Everyday Phrases - Foundations",
  "Korean Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Home and Family Sentences - Compounded",
  "Food and Cooking Sentences - Compounded",
  "Travel and Directions Sentences - Compounded",
  "Work and School Sentences - Compounded",
  "Health and Body Sentences - Compounded",
  "Emotions and Feelings Sentences - Compounded",
  "Nature and Weather Sentences - Compounded",
  "Shopping and Money Sentences - Compounded",
  "Friendship and Social Life Sentences - Compounded",
  "Technology and Communication Sentences - Compounded",
  "Korean Verb Tenses in Sentences - Compounded",
  "Korean Questions and Answers - Compounded",
  "Korean Commands and Requests - Compounded"
 ],
 "Advanced": [
  "Describing People and Places in Korean - Advanced",
  "Korean Story I: A Day at the Park - Advanced",
  "Korean Story II: The Lost Umbrella - Advanced",
  "Korean Story III: The Future Garden - Advanced",
  "Korean Idioms and Proverbs - Advanced",
  "Formal and Polite Registers in Korean - Advanced",
  "Compound and Complex Korean Sentences - Advanced",
  "Korean Conversation: At the Market - Advanced",
  "Korean Conversation: Meeting a Friend - Advanced",
  "Korean Conversation: Solving a Problem - Advanced",
  "Korean Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Lesson — "+safe+"\n"
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
    demo:{kind:"language-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-korean-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-korean',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
