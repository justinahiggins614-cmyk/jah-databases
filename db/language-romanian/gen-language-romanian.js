(function(){'use strict';
/* JAH The Romanian to English Database generator — jahdb-language-romanian-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LRON-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Romanian Language Overview - Foundations",
  "Romanian Writing System and Alphabet - Foundations",
  "Romanian Pronunciation and Phonology - Foundations",
  "Romanian Core Nouns I - Foundations",
  "Romanian Core Verbs I - Foundations",
  "Romanian Adjectives and Adverbs - Foundations",
  "Romanian Pronouns - Foundations",
  "Romanian Numbers and Time - Foundations",
  "Romanian Greetings and Everyday Phrases - Foundations",
  "Romanian Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Romanian at Home and with Family - Compounded",
  "Romanian Food and Cooking - Compounded",
  "Romanian Travel and Directions - Compounded",
  "Romanian Work and School - Compounded",
  "Romanian Health and the Body - Compounded",
  "Romanian Emotions and Feelings - Compounded",
  "Romanian Nature and Weather - Compounded",
  "Romanian Shopping and Money - Compounded",
  "Romanian Friendship and Social Life - Compounded",
  "Romanian Technology and Communication - Compounded",
  "Romanian Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Romanian Questions and Answers - Advanced",
  "Romanian Commands and Requests - Advanced",
  "Romanian Descriptions of People and Places - Advanced",
  "Romanian Story I: The Clever Shepherd - Advanced",
  "Romanian Story II: The Lost Key - Advanced",
  "Romanian Story III: The New School - Advanced",
  "Romanian Idioms and Proverbs - Advanced",
  "Romanian Formal and Polite Registers - Advanced",
  "Romanian Compound and Complex Sentences - Advanced",
  "Romanian Conversation: At the Market - Advanced",
  "Romanian Conversation: Meeting a Friend - Advanced",
  "Romanian Conversation: Solving a Problem - Advanced",
  "Romanian Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Romanian Study — "+safe+"\n"
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
    demo:{kind:"romanian-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-romanian-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-romanian',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
