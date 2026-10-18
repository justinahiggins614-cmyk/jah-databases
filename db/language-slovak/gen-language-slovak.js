(function(){'use strict';
/* JAH The Slovak Language Database generator — jahdb-language-slovak-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LSLK-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Slovak Language Overview - Foundations",
  "Slovak Writing System and Alphabet - Foundations",
  "Slovak Pronunciation and Phonology - Foundations",
  "Slovak Core Nouns I - Foundations",
  "Slovak Core Verbs I - Foundations",
  "Slovak Adjectives and Adverbs - Foundations",
  "Slovak Pronouns - Foundations",
  "Slovak Numbers and Time - Foundations",
  "Slovak Greetings and Everyday Phrases - Foundations",
  "Slovak Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Slovak At Home and with Family - Compounded",
  "Slovak Food and Cooking - Compounded",
  "Slovak Travel and Directions - Compounded",
  "Slovak Work and School - Compounded",
  "Slovak Health and the Body - Compounded",
  "Slovak Emotions and Feelings - Compounded",
  "Slovak Nature and Weather - Compounded",
  "Slovak Shopping and Money - Compounded",
  "Slovak Friendship and Social Life - Compounded",
  "Slovak Technology and Communication - Compounded",
  "Slovak Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Slovak Questions and Answers - Advanced",
  "Slovak Commands and Requests - Advanced",
  "Slovak Descriptions of People and Places - Advanced",
  "Slovak Story I: Chlapec a pes - Advanced",
  "Slovak Story II: Ro\u013en\u00edk - Advanced",
  "Slovak Story III: Nov\u00e1 \u0161kola - Advanced",
  "Slovak Idioms and Proverbs - Advanced",
  "Slovak Formal and Polite Registers - Advanced",
  "Slovak Compound and Complex Sentences - Advanced",
  "Slovak Conversation: Na trhu - Advanced",
  "Slovak Conversation: Stretnutie s priate\u013eom - Advanced",
  "Slovak Conversation: Rie\u0161enie probl\u00e9mu - Advanced",
  "Slovak Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Slovak Study — "+safe+"\n"
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
    demo:{kind:"language-slovak-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-slovak-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-slovak',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
