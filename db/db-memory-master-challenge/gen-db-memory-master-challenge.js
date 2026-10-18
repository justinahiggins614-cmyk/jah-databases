(function(){'use strict';
/* JAH The Memory Master Challenge generator — jahdb-db-memory-master-challenge-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MMC-";
var FIELDS=["How Memory Works","Techniques","Systems"];
var TOPICS={
 "How Memory Works": [
  "The Three Stages: Encode, Store, Retrieve - How Memory Works",
  "Working vs Long-Term Memory - How Memory Works",
  "Why We Forget - How Memory Works",
  "The Testing Effect - How Memory Works",
  "Depth of Processing - How Memory Works",
  "Emotion and Memory - How Memory Works",
  "Sleep and Memory - How Memory Works",
  "Interference: When Memories Collide - How Memory Works",
  "Context and State Dependence - How Memory Works",
  "The Forgetting Curve - How Memory Works",
  "Chunking: Bigger Bites - How Memory Works",
  "Attention Is the Doorway - How Memory Works"
 ],
 "Techniques": [
  "The Memory Palace - Techniques",
  "Acronyms and Acrostics - Techniques",
  "Visualization: See It to Keep It - Techniques",
  "Rhymes and Rhythm - Techniques",
  "The Peg System - Techniques",
  "Story Chains - Techniques",
  "Spaced Repetition - Techniques",
  "Interleaving Practice - Techniques",
  "Elaborative Interrogation - Techniques",
  "Dual Coding in Practice - Techniques",
  "The Feynman Drill - Techniques",
  "The Number-Shape System - Techniques"
 ],
 "Systems": [
  "Names and Faces - Systems",
  "Numbers That Stick - Systems",
  "Speeches Without Notes - Systems",
  "Exam-Day Recall - Systems",
  "The Daily Memory Workout - Systems",
  "Remembering What You Read - Systems",
  "Lifelong Memory Habits - Systems",
  "The Memory Athlete's Path - Systems",
  "Teach Memory to Others - Systems",
  "Remembering Birthdays and Dates - Systems"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Memory Master Study — "+safe+"\n"
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
    name:topic+' — memory lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A memory lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"memory-master-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-memory-master-challenge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-memory-master-challenge',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
