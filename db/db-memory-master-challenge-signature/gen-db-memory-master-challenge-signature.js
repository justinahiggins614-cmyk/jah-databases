(function(){'use strict';
/* JAH The Memory Master Challenge generator — jahdb-db-memory-master-challenge-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MMCS-";
var FIELDS=["How Memory Works","Techniques","Systems"];
var TOPICS={
 "How Memory Works": [
  "The Three Stages: Encode, Store, Retrieve (Signature Edition) - How Memory Works",
  "Working vs Long-Term Memory (Signature Edition) - How Memory Works",
  "Why We Forget (Signature Edition) - How Memory Works",
  "The Testing Effect (Signature Edition) - How Memory Works",
  "Depth of Processing (Signature Edition) - How Memory Works",
  "Emotion and Memory (Signature Edition) - How Memory Works",
  "Sleep and Memory (Signature Edition) - How Memory Works",
  "Interference: When Memories Collide (Signature Edition) - How Memory Works",
  "Context and State Dependence (Signature Edition) - How Memory Works",
  "The Forgetting Curve (Signature Edition) - How Memory Works",
  "Chunking: Bigger Bites (Signature Edition) - How Memory Works",
  "Attention Is the Doorway (Signature Edition) - How Memory Works"
 ],
 "Techniques": [
  "The Memory Palace (Signature Edition) - Techniques",
  "Acronyms and Acrostics (Signature Edition) - Techniques",
  "Visualization: See It to Keep It (Signature Edition) - Techniques",
  "Rhymes and Rhythm (Signature Edition) - Techniques",
  "The Peg System (Signature Edition) - Techniques",
  "Story Chains (Signature Edition) - Techniques",
  "Spaced Repetition (Signature Edition) - Techniques",
  "Interleaving Practice (Signature Edition) - Techniques",
  "Elaborative Interrogation (Signature Edition) - Techniques",
  "Dual Coding in Practice (Signature Edition) - Techniques",
  "The Feynman Drill (Signature Edition) - Techniques",
  "The Number-Shape System (Signature Edition) - Techniques"
 ],
 "Systems": [
  "Names and Faces (Signature Edition) - Systems",
  "Numbers That Stick (Signature Edition) - Systems",
  "Speeches Without Notes (Signature Edition) - Systems",
  "Exam-Day Recall (Signature Edition) - Systems",
  "The Daily Memory Workout (Signature Edition) - Systems",
  "Remembering What You Read (Signature Edition) - Systems",
  "Lifelong Memory Habits (Signature Edition) - Systems",
  "The Memory Athlete's Path (Signature Edition) - Systems",
  "Teach Memory to Others (Signature Edition) - Systems",
  "Remembering Birthdays and Dates (Signature Edition) - Systems"
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
var gen={version:'jahdb-db-memory-master-challenge-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-memory-master-challenge-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
