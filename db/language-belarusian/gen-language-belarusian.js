(function(){'use strict';
/* JAH The Belarusian Language Database generator — jahdb-language-belarusian-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LBEL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Belarusian Language Overview - Foundations",
  "Belarusian Writing System and Alphabet - Foundations",
  "Belarusian Pronunciation and Phonology - Foundations",
  "Belarusian Core Nouns I - Foundations",
  "Belarusian Core Verbs I - Foundations",
  "Belarusian Adjectives and Adverbs - Foundations",
  "Belarusian Pronouns - Foundations",
  "Belarusian Numbers and Time - Foundations",
  "Belarusian Greetings and Everyday Phrases - Foundations",
  "Belarusian Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Belarusian at Home and with Family - Compounded",
  "Belarusian Food and Cooking - Compounded",
  "Belarusian Travel and Directions - Compounded",
  "Belarusian Work and School - Compounded",
  "Belarusian Health and the Body - Compounded",
  "Belarusian Emotions and Feelings - Compounded",
  "Belarusian Nature and Weather - Compounded",
  "Belarusian Shopping and Money - Compounded",
  "Belarusian Friendship and Social Life - Compounded",
  "Belarusian Technology and Communication - Compounded",
  "Belarusian Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Belarusian Questions and Answers - Advanced",
  "Belarusian Commands and Requests - Advanced",
  "Belarusian Descriptions of People and Places - Advanced",
  "Belarusian Story I: The Brave Boy - Advanced",
  "Belarusian Story II: The Clever Answer - Advanced",
  "Belarusian Story III: The New School in Minsk - Advanced",
  "Belarusian Idioms and Proverbs - Advanced",
  "Belarusian Formal and Polite Registers - Advanced",
  "Belarusian Compound and Complex Sentences - Advanced",
  "Belarusian Conversation: At the Market - Advanced",
  "Belarusian Conversation: Meeting a Friend - Advanced",
  "Belarusian Conversation: Solving a Problem - Advanced",
  "Belarusian Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Belarusian Study — "+safe+"\n"
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
    demo:{kind:"belarusian-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-belarusian-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-belarusian',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
