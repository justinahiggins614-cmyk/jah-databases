(function(){'use strict';
/* JAH The Workflow and Case Records Signature Database generator — jahdb-workflow-case-records-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WFRS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Workflow (Signature Edition) - Foundations",
  "Tasks, Cases, and Processes (Signature Edition) - Foundations",
  "Ownership and Roles (Signature Edition) - Foundations",
  "Status and the Status Lifecycle (Signature Edition) - Foundations",
  "Deadlines and Due Dates (Signature Edition) - Foundations",
  "Handoffs Between People and Teams (Signature Edition) - Foundations",
  "The Audit Trail of Status Changes (Signature Edition) - Foundations",
  "Outcomes Versus Outputs (Signature Edition) - Foundations",
  "A Day in the Life of a Simple Workflow (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "State Machines and Transition Rules (Signature Edition) - Compounded",
  "Basic Workflow Patterns: Sequence, Parallel, and Choice (Signature Edition) - Compounded",
  "The Four Dependency Types (Signature Edition) - Compounded",
  "Advanced Control-Flow Patterns (Signature Edition) - Compounded",
  "BPMN 2.0 Notation Basics (Signature Edition) - Compounded",
  "Critical Path and Schedule Math (Signature Edition) - Compounded",
  "SLA Fundamentals and Tracking (Signature Edition) - Compounded",
  "Case Management Lifecycles (Signature Edition) - Compounded",
  "Escalation Paths and Tiers (Signature Edition) - Compounded",
  "Triage and Prioritization (Signature Edition) - Compounded",
  "Queues and Little's Law (Signature Edition) - Compounded",
  "Multi-Instance and Loop Patterns (Signature Edition) - Compounded",
  "Cancellation, Exceptions, and Compensation (Signature Edition) - Compounded",
  "Handoff Protocols and Acceptance Criteria (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "BPMN 2.0 Execution Semantics (Signature Edition) - Advanced",
  "Orchestration Versus Choreography (Signature Edition) - Advanced",
  "Sagas and Long-Running Transactions (Signature Edition) - Advanced",
  "Deadlock Detection in Dependency Graphs (Signature Edition) - Advanced",
  "SLA Breach Prediction (Signature Edition) - Advanced",
  "Hash-Chained Audit Trails (Signature Edition) - Advanced",
  "Cycle Time and Flow Analytics (Signature Edition) - Advanced",
  "Versioning Running Workflow Instances (Signature Edition) - Advanced",
  "Dynamic Escalation Routing (Signature Edition) - Advanced",
  "Workflow Engines and Durable Execution (Signature Edition) - Advanced",
  "Case Records at Scale (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Workflow Case Study — "+safe+"\n"
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
    name:topic+' — workflow and case record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A workflow and case record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"workflow-case-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-workflow-case-records-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('workflow-case-records-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
