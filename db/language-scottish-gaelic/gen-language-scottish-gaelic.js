(function(){'use strict';
/* JAH The Scottish Gaelic to English Database generator — jahdb-language-scottish-gaelic-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LSCG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Scottish Gaelic Language Overview - Foundations",
  "Scottish Gaelic Writing System and Alphabet - Foundations",
  "Scottish Gaelic Pronunciation and Phonology - Foundations",
  "Scottish Gaelic Core Nouns I - Foundations",
  "Scottish Gaelic Core Verbs I - Foundations",
  "Scottish Gaelic Adjectives and Adverbs - Foundations",
  "Scottish Gaelic Pronouns - Foundations",
  "Scottish Gaelic Numbers and Time - Foundations",
  "Scottish Gaelic Greetings and Everyday Phrases - Foundations",
  "Scottish Gaelic Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Scottish Gaelic at Home and with Family - Compounded",
  "Scottish Gaelic Food and Cooking - Compounded",
  "Scottish Gaelic Travel and Directions - Compounded",
  "Scottish Gaelic Work and School - Compounded",
  "Scottish Gaelic Health and the Body - Compounded",
  "Scottish Gaelic Emotions and Feelings - Compounded",
  "Scottish Gaelic Nature and Weather - Compounded",
  "Scottish Gaelic Shopping and Money - Compounded",
  "Scottish Gaelic Friendship and Social Life - Compounded",
  "Scottish Gaelic Technology and Communication - Compounded",
  "Scottish Gaelic Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Scottish Gaelic Questions and Answers - Advanced",
  "Scottish Gaelic Commands and Requests - Advanced",
  "Scottish Gaelic Descriptions of People and Places - Advanced",
  "Scottish Gaelic Story I: The Clever Shepherd - Advanced",
  "Scottish Gaelic Story II: The Lost Key - Advanced",
  "Scottish Gaelic Story III: The New School - Advanced",
  "Scottish Gaelic Idioms and Proverbs - Advanced",
  "Scottish Gaelic Formal and Polite Registers - Advanced",
  "Scottish Gaelic Compound and Complex Sentences - Advanced",
  "Scottish Gaelic Conversation: At the Market - Advanced",
  "Scottish Gaelic Conversation: Meeting a Friend - Advanced",
  "Scottish Gaelic Conversation: Solving a Problem - Advanced",
  "Scottish Gaelic Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Scottish_Gaelic Study — "+safe+"\n"
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
    demo:{kind:"scottish_gaelic-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-scottish-gaelic-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-scottish-gaelic',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
