(function(){'use strict';
/* JAH Database Design Fundamentals Database generator — jahdb-database-design-fundamentals-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DATADFS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Entities and Relationships (Signature Edition)", "Primary Keys (Signature Edition)", "Foreign Keys (Signature Edition)", "Normalization (Signature Edition)", "Denormalization (Signature Edition)", "Data Types (Signature Edition)", "Constraints (Signature Edition)", "Indexing Basics (Signature Edition)", "Views (Signature Edition)", "Transactions (Signature Edition)", "Migrations (Signature Edition)"], "Compounded": ["Choosing a Database (Signature Edition)", "Teaching Database Design (Signature Edition)", "The Schema Review (Signature Edition)", "Many-to-Many Relationships (Signature Edition)", "Hierarchies (Signature Edition)", "Temporal Data (Signature Edition)", "Soft Deletes (Signature Edition)", "Naming Conventions (Signature Edition)", "Documentation (Signature Edition)", "Security Design (Signature Edition)", "Backup and Recovery (Signature Edition)", "Performance Tuning (Signature Edition)"], "Advanced": ["Partitioning (Signature Edition)", "Replication (Signature Edition)", "NoSQL Patterns (Signature Edition)", "Graph Modeling (Signature Edition)", "Data Warehousing (Signature Edition)", "Schema Evolution (Signature Edition)", "Testing Databases (Signature Edition)", "Cloud Databases (Signature Edition)", "Polyglot Persistence (Signature Edition)", "The Design Review (Signature Edition)", "Learning Resources (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — database guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — database guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A database guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"database-design-fundamentals-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-database-design-fundamentals-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("database-design-fundamentals-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
