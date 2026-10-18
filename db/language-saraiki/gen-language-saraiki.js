(function(){'use strict';
/* JAH The Saraiki Language Database generator — jahdb-language-saraiki-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LSKR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Saraiki Language Overview - Foundations",
  "Saraiki Writing System and Alphabet - Foundations",
  "Saraiki Pronunciation and Phonology - Foundations",
  "Saraiki Core Nouns I - Foundations",
  "Saraiki Core Verbs I - Foundations",
  "Saraiki Adjectives and Adverbs - Foundations",
  "Saraiki Pronouns - Foundations",
  "Saraiki Numbers and Time - Foundations",
  "Saraiki Greetings and Everyday Phrases - Foundations",
  "Saraiki Grammar Essentials - Foundations"
 ],
 "Compounded": [
  "Saraiki at Home and with Family - Compounded",
  "Saraiki Food and Cooking - Compounded",
  "Saraiki Travel and Directions - Compounded",
  "Saraiki Work and School - Compounded",
  "Saraiki Health and the Body - Compounded",
  "Saraiki Emotions and Feelings - Compounded",
  "Saraiki Nature and Weather - Compounded",
  "Saraiki Shopping and Money - Compounded",
  "Saraiki Friendship and Social Life - Compounded",
  "Saraiki Technology and Communication - Compounded",
  "Saraiki Verb Tenses in Sentences - Compounded"
 ],
 "Advanced": [
  "Saraiki Questions and Answers - Advanced",
  "Saraiki Commands and Requests - Advanced",
  "Saraiki Descriptions of People and Places - Advanced",
  "Saraiki Story I: The Lost Key - Advanced",
  "Saraiki Story II: The Little Bird - Advanced",
  "Saraiki Story III: The Market Day - Advanced",
  "Saraiki Idioms and Proverbs - Advanced",
  "Saraiki Formal and Polite Registers - Advanced",
  "Saraiki Compound and Complex Sentences - Advanced",
  "Saraiki Conversation: At the Market - Advanced",
  "Saraiki Conversation: Meeting a Friend - Advanced",
  "Saraiki Conversation: Solving a Problem - Advanced",
  "Saraiki Mastery Review and Full Reference - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Saraiki Study — "+safe+"\n"
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
    demo:{kind:"saraiki-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-saraiki-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-saraiki',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
