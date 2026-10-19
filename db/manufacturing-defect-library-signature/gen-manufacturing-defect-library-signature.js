(function(){'use strict';
/* JAH manufacturing-defect-library-signature generator — jahdb-manufacturing-defect-library-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MDLS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Manufacturing Defect Library (Signature Edition)", "Core Concepts of Manufacturing Defect Library (Signature Edition)", "Essential Vocabulary for Manufacturing Defect Library (Signature Edition)", "Your First Manufacturing Defect Library Project (Signature Edition)", "Beginner Mistakes in Manufacturing Defect Library (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Manufacturing Defect Library (Signature Edition)", "Myths vs. Facts in Manufacturing Defect Library (Signature Edition)", "When to Start Manufacturing Defect Library (Signature Edition)", "Measuring the Basics in Manufacturing Defect Library (Signature Edition)", "Safety First in Manufacturing Defect Library (Signature Edition)", "Where to Find Help with Manufacturing Defect Library (Signature Edition)"], "Compounded": ["The Manufacturing Defect Library Workflow, Step by Step (Signature Edition)", "A Manufacturing Defect Library Decision Framework (Signature Edition)", "Manufacturing Defect Library Cost and Budget Planning (Signature Edition)", "Scheduling Manufacturing Defect Library Work (Signature Edition)", "Quality Checks for Manufacturing Defect Library (Signature Edition)", "Manufacturing Defect Library Troubleshooting Guide (Signature Edition)", "Intermediate Manufacturing Defect Library Skills (Signature Edition)", "Manufacturing Defect Library in Real-World Cases (Signature Edition)", "Comparing Manufacturing Defect Library Options (Signature Edition)", "Documenting Your Manufacturing Defect Library Work (Signature Edition)", "Collaborating on Manufacturing Defect Library (Signature Edition)", "Scaling Up Manufacturing Defect Library (Signature Edition)"], "Advanced": ["Advanced Manufacturing Defect Library Techniques (Signature Edition)", "Manufacturing Defect Library Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Manufacturing Defect Library (Signature Edition)", "Automating Manufacturing Defect Library (Signature Edition)", "Manufacturing Defect Library Long-Term Strategy (Signature Edition)", "Teaching Manufacturing Defect Library to Others (Signature Edition)", "Ethics and Responsibility in Manufacturing Defect Library (Signature Edition)", "Integrating Manufacturing Defect Library with Other Systems (Signature Edition)", "The Manufacturing Defect Library Frontier: What Comes Next (Signature Edition)", "The Manufacturing Defect Library Master Checklist (Signature Edition)", "Manufacturing Defect Library Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"manufacturing-defect-library-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-manufacturing-defect-library-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("manufacturing-defect-library-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
