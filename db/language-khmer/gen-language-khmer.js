(function(){'use strict';
/* JAH The Khmer Language Database generator — jahdb-language-khmer-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LKHM-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Khmer Language Overview - Foundations",
  "Khmer Writing System and Alphabet - Foundations",
  "Khmer Pronunciation and Phonology - Foundations",
  "Khmer Core Nouns I - Foundations",
  "Khmer Core Verbs I - Foundations",
  "Khmer Adjectives and Adverbs - Foundations",
  "Khmer Pronouns - Foundations",
  "Khmer Numbers and Time - Foundations",
  "Khmer Greetings and Everyday Phrases - Foundations",
  "Khmer Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Khmer at Home and with Family - Compounded",
  "Khmer Food and Cooking - Compounded",
  "Khmer Travel and Directions - Compounded",
  "Khmer Work and School - Compounded",
  "Khmer Health and the Body - Compounded",
  "Khmer Emotions and Feelings - Compounded",
  "Khmer Nature and Weather - Compounded",
  "Khmer Shopping and Money - Compounded",
  "Khmer Friendship and Social Life - Compounded",
  "Khmer Technology and Communication - Compounded",
  "Khmer Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Khmer Questions and Answers - Advanced",
  "Khmer Commands and Requests - Advanced",
  "Khmer Descriptions of People and Places - Advanced",
  "Khmer Story I: The Clever Farmer - Advanced",
  "Khmer Story II: The Lost Buffalo - Advanced",
  "Khmer Story III: The New School - Advanced",
  "Khmer Idioms and Proverbs - Advanced",
  "Khmer Formal and Polite Registers - Advanced",
  "Khmer Compound and Complex Sentences - Advanced",
  "Khmer Conversation: At the Market - Advanced",
  "Khmer Conversation: Meeting a Friend - Advanced",
  "Khmer Conversation: Solving a Problem - Advanced",
  "Khmer Mastery Review and Full Reference - Advanced"
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Khmer Study — "+safe+"\n"
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
    demo:{kind:"khmer-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-khmer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-khmer',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
