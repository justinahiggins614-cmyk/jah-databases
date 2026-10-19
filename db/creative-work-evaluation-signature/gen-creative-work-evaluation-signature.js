(function(){'use strict';
/* JAH creative-work-evaluation-signature generator — jahdb-creative-work-evaluation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CWES-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Creative Work Evaluation (Signature Edition)", "Core Concepts of Creative Work Evaluation (Signature Edition)", "Essential Vocabulary for Creative Work Evaluation (Signature Edition)", "Your First Creative Work Evaluation Project (Signature Edition)", "Beginner Mistakes in Creative Work Evaluation (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Creative Work Evaluation (Signature Edition)", "Myths vs. Facts in Creative Work Evaluation (Signature Edition)", "When to Start Creative Work Evaluation (Signature Edition)", "Measuring the Basics in Creative Work Evaluation (Signature Edition)", "Safety First in Creative Work Evaluation (Signature Edition)", "Where to Find Help with Creative Work Evaluation (Signature Edition)"], "Compounded": ["The Creative Work Evaluation Workflow, Step by Step (Signature Edition)", "A Creative Work Evaluation Decision Framework (Signature Edition)", "Creative Work Evaluation Cost and Budget Planning (Signature Edition)", "Scheduling Creative Work Evaluation Work (Signature Edition)", "Quality Checks for Creative Work Evaluation (Signature Edition)", "Creative Work Evaluation Troubleshooting Guide (Signature Edition)", "Intermediate Creative Work Evaluation Skills (Signature Edition)", "Creative Work Evaluation in Real-World Cases (Signature Edition)", "Comparing Creative Work Evaluation Options (Signature Edition)", "Documenting Your Creative Work Evaluation Work (Signature Edition)", "Collaborating on Creative Work Evaluation (Signature Edition)", "Scaling Up Creative Work Evaluation (Signature Edition)"], "Advanced": ["Advanced Creative Work Evaluation Techniques (Signature Edition)", "Creative Work Evaluation Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Creative Work Evaluation (Signature Edition)", "Automating Creative Work Evaluation (Signature Edition)", "Creative Work Evaluation Long-Term Strategy (Signature Edition)", "Teaching Creative Work Evaluation to Others (Signature Edition)", "Ethics and Responsibility in Creative Work Evaluation (Signature Edition)", "Integrating Creative Work Evaluation with Other Systems (Signature Edition)", "The Creative Work Evaluation Frontier: What Comes Next (Signature Edition)", "The Creative Work Evaluation Master Checklist (Signature Edition)", "Creative Work Evaluation Capstone Review: Putting It All Together (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — problem-solving guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — problem-solving guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A Signature-original sample of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"creative-work-evaluation-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-creative-work-evaluation-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("creative-work-evaluation-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
