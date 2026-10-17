(function(){'use strict';
/* JAH The Workflow and Case Records Database generator — jahdb-workflow-case-records-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WFR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Workflow - Foundations",
  "Tasks, Cases, and Processes - Foundations",
  "Ownership and Roles - Foundations",
  "Status and the Status Lifecycle - Foundations",
  "Deadlines and Due Dates - Foundations",
  "Handoffs Between People and Teams - Foundations",
  "The Audit Trail of Status Changes - Foundations",
  "Outcomes Versus Outputs - Foundations",
  "A Day in the Life of a Simple Workflow - Foundations"
 ],
 "Compounded": [
  "State Machines and Transition Rules - Compounded",
  "Basic Workflow Patterns: Sequence, Parallel, and Choice - Compounded",
  "The Four Dependency Types - Compounded",
  "Advanced Control-Flow Patterns - Compounded",
  "BPMN 2.0 Notation Basics - Compounded",
  "Critical Path and Schedule Math - Compounded",
  "SLA Fundamentals and Tracking - Compounded",
  "Case Management Lifecycles - Compounded",
  "Escalation Paths and Tiers - Compounded",
  "Triage and Prioritization - Compounded",
  "Queues and Little's Law - Compounded",
  "Multi-Instance and Loop Patterns - Compounded",
  "Cancellation, Exceptions, and Compensation - Compounded",
  "Handoff Protocols and Acceptance Criteria - Compounded"
 ],
 "Advanced": [
  "BPMN 2.0 Execution Semantics - Advanced",
  "Orchestration Versus Choreography - Advanced",
  "Sagas and Long-Running Transactions - Advanced",
  "Deadlock Detection in Dependency Graphs - Advanced",
  "SLA Breach Prediction - Advanced",
  "Hash-Chained Audit Trails - Advanced",
  "Cycle Time and Flow Analytics - Advanced",
  "Versioning Running Workflow Instances - Advanced",
  "Dynamic Escalation Routing - Advanced",
  "Workflow Engines and Durable Execution - Advanced",
  "Case Records at Scale - Advanced"
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
var gen={version:'jahdb-workflow-case-records-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('workflow-case-records',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
