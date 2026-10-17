(function(){'use strict';
/* JAH The Asset and Equipment Registry Database generator — jahdb-asset-equipment-registry-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AREG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is an Asset: Property, Equipment, and Inventory - Foundations",
  "The Asset Register: What Every Record Carries - Foundations",
  "Asset Tags and Physical Identification - Foundations",
  "Asset Categories and Classification - Foundations",
  "Naming Conventions and Asset Taxonomy - Foundations",
  "Acquisition and Capitalization - Foundations",
  "Assignment and Custody - Foundations",
  "Asset Condition Ratings - Foundations",
  "Asset Location and Site Tracking - Foundations",
  "Asset Lifecycle States - Foundations"
 ],
 "Compounded": [
  "Tag Technologies: Barcode, QR Code, and RFID - Compounded",
  "Depreciation Schedules: Straight-Line and Declining Balance - Compounded",
  "CMDB-Style Configuration Records - Compounded",
  "Maintenance History and Work Orders - Compounded",
  "Preventive and Predictive Maintenance Scheduling - Compounded",
  "Warranty Tracking and Claims - Compounded",
  "Calibration Management and Traceability - Compounded",
  "Asset Audits and Physical Verification - Compounded",
  "Asset Utilization and Performance Metrics - Compounded",
  "Spare Parts Linkage and Inventory - Compounded",
  "Asset Risk and Criticality Assessment - Compounded",
  "Configuration Baselines and Change Control - Compounded"
 ],
 "Advanced": [
  "Reliability Metrics: MTBF, MTTR, and Availability - Advanced",
  "Total Cost of Ownership Modeling - Advanced",
  "The ISO 55000 Asset Management Framework - Advanced",
  "Asset Finance: Leasing Versus Buying - Advanced",
  "Asset Health Scoring and Predictive Replacement - Advanced",
  "Disposal, Decommissioning, and Data Sanitization - Advanced",
  "CMDB Federation and Automated Discovery - Advanced",
  "Asset Insurance and Loss Coverage - Advanced",
  "Registry Data Quality and Governance - Advanced",
  "Registry Analytics and Key Performance Indicators - Advanced",
  "Fleet Management and Multi-Site Consolidation - Advanced",
  "Building an Asset Registry Program - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Asset Registry Study — "+safe+"\n"
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
    name:topic+' — asset and equipment registry record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A asset and equipment registry record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"asset-registry-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-asset-equipment-registry-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('asset-equipment-registry',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
