(function(){'use strict';
/* JAH The American Sign Language to English Database generator — jahdb-language-american-sign-language-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LASL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "American Sign Language Language Overview - Foundations",
  "American Sign Language Writing System and Alphabet - Foundations",
  "American Sign Language Pronunciation and Phonology - Foundations",
  "American Sign Language Core Nouns I - Foundations",
  "American Sign Language Core Verbs I - Foundations",
  "American Sign Language Adjectives and Adverbs - Foundations",
  "American Sign Language Pronouns - Foundations",
  "American Sign Language Numbers and Time - Foundations",
  "American Sign Language Greetings and Everyday Phrases - Foundations",
  "American Sign Language Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "American Sign Language at Home and with Family - Compounded",
  "American Sign Language Food and Cooking - Compounded",
  "American Sign Language Travel and Directions - Compounded",
  "American Sign Language Work and School - Compounded",
  "American Sign Language Health and the Body - Compounded",
  "American Sign Language Emotions and Feelings - Compounded",
  "American Sign Language Nature and Weather - Compounded",
  "American Sign Language Shopping and Money - Compounded",
  "American Sign Language Friendship and Social Life - Compounded",
  "American Sign Language Technology and Communication - Compounded",
  "American Sign Language Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "American Sign Language Questions and Answers - Advanced",
  "American Sign Language Commands and Requests - Advanced",
  "American Sign Language Descriptions of People and Places - Advanced",
  "American Sign Language Story I: The Clever Shepherd - Advanced",
  "American Sign Language Story II: The Lost Key - Advanced",
  "American Sign Language Story III: The New School - Advanced",
  "American Sign Language Idioms and Proverbs - Advanced",
  "American Sign Language Formal and Polite Registers - Advanced",
  "American Sign Language Compound and Complex Sentences - Advanced",
  "American Sign Language Conversation: At the Market - Advanced",
  "American Sign Language Conversation: Meeting a Friend - Advanced",
  "American Sign Language Conversation: Solving a Problem - Advanced",
  "American Sign Language Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# American_Sign_Language Study — "+safe+"\n"
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
    demo:{kind:"american_sign_language-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-american-sign-language-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-american-sign-language',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
