(function(){'use strict';
/* JAH The Swedish Language Database generator — jahdb-language-swedish-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LSWE-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Swedish Language Overview - Foundations",
  "Swedish Writing System and Alphabet - Foundations",
  "Swedish Pronunciation and Phonology - Foundations",
  "Swedish Core Nouns I - Foundations",
  "Swedish Core Verbs I - Foundations",
  "Swedish Adjectives and Adverbs - Foundations",
  "Swedish Pronouns - Foundations",
  "Swedish Numbers and Time - Foundations",
  "Swedish Greetings and Everyday Phrases - Foundations",
  "Swedish Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Swedish at Home and with Family - Compounded",
  "Swedish Food and Cooking - Compounded",
  "Swedish Travel and Directions - Compounded",
  "Swedish Work and School - Compounded",
  "Swedish Health and the Body - Compounded",
  "Swedish Emotions and Feelings - Compounded",
  "Swedish Nature and Weather - Compounded",
  "Swedish Shopping and Money - Compounded",
  "Swedish Friendship and Social Life - Compounded",
  "Swedish Technology and Communication - Compounded",
  "Swedish Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Swedish Questions and Answers - Advanced",
  "Swedish Commands and Requests - Advanced",
  "Swedish Descriptions of People and Places - Advanced",
  "Swedish Story I: The Strong Girl - Advanced",
  "Swedish Story II: The Clever Answer - Advanced",
  "Swedish Story III: The New School in Stockholm - Advanced",
  "Swedish Idioms and Proverbs - Advanced",
  "Swedish Formal and Polite Registers - Advanced",
  "Swedish Compound and Complex Sentences - Advanced",
  "Swedish Conversation: At the Market - Advanced",
  "Swedish Conversation: Meeting a Friend - Advanced",
  "Swedish Conversation: Solving a Problem - Advanced",
  "Swedish Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Swedish Study — "+safe+"\n"
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
    demo:{kind:"swedish-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-swedish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-swedish',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
