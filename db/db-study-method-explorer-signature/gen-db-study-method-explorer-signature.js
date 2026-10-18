(function(){'use strict';
/* JAH The Study Method Explorer generator — jahdb-db-study-method-explorer-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SMES-";
var FIELDS=["Foundations","Methods","Exam Strategy"];
var TOPICS={
 "Foundations": [
  "The Science of Studying (Signature Edition) - Foundations",
  "Know Thyself: Metacognition (Signature Edition) - Foundations",
  "Goals vs Systems (Signature Edition) - Foundations",
  "Time Management for Students (Signature Edition) - Foundations",
  "Energy Management (Signature Edition) - Foundations",
  "The Study Environment (Signature Edition) - Foundations",
  "Motivation: The Engine (Signature Edition) - Foundations",
  "Procrastination: The Thief (Signature Edition) - Foundations",
  "Focus in a Distracted World (Signature Edition) - Foundations",
  "Learning Styles: The Myth (Signature Edition) - Foundations",
  "Sleep: The Study Hack (Signature Edition) - Foundations",
  "Exercise for the Brain (Signature Edition) - Foundations"
 ],
 "Methods": [
  "Retrieval Practice (Signature Edition) - Methods",
  "Spaced Practice (Signature Edition) - Methods",
  "Elaboration: Explain It Deeply (Signature Edition) - Methods",
  "Interleaving (Signature Edition) - Methods",
  "Concrete Examples Method (Signature Edition) - Methods",
  "Dual Coding (Signature Edition) - Methods",
  "Note-Taking That Works (Signature Edition) - Methods",
  "Summarizing From Memory (Signature Edition) - Methods",
  "Past Papers: The Gold Standard (Signature Edition) - Methods",
  "Teaching to Learn (Signature Edition) - Methods",
  "What Doesn't Work (Stop Doing This) (Signature Edition) - Methods",
  "Building Your System (Signature Edition) - Methods"
 ],
 "Exam Strategy": [
  "Exam Prep Timeline (Signature Edition) - Exam Strategy",
  "The Week Before (Signature Edition) - Exam Strategy",
  "Exam-Day Tactics (Signature Edition) - Exam Strategy",
  "Multiple Choice Mastery (Signature Edition) - Exam Strategy",
  "Essay Exams (Signature Edition) - Exam Strategy",
  "Math/Science Exams (Signature Edition) - Exam Strategy",
  "Managing Exam Anxiety (Signature Edition) - Exam Strategy",
  "After the Exam: The Review (Signature Edition) - Exam Strategy",
  "Retakes and Resilience (Signature Edition) - Exam Strategy",
  "Your Study Playbook (Signature Edition) - Exam Strategy"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Study Method Study — "+safe+"\n"
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
    name:topic+' — study method lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A study method lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"study-method-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-study-method-explorer-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-study-method-explorer-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
