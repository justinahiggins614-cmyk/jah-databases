(function(){'use strict';
/* JAH The Language Learning Quest generator — jahdb-db-language-learning-quest-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LLQS-";
var FIELDS=["First Words","Grammar","Fluency"];
var TOPICS={
 "First Words": [
  "Your First 100 Words (Signature Edition) - First Words",
  "Sounds: Train Your Ear First (Signature Edition) - First Words",
  "Greetings and Introductions (Signature Edition) - First Words",
  "Numbers 1-100 (Signature Edition) - First Words",
  "Survival Phrases (Signature Edition) - First Words",
  "Food Words: Eat Anywhere (Signature Edition) - First Words",
  "Question Words (Signature Edition) - First Words",
  "Yes, No, and Politeness (Signature Edition) - First Words",
  "Colors and Descriptions (Signature Edition) - First Words",
  "Time Words (Signature Edition) - First Words",
  "Family Words (Signature Edition) - First Words",
  "The First Conversation (Signature Edition) - First Words"
 ],
 "Grammar": [
  "Present Tense: The Engine (Signature Edition) - Grammar",
  "Past Tense: Telling Stories (Signature Edition) - Grammar",
  "Future: Plans and Promises (Signature Edition) - Grammar",
  "Articles: A, The, or Nothing (Signature Edition) - Grammar",
  "Gender: Le, La, and Friends (Signature Edition) - Grammar",
  "Word Order: The Skeleton (Signature Edition) - Grammar",
  "Negation: Saying No (Signature Edition) - Grammar",
  "Pronouns: Standing In (Signature Edition) - Grammar",
  "Prepositions: Small Words, Big Trouble (Signature Edition) - Grammar",
  "Questions: Asking Right (Signature Edition) - Grammar",
  "Adjectives Agree (Sometimes) (Signature Edition) - Grammar",
  "Conditionals: If and Would (Signature Edition) - Grammar"
 ],
 "Fluency": [
  "Listening: The 80/20 Skill (Signature Edition) - Fluency",
  "Speaking: Fluency Over Accuracy (Signature Edition) - Fluency",
  "Reading: Graded to Real (Signature Edition) - Fluency",
  "Writing: Think on Paper (Signature Edition) - Fluency",
  "The Plateau: Breaking Through (Signature Edition) - Fluency",
  "Idioms: The Color of Language (Signature Edition) - Fluency",
  "Slang and Register (Signature Edition) - Fluency",
  "Thinking in the Language (Signature Edition) - Fluency",
  "Conversation Repair Strategies (Signature Edition) - Fluency",
  "Your Maintenance Plan (Signature Edition) - Fluency"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Language Quest Study — "+safe+"\n"
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
    name:topic+' — language lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A language lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"language-quest-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-language-learning-quest-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-language-learning-quest-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
