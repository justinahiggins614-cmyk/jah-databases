(function(){'use strict';
/* JAH The Mongolian Language Database generator — jahdb-language-mongolian-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LMON-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Mongolian Language Overview - Foundations",
  "Mongolian Writing System and Alphabet - Foundations",
  "Mongolian Pronunciation and Phonology - Foundations",
  "Mongolian Core Nouns I - Foundations",
  "Mongolian Core Verbs I - Foundations",
  "Mongolian Adjectives and Adverbs - Foundations",
  "Mongolian Pronouns - Foundations",
  "Mongolian Numbers and Time - Foundations",
  "Mongolian Greetings and Everyday Phrases - Foundations",
  "Mongolian Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Mongolian At Home and with Family - Compounded",
  "Mongolian Food and Cooking - Compounded",
  "Mongolian Travel and Directions - Compounded",
  "Mongolian Work and School - Compounded",
  "Mongolian Health and the Body - Compounded",
  "Mongolian Emotions and Feelings - Compounded",
  "Mongolian Nature and Weather - Compounded",
  "Mongolian Shopping and Money - Compounded",
  "Mongolian Friendship and Social Life - Compounded",
  "Mongolian Technology and Communication - Compounded",
  "Mongolian Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Mongolian Questions and Answers - Advanced",
  "Mongolian Commands and Requests - Advanced",
  "Mongolian Descriptions of People and Places - Advanced",
  "Mongolian Story I: \u0425\u04af\u04af\u0445\u044d\u0434 \u0431\u0430 \u043d\u043e\u0445\u043e\u0439 - Advanced",
  "Mongolian Story II: \u041c\u0430\u043b\u0447\u0438\u043d - Advanced",
  "Mongolian Story III: \u0428\u0438\u043d\u044d \u0441\u0443\u0440\u0433\u0443\u0443\u043b\u044c - Advanced",
  "Mongolian Idioms and Proverbs - Advanced",
  "Mongolian Formal and Polite Registers - Advanced",
  "Mongolian Compound and Complex Sentences - Advanced",
  "Mongolian Conversation: \u0417\u0430\u0445\u0430\u0434 - Advanced",
  "Mongolian Conversation: \u041d\u0430\u0439\u0437\u0442\u0430\u0439\u0433\u0430\u0430 \u0443\u0443\u043b\u0437\u0430\u0445 - Advanced",
  "Mongolian Conversation: \u0410\u0441\u0443\u0443\u0434\u043b\u044b\u0433 \u0448\u0438\u0439\u0434\u044d\u0445 - Advanced",
  "Mongolian Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Mongolian Study — "+safe+"\n"
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
    demo:{kind:"language-mongolian-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-mongolian-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-mongolian',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
