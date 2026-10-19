(function(){'use strict';
/* JAH grammar-explanation-library-signature generator — jahdb-grammar-explanation-library-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GELS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Grammar Explanation Library (Signature Edition)", "Core Concepts of Grammar Explanation Library (Signature Edition)", "Essential Vocabulary for Grammar Explanation Library (Signature Edition)", "Your First Grammar Explanation Library Project (Signature Edition)", "Beginner Mistakes in Grammar Explanation Library (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Grammar Explanation Library (Signature Edition)", "Myths vs. Facts in Grammar Explanation Library (Signature Edition)", "When to Start Grammar Explanation Library (Signature Edition)", "Measuring the Basics in Grammar Explanation Library (Signature Edition)", "Safety First in Grammar Explanation Library (Signature Edition)", "Where to Find Help with Grammar Explanation Library (Signature Edition)"], "Compounded": ["The Grammar Explanation Library Workflow, Step by Step (Signature Edition)", "A Grammar Explanation Library Decision Framework (Signature Edition)", "Grammar Explanation Library Cost and Budget Planning (Signature Edition)", "Scheduling Grammar Explanation Library Work (Signature Edition)", "Quality Checks for Grammar Explanation Library (Signature Edition)", "Grammar Explanation Library Troubleshooting Guide (Signature Edition)", "Intermediate Grammar Explanation Library Skills (Signature Edition)", "Grammar Explanation Library in Real-World Cases (Signature Edition)", "Comparing Grammar Explanation Library Options (Signature Edition)", "Documenting Your Grammar Explanation Library Work (Signature Edition)", "Collaborating on Grammar Explanation Library (Signature Edition)", "Scaling Up Grammar Explanation Library (Signature Edition)"], "Advanced": ["Advanced Grammar Explanation Library Techniques (Signature Edition)", "Grammar Explanation Library Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Grammar Explanation Library (Signature Edition)", "Automating Grammar Explanation Library (Signature Edition)", "Grammar Explanation Library Long-Term Strategy (Signature Edition)", "Teaching Grammar Explanation Library to Others (Signature Edition)", "Ethics and Responsibility in Grammar Explanation Library (Signature Edition)", "Integrating Grammar Explanation Library with Other Systems (Signature Edition)", "The Grammar Explanation Library Frontier: What Comes Next (Signature Edition)", "The Grammar Explanation Library Master Checklist (Signature Edition)", "Grammar Explanation Library Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"grammar-explanation-library-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-grammar-explanation-library-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("grammar-explanation-library-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
