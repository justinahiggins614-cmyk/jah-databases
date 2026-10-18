(function(){'use strict';
/* JAH The Dutch Language Database generator — jahdb-language-dutch-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LNLD-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Dutch Language Overview - Foundations",
  "Dutch Writing System and Alphabet - Foundations",
  "Dutch Pronunciation and Phonology - Foundations",
  "Dutch Core Nouns I - Foundations",
  "Dutch Core Verbs I - Foundations",
  "Dutch Adjectives and Adverbs - Foundations",
  "Dutch Pronouns - Foundations",
  "Dutch Numbers and Time - Foundations",
  "Dutch Greetings and Everyday Phrases - Foundations",
  "Dutch Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Dutch at Home and with Family - Compounded",
  "Dutch Food and Cooking - Compounded",
  "Dutch Travel and Directions - Compounded",
  "Dutch Work and School - Compounded",
  "Dutch Health and the Body - Compounded",
  "Dutch Emotions and Feelings - Compounded",
  "Dutch Nature and Weather - Compounded",
  "Dutch Shopping and Money - Compounded",
  "Dutch Friendship and Social Life - Compounded",
  "Dutch Technology and Communication - Compounded",
  "Dutch Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Dutch Questions and Answers - Advanced",
  "Dutch Commands and Requests - Advanced",
  "Dutch Descriptions of People and Places - Advanced",
  "Dutch Story I: The Clever Boy - Advanced",
  "Dutch Story II: The Lost Bicycle - Advanced",
  "Dutch Story III: The New School - Advanced",
  "Dutch Idioms and Proverbs - Advanced",
  "Dutch Formal and Polite Registers - Advanced",
  "Dutch Compound and Complex Sentences - Advanced",
  "Dutch Conversation: At the Market - Advanced",
  "Dutch Conversation: Meeting a Friend - Advanced",
  "Dutch Conversation: Solving a Problem - Advanced",
  "Dutch Mastery Review and Full Reference - Advanced"
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Dutch Study — "+safe+"\n"
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
    demo:{kind:"dutch-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-dutch-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-dutch',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
