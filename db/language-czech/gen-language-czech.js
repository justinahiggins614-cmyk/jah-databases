(function(){'use strict';
/* JAH The Czech Language Database generator — jahdb-language-czech-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LCES-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Czech Language Overview - Foundations",
  "Czech Writing System and Alphabet - Foundations",
  "Czech Pronunciation and Phonology - Foundations",
  "Czech Core Nouns I - Foundations",
  "Czech Core Verbs I - Foundations",
  "Czech Adjectives and Adverbs - Foundations",
  "Czech Pronouns - Foundations",
  "Czech Numbers and Time - Foundations",
  "Czech Greetings and Everyday Phrases - Foundations",
  "Czech Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Czech at Home and with Family - Compounded",
  "Czech Food and Cooking - Compounded",
  "Czech Travel and Directions - Compounded",
  "Czech Work and School - Compounded",
  "Czech Health and the Body - Compounded",
  "Czech Emotions and Feelings - Compounded",
  "Czech Nature and Weather - Compounded",
  "Czech Shopping and Money - Compounded",
  "Czech Friendship and Social Life - Compounded",
  "Czech Technology and Communication - Compounded",
  "Czech Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Czech Questions and Answers - Advanced",
  "Czech Commands and Requests - Advanced",
  "Czech Descriptions of People and Places - Advanced",
  "Czech Story I: Honza and the Dragon - Advanced",
  "Czech Story II: Honza and the Clever Answer - Advanced",
  "Czech Story III: The New School in Prague - Advanced",
  "Czech Idioms and Proverbs - Advanced",
  "Czech Formal and Polite Registers - Advanced",
  "Czech Compound and Complex Sentences - Advanced",
  "Czech Conversation: At the Market - Advanced",
  "Czech Conversation: Meeting a Friend - Advanced",
  "Czech Conversation: Solving a Problem - Advanced",
  "Czech Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Czech Study — "+safe+"\n"
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
    demo:{kind:"czech-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-czech-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-czech',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
