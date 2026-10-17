(function(){'use strict';
/* JAH The Event Streams Database generator — jahdb-event-streams-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EVS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is an Event - Foundations",
  "Commands, Events, and State - Foundations",
  "Event Time Versus Processing Time - Foundations",
  "The Append-Only Event Log - Foundations",
  "Event Schemas and Contracts - Foundations",
  "Ordering, Causality, and Happened-Before - Foundations",
  "Stream Partitioning - Foundations",
  "Serializing Events: Formats and Choices - Foundations",
  "Consumers and Consumer Groups - Foundations",
  "Delivery Semantics: At-Most, At-Least, Exactly-Once - Foundations"
 ],
 "Compounded": [
  "Change Data Capture (CDC) - Compounded",
  "The Outbox Pattern - Compounded",
  "Designing an Event Store - Compounded",
  "Snapshotting Aggregates - Compounded",
  "Consumer Offsets and Seek - Compounded",
  "Event Sourcing Fundamentals - Compounded",
  "Stateful Stream Processing - Compounded",
  "Windows Over Event Time - Compounded",
  "Pub-Sub and Event-Driven Architecture - Compounded",
  "Schema Evolution - Compounded",
  "Correlation and Causation IDs - Compounded",
  "Projections and Read Models - Compounded",
  "Replaying and Reprocessing Events - Compounded",
  "Dead Letters and Poison Events - Compounded",
  "Watermarks and Late Data - Compounded",
  "Event Routing and Filtering - Compounded"
 ],
 "Advanced": [
  "Sagas: Distributed Transactions Without Two-Phase Commit - Advanced",
  "End-to-End Exactly-Once Processing - Advanced",
  "Compaction, Retention, and Archiving - Advanced",
  "Event Governance and the Schema Registry - Advanced",
  "Observing Event Streams: Lag, Metrics, and Alerts - Advanced",
  "Multi-Region Replication and Failover - Advanced",
  "Securing Event Data: Encryption and Redaction - Advanced",
  "Temporal Queries and Time Travel - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Event Stream Study — "+safe+"\n"
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
    name:topic+' — event stream record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A event stream record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"event-stream-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-event-streams-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('event-streams',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
