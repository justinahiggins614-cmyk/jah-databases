(function(){'use strict';
/* JAH The Tooling and Fixture Designs Signature Database generator — jahdb-tooling-fixture-designs-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TFDS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Makes a Good Fixture (Signature Edition) - Setup & Workholding",
  "The 3-2-1 Locating Principle (Signature Edition) - Setup & Workholding",
  "Drill Jig Basics (Signature Edition) - Jigs",
  "Simple V-Block Fixture (Signature Edition) - Fixtures",
  "Marking and Layout Templates (Signature Edition) - Templates & Gauges",
  "Go/No-Go Gauge Design (Signature Edition) - Templates & Gauges",
  "Clamping Force Basics (Signature Edition) - Setup & Workholding",
  "Toggle Clamp Selection (Signature Edition) - Setup & Workholding",
  "Dowel Pin Locating (Signature Edition) - Setup & Workholding",
  "Fixture Material Selection (Signature Edition) - Fixtures"
 ],
 "Compounded": [
  "Welding Fixture Design (Signature Edition) - Fixtures",
  "Machining Fixture with Multiple Setups (Signature Edition) - Fixtures",
  "3D-Printed Drill Guide (Signature Edition) - Jigs",
  "3D-Printed Assembly Fixture (Signature Edition) - Fixtures",
  "Inspection Fixture Design (Signature Edition) - Fixtures",
  "Press-Fit Assembly Fixture (Signature Edition) - Fixtures",
  "Soldering and Rework Jig (Signature Edition) - Jigs",
  "Cable Harness Assembly Board (Signature Edition) - Fixtures",
  "Angle Plate and Sine Bar Setup (Signature Edition) - Setup & Workholding",
  "Vacuum Workholding Basics (Signature Edition) - Setup & Workholding",
  "Template Routing Guides (Signature Edition) - Templates & Gauges",
  "Radius and Profile Gauges (Signature Edition) - Templates & Gauges"
 ],
 "Advanced": [
  "Tolerance Analysis for Fixture Design (Signature Edition) - Fixtures",
  "Quick-Change Fixture Systems (Signature Edition) - Fixtures",
  "Pneumatic Clamping Circuits (Signature Edition) - Setup & Workholding",
  "Error-Proofing (Poka-Yoke) in Fixtures (Signature Edition) - Fixtures",
  "CMM Inspection Fixture (Signature Edition) - Fixtures",
  "Multi-Part Pallet Fixture (Signature Edition) - Fixtures",
  "Flexible Fixture for Product Families (Signature Edition) - Fixtures",
  "Thermal Effects in Precision Fixtures (Signature Edition) - Fixtures",
  "Fixture Maintenance and Calibration (Signature Edition) - Setup & Workholding",
  "Cost Estimation for Custom Tooling (Signature Edition) - Fixtures",
  "3D-Printed Soft Jaws (Signature Edition) - Setup & Workholding",
  "Fixture Documentation Package (Signature Edition) - Fixtures"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Tooling Fixture Designs Signature — "+safe+"\n"
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
var gen={version:'jahdb-tooling-fixture-designs-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tooling-fixture-designs-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
