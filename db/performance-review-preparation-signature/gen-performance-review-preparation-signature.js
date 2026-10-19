(function(){'use strict';
/* JAH Performance Review Preparation Database generator — jahdb-performance-review-preparation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PERFRPS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Brag Document (Signature Edition)", "Quantifying Impact (Signature Edition)", "Writing the Self-Assessment (Signature Edition)", "Gathering Peer Feedback (Signature Edition)", "Reviewing the Job Description (Signature Edition)", "Goal Review and Calibration (Signature Edition)", "Handling Critical Feedback (Signature Edition)", "Disagreeing Professionally (Signature Edition)", "The Compensation Conversation (Signature Edition)", "Promotion Readiness (Signature Edition)", "360-Degree Feedback (Signature Edition)"], "Compounded": ["Managing Up (Signature Edition)", "Difficult Review Scenarios (Signature Edition)", "Performance Improvement Plans (Signature Edition)", "Self-Review Rating Strategy (Signature Edition)", "The Review Meeting (Signature Edition)", "Post-Review Follow-Up (Signature Edition)", "Reviewing Your Manager (Signature Edition)", "Calibration and Bias (Signature Edition)", "Remote Review Dynamics (Signature Edition)", "New Role Reviews (Signature Edition)", "Career Pathing Conversations (Signature Edition)", "Bonus and Equity Reviews (Signature Edition)"], "Advanced": ["When Reviews Are Unfair (Signature Edition)", "Continuous Feedback Cultures (Signature Edition)", "Teaching Review Skills (Signature Edition)", "The Annual Career Audit (Signature Edition)", "Negotiating Title Changes (Signature Edition)", "Reference Building (Signature Edition)", "Review Season Stress (Signature Edition)", "Long-Term Performance Trends (Signature Edition)", "Self-Advocacy Scripts (Signature Edition)", "Documenting Difficult Periods (Signature Edition)", "The Review Prep Timeline (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — review guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — review guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A review guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"performance-review-preparation-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-performance-review-preparation-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("performance-review-preparation-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
