(function(){'use strict';
/* JAH The Igbo Language Signature Database generator — jahdb-language-igbo-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LIBOS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Igbo Language Overview (Signature Edition) - Foundations",
  "Igbo Writing System and Alphabet (Signature Edition) - Foundations",
  "Igbo Pronunciation and Phonology (Signature Edition) - Foundations",
  "Igbo Core Nouns I (Signature Edition) - Foundations",
  "Igbo Core Verbs I (Signature Edition) - Foundations",
  "Igbo Adjectives and Adverbs (Signature Edition) - Foundations",
  "Igbo Pronouns (Signature Edition) - Foundations",
  "Igbo Numbers and Time (Signature Edition) - Foundations",
  "Igbo Greetings and Everyday Phrases (Signature Edition) - Foundations",
  "Igbo Grammar Essentials (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Igbo at Home and with Family (Signature Edition) - Compounded",
  "Igbo Food and Cooking (Signature Edition) - Compounded",
  "Igbo Travel and Directions (Signature Edition) - Compounded",
  "Igbo Work and School (Signature Edition) - Compounded",
  "Igbo Health and the Body (Signature Edition) - Compounded",
  "Igbo Emotions and Feelings (Signature Edition) - Compounded",
  "Igbo Nature and Weather (Signature Edition) - Compounded",
  "Igbo Shopping and Money (Signature Edition) - Compounded",
  "Igbo Friendship and Social Life (Signature Edition) - Compounded",
  "Igbo Technology and Communication (Signature Edition) - Compounded",
  "Igbo Verb Tenses in Sentences (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Igbo Questions and Answers (Signature Edition) - Advanced",
  "Igbo Commands and Requests (Signature Edition) - Advanced",
  "Igbo Descriptions of People and Places (Signature Edition) - Advanced",
  "Igbo Story I: The Clever Tortoise (Signature Edition) - Advanced",
  "Igbo Story II: The Lost Goat (Signature Edition) - Advanced",
  "Igbo Story III: The New School (Signature Edition) - Advanced",
  "Igbo Idioms and Proverbs (Signature Edition) - Advanced",
  "Igbo Formal and Polite Registers (Signature Edition) - Advanced",
  "Igbo Compound and Complex Sentences (Signature Edition) - Advanced",
  "Igbo Conversation: At the Market (Signature Edition) - Advanced",
  "Igbo Conversation: Meeting a Friend (Signature Edition) - Advanced",
  "Igbo Conversation: Solving a Problem (Signature Edition) - Advanced",
  "Igbo Mastery Review and Full Reference (Signature Edition) - Advanced"
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Igbo Study — "+safe+"\n"
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
    demo:{kind:"igbo-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-language-igbo-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('language-igbo-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
