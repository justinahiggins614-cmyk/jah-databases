(function(){'use strict';
/* JAH The Danish Language Database generator — jahdb-language-danish-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LDAN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Danish Language Overview - Foundations",
  "Danish Writing System and Alphabet - Foundations",
  "Danish Pronunciation and Phonology - Foundations",
  "Danish Core Nouns I - Foundations",
  "Danish Core Verbs I - Foundations",
  "Danish Adjectives and Adverbs - Foundations",
  "Danish Pronouns - Foundations",
  "Danish Numbers and Time - Foundations",
  "Danish Greetings and Everyday Phrases - Foundations",
  "Danish Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Danish At Home and with Family - Compounded",
  "Danish Food and Cooking - Compounded",
  "Danish Travel and Directions - Compounded",
  "Danish Work and School - Compounded",
  "Danish Health and the Body - Compounded",
  "Danish Emotions and Feelings - Compounded",
  "Danish Nature and Weather - Compounded",
  "Danish Shopping and Money - Compounded",
  "Danish Friendship and Social Life - Compounded",
  "Danish Technology and Communication - Compounded",
  "Danish Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Danish Questions and Answers - Advanced",
  "Danish Commands and Requests - Advanced",
  "Danish Descriptions of People and Places - Advanced",
  "Danish Story I: Drengen og hunden - Advanced",
  "Danish Story II: Landmanden - Advanced",
  "Danish Story III: Den nye skole - Advanced",
  "Danish Idioms and Proverbs - Advanced",
  "Danish Formal and Polite Registers - Advanced",
  "Danish Compound and Complex Sentences - Advanced",
  "Danish Conversation: P\u00e5 markedet - Advanced",
  "Danish Conversation: M\u00f8de en ven - Advanced",
  "Danish Conversation: L\u00f8se et problem - Advanced",
  "Danish Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Danish Study — "+safe+"\n"
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
    demo:{kind:"language-danish-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-danish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-danish',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
