(function(){'use strict';
/* JAH The Hindi to English Database generator — jahdb-language-hindi-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LHIN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Hindi Language Overview - Foundations",
  "Hindi Writing System: Devanagari - Foundations",
  "Hindi Pronunciation and Phonology - Foundations",
  "Hindi Core Nouns I: People, Places, Things - Foundations",
  "Hindi Core Verbs I: Essential Actions - Foundations",
  "Hindi Adjectives and Adverbs - Foundations",
  "Hindi Pronouns: Full Paradigms - Foundations",
  "Hindi Numbers, Time, Days, and Dates - Foundations",
  "Hindi Greetings and Everyday Phrases - Foundations",
  "Hindi Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Hindi Sentences: Home and Family - Compounded",
  "Hindi Sentences: Food and Cooking - Compounded",
  "Hindi Sentences: Travel and Directions - Compounded",
  "Hindi Sentences: Work and School - Compounded",
  "Hindi Sentences: Health and the Body - Compounded",
  "Hindi Sentences: Emotions and Feelings - Compounded",
  "Hindi Sentences: Nature and Weather - Compounded",
  "Hindi Sentences: Shopping and Money - Compounded",
  "Hindi Sentences: Friendship and Social Life - Compounded",
  "Hindi Sentences: Technology and Communication - Compounded"
 ],
 "Advanced": [
  "Hindi Verb Tenses in Sentences - Advanced",
  "Hindi Questions and Answers - Advanced",
  "Hindi Commands and Polite Requests - Advanced",
  "Hindi Descriptions: People and Places - Advanced",
  "Hindi Story I: A Simple Story - Advanced",
  "Hindi Story II: A Story in the Past Tense - Advanced",
  "Hindi Story III: A Story in Future and Conditional - Advanced",
  "Hindi Idioms and Proverbs - Advanced",
  "Hindi Formal and Polite Registers - Advanced",
  "Hindi Compound and Complex Sentences - Advanced",
  "Hindi Conversation: At the Market - Advanced",
  "Hindi Conversation: Meeting a Friend - Advanced",
  "Hindi Conversation: Solving a Problem - Advanced",
  "Hindi Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hindi Lesson — "+safe+"\n"
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
    demo:{kind:"hindi-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-hindi-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-hindi',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
