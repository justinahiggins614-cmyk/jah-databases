(function(){'use strict';
/* JAH The Balochi Language Database generator — jahdb-language-balochi-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LBAL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Balochi Language Overview - Foundations",
  "Balochi Writing System and Alphabet - Foundations",
  "Balochi Pronunciation and Phonology - Foundations",
  "Balochi Core Nouns I - Foundations",
  "Balochi Core Verbs I - Foundations",
  "Balochi Adjectives and Adverbs - Foundations",
  "Balochi Pronouns - Foundations",
  "Balochi Numbers and Time - Foundations",
  "Balochi Greetings and Everyday Phrases - Foundations",
  "Balochi Grammar Essentials - Foundations",
 ],
 "Compounded": [
  "Balochi at Home and Family - Compounded",
  "Balochi Food and Cooking - Compounded",
  "Balochi Travel and Directions - Compounded",
  "Balochi Work and School - Compounded",
  "Balochi Health and the Body - Compounded",
  "Balochi Emotions and Feelings - Compounded",
  "Balochi Nature and Weather - Compounded",
  "Balochi Shopping and Money - Compounded",
  "Balochi Friendship and Social Life - Compounded",
  "Balochi Technology and Communication - Compounded",
  "Balochi Verb Tenses in Sentences - Compounded",
 ],
 "Advanced": [
  "Balochi Questions and Answers - Advanced",
  "Balochi Commands and Requests - Advanced",
  "Balochi Descriptions of People and Places - Advanced",
  "Balochi Story I: The Boy and the Lamb - Advanced",
  "Balochi Story II: The Rainy Day - Advanced",
  "Balochi Story III: The Market Trip - Advanced",
  "Balochi Idioms and Proverbs - Advanced",
  "Balochi Formal and Polite Registers - Advanced",
  "Balochi Compound and Complex Sentences - Advanced",
  "Balochi Conversation: At the Market - Advanced",
  "Balochi Conversation: Meeting a Friend - Advanced",
  "Balochi Conversation: Solving a Problem - Advanced",
  "Balochi Mastery Review and Full Reference - Advanced",
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Balochi Study — "+safe+"\n"
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
    demo:{kind:"balochi-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-balochi-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-balochi',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
