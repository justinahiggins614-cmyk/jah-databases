(function(){'use strict';
/* JAH The Latin to English Database generator — jahdb-language-latin-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LLAT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Latin Language Overview - Foundations",
  "Latin Writing System and Alphabet - Foundations",
  "Latin Pronunciation and Phonology - Foundations",
  "Latin Core Nouns I - Foundations",
  "Latin Core Verbs I - Foundations",
  "Latin Adjectives and Adverbs - Foundations",
  "Latin Pronouns - Foundations",
  "Latin Numbers and Time - Foundations",
  "Latin Greetings and Everyday Phrases - Foundations",
  "Latin Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Latin at Home and with Family - Compounded",
  "Latin Food and Cooking - Compounded",
  "Latin Travel and Directions - Compounded",
  "Latin Work and School - Compounded",
  "Latin Health and the Body - Compounded",
  "Latin Emotions and Feelings - Compounded",
  "Latin Nature and Weather - Compounded",
  "Latin Shopping and Money - Compounded",
  "Latin Friendship and Social Life - Compounded",
  "Latin Technology and Communication - Compounded",
  "Latin Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Latin Questions and Answers - Advanced",
  "Latin Commands and Requests - Advanced",
  "Latin Descriptions of People and Places - Advanced",
  "Latin Story I: Romulus and Remus - Advanced",
  "Latin Story II: The Tortoise and the Hare - Advanced",
  "Latin Story III: Cincinnatus at the Plow - Advanced",
  "Latin Idioms and Proverbs - Advanced",
  "Latin Formal and Polite Registers - Advanced",
  "Latin Compound and Complex Sentences - Advanced",
  "Latin Conversation: At the Market - Advanced",
  "Latin Conversation: Meeting a Friend - Advanced",
  "Latin Conversation: Solving a Problem - Advanced",
  "Latin Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Latin Study — "+safe+"\n"
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
    demo:{kind:"latin-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-latin-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-latin',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
