(function(){'use strict';
/* JAH The Malagasy Language Database generator — jahdb-language-malagasy-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LMLG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Malagasy Language Overview - Foundations",
  "Malagasy Writing System and Alphabet - Foundations",
  "Malagasy Pronunciation and Phonology - Foundations",
  "Malagasy Core Nouns I - Foundations",
  "Malagasy Core Verbs I - Foundations",
  "Malagasy Adjectives and Adverbs - Foundations",
  "Malagasy Pronouns - Foundations",
  "Malagasy Numbers and Time - Foundations",
  "Malagasy Greetings and Everyday Phrases - Foundations",
  "Malagasy Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Malagasy at Home and with Family - Compounded",
  "Malagasy Food and Cooking - Compounded",
  "Malagasy Travel and Directions - Compounded",
  "Malagasy Work and School - Compounded",
  "Malagasy Health and the Body - Compounded",
  "Malagasy Emotions and Feelings - Compounded",
  "Malagasy Nature and Weather - Compounded",
  "Malagasy Shopping and Money - Compounded",
  "Malagasy Friendship and Social Life - Compounded",
  "Malagasy Technology and Communication - Compounded",
  "Malagasy Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Malagasy Questions and Answers - Advanced",
  "Malagasy Commands and Requests - Advanced",
  "Malagasy Descriptions of People and Places - Advanced",
  "Malagasy Story I: The Clever Farmer - Advanced",
  "Malagasy Story II: The Lost Zebu - Advanced",
  "Malagasy Story III: The New School - Advanced",
  "Malagasy Idioms and Proverbs - Advanced",
  "Malagasy Formal and Polite Registers - Advanced",
  "Malagasy Compound and Complex Sentences - Advanced",
  "Malagasy Conversation: At the Market - Advanced",
  "Malagasy Conversation: Meeting a Friend - Advanced",
  "Malagasy Conversation: Solving a Problem - Advanced",
  "Malagasy Mastery Review and Full Reference - Advanced"
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Malagasy Study — "+safe+"\n"
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
    demo:{kind:"malagasy-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-malagasy-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-malagasy',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
