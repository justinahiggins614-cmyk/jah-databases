(function(){'use strict';
/* JAH The Haitian Creole Language Database generator — jahdb-language-haitian-creole-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LHAT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Haitian Creole Language Overview - Foundations",
  "Haitian Creole Writing System and Alphabet - Foundations",
  "Haitian Creole Pronunciation and Phonology - Foundations",
  "Haitian Creole Core Nouns I - Foundations",
  "Haitian Creole Core Verbs I - Foundations",
  "Haitian Creole Adjectives and Adverbs - Foundations",
  "Haitian Creole Pronouns - Foundations",
  "Haitian Creole Numbers and Time - Foundations",
  "Haitian Creole Greetings and Everyday Phrases - Foundations",
  "Haitian Creole Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Haitian Creole at Home and with Family - Compounded",
  "Haitian Creole Food and Cooking - Compounded",
  "Haitian Creole Travel and Directions - Compounded",
  "Haitian Creole Work and School - Compounded",
  "Haitian Creole Health and the Body - Compounded",
  "Haitian Creole Emotions and Feelings - Compounded",
  "Haitian Creole Nature and Weather - Compounded",
  "Haitian Creole Shopping and Money - Compounded",
  "Haitian Creole Friendship and Social Life - Compounded",
  "Haitian Creole Technology and Communication - Compounded",
  "Haitian Creole Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Haitian Creole Questions and Answers - Advanced",
  "Haitian Creole Commands and Requests - Advanced",
  "Haitian Creole Descriptions of People and Places - Advanced",
  "Haitian Creole Story I: Bouki and Malis at the River - Advanced",
  "Haitian Creole Story II: Bouki and the Clever Answer - Advanced",
  "Haitian Creole Story III: The New School in Port-au-Prince - Advanced",
  "Haitian Creole Idioms and Proverbs - Advanced",
  "Haitian Creole Formal and Polite Registers - Advanced",
  "Haitian Creole Compound and Complex Sentences - Advanced",
  "Haitian Creole Conversation: At the Market - Advanced",
  "Haitian Creole Conversation: Meeting a Friend - Advanced",
  "Haitian Creole Conversation: Solving a Problem - Advanced",
  "Haitian Creole Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Haitian Creole Study — "+safe+"\n"
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
    demo:{kind:"haitian-creole-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-haitian-creole-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-haitian-creole',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
