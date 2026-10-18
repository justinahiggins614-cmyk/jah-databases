(function(){'use strict';
/* JAH The Morse Code to English Database generator — jahdb-language-morse-code-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LMOR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Morse Code Language Overview - Foundations",
  "Morse Code Writing System and Alphabet - Foundations",
  "Morse Code Pronunciation and Phonology - Foundations",
  "Morse Code Core Nouns I - Foundations",
  "Morse Code Core Verbs I - Foundations",
  "Morse Code Adjectives and Adverbs - Foundations",
  "Morse Code Pronouns - Foundations",
  "Morse Code Numbers and Time - Foundations",
  "Morse Code Greetings and Everyday Phrases - Foundations",
  "Morse Code Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Morse Code at Home and with Family - Compounded",
  "Morse Code Food and Cooking - Compounded",
  "Morse Code Travel and Directions - Compounded",
  "Morse Code Work and School - Compounded",
  "Morse Code Health and the Body - Compounded",
  "Morse Code Emotions and Feelings - Compounded",
  "Morse Code Nature and Weather - Compounded",
  "Morse Code Shopping and Money - Compounded",
  "Morse Code Friendship and Social Life - Compounded",
  "Morse Code Technology and Communication - Compounded",
  "Morse Code Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Morse Code Questions and Answers - Advanced",
  "Morse Code Commands and Requests - Advanced",
  "Morse Code Descriptions of People and Places - Advanced",
  "Morse Code Story I: What Hath God Wrought - Advanced",
  "Morse Code Story II: The Titanic Calls - Advanced",
  "Morse Code Story III: The New Operator - Advanced",
  "Morse Code Idioms and Proverbs - Advanced",
  "Morse Code Formal and Polite Registers - Advanced",
  "Morse Code Compound and Complex Sentences - Advanced",
  "Morse Code Conversation: At the Market - Advanced",
  "Morse Code Conversation: Meeting a Friend - Advanced",
  "Morse Code Conversation: Solving a Problem - Advanced",
  "Morse Code Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Morse_Code Study — "+safe+"\n"
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
    demo:{kind:"morse_code-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-morse-code-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-morse-code',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
