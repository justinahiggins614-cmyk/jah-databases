(function(){'use strict';
/* JAH The Language Learning Quest generator — jahdb-db-language-learning-quest-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LLQ-";
var FIELDS=["First Words","Grammar","Fluency"];
var TOPICS={
 "First Words": [
  "Your First 100 Words - First Words",
  "Sounds: Train Your Ear First - First Words",
  "Greetings and Introductions - First Words",
  "Numbers 1-100 - First Words",
  "Survival Phrases - First Words",
  "Food Words: Eat Anywhere - First Words",
  "Question Words - First Words",
  "Yes, No, and Politeness - First Words",
  "Colors and Descriptions - First Words",
  "Time Words - First Words",
  "Family Words - First Words",
  "The First Conversation - First Words"
 ],
 "Grammar": [
  "Present Tense: The Engine - Grammar",
  "Past Tense: Telling Stories - Grammar",
  "Future: Plans and Promises - Grammar",
  "Articles: A, The, or Nothing - Grammar",
  "Gender: Le, La, and Friends - Grammar",
  "Word Order: The Skeleton - Grammar",
  "Negation: Saying No - Grammar",
  "Pronouns: Standing In - Grammar",
  "Prepositions: Small Words, Big Trouble - Grammar",
  "Questions: Asking Right - Grammar",
  "Adjectives Agree (Sometimes) - Grammar",
  "Conditionals: If and Would - Grammar"
 ],
 "Fluency": [
  "Listening: The 80/20 Skill - Fluency",
  "Speaking: Fluency Over Accuracy - Fluency",
  "Reading: Graded to Real - Fluency",
  "Writing: Think on Paper - Fluency",
  "The Plateau: Breaking Through - Fluency",
  "Idioms: The Color of Language - Fluency",
  "Slang and Register - Fluency",
  "Thinking in the Language - Fluency",
  "Conversation Repair Strategies - Fluency",
  "Your Maintenance Plan - Fluency"
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
var gen={version:'jahdb-db-language-learning-quest-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-language-learning-quest',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
