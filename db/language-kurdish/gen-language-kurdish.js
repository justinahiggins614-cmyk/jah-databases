(function(){'use strict';
/* JAH The Kurdish Language Database generator — jahdb-language-kurdish-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LKUR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Kurdish Language Overview - Foundations",
  "Kurdish Writing System and Alphabet - Foundations",
  "Kurdish Pronunciation and Phonology - Foundations",
  "Kurdish Core Nouns I - Foundations",
  "Kurdish Core Verbs I - Foundations",
  "Kurdish Adjectives and Adverbs - Foundations",
  "Kurdish Pronouns - Foundations",
  "Kurdish Numbers and Time - Foundations",
  "Kurdish Greetings and Everyday Phrases - Foundations",
  "Kurdish Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Kurdish at Home and with Family - Compounded",
  "Kurdish Food and Cooking - Compounded",
  "Kurdish Travel and Directions - Compounded",
  "Kurdish Work and School - Compounded",
  "Kurdish Health and the Body - Compounded",
  "Kurdish Emotions and Feelings - Compounded",
  "Kurdish Nature and Weather - Compounded",
  "Kurdish Shopping and Money - Compounded",
  "Kurdish Friendship and Social Life - Compounded",
  "Kurdish Technology and Communication - Compounded",
  "Kurdish Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Kurdish Questions and Answers - Advanced",
  "Kurdish Commands and Requests - Advanced",
  "Kurdish Descriptions of People and Places - Advanced",
  "Kurdish Story I: The Clever Shepherd - Advanced",
  "Kurdish Story II: The Lost Lamb - Advanced",
  "Kurdish Story III: The New School - Advanced",
  "Kurdish Idioms and Proverbs - Advanced",
  "Kurdish Formal and Polite Registers - Advanced",
  "Kurdish Compound and Complex Sentences - Advanced",
  "Kurdish Conversation: At the Market - Advanced",
  "Kurdish Conversation: Meeting a Friend - Advanced",
  "Kurdish Conversation: Solving a Problem - Advanced",
  "Kurdish Mastery Review and Full Reference - Advanced"
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Kurdish Study — "+safe+"\n"
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
    demo:{kind:"kurdish-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-kurdish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-kurdish',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
