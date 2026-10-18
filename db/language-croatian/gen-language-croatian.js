(function(){'use strict';
/* JAH The Croatian Language Database generator — jahdb-language-croatian-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LHRV-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Croatian Language Overview - Foundations",
  "Croatian Writing System and Alphabet - Foundations",
  "Croatian Pronunciation and Phonology - Foundations",
  "Croatian Core Nouns I - Foundations",
  "Croatian Core Verbs I - Foundations",
  "Croatian Adjectives and Adverbs - Foundations",
  "Croatian Pronouns - Foundations",
  "Croatian Numbers and Time - Foundations",
  "Croatian Greetings and Everyday Phrases - Foundations",
  "Croatian Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Croatian At Home and with Family - Compounded",
  "Croatian Food and Cooking - Compounded",
  "Croatian Travel and Directions - Compounded",
  "Croatian Work and School - Compounded",
  "Croatian Health and the Body - Compounded",
  "Croatian Emotions and Feelings - Compounded",
  "Croatian Nature and Weather - Compounded",
  "Croatian Shopping and Money - Compounded",
  "Croatian Friendship and Social Life - Compounded",
  "Croatian Technology and Communication - Compounded",
  "Croatian Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Croatian Questions and Answers - Advanced",
  "Croatian Commands and Requests - Advanced",
  "Croatian Descriptions of People and Places - Advanced",
  "Croatian Story I: Dje\u010dak i pas - Advanced",
  "Croatian Story II: Seljak - Advanced",
  "Croatian Story III: Nova \u0161kola - Advanced",
  "Croatian Idioms and Proverbs - Advanced",
  "Croatian Formal and Polite Registers - Advanced",
  "Croatian Compound and Complex Sentences - Advanced",
  "Croatian Conversation: Na tr\u017enici - Advanced",
  "Croatian Conversation: Susret s prijateljem - Advanced",
  "Croatian Conversation: Rje\u0161avanje problema - Advanced",
  "Croatian Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Croatian Study — "+safe+"\n"
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
    demo:{kind:"language-croatian-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-croatian-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-croatian',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
