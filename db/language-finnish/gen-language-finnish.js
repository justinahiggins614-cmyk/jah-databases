(function(){'use strict';
/* JAH The Finnish Language Database generator — jahdb-language-finnish-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LFIN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Finnish Language Overview - Foundations",
  "Finnish Writing System and Alphabet - Foundations",
  "Finnish Pronunciation and Phonology - Foundations",
  "Finnish Core Nouns I - Foundations",
  "Finnish Core Verbs I - Foundations",
  "Finnish Adjectives and Adverbs - Foundations",
  "Finnish Pronouns - Foundations",
  "Finnish Numbers and Time - Foundations",
  "Finnish Greetings and Everyday Phrases - Foundations",
  "Finnish Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Finnish At Home and with Family - Compounded",
  "Finnish Food and Cooking - Compounded",
  "Finnish Travel and Directions - Compounded",
  "Finnish Work and School - Compounded",
  "Finnish Health and the Body - Compounded",
  "Finnish Emotions and Feelings - Compounded",
  "Finnish Nature and Weather - Compounded",
  "Finnish Shopping and Money - Compounded",
  "Finnish Friendship and Social Life - Compounded",
  "Finnish Technology and Communication - Compounded",
  "Finnish Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Finnish Questions and Answers - Advanced",
  "Finnish Commands and Requests - Advanced",
  "Finnish Descriptions of People and Places - Advanced",
  "Finnish Story I: Poika ja koira - Advanced",
  "Finnish Story II: Maanviljelij\u00e4 - Advanced",
  "Finnish Story III: Uusi koulu - Advanced",
  "Finnish Idioms and Proverbs - Advanced",
  "Finnish Formal and Polite Registers - Advanced",
  "Finnish Compound and Complex Sentences - Advanced",
  "Finnish Conversation: Torilla - Advanced",
  "Finnish Conversation: Yst\u00e4v\u00e4n tapaaminen - Advanced",
  "Finnish Conversation: Ongelman ratkaisu - Advanced",
  "Finnish Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Finnish Study — "+safe+"\n"
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
    demo:{kind:"language-finnish-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-finnish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-finnish',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
