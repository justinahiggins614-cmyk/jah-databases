(function(){'use strict';
/* JAH The Thai to English Database generator — jahdb-language-thai-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LTHA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Thai Language Overview - Foundations",
  "Thai Writing System and Alphabet - Foundations",
  "Thai Pronunciation and Phonology - Foundations",
  "Thai Core Nouns I - Foundations",
  "Thai Core Verbs I - Foundations",
  "Thai Adjectives and Adverbs - Foundations",
  "Thai Pronouns - Foundations",
  "Thai Numbers and Time - Foundations",
  "Thai Greetings and Everyday Phrases - Foundations",
  "Thai Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Thai at Home and with Family - Compounded",
  "Thai Food and Cooking - Compounded",
  "Thai Travel and Directions - Compounded",
  "Thai Work and School - Compounded",
  "Thai Health and the Body - Compounded",
  "Thai Emotions and Feelings - Compounded",
  "Thai Nature and Weather - Compounded",
  "Thai Shopping and Money - Compounded",
  "Thai Friendship and Social Life - Compounded",
  "Thai Technology and Communication - Compounded",
  "Thai Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Thai Questions and Answers - Advanced",
  "Thai Commands and Requests - Advanced",
  "Thai Descriptions of People and Places - Advanced",
  "Thai Story I: The Clever Buffalo Boy - Advanced",
  "Thai Story II: The Lost Key - Advanced",
  "Thai Story III: The New School - Advanced",
  "Thai Idioms and Proverbs - Advanced",
  "Thai Formal and Polite Registers - Advanced",
  "Thai Compound and Complex Sentences - Advanced",
  "Thai Conversation: At the Market - Advanced",
  "Thai Conversation: Meeting a Friend - Advanced",
  "Thai Conversation: Solving a Problem - Advanced",
  "Thai Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Thai Study — "+safe+"\n"
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
    demo:{kind:"thai-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-thai-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-thai',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
