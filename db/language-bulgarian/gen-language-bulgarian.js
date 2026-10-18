(function(){'use strict';
/* JAH The Bulgarian Language Database generator — jahdb-language-bulgarian-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LBUL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Bulgarian Language Overview - Foundations",
  "Bulgarian Writing System and Alphabet - Foundations",
  "Bulgarian Pronunciation and Phonology - Foundations",
  "Bulgarian Core Nouns I - Foundations",
  "Bulgarian Core Verbs I - Foundations",
  "Bulgarian Adjectives and Adverbs - Foundations",
  "Bulgarian Pronouns - Foundations",
  "Bulgarian Numbers and Time - Foundations",
  "Bulgarian Greetings and Everyday Phrases - Foundations",
  "Bulgarian Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Bulgarian At Home and with Family - Compounded",
  "Bulgarian Food and Cooking - Compounded",
  "Bulgarian Travel and Directions - Compounded",
  "Bulgarian Work and School - Compounded",
  "Bulgarian Health and the Body - Compounded",
  "Bulgarian Emotions and Feelings - Compounded",
  "Bulgarian Nature and Weather - Compounded",
  "Bulgarian Shopping and Money - Compounded",
  "Bulgarian Friendship and Social Life - Compounded",
  "Bulgarian Technology and Communication - Compounded",
  "Bulgarian Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Bulgarian Questions and Answers - Advanced",
  "Bulgarian Commands and Requests - Advanced",
  "Bulgarian Descriptions of People and Places - Advanced",
  "Bulgarian Story I: \u041c\u043e\u043c\u0447\u0435\u0442\u043e \u0438 \u043a\u0443\u0447\u0435\u0442\u043e - Advanced",
  "Bulgarian Story II: \u0424\u0435\u0440\u043c\u0435\u0440\u044a\u0442 - Advanced",
  "Bulgarian Story III: \u041d\u043e\u0432\u043e\u0442\u043e \u0443\u0447\u0438\u043b\u0438\u0449\u0435 - Advanced",
  "Bulgarian Idioms and Proverbs - Advanced",
  "Bulgarian Formal and Polite Registers - Advanced",
  "Bulgarian Compound and Complex Sentences - Advanced",
  "Bulgarian Conversation: \u041d\u0430 \u043f\u0430\u0437\u0430\u0440\u0430 - Advanced",
  "Bulgarian Conversation: \u0421\u0440\u0435\u0449\u0430 \u0441 \u043f\u0440\u0438\u044f\u0442\u0435\u043b - Advanced",
  "Bulgarian Conversation: \u0420\u0435\u0448\u0430\u0432\u0430\u043d\u0435 \u043d\u0430 \u043f\u0440\u043e\u0431\u043b\u0435\u043c - Advanced",
  "Bulgarian Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Bulgarian Study — "+safe+"\n"
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
    demo:{kind:"language-bulgarian-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-bulgarian-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-bulgarian',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
