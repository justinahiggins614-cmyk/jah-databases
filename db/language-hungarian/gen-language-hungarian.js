(function(){'use strict';
/* JAH The Hungarian Language Database generator — jahdb-language-hungarian-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LHUN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Hungarian Language Overview - Foundations",
  "Hungarian Writing System and Alphabet - Foundations",
  "Hungarian Pronunciation and Phonology - Foundations",
  "Hungarian Core Nouns I - Foundations",
  "Hungarian Core Verbs I - Foundations",
  "Hungarian Adjectives and Adverbs - Foundations",
  "Hungarian Pronouns - Foundations",
  "Hungarian Numbers and Time - Foundations",
  "Hungarian Greetings and Everyday Phrases - Foundations",
  "Hungarian Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Hungarian at Home and with Family - Compounded",
  "Hungarian Food and Cooking - Compounded",
  "Hungarian Travel and Directions - Compounded",
  "Hungarian Work and School - Compounded",
  "Hungarian Health and the Body - Compounded",
  "Hungarian Emotions and Feelings - Compounded",
  "Hungarian Nature and Weather - Compounded",
  "Hungarian Shopping and Money - Compounded",
  "Hungarian Friendship and Social Life - Compounded",
  "Hungarian Technology and Communication - Compounded",
  "Hungarian Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Hungarian Questions and Answers - Advanced",
  "Hungarian Commands and Requests - Advanced",
  "Hungarian Descriptions of People and Places - Advanced",
  "Hungarian Story I: King Matthias and the Shepherd - Advanced",
  "Hungarian Story II: King Matthias and the Clever Peasant - Advanced",
  "Hungarian Story III: The New School in Budapest - Advanced",
  "Hungarian Idioms and Proverbs - Advanced",
  "Hungarian Formal and Polite Registers - Advanced",
  "Hungarian Compound and Complex Sentences - Advanced",
  "Hungarian Conversation: At the Market - Advanced",
  "Hungarian Conversation: Meeting a Friend - Advanced",
  "Hungarian Conversation: Solving a Problem - Advanced",
  "Hungarian Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hungarian Study — "+safe+"\n"
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
    demo:{kind:"hungarian-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-hungarian-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-hungarian',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
