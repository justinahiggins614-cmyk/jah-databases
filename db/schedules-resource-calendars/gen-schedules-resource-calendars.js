(function(){'use strict';
/* JAH The Schedules and Resource Calendars Database generator — jahdb-schedules-resource-calendars-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SCH-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Schedule and a Resource Calendar - Foundations",
  "Calendar Data Models: Events, Slots, and Resources - Foundations",
  "Time, Duration, and the Interval - Foundations",
  "Recurrence Rules: RRULE and Recurring Events - Foundations",
  "Time Zones, DST, and the True Instant - Foundations",
  "Appointments and Booking Slots - Foundations",
  "Personnel Shifts and Rotation Plans - Foundations",
  "Equipment Availability and Reservations - Foundations",
  "Facilities and Room Scheduling - Foundations",
  "Maintenance Windows and Change Control - Foundations",
  "iCalendar RFC 5545: The Interchange Standard - Foundations"
 ],
 "Compounded": [
  "Interval Overlap and Conflict Detection - Compounded",
  "Constraint Satisfaction for Scheduling - Compounded",
  "Shift-Rotation Rules and Circadian Planning - Compounded",
  "Scheduling Algorithms: Greedy, Backtracking, and the Hungarian Method - Compounded",
  "Resource Allocation and Bin Packing - Compounded",
  "Queueing Theory for Service Capacity - Compounded",
  "Lead Times, Setup, and Teardown Buffers - Compounded",
  "Multi-Resource and Team Scheduling - Compounded",
  "Calendar Synchronization: CalDAV and Federation - Compounded",
  "Preventive Maintenance Scheduling - Compounded",
  "Downtime Windows and Availability SLAs - Compounded",
  "Scheduling Under Uncertainty: Stochastic Models - Compounded"
 ],
 "Advanced": [
  "Linear Programming for Workforce Scheduling - Advanced",
  "Timetabling by Graph Coloring - Advanced",
  "Job-Shop Scheduling and Makespan - Advanced",
  "Priority Scheduling and Real-Time Deadlines - Advanced",
  "Distributed Calendars: Consensus and Conflict Resolution - Advanced",
  "Scheduling Fairness and Load Balancing - Advanced",
  "Master Production Scheduling and MRP - Advanced",
  "Predictive Maintenance and Condition-Based Windows - Advanced",
  "The Scheduling System Architecture - Advanced",
  "Schedule Audit, Compliance, and Forensics - Advanced",
  "The Resource Calendar Operating Picture - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Scheduling Study — "+safe+"\n"
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
    name:topic+' — schedule and calendar record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A schedule and calendar record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"scheduling-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-schedules-resource-calendars-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('schedules-resource-calendars',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
