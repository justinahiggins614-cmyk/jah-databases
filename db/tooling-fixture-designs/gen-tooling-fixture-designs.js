(function(){'use strict';
/* JAH The Tooling and Fixture Designs Database generator — jahdb-tooling-fixture-designs-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TFD-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Makes a Good Fixture - Setup & Workholding",
  "The 3-2-1 Locating Principle - Setup & Workholding",
  "Drill Jig Basics - Jigs",
  "Simple V-Block Fixture - Fixtures",
  "Marking and Layout Templates - Templates & Gauges",
  "Go/No-Go Gauge Design - Templates & Gauges",
  "Clamping Force Basics - Setup & Workholding",
  "Toggle Clamp Selection - Setup & Workholding",
  "Dowel Pin Locating - Setup & Workholding",
  "Fixture Material Selection - Fixtures"
 ],
 "Compounded": [
  "Welding Fixture Design - Fixtures",
  "Machining Fixture with Multiple Setups - Fixtures",
  "3D-Printed Drill Guide - Jigs",
  "3D-Printed Assembly Fixture - Fixtures",
  "Inspection Fixture Design - Fixtures",
  "Press-Fit Assembly Fixture - Fixtures",
  "Soldering and Rework Jig - Jigs",
  "Cable Harness Assembly Board - Fixtures",
  "Angle Plate and Sine Bar Setup - Setup & Workholding",
  "Vacuum Workholding Basics - Setup & Workholding",
  "Template Routing Guides - Templates & Gauges",
  "Radius and Profile Gauges - Templates & Gauges"
 ],
 "Advanced": [
  "Tolerance Analysis for Fixture Design - Fixtures",
  "Quick-Change Fixture Systems - Fixtures",
  "Pneumatic Clamping Circuits - Setup & Workholding",
  "Error-Proofing (Poka-Yoke) in Fixtures - Fixtures",
  "CMM Inspection Fixture - Fixtures",
  "Multi-Part Pallet Fixture - Fixtures",
  "Flexible Fixture for Product Families - Fixtures",
  "Thermal Effects in Precision Fixtures - Fixtures",
  "Fixture Maintenance and Calibration - Setup & Workholding",
  "Cost Estimation for Custom Tooling - Fixtures",
  "3D-Printed Soft Jaws - Setup & Workholding",
  "Fixture Documentation Package - Fixtures"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Tooling Fixture Designs — "+safe+"\n"
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
    name:topic+' — tooling fixture design record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A tooling fixture design record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tooling-fixture-designs-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tooling-fixture-designs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
