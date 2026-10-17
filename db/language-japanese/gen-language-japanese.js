(function(){'use strict';
/* JAH The Japanese to English Database generator — jahdb-language-japanese-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LJPN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Japanese Language Overview - Foundations",
  "Japanese Writing System: Hiragana, Katakana, and Kanji - Foundations",
  "Japanese Pronunciation and Phonology - Foundations",
  "Japanese Core Nouns I: People, Places, and Things - Foundations",
  "Japanese Core Verbs I: Everyday Actions - Foundations",
  "Japanese Adjectives and Adverbs - Foundations",
  "Japanese Pronouns: I, You, This, That, Who - Foundations",
  "Japanese Numbers and Time - Foundations",
  "Japanese Greetings and Everyday Phrases - Foundations",
  "Japanese Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Japanese Home and Family Sentences - Compounded",
  "Japanese Food and Cooking Sentences - Compounded",
  "Japanese Travel and Directions Sentences - Compounded",
  "Japanese Work and School Sentences - Compounded",
  "Japanese Health and Body Sentences - Compounded",
  "Japanese Emotions and Feelings Sentences - Compounded",
  "Japanese Nature and Weather Sentences - Compounded",
  "Japanese Shopping and Money Sentences - Compounded",
  "Japanese Friendship and Social Life Sentences - Compounded",
  "Japanese Technology and Communication Sentences - Compounded"
 ],
 "Advanced": [
  "Japanese Verb Tenses in Sentences - Advanced",
  "Japanese Questions and Answers - Advanced",
  "Japanese Commands and Requests - Advanced",
  "Japanese Descriptions of People and Places - Advanced",
  "Japanese Short Story I: A Simple Day - Advanced",
  "Japanese Short Story II: A Past Adventure - Advanced",
  "Japanese Short Story III: A Future Dream - Advanced",
  "Japanese Idioms and Proverbs - Advanced",
  "Japanese Formal and Polite Registers - Advanced",
  "Japanese Compound and Complex Sentences - Advanced",
  "Japanese Conversation: At the Market - Advanced",
  "Japanese Conversation: Meeting a Friend - Advanced",
  "Japanese Conversation: Solving a Problem - Advanced",
  "Japanese Mastery Review and Full Reference - Advanced"
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
    demo:{kind:"language-lesson-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-japanese-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-japanese',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
