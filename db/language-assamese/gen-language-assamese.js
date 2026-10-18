(function(){'use strict';
/* JAH The Assamese Language Database generator — jahdb-language-assamese-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LASM-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Assamese Language Overview - Foundations",
  "Assamese Writing System and Alphabet - Foundations",
  "Assamese Pronunciation and Phonology - Foundations",
  "Assamese Core Nouns I - Foundations",
  "Assamese Core Verbs I - Foundations",
  "Assamese Adjectives and Adverbs - Foundations",
  "Assamese Pronouns - Foundations",
  "Assamese Numbers and Time - Foundations",
  "Assamese Greetings and Everyday Phrases - Foundations",
  "Assamese Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Assamese at Home and with Family - Compounded",
  "Assamese Food and Cooking - Compounded",
  "Assamese Travel and Directions - Compounded",
  "Assamese Work and School - Compounded",
  "Assamese Health and the Body - Compounded",
  "Assamese Emotions and Feelings - Compounded",
  "Assamese Nature and Weather - Compounded",
  "Assamese Shopping and Money - Compounded",
  "Assamese Friendship and Social Life - Compounded",
  "Assamese Technology and Communication - Compounded",
  "Assamese Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Assamese Questions and Answers - Advanced",
  "Assamese Commands and Requests - Advanced",
  "Assamese Descriptions of People and Places - Advanced",
  "Assamese Story I: The Clever Farmer - Advanced",
  "Assamese Story II: The Lost Buffalo - Advanced",
  "Assamese Story III: The New School - Advanced",
  "Assamese Idioms and Proverbs - Advanced",
  "Assamese Formal and Polite Registers - Advanced",
  "Assamese Compound and Complex Sentences - Advanced",
  "Assamese Conversation: At the Market - Advanced",
  "Assamese Conversation: Meeting a Friend - Advanced",
  "Assamese Conversation: Solving a Problem - Advanced",
  "Assamese Mastery Review and Full Reference - Advanced"
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Assamese Study — "+safe+"\n"
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
    demo:{kind:"assamese-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-assamese-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-assamese',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
