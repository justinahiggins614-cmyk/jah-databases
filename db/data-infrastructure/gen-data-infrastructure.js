(function(){'use strict';
/* JAH The Data Infrastructure Database generator — jahdb-data-infrastructure-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DIN-";
var FIELDS=["infra"];
var TOPICS={
 "infra": [
  "Distributed Caches \u2014 infra",
  "Memory Caches \u2014 infra",
  "L1 Caches \u2014 infra",
  "L2 Caches \u2014 infra",
  "L3 Caches \u2014 infra",
  "CDN Caches \u2014 infra",
  "Web Caches \u2014 infra",
  "Query Caches \u2014 infra",
  "Object Caches \u2014 infra",
  "Page Caches \u2014 infra",
  "Buffer Caches \u2014 infra",
  "DNS Caches \u2014 infra",
  "Data Lakes \u2014 infra",
  "Data Warehouses \u2014 infra",
  "Data Marts \u2014 infra",
  "Lakehouses \u2014 infra",
  "Data Stores \u2014 infra",
  "Data Dumps \u2014 infra",
  "Data Indices \u2014 infra",
  "Data Catalogs \u2014 infra",
  "Data Libraries \u2014 infra",
  "Data Inventories \u2014 infra",
  "Data Manifests \u2014 infra",
  "Metadata Repositories \u2014 infra",
  "Master Data Stores \u2014 infra",
  "Reference Data Stores \u2014 infra",
  "Staging Areas \u2014 infra",
  "Operational Data Stores \u2014 infra",
  "Archive Tiers \u2014 infra",
  "Backup Tiers \u2014 infra",
  "WORM Stores \u2014 infra",
  "Content Repositories \u2014 infra",
  "Document Stores \u2014 infra",
  "File Shares \u2014 infra",
  "NAS Systems \u2014 infra",
  "SAN Fabrics \u2014 infra",
  "Object Gateways \u2014 infra",
  "Storage Virtualization \u2014 infra",
  "Software-Defined Storage \u2014 infra",
  "Hyperconverged Storage \u2014 infra",
  "Cloud Volumes \u2014 infra",
  "Ephemeral Storage \u2014 infra",
  "Persistent Volumes \u2014 infra",
  "StatefulSets Storage \u2014 infra",
  "Backup Appliances \u2014 infra",
  "Tape Libraries \u2014 infra",
  "Optical Archives \u2014 infra",
  "DNA Storage \u2014 infra",
  "Holographic Storage \u2014 infra",
  "Data Diodes \u2014 infra",
  "Cross-Domain Guards \u2014 infra",
  "Data Clean Rooms \u2014 infra",
  "Confidential Stores \u2014 infra"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Data Infrastructure — "+safe+"\n"
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
    name:topic+' — data infrastructure record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A data infrastructure record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-data-infrastructure-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('data-infrastructure',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
