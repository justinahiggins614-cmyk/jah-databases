(function(){'use strict';
/* JAH The Event Streams Signature Database generator — jahdb-event-streams-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EVSS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is an Event (Signature Edition) - Foundations",
  "Commands, Events, and State (Signature Edition) - Foundations",
  "Event Time Versus Processing Time (Signature Edition) - Foundations",
  "The Append-Only Event Log (Signature Edition) - Foundations",
  "Event Schemas and Contracts (Signature Edition) - Foundations",
  "Ordering, Causality, and Happened-Before (Signature Edition) - Foundations",
  "Stream Partitioning (Signature Edition) - Foundations",
  "Serializing Events: Formats and Choices (Signature Edition) - Foundations",
  "Consumers and Consumer Groups (Signature Edition) - Foundations",
  "Delivery Semantics: At-Most, At-Least, Exactly-Once (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Change Data Capture (CDC) (Signature Edition) - Compounded",
  "The Outbox Pattern (Signature Edition) - Compounded",
  "Designing an Event Store (Signature Edition) - Compounded",
  "Snapshotting Aggregates (Signature Edition) - Compounded",
  "Consumer Offsets and Seek (Signature Edition) - Compounded",
  "Event Sourcing Fundamentals (Signature Edition) - Compounded",
  "Stateful Stream Processing (Signature Edition) - Compounded",
  "Windows Over Event Time (Signature Edition) - Compounded",
  "Pub-Sub and Event-Driven Architecture (Signature Edition) - Compounded",
  "Schema Evolution (Signature Edition) - Compounded",
  "Correlation and Causation IDs (Signature Edition) - Compounded",
  "Projections and Read Models (Signature Edition) - Compounded",
  "Replaying and Reprocessing Events (Signature Edition) - Compounded",
  "Dead Letters and Poison Events (Signature Edition) - Compounded",
  "Watermarks and Late Data (Signature Edition) - Compounded",
  "Event Routing and Filtering (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Sagas: Distributed Transactions Without Two-Phase Commit (Signature Edition) - Advanced",
  "End-to-End Exactly-Once Processing (Signature Edition) - Advanced",
  "Compaction, Retention, and Archiving (Signature Edition) - Advanced",
  "Event Governance and the Schema Registry (Signature Edition) - Advanced",
  "Observing Event Streams: Lag, Metrics, and Alerts (Signature Edition) - Advanced",
  "Multi-Region Replication and Failover (Signature Edition) - Advanced",
  "Securing Event Data: Encryption and Redaction (Signature Edition) - Advanced",
  "Temporal Queries and Time Travel (Signature Edition) - Advanced"
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
var gen={version:'jahdb-event-streams-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('event-streams-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
