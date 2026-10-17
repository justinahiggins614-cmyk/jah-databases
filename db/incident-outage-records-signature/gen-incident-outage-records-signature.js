(function(){'use strict';
/* JAH The Incident and Outage Records Signature Database generator — jahdb-incident-outage-records-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-INCS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is an Incident (Signature Edition) - Foundations",
  "What Is an Outage (Signature Edition) - Foundations",
  "The Incident Lifecycle (Signature Edition) - Foundations",
  "Mean Time to Restore: MTTR (Signature Edition) - Foundations",
  "Mean Time Between Failures: MTBF (Signature Edition) - Foundations",
  "Availability and the Nines (Signature Edition) - Foundations",
  "Recording the Fault Timeline (Signature Edition) - Foundations",
  "Mapping Affected Systems and Blast Radius (Signature Edition) - Foundations",
  "Assessing Incident Impact (Signature Edition) - Foundations",
  "Detection and Alerting (Signature Edition) - Foundations",
  "On-Call Rotations and Escalation Ladders (Signature Edition) - Foundations",
  "Incident Communication Discipline (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "The Incident Commander (Signature Edition) - Compounded",
  "Triage and Severity Assignment (Signature Edition) - Compounded",
  "Mitigation Before Resolution (Signature Edition) - Compounded",
  "Restoration and Rollback Plans (Signature Edition) - Compounded",
  "The Five Whys (Signature Edition) - Compounded",
  "Fishbone Diagrams and Fault Trees (Signature Edition) - Compounded",
  "Blameless Postmortems (Signature Edition) - Compounded",
  "The Postmortem Template (Signature Edition) - Compounded",
  "Tracking Remediation Action Items (Signature Edition) - Compounded",
  "Status Page Operations (Signature Edition) - Compounded",
  "Paging and Alert Routing (Signature Edition) - Compounded",
  "The Incident Bridge and War Room (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Site Reliability Engineering and Error Budgets (Signature Edition) - Advanced",
  "Chaos Engineering (Signature Edition) - Advanced",
  "Observability in Incident Response (Signature Edition) - Advanced",
  "Incident Metrics Dashboards (Signature Edition) - Advanced",
  "DORA Metrics and Elite Performer Benchmarks (Signature Edition) - Advanced",
  "Game Days and Incident Drills (Signature Edition) - Advanced",
  "Incident Review Boards (Signature Edition) - Advanced",
  "Case Study: The Dyn DDoS Outage of October 2016 (Signature Edition) - Advanced",
  "Case Study: The Fastly Global Outage of June 2021 (Signature Edition) - Advanced",
  "Case Study: The AWS US-East-1 Outage of December 2021 (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Incident Outage Study — "+safe+"\n"
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
    name:topic+' — incident and outage record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A incident and outage record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"incident-outage-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-incident-outage-records-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('incident-outage-records-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
