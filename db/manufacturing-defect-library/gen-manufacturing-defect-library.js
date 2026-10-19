(function(){'use strict';
/* JAH manufacturing-defect-library generator — jahdb-manufacturing-defect-library-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MDL-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Manufacturing Defect Library", "Core Concepts of Manufacturing Defect Library", "Essential Vocabulary for Manufacturing Defect Library", "Your First Manufacturing Defect Library Project", "Beginner Mistakes in Manufacturing Defect Library (and How to Avoid Them)", "The Tools You Need for Manufacturing Defect Library", "Myths vs. Facts in Manufacturing Defect Library", "When to Start Manufacturing Defect Library", "Measuring the Basics in Manufacturing Defect Library", "Safety First in Manufacturing Defect Library", "Where to Find Help with Manufacturing Defect Library"], "Compounded": ["The Manufacturing Defect Library Workflow, Step by Step", "A Manufacturing Defect Library Decision Framework", "Manufacturing Defect Library Cost and Budget Planning", "Scheduling Manufacturing Defect Library Work", "Quality Checks for Manufacturing Defect Library", "Manufacturing Defect Library Troubleshooting Guide", "Intermediate Manufacturing Defect Library Skills", "Manufacturing Defect Library in Real-World Cases", "Comparing Manufacturing Defect Library Options", "Documenting Your Manufacturing Defect Library Work", "Collaborating on Manufacturing Defect Library", "Scaling Up Manufacturing Defect Library"], "Advanced": ["Advanced Manufacturing Defect Library Techniques", "Manufacturing Defect Library Edge Cases and Exceptions", "Auditing and Verifying Manufacturing Defect Library", "Automating Manufacturing Defect Library", "Manufacturing Defect Library Long-Term Strategy", "Teaching Manufacturing Defect Library to Others", "Ethics and Responsibility in Manufacturing Defect Library", "Integrating Manufacturing Defect Library with Other Systems", "The Manufacturing Defect Library Frontier: What Comes Next", "The Manufacturing Defect Library Master Checklist", "Manufacturing Defect Library Capstone Review: Putting It All Together"]};
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
    description:'SAMPLE RECORD (generated — structural sample). A public-record sample of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"manufacturing-defect-library-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-manufacturing-defect-library-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("manufacturing-defect-library",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
